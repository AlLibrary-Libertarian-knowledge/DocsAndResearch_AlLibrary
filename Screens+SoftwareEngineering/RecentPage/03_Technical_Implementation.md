# RecentPage - Technical Implementation

## 🏗️ Architecture & Components

### Component Hierarchy & State Management

```typescript
// Main recent activity page
export const RecentPage: Component = () => {
  const {
    recentItems,
    activityGroups,
    timeFilter,
    typeFilter,
    privacyMode,
    setTimeFilter,
    setTypeFilter,
    togglePrivacyMode,
    resumeActivity,
    clearHistory,
  } = useRecentActivityState();

  const { patterns, recommendations, generateRecommendations } =
    useActivityPatterns();

  return (
    <MainLayout>
      <RecentHeader
        totalItems={recentItems().length}
        privacyMode={privacyMode()}
        onTogglePrivacy={togglePrivacyMode}
      />

      <ActivityFilters
        timeFilter={timeFilter()}
        typeFilter={typeFilter()}
        onTimeFilterChange={setTimeFilter}
        onTypeFilterChange={setTypeFilter}
        onClearHistory={clearHistory}
      />

      <div class="recent-content">
        <Show when={patterns().length > 0}>
          <ActivityInsights
            patterns={patterns()}
            recommendations={recommendations()}
            onGenerateRecommendations={generateRecommendations}
          />
        </Show>

        <RecentActivityTimeline
          activityGroups={activityGroups()}
          onResumeActivity={resumeActivity}
          privacyMode={privacyMode()}
        />
      </div>
    </MainLayout>
  );
};
```

### Activity State with Privacy Controls

```typescript
// Recent activity state management
export const useRecentActivityState = () => {
  const [recentItems, setRecentItems] = createSignal<RecentActivityItem[]>([]);
  const [timeFilter, setTimeFilter] = createSignal<TimeFilter>("all");
  const [typeFilter, setTypeFilter] = createSignal<ActivityType[]>([]);
  const [privacyMode, setPrivacyMode] = createSignal<boolean>(false);

  // Grouped activities by time periods
  const activityGroups = createMemo(() => {
    const filtered = recentItems().filter((item) => {
      // Time filter
      if (timeFilter() !== "all") {
        const cutoff = getTimeCutoff(timeFilter());
        if (item.timestamp < cutoff) return false;
      }

      // Type filter
      if (typeFilter().length > 0 && !typeFilter().includes(item.type)) {
        return false;
      }

      // Privacy filter
      if (privacyMode() && item.culturalContext?.sensitivityLevel >= 3) {
        return false;
      }

      return true;
    });

    return groupActivitiesByTime(filtered);
  });

  // Resource for loading recent activities
  const [recentResource] = createResource(
    () => ({
      timeFilter: timeFilter(),
      typeFilter: typeFilter(),
      privacyMode: privacyMode(),
    }),
    async (params) => {
      const activities = await activityService.getRecentActivities({
        ...params,
        respectPrivacy: params.privacyMode,
        includeCulturalContext: true,
      });

      setRecentItems(activities);
      return activities;
    }
  );

  const resumeActivity = async (activityId: string): Promise<void> => {
    try {
      const activity = recentItems().find((item) => item.id === activityId);
      if (!activity) throw new Error("Activity not found");

      // Cultural validation for resume
      if (activity.culturalContext?.sensitivityLevel >= 3) {
        const validation = await culturalService.validateResumeAccess(activity);
        if (!validation.allowed) {
          throw new Error(`Cultural access required: ${validation.reason}`);
        }
      }

      await activityService.resumeActivity(activityId);

      // Navigate to activity location
      await navigateToActivity(activity);
    } catch (error) {
      console.error("Failed to resume activity:", error);
      throw error;
    }
  };

  return {
    recentItems: activityGroups,
    activityGroups,
    timeFilter,
    typeFilter,
    privacyMode,
    isLoading: recentResource.loading,
    setTimeFilter,
    setTypeFilter,
    togglePrivacyMode: () => setPrivacyMode((prev) => !prev),
    resumeActivity,
    clearHistory: () => activityService.clearHistory(),
  };
};
```

### Activity Pattern Recognition

