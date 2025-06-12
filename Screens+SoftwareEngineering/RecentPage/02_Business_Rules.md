# RecentPage - Business Rules & Software Engineering Requirements

## 🎯 Business Objectives

### Core Functionality Goals

1. **Activity Tracking**: Comprehensive tracking of user's recent content access and interactions
2. **Quick Resume**: Enable users to quickly resume work on recently accessed content
3. **Cultural Context Preservation**: Maintain cultural context and sensitivity in activity history
4. **Pattern Recognition**: Identify usage patterns to improve content discovery and recommendations
5. **Privacy-Aware History**: Provide detailed activity history while respecting cultural privacy requirements

### Success Metrics

- **Resume Efficiency**: 85%+ users successfully resume work within 10 seconds using recent activity
- **Activity Accuracy**: 99%+ accuracy in tracking and displaying recent content interactions
- **Cultural Compliance**: 100% culturally sensitive activity properly classified and protected
- **Privacy Satisfaction**: 90%+ user satisfaction with privacy controls for activity history
- **Discovery Enhancement**: 70%+ improvement in content discovery through activity-based recommendations

### User Value Proposition

- **Seamless Continuity**: Pick up exactly where you left off with any content or activity
- **Activity Insights**: Understand your content consumption patterns and cultural engagement
- **Quick Access**: Instant access to recently used documents, collections, and cultural content
- **Cultural Journey**: Track your cultural learning and engagement journey over time
- **Privacy Control**: Full control over activity history visibility and retention

## 📋 Functional Requirements

### Core Activity Tracking Features

#### F1: Comprehensive Activity Monitoring

- **Requirement**: Track all user interactions with content while respecting cultural privacy
- **Activity Types**: Document access, collection browsing, cultural content interaction, network activity
- **Granularity**: Page-level for documents, section-level for collections, interaction-level for cultural content
- **Metadata**: Timestamp, duration, interaction type, cultural context, device information
- **Privacy Controls**: User-configurable activity retention and visibility settings

#### F2: Recent Content Display

```typescript
interface RecentActivity {
  id: string;
  userId: string;
  contentId: string;
  contentType:
    | "document"
    | "collection"
    | "cultural_context"
    | "network_peer"
    | "search_query";
  activityType: ActivityType;

  // Timing information
  timestamp: Date;
  duration: number; // seconds spent
  lastPosition?: number; // for documents: page number, for audio/video: timestamp

  // Content metadata
  title: string;
  description?: string;
  thumbnail?: string;

  // Cultural context
  culturalContext: CulturalContext;
  culturalInteraction: CulturalInteraction;
  sensitivityLevel: SensitivityLevel;

  // Activity context
  deviceInfo: DeviceInfo;
  sessionId: string;
  interactionDetails: InteractionDetails;

  // Privacy and retention
  isPrivate: boolean;
  retentionPolicy: RetentionPolicy;
  culturalPrivacyLevel: CulturalPrivacyLevel;
}

enum ActivityType {
  OPENED = "opened",
  VIEWED = "viewed",
  EDITED = "edited",
  SHARED = "shared",
  FAVORITED = "favorited",
  DOWNLOADED = "downloaded",
  SEARCHED = "searched",
  CULTURAL_INTERACTION = "cultural_interaction",
}
```

#### F3: Cultural Activity Management

- **Sensitivity Tracking**: Track interactions with culturally sensitive content with appropriate privacy
- **Cultural Learning**: Monitor cultural education and awareness activities
- **Community Engagement**: Track participation in cultural communities and discussions
- **Guardian Oversight**: Provide cultural guardians with appropriate activity visibility
- **Educational Progress**: Track progress through cultural education materials

#### F4: Smart Activity Organization

- **Temporal Grouping**: Group activities by time periods (today, yesterday, this week, etc.)
- **Content Clustering**: Group related activities (same document, collection, or cultural topic)
- **Cultural Categorization**: Organize activities by cultural context and community
- **Project Tracking**: Identify and group activities related to specific projects or research
- **Session Reconstruction**: Reconstruct work sessions across multiple content items

