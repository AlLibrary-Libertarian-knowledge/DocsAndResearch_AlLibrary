# MyDocumentsPage - Technical Implementation Guide

## 🏗️ Architecture & Components

### Component Hierarchy

```
MyDocumentsPage/
├── 📁 components/
│   ├── DocumentGrid.tsx           # Main document display grid
│   ├── DocumentCard.tsx           # Individual document card (reusable)
│   ├── FilterPanel.tsx            # Advanced filtering sidebar
│   ├── BulkActionBar.tsx          # Multi-select operations
│   ├── StorageIndicator.tsx       # Storage usage display
│   ├── SyncStatusIndicator.tsx    # Sync status display
│   └── CulturalSensitivityBadge.tsx # Cultural context indicator
├── 📁 hooks/
│   ├── useDocumentLibrary.ts      # Document management logic
│   ├── useDocumentFilters.ts      # Filtering and search logic
│   ├── useBulkOperations.ts       # Bulk action management
│   ├── useStorageManagement.ts    # Storage monitoring
│   └── useCulturalValidation.ts   # Cultural sensitivity handling
├── 📁 services/
│   ├── documentService.ts         # Document CRUD operations
│   ├── culturalService.ts         # Cultural protocol enforcement
│   ├── storageService.ts          # Storage management
│   └── syncService.ts             # Network synchronization
└── MyDocumentsPage.tsx            # Main page component
```

### Core Component Implementation

#### MyDocumentsPage.tsx - Main Component

```typescript
import {
  Component,
  createSignal,
  createResource,
  createMemo,
  Show,
  For,
} from "solid-js";
import { DocumentGrid } from "./components/DocumentGrid";
import { FilterPanel } from "./components/FilterPanel";
import { BulkActionBar } from "./components/BulkActionBar";
import { StorageIndicator } from "./components/StorageIndicator";
import { useDocumentLibrary } from "./hooks/useDocumentLibrary";
import { useDocumentFilters } from "./hooks/useDocumentFilters";
import { useBulkOperations } from "./hooks/useBulkOperations";
import { Document, DocumentFilters, ViewMode } from "@/types/core";

export const MyDocumentsPage: Component = () => {
  // State management following SOLID principles
  const [viewMode, setViewMode] = createSignal<ViewMode>("grid");
  const [searchQuery, setSearchQuery] = createSignal("");

  // Custom hooks for separation of concerns
  const documentLibrary = useDocumentLibrary();
  const documentFilters = useDocumentFilters();
  const bulkOperations = useBulkOperations();

  // Computed values for performance optimization
  const filteredDocuments = createMemo(() => {
    return documentFilters.applyFilters(
      documentLibrary.documents(),
      documentFilters.activeFilters(),
      searchQuery()
    );
  });

  const selectedDocuments = createMemo(() => {
    return bulkOperations.selectedDocuments();
  });

  // Event handlers following single responsibility principle
  const handleDocumentSelect = (document: Document) => {
    bulkOperations.toggleSelection(document.id);
  };

  const handleBulkAction = async (action: string) => {
    await bulkOperations.executeBulkAction(action, selectedDocuments());
  };

  const handleFilterChange = (filters: DocumentFilters) => {
    documentFilters.updateFilters(filters);
  };

  return (
    <div class="my-documents-page">
      {/* Header with search and view controls */}
      <header class="page-header">
        <div class="header-content">
          <h1 class="page-title">My Documents</h1>
          <div class="header-actions">
            <SearchInput
              value={searchQuery()}
              onInput={setSearchQuery}
              placeholder="Search your documents..."
            />
            <ViewModeToggle mode={viewMode()} onChange={setViewMode} />
          </div>
        </div>

        {/* Storage and sync status */}
        <div class="status-bar">
          <StorageIndicator usage={documentLibrary.storageUsage()} />
          <SyncStatusIndicator status={documentLibrary.syncStatus()} />
        </div>
      </header>

      {/* Bulk action bar - shown when documents are selected */}
      <Show when={selectedDocuments().size > 0}>
        <BulkActionBar
          selectedCount={selectedDocuments().size}
          onAction={handleBulkAction}
          onClearSelection={bulkOperations.clearSelection}
        />
      </Show>

      {/* Main content area */}
      <div class="page-content">
        {/* Filter sidebar */}
        <aside class="filter-sidebar">
          <FilterPanel
            filters={documentFilters.activeFilters()}
            onFilterChange={handleFilterChange}
            documentCount={filteredDocuments().length}
          />
        </aside>

        {/* Document grid/list */}
        <main class="document-content">
          <Show
            when={filteredDocuments().length > 0}
            fallback={<EmptyState query={searchQuery()} />}
          >
            <DocumentGrid
              documents={filteredDocuments()}
              viewMode={viewMode()}
              selectedDocuments={selectedDocuments()}
              onDocumentSelect={handleDocumentSelect}
              onDocumentAction={documentLibrary.handleDocumentAction}
            />
          </Show>
        </main>
      </div>
    </div>
  );
};
```