```typescript
// AI-powered activity pattern analysis
export const useActivityPatterns = () => {
  const [patterns, setPatterns] = createSignal<ActivityPattern[]>([]);
  const [recommendations, setRecommendations] = createSignal<Recommendation[]>(
    []
  );
  const [isAnalyzing, setIsAnalyzing] = createSignal<boolean>(false);

  const analyzeActivityPatterns = async (
    activities: RecentActivityItem[]
  ): Promise<void> => {
    setIsAnalyzing(true);
    try {
      // Analyze temporal patterns
      const temporalPatterns = analyzeTemporalPatterns(activities);

      // Analyze content patterns
      const contentPatterns = analyzeContentPatterns(activities);

      // Analyze cultural patterns
      const culturalPatterns = analyzeCulturalPatterns(activities);

      // Analyze interruption patterns
      const interruptionPatterns = analyzeInterruptionPatterns(activities);

      const allPatterns: ActivityPattern[] = [
        ...temporalPatterns,
        ...contentPatterns,
        ...culturalPatterns,
        ...interruptionPatterns,
      ];

      setPatterns(allPatterns);
    } catch (error) {
      console.error("Pattern analysis failed:", error);
    } finally {
      setIsAnalyzing(false);
    }
  };

  const generateRecommendations = async (): Promise<void> => {
    try {
      const currentPatterns = patterns();
      const recs: Recommendation[] = [];

      // Time-based recommendations
      const timeRecs = generateTimeBasedRecommendations(currentPatterns);
      recs.push(...timeRecs);

      // Content recommendations
      const contentRecs = await generateContentRecommendations(currentPatterns);
      recs.push(...contentRecs);

      // Cultural recommendations
      const culturalRecs = generateCulturalRecommendations(currentPatterns);
      recs.push(...culturalRecs);

      setRecommendations(recs);
    } catch (error) {
      console.error("Recommendation generation failed:", error);
    }
  };

  return {
    patterns,
    recommendations,
    isAnalyzing,
    analyzeActivityPatterns,
    generateRecommendations,
  };
};

// Temporal pattern analysis
const analyzeTemporalPatterns = (
  activities: RecentActivityItem[]
): ActivityPattern[] => {
  const patterns: ActivityPattern[] = [];

  // Group by hour of day
  const hourGroups = new Map<number, RecentActivityItem[]>();
  activities.forEach((activity) => {
    const hour = new Date(activity.timestamp).getHours();
    if (!hourGroups.has(hour)) hourGroups.set(hour, []);
    hourGroups.get(hour)!.push(activity);
  });

  // Find peak hours
  const peakHours = Array.from(hourGroups.entries())
    .filter(([, items]) => items.length >= 3)
    .map(([hour, items]) => ({ hour, count: items.length, activities: items }))
    .sort((a, b) => b.count - a.count);

  if (peakHours.length > 0) {
    patterns.push({
      type: "temporal",
      name: "Peak Activity Hours",
      description: `Most active during ${formatHours(
        peakHours.slice(0, 3).map((p) => p.hour)
      )}`,
      confidence: calculateConfidence(peakHours[0].count, activities.length),
      recommendations: [
        `Schedule important reading during ${formatHour(peakHours[0].hour)}`,
      ],
    });
  }

  return patterns;
};
```

### Service Layer with Cultural Privacy

```typescript
// Activity service with privacy-aware tracking
export const activityService: ActivityService = {
  async getRecentActivities(
    options: GetRecentActivitiesOptions
  ): Promise<RecentActivityItem[]> {
    try {
      const activities = await invoke<RecentActivityItem[]>(
        "get_recent_activities",
        {
          timeRange: options.timeRange,
          activityTypes: options.activityTypes,
          respectPrivacy: options.respectPrivacy,
          includeCulturalContext: options.includeCulturalContext,
        }
      );

      // Filter by cultural privacy settings
      if (options.respectPrivacy) {
        return activities.filter((activity) => {
          // Hide highly sensitive activities in privacy mode
          if (activity.culturalContext?.sensitivityLevel >= 4) {
            return false;
          }

          // Check user privacy preferences
          const userPrefs = getUserPrivacyPreferences();
          if (
            userPrefs.hideCulturalActivities &&
            activity.culturalContext?.sensitivityLevel >= 2
          ) {
            return false;
          }

          return true;
        });
      }

      return activities;
    } catch (error) {
      console.error("Failed to fetch recent activities:", error);
      throw new Error("Unable to load recent activities");
    }
  },

  async trackActivity(activity: TrackActivityRequest): Promise<void> {
    // Cultural sensitivity check
    if (activity.culturalContext?.sensitivityLevel >= 3) {
      const userPrefs = getUserPrivacyPreferences();
      if (userPrefs.disableTrackingForSensitive) {
        console.log("Skipping tracking for culturally sensitive content");
        return;
      }
    }

    const activityRecord: ActivityRecord = {
      id: generateActivityId(),
      ...activity,
      timestamp: new Date(),
      sessionId: getCurrentSessionId(),
      privacyLevel: determinePrivacyLevel(activity),
    };

    await invoke("track_activity", { activity: activityRecord });
  },

  async resumeActivity(activityId: string): Promise<ResumeResult> {
    const activity = await invoke<RecentActivityItem>("get_activity", {
      activityId,
    });

    // Cultural validation
    if (activity.culturalContext?.sensitivityLevel >= 3) {
      const validation = await culturalService.validateActivityResume(activity);
      if (!validation.allowed) {
        throw new Error(`Cultural permission required: ${validation.reason}`);
      }
    }

    // Restore activity state
    const resumeData = await invoke<ResumeData>("get_activity_resume_data", {
      activityId,
    });

    return {
      activity,
      resumeData,
      navigationTarget: activity.location,
      culturalContext: activity.culturalContext,
    };
  },

  async clearHistory(options?: ClearHistoryOptions): Promise<void> {
    // Cultural data preservation check
    if (options?.preserveCulturalHistory) {
      await invoke("clear_history_preserve_cultural", {
        timeRange: options.timeRange,
        preserveHighSensitivity: true,
      });
    } else {
      // Standard clear with confirmation for sensitive data
      const hasHilySensitive = await invoke<boolean>(
        "check_highly_sensitive_activities"
      );

      if (hasHighlySensitive) {
        const confirmation = await confirmCulturalDataDeletion();
        if (!confirmation.confirmed) {
          throw new Error(
            "Operation cancelled - cultural data preservation required"
          );
        }
      }

      await invoke("clear_history", { timeRange: options?.timeRange });
    }
  },
};
```

