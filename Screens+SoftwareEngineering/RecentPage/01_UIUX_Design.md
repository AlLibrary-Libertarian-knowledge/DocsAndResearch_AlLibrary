# Recent Page - UI/UX Design Specification

## 🎨 Visual Design

### Layout Structure

```
┌─────────────────────────────────────────────────────────────────┐
│ Header: Recent Activity 🕒 | Time Filter | Clear History        │
├─────────────────────────────────────────────────────────────────┤
│ ┌─────────────────┐ ┌─────────────────────────────────────────┐ │
│ │ Time Filters    │ │ Recent Activity Timeline                │ │
│ │ - Today         │ │ ┌─────────────────────────────────────┐ │ │
│ │ - Yesterday     │ │ │ Today - January 25, 2025            │ │ │
│ │ - This Week     │ │ │ ┌─────────────────────────────────┐ │ │ │
│ │ - This Month    │ │ │ │ 2:30 PM - Opened Document      │ │ │ │
│ │ - All Time      │ │ │ │ [📄] Traditional Healing Guide │ │ │ │
│ │                 │ │ │ │ Read for 15 minutes             │ │ │ │
│ │ Activity Types  │ │ │ └─────────────────────────────────┘ │ │ │
│ │ - Opened        │ │ │ ┌─────────────────────────────────┐ │ │ │
│ │ - Downloaded    │ │ │ │ 11:45 AM - Added to Collection │ │ │ │
│ │ - Shared        │ │ │ │ [📚] Medicinal Plants Research │ │ │ │
│ │ - Created       │ │ │ │ Added 3 new documents           │ │ │ │
│ │ - Modified      │ │ │ └─────────────────────────────────┘ │ │ │
│ │                 │ │ │ ┌─────────────────────────────────┐ │ │ │
│ │ Quick Stats     │ │ │ │ 9:15 AM - Network Discovery    │ │ │ │
│ │ - Today: 12     │ │ │ │ [🌐] Found 5 new documents     │ │ │ │
│ │ - This Week: 47 │ │ │ │ Cultural: Indigenous Knowledge  │ │ │ │
│ │ - Documents: 34 │ │ │ └─────────────────────────────────┘ │ │ │
│ │ - Collections:8 │ │ └─────────────────────────────────────┘ │ │
│ └─────────────────┘ └─────────────────────────────────────────┘ │
├─────────────────────────────────────────────────────────────────┤
│ Footer: 47 Activities This Week | Privacy: Local Only           │
└─────────────────────────────────────────────────────────────────┘
```

### Activity Item Design

```css
.activity-item {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 12px 16px;
  margin-bottom: 8px;
  transition: all 0.2s ease;
  position: relative;
}

.activity-item::before {
  content: "";
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  width: 3px;
  background: var(--primary-color);
  border-radius: 0 3px 3px 0;
}

.activity-item.cultural::before {
  background: var(--purple-500);
}

.activity-item.sacred::before {
  background: var(--purple-700);
}

.activity-timestamp {
  font-size: 0.875rem;
  color: var(--text-secondary);
  font-weight: 500;
}

.activity-content {
  margin: 4px 0;
  display: flex;
  align-items: center;
  gap: 8px;
}

.activity-icon {
  width: 20px;
  height: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.activity-details {
  font-size: 0.875rem;
  color: var(--text-secondary);
  margin-top: 4px;
}
```

### Timeline Organization

- **Chronological Grouping**: Activities grouped by day/week
- **Activity Types**: Different icons and colors for different actions
- **Cultural Indicators**: Special styling for culturally sensitive activities
- **Quick Actions**: Hover actions to repeat or undo activities

## 🧭 User Experience

### Activity Tracking

- **Comprehensive Logging**: All user interactions with content
- **Privacy Focused**: Local-only activity tracking
- **Cultural Awareness**: Special handling of culturally sensitive activities
- **Smart Filtering**: Intelligent categorization and filtering options

### Interaction Patterns

- **Timeline Navigation**: Smooth scrolling through activity history
- **Quick Repeat**: One-click to repeat previous actions
- **Activity Details**: Expandable details for complex activities
- **Bulk Management**: Select multiple activities for batch operations

## 📱 Interface Components

### Activity Type Variations

```
Document Access:
┌─────────────────────────────────────────────────────────┐
│ 2:30 PM - Opened Document                              │
│ [📄] Traditional Healing Practices of the Amazon       │
│ Read for 15 minutes • Scrolled to page 23              │
│ Cultural Context: Traditional Knowledge                 │
│ [Open Again] [Add to Favorites] [Share]                │
└─────────────────────────────────────────────────────────┘

Network Activity:
┌─────────────────────────────────────────────────────────┐
│ 11:45 AM - Network Discovery                           │
│ [🌐] Found 5 new documents from 3 peers               │
│ Topics: Traditional Medicine, Oral History             │
│ Cultural Contexts: Brazilian Indigenous, Andean        │
│ [View Discoveries] [Configure Alerts]                  │
└─────────────────────────────────────────────────────────┘

Cultural Activity:
┌─────────────────────────────────────────────────────────┐
│ 9:15 AM - Cultural Permission Granted                  │
│ [🛡️] Access granted to Sacred Stories Collection      │
│ Granted by: Elder Maria Santos                         │
│ Duration: 30 days • Purpose: Educational Research      │
│ [View Guidelines] [Thank Elder] [Access Collection]    │
└─────────────────────────────────────────────────────────┘
```

### Privacy Controls

- **Local Storage**: All activity data stored locally only
- **Selective Sharing**: Option to share activity summaries with community
- **Cultural Privacy**: Extra protection for culturally sensitive activities
- **Data Retention**: Configurable retention periods for different activity types

---

_Recent Activity Excellence: This design provides comprehensive activity tracking while maintaining user privacy and cultural sensitivity, enabling users to understand and repeat their knowledge discovery patterns._