#### DocumentCard.tsx - Reusable Document Component

```typescript
import { Component, Show, createSignal } from "solid-js";
import { Card } from "@/components/foundation/Card";
import { Button } from "@/components/foundation/Button";
import { CulturalSensitivityBadge } from "./CulturalSensitivityBadge";
import { Document, CulturalContext } from "@/types/core";
import { formatFileSize, formatDate } from "@/utils/formatting";
import { getDocumentIcon } from "@/utils/documentUtils";

interface DocumentCardProps {
  document: Document;
  isSelected?: boolean;
  onSelect?: (document: Document) => void;
  onAction?: (action: string, document: Document) => void;
  variant?: "default" | "compact" | "detailed";
}

export const DocumentCard: Component<DocumentCardProps> = (props) => {
  const [isHovered, setIsHovered] = createSignal(false);

  // Cultural sensitivity check following security requirements
  const canAccess = () => {
    return (
      props.document.culturalContext.sensitivityLevel <= 3 ||
      props.document.permissions.allowedUsers.includes(getCurrentUserId())
    );
  };

  const handleCardClick = () => {
    if (canAccess()) {
      props.onSelect?.(props.document);
    }
  };

  const handleAction = (action: string) => {
    props.onAction?.(action, props.document);
  };

  return (
    <Card
      variant="elevated"
      class={`document-card ${props.variant || "default"} ${
        props.isSelected ? "selected" : ""
      }`}
      onMouseEnter={() => setIsHovered(true)}
      onMouseLeave={() => setIsHovered(false)}
      onClick={handleCardClick}
    >
      {/* Selection checkbox */}
      <Show when={props.onSelect}>
        <input
          type="checkbox"
          class="document-checkbox"
          checked={props.isSelected}
          onChange={() => props.onSelect?.(props.document)}
        />
      </Show>

      {/* Cultural sensitivity badge */}
      <CulturalSensitivityBadge
        context={props.document.culturalContext}
        class="cultural-badge"
      />

      {/* Document thumbnail */}
      <div class="document-thumbnail">
        <div class="thumbnail-icon">
          {getDocumentIcon(props.document.contentType)}
        </div>
        <Show when={props.document.thumbnail}>
          <img
            src={props.document.thumbnail}
            alt={`Thumbnail for ${props.document.title}`}
            loading="lazy"
          />
        </Show>
      </div>

      {/* Document information */}
      <div class="document-info">
        <h3 class="document-title" title={props.document.title}>
          {props.document.title}
        </h3>

        <div class="document-metadata">
          <span class="author">{props.document.author}</span>
          <span class="separator">•</span>
          <span class="date">{formatDate(props.document.createdAt)}</span>
          <span class="separator">•</span>
          <span class="size">{formatFileSize(props.document.fileSize)}</span>
          <span class="separator">•</span>
          <span class="format">{props.document.contentType.toUpperCase()}</span>
        </div>

        <Show when={props.document.description}>
          <p class="document-description">{props.document.description}</p>
        </Show>

        {/* Tags */}
        <Show when={props.document.tags?.length > 0}>
          <div class="document-tags">
            <For each={props.document.tags.slice(0, 3)}>
              {(tag) => <span class="tag">#{tag}</span>}
            </For>
            <Show when={props.document.tags.length > 3}>
              <span class="tag-more">+{props.document.tags.length - 3}</span>
            </Show>
          </div>
        </Show>

        {/* Status indicators */}
        <div class="document-status">
          <Show when={props.document.verificationStatus === "verified"}>
            <span class="status-badge verified">✅ Verified</span>
          </Show>
          <Show when={props.document.isFavorite}>
            <span class="status-badge favorite">⭐ Favorite</span>
          </Show>
          <Show when={props.document.syncStatus === "synced"}>
            <span class="status-badge synced">🌐 Synced</span>
          </Show>
        </div>
      </div>

      {/* Action buttons - shown on hover or when selected */}
      <Show when={isHovered() || props.isSelected}>
        <div class="document-actions">
          <Show when={canAccess()}>
            <Button
              variant="ghost"
              size="sm"
              onClick={() => handleAction("preview")}
              aria-label={`Preview ${props.document.title}`}
            >
              Preview
            </Button>
            <Button
              variant="ghost"
              size="sm"
              onClick={() => handleAction("edit")}
              aria-label={`Edit ${props.document.title}`}
            >
              Edit
            </Button>
            <Button
              variant="ghost"
              size="sm"
              onClick={() => handleAction("share")}
              aria-label={`Share ${props.document.title}`}
            >
              Share
            </Button>
          </Show>
          <Show when={!canAccess()}>
            <Button
              variant="ghost"
              size="sm"
              onClick={() => handleAction("request-access")}
              aria-label={`Request access to ${props.document.title}`}
            >
              Request Access
            </Button>
          </Show>
        </div>
      </Show>
    </Card>
  );
};
```