#### F5: Activity-Based Recommendations

- **Resume Suggestions**: Intelligent suggestions for resuming interrupted activities
- **Related Content**: Recommend content based on recent activity patterns
- **Cultural Exploration**: Suggest cultural content based on recent cultural interactions
- **Collaborative Opportunities**: Suggest collaboration based on similar recent activities
- **Learning Paths**: Recommend educational content based on recent cultural engagement

### Data Requirements

#### Activity Tracking Schema

```sql
-- Comprehensive activity tracking with cultural sensitivity
CREATE TABLE user_activities (
    id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL,
    content_id TEXT NOT NULL,
    content_type TEXT CHECK(content_type IN ('document', 'collection', 'cultural_context', 'network_peer', 'search_query')) NOT NULL,
    activity_type TEXT NOT NULL,

    -- Timing information
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    duration INTEGER DEFAULT 0, -- seconds
    last_position INTEGER, -- page, timestamp, etc.
    session_id TEXT NOT NULL,

    -- Content metadata (cached for performance)
    title TEXT NOT NULL,
    description TEXT,
    thumbnail_url TEXT,

    -- Cultural context
    cultural_context TEXT, -- JSON object
    cultural_interaction TEXT, -- JSON object describing cultural interaction
    sensitivity_level INTEGER CHECK(sensitivity_level BETWEEN 1 AND 5),

    -- Activity context
    device_info TEXT, -- JSON object with device information
    interaction_details TEXT, -- JSON object with specific interaction details

    -- Privacy and retention
    is_private BOOLEAN DEFAULT FALSE,
    retention_policy TEXT CHECK(retention_policy IN ('standard', 'extended', 'minimal', 'cultural_sensitive')) DEFAULT 'standard',
    cultural_privacy_level INTEGER CHECK(cultural_privacy_level BETWEEN 1 AND 5) DEFAULT 1,

    -- Cleanup and archival
    archived_at DATETIME,
    expires_at DATETIME
);

-- Activity sessions for grouping related activities
CREATE TABLE activity_sessions (
    id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL,
    start_time DATETIME NOT NULL,
    end_time DATETIME,
    device_info TEXT, -- JSON object

    -- Session metadata
    primary_content_type TEXT,
    cultural_contexts TEXT, -- JSON array of cultural contexts engaged with
    activity_count INTEGER DEFAULT 0,
    total_duration INTEGER DEFAULT 0,

    -- Cultural session tracking
    cultural_learning_activities INTEGER DEFAULT 0,
    sacred_content_interactions INTEGER DEFAULT 0,
    community_engagements INTEGER DEFAULT 0
);

-- Cultural activity analytics (privacy-preserving)
CREATE TABLE cultural_activity_analytics (
    user_id TEXT NOT NULL,
    cultural_context TEXT NOT NULL, -- JSON object (anonymized)
    activity_date DATE NOT NULL,

    -- Aggregated metrics
    total_interactions INTEGER DEFAULT 0,
    unique_content_items INTEGER DEFAULT 0,
    total_duration INTEGER DEFAULT 0,
    learning_activities INTEGER DEFAULT 0,

    -- Cultural engagement metrics
    sensitivity_levels_accessed TEXT, -- JSON array of sensitivity levels
    community_participation BOOLEAN DEFAULT FALSE,
    guardian_interactions INTEGER DEFAULT 0,

    PRIMARY KEY (user_id, cultural_context, activity_date)
);

-- Activity-based recommendations
CREATE TABLE activity_recommendations (
    user_id TEXT NOT NULL,
    content_id TEXT NOT NULL,
    recommendation_type TEXT NOT NULL, -- 'resume', 'related', 'cultural_exploration'
    score REAL NOT NULL,
    reasoning TEXT, -- Explanation based on recent activity
    cultural_context TEXT, -- JSON object
    generated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    expires_at DATETIME,
    clicked BOOLEAN DEFAULT FALSE,

    PRIMARY KEY (user_id, content_id, recommendation_type)
);
```