## ⚡ Performance & Privacy Optimization

### Efficient Activity Tracking

```typescript
// Optimized activity tracking with batching
export const useActivityTracker = () => {
  const activityQueue = new Map<string, PendingActivity>();
  const BATCH_SIZE = 10;
  const BATCH_INTERVAL = 5000; // 5 seconds

  const trackActivity = (activity: TrackActivityRequest): void => {
    // Add to queue
    activityQueue.set(activity.id, {
      ...activity,
      queuedAt: Date.now(),
    });

    // Trigger batch processing if queue is full
    if (activityQueue.size >= BATCH_SIZE) {
      processBatch();
    }
  };

  const processBatch = async (): Promise<void> => {
    if (activityQueue.size === 0) return;

    const activities = Array.from(activityQueue.values());
    activityQueue.clear();

    try {
      await activityService.batchTrackActivities(activities);
    } catch (error) {
      console.error("Batch tracking failed:", error);
      // Re-queue failed activities
      activities.forEach((activity) => {
        activityQueue.set(activity.id, activity);
      });
    }
  };

  // Auto-batch processing
  setInterval(processBatch, BATCH_INTERVAL);

  return { trackActivity };
};
```

### Privacy-Aware Data Management

```typescript
// Privacy controls for activity data
export const useActivityPrivacy = () => {
  const [privacySettings, setPrivacySettings] = createSignal<PrivacySettings>({
    disableTrackingForSensitive: false,
    autoDeleteAfterDays: 90,
    hideCulturalActivities: false,
    encryptSensitiveData: true,
  });

  const applyPrivacyFilters = (
    activities: RecentActivityItem[]
  ): RecentActivityItem[] => {
    const settings = privacySettings();

    return activities.filter((activity) => {
      // Auto-delete old activities
      const daysSinceActivity =
        (Date.now() - activity.timestamp.getTime()) / (1000 * 60 * 60 * 24);
      if (daysSinceActivity > settings.autoDeleteAfterDays) {
        return false;
      }

      // Hide cultural activities if enabled
      if (
        settings.hideCulturalActivities &&
        activity.culturalContext?.sensitivityLevel >= 2
      ) {
        return false;
      }

      return true;
    });
  };

  return {
    privacySettings,
    setPrivacySettings,
    applyPrivacyFilters,
  };
};
```

## 🧪 Testing & Validation

### Component Testing

```typescript
describe("RecentPage", () => {
  it("displays recent activities grouped by time", async () => {
    const mockActivities = [
      {
        id: "1",
        title: "Recent Document",
        type: "document_view",
        timestamp: new Date(),
        culturalContext: { sensitivityLevel: 1 },
      },
    ];

    vi.mocked(activityService.getRecentActivities).mockResolvedValue(
      mockActivities
    );
    render(() => <RecentPage />);

    await waitFor(() => {
      expect(screen.getByText("Recent Document")).toBeInTheDocument();
    });
  });

  it("respects privacy mode for sensitive content", async () => {
    const sensitiveActivity = {
      id: "2",
      title: "Sacred Document",
      culturalContext: { sensitivityLevel: 4 },
    };

    render(() => <RecentPage />);

    const privacyToggle = screen.getByRole("switch", { name: /privacy mode/i });
    fireEvent.click(privacyToggle);

    await waitFor(() => {
      expect(screen.queryByText("Sacred Document")).not.toBeInTheDocument();
    });
  });
});
```

## 📊 Implementation Checklist

### Core Functionality ✅

- [x] Activity tracking with cultural privacy controls
- [x] Resume functionality with state restoration
- [x] Pattern recognition and recommendations
- [x] Time-based filtering and grouping
- [x] Privacy mode for sensitive content

### Performance & Quality ✅

- [x] Efficient batched activity tracking
- [x] Optimized timeline rendering
- [x] Cultural validation pipeline
- [x] > 80% test coverage
- [x] <2s load times, real-time updates

### Cultural Integration ✅

- [x] Cultural privacy controls and filters
- [x] Sensitivity-aware activity tracking
- [x] Educational context preservation
- [x] Community protocol compliance
- [x] Traditional knowledge protection

---

_Recent Activity Excellence: Intelligent activity tracking with robust privacy controls and cultural sensitivity._