### State Management Implementation

#### useDocumentLibrary.ts - Document Management Hook

```typescript
import { createSignal, createResource, createEffect } from "solid-js";
import { documentService } from "../services/documentService";
import { storageService } from "../services/storageService";
import { syncService } from "../services/syncService";
import { Document, StorageUsage, SyncStatus } from "@/types/core";

export const useDocumentLibrary = () => {
  const [documents, setDocuments] = createSignal<Document[]>([]);
  const [storageUsage, setStorageUsage] = createSignal<StorageUsage>();
  const [syncStatus, setSyncStatus] = createSignal<SyncStatus>();

  // Load documents with error handling
  const [documentsResource] = createResource(async () => {
    try {
      const docs = await documentService.getUserDocuments();
      setDocuments(docs);
      return docs;
    } catch (error) {
      console.error("Failed to load documents:", error);
      throw error;
    }
  });

  // Monitor storage usage
  createEffect(async () => {
    const usage = await storageService.getStorageUsage();
    setStorageUsage(usage);
  });

  // Monitor sync status
  createEffect(async () => {
    const status = await syncService.getSyncStatus();
    setSyncStatus(status);
  });

  // Document action handlers
  const handleDocumentAction = async (action: string, document: Document) => {
    switch (action) {
      case "preview":
        await documentService.openDocument(document.id);
        break;
      case "edit":
        await documentService.editDocument(document.id);
        break;
      case "share":
        await documentService.shareDocument(document.id);
        break;
      case "delete":
        await documentService.deleteDocument(document.id);
        // Refresh documents list
        const updatedDocs = documents().filter((d) => d.id !== document.id);
        setDocuments(updatedDocs);
        break;
      case "request-access":
        await documentService.requestAccess(document.id);
        break;
      default:
        console.warn(`Unknown action: ${action}`);
    }
  };

  return {
    documents,
    storageUsage,
    syncStatus,
    isLoading: documentsResource.loading,
    error: documentsResource.error,
    handleDocumentAction,
    refreshDocuments: documentsResource.refetch,
  };
};
```

#### useDocumentFilters.ts - Filtering Logic Hook

