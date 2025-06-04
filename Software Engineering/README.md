# AlLibrary Software Engineering Documentation

This folder contains the software engineering documentation for the AlLibrary project, including various UML diagrams in Mermaid format.

## Diagrams Overview

### Class Diagram (`class_diagram.md`)

The class diagram shows the main classes and their relationships in the AlLibrary system. It includes:

- Core domain classes (Document, Content, Metadata, Version)
- P2P Network classes (Peer, NetworkManager, ContentRouter)
- Storage classes (ContentStore, IPFSManager)
- UI classes (DocumentViewer, SearchEngine)

### Sequence Diagram (`sequence_diagram.md`)

The sequence diagrams illustrate the main operations in the system:

- Document sharing process
- Document retrieval process
  These diagrams show the interaction between different components and the flow of operations.

### Component Diagram (`component_diagram.md`)

The component diagram provides a high-level view of the system architecture, showing:

- Frontend components
- Core services
- P2P Network components
- Storage components
- Security components

### State Diagram (`state_diagram.md`)

The state diagram shows the lifecycle of documents in the system:

- Document states (Draft, UnderReview, Verified, Published, Archived)
- State transitions and conditions
- Nested states for complex processes

### Activity Diagram (`activity_diagram.md`)

The activity diagram illustrates the search process flow:

- Query processing
- Local and network search
- Result ranking and filtering
- Pagination and display

### Deployment Diagram (`deployment_diagram.md`)

The deployment diagram shows the physical architecture:

- Client application components
- P2P network nodes
- IPFS network structure
- Local storage components

## How to Use These Diagrams

1. **Class Diagram**: Use this to understand the object-oriented structure of the system and the relationships between different classes.

2. **Sequence Diagram**: Use these to understand the flow of operations and how different components interact during specific processes.

3. **Component Diagram**: Use this to understand the high-level architecture and how different parts of the system are organized.

4. **State Diagram**: Use this to understand the lifecycle of documents and the conditions for state transitions.

5. **Activity Diagram**: Use this to understand the detailed flow of complex processes like search and document handling.

6. **Deployment Diagram**: Use this to understand the physical deployment of the system components and their interactions.

## Diagram Format

All diagrams are written in Mermaid notation, which can be rendered using:

- Mermaid extension in VS Code
- GitHub's built-in Mermaid support
- Online Mermaid Live Editor
- Local Mermaid installation

## Updating Diagrams

When making changes to the system:

1. Update the relevant diagrams to reflect the changes
2. Ensure all relationships and dependencies are properly represented
3. Keep the documentation in sync with the actual implementation

## Additional Documentation

For more detailed information about specific components, refer to:

- Technical documentation in the `Docs` folder
- API documentation
- Implementation guides