#### Performance and Privacy Optimization

```sql
-- Indexes for efficient activity querying
CREATE INDEX idx_activities_user_time ON user_activities(user_id, timestamp DESC);
CREATE INDEX idx_activities_content ON user_activities(content_id, content_type);
CREATE INDEX idx_activities_cultural ON user_activities(user_id, cultural_context);
CREATE INDEX idx_activities_session ON user_activities(session_id);
CREATE INDEX idx_activities_retention ON user_activities(expires_at) WHERE expires_at IS NOT NULL;

-- Automated cleanup for expired activities
CREATE TRIGGER cleanup_expired_activities
AFTER INSERT ON user_activities
BEGIN
    DELETE FROM user_activities
    WHERE expires_at IS NOT NULL AND expires_at < datetime('now');
END;

-- Privacy-preserving activity aggregation
CREATE VIEW recent_activity_summary AS
SELECT
    user_id,
    DATE(timestamp) as activity_date,
    content_type,
    COUNT(*) as activity_count,
    SUM(duration) as total_duration,
    COUNT(DISTINCT content_id) as unique_content,
    MAX(timestamp) as last_activity
FROM user_activities
WHERE timestamp > datetime('now', '-30 days')
  AND archived_at IS NULL
GROUP BY user_id, DATE(timestamp), content_type;
```

### Integration Requirements

#### Tauri Backend Services

- **Activity Service**: Comprehensive activity tracking with cultural sensitivity
- **Content Service**: Integration for content metadata and cultural context
- **Privacy Service**: User privacy controls and data retention management
- **Analytics Service**: Activity pattern analysis for recommendations
- **Cultural Service**: Cultural protocol enforcement for activity tracking

#### Frontend State Management

```typescript
interface RecentPageState {
  // Activity data
  recentActivities: RecentActivity[];
  activitySessions: ActivitySession[];
  recommendations: ActivityRecommendation[];

  // View state
  viewMode: "timeline" | "grouped" | "cultural";
  timeFilter: "today" | "yesterday" | "week" | "month" | "all";
  contentTypeFilter: ContentType[];

  // Grouping and organization
  groupBy: "time" | "content" | "cultural" | "session";
  showPrivateActivities: boolean;
  culturalContextFilter: string[];

  // UI state
  isLoading: boolean;
  selectedActivities: Set<string>;
  expandedSessions: Set<string>;

  // Privacy and settings
  privacySettings: PrivacySettings;
  retentionSettings: RetentionSettings;
  culturalPrivacyLevel: number;

  // Recommendations
  showRecommendations: boolean;
  recommendationTypes: RecommendationType[];
}
```

### Performance Requirements

#### Load Time and Responsiveness

- **Activity List**: <1 second for 1,000+ recent activities
- **Timeline Navigation**: <200ms for time period switching
- **Content Resume**: <500ms to resume content from last position
- **Search Activities**: <300ms for activity search across all history
- **Recommendation Generation**: <1 second for activity-based recommendations

#### Scalability Targets

- **Activity Volume**: Handle 10,000+ activities per user efficiently
- **Retention Period**: Support configurable retention from 1 week to 5 years
- **Concurrent Sessions**: Track multiple simultaneous sessions across devices
- **Cultural Contexts**: Handle 100+ different cultural contexts per user
- **Real-time Updates**: <100ms latency for activity tracking

## 🔒 Security & Cultural Requirements

### Data Protection and Privacy

- **Activity Encryption**: Encrypt activity data at rest with user-controlled keys
- **Selective Retention**: User-configurable retention policies for different activity types
- **Privacy Controls**: Granular controls over activity visibility and sharing
- **Cultural Privacy**: Enhanced privacy protections for culturally sensitive activities
- **Data Minimization**: Collect only necessary activity data with user consent