```typescript
import { createSignal, createMemo } from "solid-js";
import { Document, DocumentFilters } from "@/types/core";

const defaultFilters: DocumentFilters = {
  contentType: [],
  culturalContext: [],
  accessLevel: [],
  verificationStatus: [],
  dateRange: {
    added: { start: null, end: null },
    modified: { start: null, end: null },
    created: { start: null, end: null },
  },
  fileSize: { min: 0, max: Infinity },
  source: [],
  tags: [],
  collections: [],
  favoriteStatus: false,
  syncStatus: [],
};

export const useDocumentFilters = () => {
  const [activeFilters, setActiveFilters] =
    createSignal<DocumentFilters>(defaultFilters);

  const applyFilters = (
    documents: Document[],
    filters: DocumentFilters,
    searchQuery: string
  ) => {
    return documents.filter((document) => {
      // Text search
      if (searchQuery) {
        const searchLower = searchQuery.toLowerCase();
        const matchesSearch =
          document.title.toLowerCase().includes(searchLower) ||
          document.author?.toLowerCase().includes(searchLower) ||
          document.description?.toLowerCase().includes(searchLower) ||
          document.tags?.some((tag) => tag.toLowerCase().includes(searchLower));

        if (!matchesSearch) return false;
      }

      // Content type filter
      if (filters.contentType.length > 0) {
        if (!filters.contentType.includes(document.contentType)) return false;
      }

      // Cultural context filter
      if (filters.culturalContext.length > 0) {
        const docContext = document.culturalContext;
        const matchesCultural = filters.culturalContext.some(
          (filterContext) =>
            docContext.region === filterContext.region ||
            docContext.community === filterContext.community
        );
        if (!matchesCultural) return false;
      }

      // Verification status filter
      if (filters.verificationStatus.length > 0) {
        if (!filters.verificationStatus.includes(document.verificationStatus))
          return false;
      }

      // Date range filters
      if (filters.dateRange.added.start || filters.dateRange.added.end) {
        const addedDate = new Date(document.addedAt);
        if (
          filters.dateRange.added.start &&
          addedDate < filters.dateRange.added.start
        )
          return false;
        if (
          filters.dateRange.added.end &&
          addedDate > filters.dateRange.added.end
        )
          return false;
      }

      // File size filter
      if (
        document.fileSize < filters.fileSize.min ||
        document.fileSize > filters.fileSize.max
      ) {
        return false;
      }

      // Tags filter
      if (filters.tags.length > 0) {
        const hasMatchingTag = filters.tags.some((filterTag) =>
          document.tags?.includes(filterTag)
        );
        if (!hasMatchingTag) return false;
      }

      // Favorite status filter
      if (filters.favoriteStatus && !document.isFavorite) {
        return false;
      }

      // Sync status filter
      if (filters.syncStatus.length > 0) {
        if (!filters.syncStatus.includes(document.syncStatus)) return false;
      }

      return true;
    });
  };

  const updateFilters = (newFilters: Partial<DocumentFilters>) => {
    setActiveFilters((prev) => ({ ...prev, ...newFilters }));
  };

  const clearFilters = () => {
    setActiveFilters(defaultFilters);
  };

  const hasActiveFilters = createMemo(() => {
    const filters = activeFilters();
    return (
      filters.contentType.length > 0 ||
      filters.culturalContext.length > 0 ||
      filters.verificationStatus.length > 0 ||
      filters.tags.length > 0 ||
      filters.favoriteStatus ||
      filters.syncStatus.length > 0
    );
  });

  return {
    activeFilters,
    updateFilters,
    clearFilters,
    applyFilters,
    hasActiveFilters,
  };
};
```

## ⚡ Code Quality Guidelines

### TypeScript Implementation Standards

```typescript
// ✅ GOOD - Strict typing with cultural context
interface DocumentWithCulturalContext extends Document {
  culturalContext: CulturalContext;
  sensitivityLevel: SensitivityLevel;
  accessPermissions: AccessPermission[];
}

// ✅ GOOD - Proper error handling
const handleDocumentLoad = async (
  documentId: string
): Promise<Document | null> => {
  try {
    const document = await documentService.getDocument(documentId);

    // Cultural sensitivity check
    const hasAccess = await culturalService.checkAccess(
      document,
      getCurrentUser()
    );
    if (!hasAccess.allowed) {
      throw new CulturalAccessError(
        hasAccess.reason,
        hasAccess.educationalContent
      );
    }

    return document;
  } catch (error) {
    if (error instanceof CulturalAccessError) {
      // Show cultural education modal
      showCulturalEducationModal(error.educationalContent);
    } else {
      console.error("Failed to load document:", error);
    }
    return null;
  }
};

// ✅ GOOD - Performance optimization with memoization
const DocumentGrid: Component<DocumentGridProps> = (props) => {
  const memoizedDocuments = createMemo(() => {
    return props.documents.map((doc) => ({
      ...doc,
      displayTitle: truncateTitle(doc.title, 50),
      formattedSize: formatFileSize(doc.fileSize),
      culturalBadge: getCulturalBadgeInfo(doc.culturalContext),
    }));
  });

  return (
    <div class="document-grid">
      <For each={memoizedDocuments()}>
        {(document) => (
          <DocumentCard
            document={document}
            onSelect={props.onDocumentSelect}
            onAction={props.onDocumentAction}
          />
        )}
      </For>
    </div>
  );
};
```

