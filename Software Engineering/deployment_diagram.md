```mermaid
graph TB
    %% Client Node
    subgraph Client[Client Application]
        UI[User Interface]
        LocalCache[Local Cache]
        P2PClient[P2P Client]
    end

    %% Network Nodes
    subgraph Network[P2P Network]
        Peer1[Peer Node 1]
        Peer2[Peer Node 2]
        Peer3[Peer Node 3]
    end

    %% IPFS Network
    subgraph IPFSNetwork[IPFS Network]
        IPFSNode1[IPFS Node 1]
        IPFSNode2[IPFS Node 2]
        IPFSNode3[IPFS Node 3]
    end

    %% Connections
    UI --> LocalCache
    UI --> P2PClient
    P2PClient --> Peer1
    P2PClient --> Peer2
    P2PClient --> Peer3

    Peer1 --> IPFSNode1
    Peer2 --> IPFSNode2
    Peer3 --> IPFSNode3

    IPFSNode1 <--> IPFSNode2
    IPFSNode2 <--> IPFSNode3
    IPFSNode3 <--> IPFSNode1

    %% Storage
    subgraph Storage[Local Storage]
        SQLite[(SQLite DB)]
        FileSystem[File System]
    end

    %% SQLite Connections
    LocalCache --> SQLite
    UI --> SQLite
    P2PClient --> SQLite

    %% File System Connections
    LocalCache --> FileSystem

    %% SQLite Responsibilities
    subgraph SQLiteRoles[SQLite Responsibilities]
        Metadata[Metadata Storage]
        Indexes[Search Indexes]
        CacheState[Cache State]
        SyncState[Sync State]
    end

    SQLite --> Metadata
    SQLite --> Indexes
    SQLite --> CacheState
    SQLite --> SyncState
```