### Cultural Sensitivity Implementation

#### Cultural Activity Protection

```typescript
interface CulturalActivityProtection {
  sensitivityLevel: SensitivityLevel;
  privacyRequirements: PrivacyRequirement[];
  retentionPolicy: CulturalRetentionPolicy;
  guardianVisibility: GuardianVisibilityLevel;
  communitySharing: CommunityShareLevel;
  educationalTracking: boolean;
}

interface CulturalPrivacySettings {
  trackSacredContent: boolean;
  shareWithGuardians: boolean;
  communityVisibility: CommunityVisibilityLevel;
  culturalLearningTracking: boolean;
  anonymizeAfterPeriod: number; // days
}
```

#### Cultural Protocol Enforcement

- **Sensitivity-Aware Tracking**: Adjust tracking granularity based on cultural sensitivity
- **Guardian Visibility**: Provide appropriate activity visibility to cultural guardians
- **Community Privacy**: Respect community privacy norms for activity sharing
- **Educational Tracking**: Track cultural education progress with appropriate privacy
- **Sacred Content Protection**: Enhanced protection for sacred content activity

### Compliance and Governance

- **Cultural Data Sovereignty**: Respect indigenous and community data governance principles
- **Activity Attribution**: Proper attribution while maintaining privacy
- **Community Protocols**: Integration with cultural community governance systems
- **International Standards**: Compliance with privacy and cultural heritage protection guidelines
- **Audit Requirements**: Comprehensive logging for compliance and cultural sensitivity

## 🔄 Business Logic Workflows

### Activity Tracking Workflow

1. **User Interaction**: User interacts with content (open, view, edit, etc.)
2. **Cultural Assessment**: Determine cultural sensitivity and privacy requirements
3. **Privacy Check**: Verify user privacy settings and cultural protocols
4. **Activity Recording**: Record activity with appropriate granularity and metadata
5. **Session Management**: Associate activity with current session or create new session
6. **Cultural Notification**: Notify cultural guardians if required by protocols
7. **Retention Setup**: Apply appropriate retention policy based on content and cultural sensitivity

### Content Resume Workflow

1. **Resume Request**: User requests to resume content from recent activity
2. **Activity Lookup**: Find most recent activity for the requested content
3. **Cultural Validation**: Verify current access permissions for cultural content
4. **Position Restoration**: Restore last position (page, timestamp, etc.)
5. **Context Recreation**: Recreate relevant context (filters, settings, etc.)
6. **Cultural Education**: Provide cultural context if required
7. **Activity Update**: Record resume activity for future tracking

### Recommendation Generation Workflow

1. **Pattern Analysis**: Analyze recent activity patterns and preferences
2. **Cultural Context**: Consider cultural interests and community connections
3. **Content Similarity**: Identify similar content based on recent activities
4. **Temporal Relevance**: Factor in time-based patterns and cultural events
5. **Cultural Appropriateness**: Ensure recommendations respect cultural protocols
6. **Privacy Filtering**: Filter recommendations based on privacy settings
7. **Presentation**: Present recommendations with reasoning and cultural context

### Privacy Management Workflow

1. **Privacy Assessment**: Evaluate privacy requirements for each activity
2. **User Preferences**: Apply user-configured privacy settings
3. **Cultural Protocols**: Apply cultural community privacy requirements
4. **Retention Policy**: Determine appropriate retention period
5. **Access Control**: Set appropriate access controls for activity data
6. **Anonymization**: Schedule anonymization for sensitive activities
7. **Cleanup Scheduling**: Schedule automatic cleanup based on retention policies

---

_This business rules document ensures RecentPage provides comprehensive activity tracking and resume capabilities while maintaining the highest standards of cultural sensitivity and user privacy control._