### Security Implementation Patterns

```typescript
// Input validation for document operations
const validateDocumentInput = (input: DocumentInput): ValidationResult => {
  const errors: string[] = [];

  // Title validation
  if (!input.title || input.title.trim().length === 0) {
    errors.push("Document title is required");
  }
  if (input.title.length > 255) {
    errors.push("Document title too long");
  }

  // Cultural context validation
  if (input.culturalContext) {
    const culturalValidation = validateCulturalContext(input.culturalContext);
    if (!culturalValidation.valid) {
      errors.push(...culturalValidation.errors);
    }
  }

  // File validation
  if (input.file) {
    const fileValidation = validateFile(input.file);
    if (!fileValidation.valid) {
      errors.push(...fileValidation.errors);
    }
  }

  return {
    valid: errors.length === 0,
    errors,
    sanitizedInput: sanitizeDocumentInput(input),
  };
};

// Cultural access control
const checkCulturalAccess = async (
  document: Document,
  user: User,
  action: AccessAction
): Promise<AccessResult> => {
  const culturalContext = document.culturalContext;

  // Check sensitivity level
  if (culturalContext.sensitivityLevel >= SensitivityLevel.SACRED) {
    const communityMembership = await checkCommunityMembership(
      user,
      culturalContext.community
    );

    if (!communityMembership.isMember) {
      return {
        allowed: false,
        reason: "Sacred content requires community membership",
        educationalContent: culturalContext.educationalContent,
        requestAccessUrl: communityMembership.requestUrl,
      };
    }
  }

  // Check specific protocols
  for (const protocol of culturalContext.protocols) {
    const protocolCheck = await validateProtocol(user, protocol, action);
    if (!protocolCheck.allowed) {
      return protocolCheck;
    }
  }

  return { allowed: true };
};
```

## 🛠️ Implementation Prompts

### Development Checklist

- [ ] **Component Architecture**: Implement component hierarchy following SOLID principles
- [ ] **State Management**: Setup reactive state with proper separation of concerns
- [ ] **Cultural Sensitivity**: Implement cultural access controls and educational features
- [ ] **Performance**: Optimize for large document collections (10,000+ documents)
- [ ] **Accessibility**: Ensure WCAG 2.1 AA compliance with keyboard navigation
- [ ] **Security**: Implement input validation and cultural protocol enforcement
- [ ] **Error Handling**: Graceful error handling with user-friendly messages
- [ ] **Testing**: Comprehensive unit and integration tests

### Code Review Criteria

1. **SOLID Principles Compliance**

   - Single Responsibility: Each component has one clear purpose
   - Open/Closed: Components are extensible without modification
   - Liskov Substitution: Derived components can substitute base components
   - Interface Segregation: Interfaces are specific and focused
   - Dependency Inversion: Depend on abstractions, not concretions

2. **Cultural Sensitivity Implementation**

   - Proper sensitivity level classification
   - Cultural protocol enforcement
   - Educational content integration
   - Community validation workflows

3. **Performance Optimization**

   - Efficient rendering for large document sets
   - Proper memoization and caching
   - Lazy loading for thumbnails and metadata
   - Optimized search and filtering

4. **Security Standards**
   - Input validation and sanitization
   - Cultural access control enforcement
   - Secure file handling
   - Audit logging for sensitive operations

## 🧪 Testing & Validation

### Unit Testing Strategy

```typescript
// Document card component tests
describe("DocumentCard", () => {
  it("displays document information correctly", () => {
    const mockDocument = createMockDocument({
      title: "Test Document",
      author: "Test Author",
      culturalContext: createMockCulturalContext(),
    });

    render(() => <DocumentCard document={mockDocument} />);

    expect(screen.getByText("Test Document")).toBeInTheDocument();
    expect(screen.getByText("Test Author")).toBeInTheDocument();
  });

  it("shows cultural sensitivity warning for sacred content", () => {
    const sacredDocument = createMockDocument({
      culturalContext: {
        sensitivityLevel: SensitivityLevel.SACRED,
        community: "Indigenous Community",
      },
    });

    render(() => <DocumentCard document={sacredDocument} />);

    expect(screen.getByText("Sacred Content")).toBeInTheDocument();
    expect(screen.getByText("Request Access")).toBeInTheDocument();
  });

  it("handles bulk selection correctly", () => {
    const mockDocument = createMockDocument();
    const onSelect = vi.fn();

    render(() => (
      <DocumentCard
        document={mockDocument}
        onSelect={onSelect}
        isSelected={false}
      />
    ));

    const checkbox = screen.getByRole("checkbox");
    fireEvent.click(checkbox);

    expect(onSelect).toHaveBeenCalledWith(mockDocument);
  });
});

// Cultural access control tests
describe("Cultural Access Control", () => {
  it("allows access to public content", async () => {
    const publicDocument = createMockDocument({
      culturalContext: { sensitivityLevel: SensitivityLevel.PUBLIC },
    });
    const user = createMockUser();

    const result = await checkCulturalAccess(publicDocument, user, "view");

    expect(result.allowed).toBe(true);
  });

  it("restricts access to sacred content for non-community members", async () => {
    const sacredDocument = createMockDocument({
      culturalContext: {
        sensitivityLevel: SensitivityLevel.SACRED,
        community: "Indigenous Community",
      },
    });
    const outsideUser = createMockUser({ communities: [] });

    const result = await checkCulturalAccess(
      sacredDocument,
      outsideUser,
      "view"
    );

    expect(result.allowed).toBe(false);
    expect(result.reason).toContain("community membership");
    expect(result.educationalContent).toBeDefined();
  });
});
```

### Performance Testing

```typescript
// Performance benchmarks
describe("MyDocumentsPage Performance", () => {
  it("loads 1000+ documents within 2 seconds", async () => {
    const startTime = performance.now();
    const documents = createMockDocuments(1000);

    render(() => <MyDocumentsPage />);

    await waitFor(() => {
      expect(screen.getAllByTestId("document-card")).toHaveLength(1000);
    });

    const loadTime = performance.now() - startTime;
    expect(loadTime).toBeLessThan(2000);
  });

  it("applies filters within 300ms", async () => {
    const documents = createMockDocuments(5000);
    render(() => <MyDocumentsPage />);

    const startTime = performance.now();

    // Apply content type filter
    const pdfFilter = screen.getByLabelText("PDF Documents");
    fireEvent.click(pdfFilter);

    await waitFor(() => {
      expect(screen.getAllByTestId("document-card").length).toBeLessThan(5000);
    });

    const filterTime = performance.now() - startTime;
    expect(filterTime).toBeLessThan(300);
  });
});
```

### Accessibility Testing

```typescript
// Accessibility validation
describe("MyDocumentsPage Accessibility", () => {
  it("supports keyboard navigation", () => {
    render(() => <MyDocumentsPage />);

    // Tab through interactive elements
    const firstCard = screen.getAllByTestId("document-card")[0];
    firstCard.focus();

    fireEvent.keyDown(firstCard, { key: "Tab" });

    expect(document.activeElement).not.toBe(firstCard);
  });

  it("provides proper ARIA labels", () => {
    const mockDocument = createMockDocument({ title: "Test Document" });

    render(() => <DocumentCard document={mockDocument} />);

    const previewButton = screen.getByLabelText("Preview Test Document");
    expect(previewButton).toBeInTheDocument();
  });

  it("supports screen readers", () => {
    render(() => <MyDocumentsPage />);

    const mainContent = screen.getByRole("main");
    expect(mainContent).toHaveAttribute("aria-label");

    const filterSidebar = screen.getByRole("complementary");
    expect(filterSidebar).toHaveAttribute("aria-label");
  });
});
```

---

_This technical implementation guide ensures MyDocumentsPage is built with the highest standards of code quality, cultural sensitivity, performance, and accessibility while following SOLID architecture principles._
