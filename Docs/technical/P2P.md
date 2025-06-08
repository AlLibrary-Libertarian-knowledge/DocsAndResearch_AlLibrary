# AlLibrary P2P Architecture

## 🌐 Core P2P Concepts

### What is P2P in AlLibrary?

AlLibrary uses a simple peer-to-peer architecture inspired by BitTorrent:

- Each user's device becomes a node in the network
- Documents are stored in a local folder
- Documents in the folder are automatically shared when connected
- Downloaded documents are saved to the same folder
- No central server needed for file distribution

### Basic Architecture

```
┌─────────────────────────────────────────┐
│            User's Computer              │
├─────────────────┬───────────────────────┤
│   AlLibrary     │     Local Folder      │
│    Application  │                       │
│                 │  ┌─────────────────┐  │
│  ┌───────────┐  │  │  Document 1     │  │
│  │  Search   │  │  │  (Shared)       │  │
│  └───────────┘  │  └─────────────────┘  │
│                 │                       │
│  ┌───────────┐  │  ┌─────────────────┐  │
│  │  Browse   │  │  │  Document 2     │  │
│  └───────────┘  │  │  (Shared)       │  │
│                 │  └─────────────────┘  │
│  ┌───────────┐  │                       │
│  │  Download │  │  ┌─────────────────┐  │
│  └───────────┘  │  │  Document 3     │  │
│                 │  │  (Downloaded)   │  │
│                 │  └─────────────────┘  │
└─────────────────┴───────────────────────┘
```

## 🔧 How It Works

### 1. Local Storage

- **Shared Folder**: All documents are stored in a designated folder
- **Automatic Sharing**: Documents in the folder are automatically shared
- **Download Location**: New downloads go to the same folder
- **File Management**: Users can add/remove files from the folder

### 2. Network Connection

```
┌─────────┐     ┌─────────┐     ┌─────────┐
│  Node A │◄───►│  Node B │◄───►│  Node C │
└────┬────┘     └────┬────┘     └────┬────┘
     │               │               │
     ▼               ▼               ▼
┌─────────┐     ┌─────────┐     ┌─────────┐
│  Files  │     │  Files  │     │  Files  │
└─────────┘     └─────────┘     └─────────┘
```

### 3. Basic Operations

1. **Searching Documents**

   - User enters search terms in the app
   - App queries the P2P network
   - Results show available documents
   - User can select to download

2. **Downloading Documents**

   - User selects a document
   - App finds peers with the file
   - Downloads in chunks from multiple peers
   - Saves to the shared folder
   - Automatically becomes available for sharing

3. **Sharing Documents**
   - Add files to the shared folder
   - App automatically shares them
   - Other users can find and download
   - Remove files to stop sharing

## 📦 Implementation Details

### 1. File Management

```
┌─────────────────┐
│  Shared Folder  │
├─────────────────┤
│  - Document 1   │
│  - Document 2   │
│  - Document 3   │
└─────────────────┘
```

- **Location**: User-defined folder
- **Permissions**: Read/Write access
- **Organization**: Simple file structure
- **Sharing**: Automatic when connected

### 2. Network Connection

- **Connection**: Automatic when app starts
- **Discovery**: Uses DHT (Distributed Hash Table)
- **Peers**: Connects to other AlLibrary users
- **Bandwidth**: Configurable upload/download limits

### 3. Search & Discovery

- **Search**: Local index + network query
- **Results**: Shows available documents
- **Details**: File size, availability, sources
- **Download**: One-click to shared folder

## 🎯 User Experience

### 1. Basic Usage

1. **Start the App**

   - App connects to network
   - Shared folder is monitored
   - Ready to search/download

2. **Search for Documents**

   - Enter search terms
   - Browse results
   - Select to download

3. **Manage Files**
   - Add files to share
   - Remove files to stop sharing
   - Organize as needed

### 2. Connection Management

- **Connect**: App starts automatically
- **Disconnect**: Close app or toggle connection
- **Bandwidth**: Set upload/download limits
- **Status**: Shows connection state

## 🔒 Security Basics

### 1. File Integrity

- **Verification**: Hash checking
- **Corruption**: Automatic detection
- **Repair**: Re-download corrupted chunks

### 2. Basic Privacy

- **IP Address**: Visible to peers
- **Files**: Only shared files visible
- **Search**: Only shared content indexed

## 📈 Performance

### 1. Resource Usage

- **Memory**: Moderate (like BitTorrent)
- **CPU**: Low to moderate
- **Disk**: Only shared folder
- **Network**: Configurable bandwidth

### 2. Optimization

- **Downloads**: Chunked transfer
- **Uploads**: Rate limiting
- **Search**: Local caching
- **Storage**: Efficient file handling

## 🔧 Technical Requirements

### 1. Network

- **Port**: One open port (configurable)
- **Protocol**: TCP/UDP for P2P
- **Bandwidth**: Adjustable limits

### 2. Storage

- **Space**: Depends on shared files
- **Access**: Read/Write permissions
- **Organization**: Simple folder structure

## 🚀 Getting Started

### 1. Setup

1. **Install App**

   - Download and install
   - Choose shared folder
   - Set bandwidth limits

2. **First Run**
   - App connects to network
   - Shared folder is ready
   - Start searching/downloading

### 2. Basic Usage

1. **Search**

   - Use search interface
   - Browse results
   - Download files

2. **Share**
   - Add files to folder
   - Automatic sharing
   - Remove to stop sharing

## 🔌 Connection Methods

### 1. Direct P2P (Basic Method)

```
┌─────────┐     ┌─────────┐     ┌─────────┐
│  Node A │◄───►│  Node B │◄───►│  Node C │
└─────────┘     └─────────┘     └─────────┘
```

**Requirements**:

- Open port (configurable, default 6881)
- Port forwarding on router
- Public IP address
- Direct internet connection

**Pros**:

- Fastest connection
- Lowest latency
- Simple implementation
- Less resource usage

**Cons**:

- Requires port forwarding
- IP address visible to peers
- May be blocked by ISPs
- Doesn't work behind strict firewalls

### 2. NAT Traversal (UPnP/STUN)

```
┌─────────┐     ┌─────────┐     ┌─────────┐
│  Node A │◄───►│  Node B │◄───►│  Node C │
└─────────┘     └─────────┘     └─────────┘
      ▲               ▲               ▲
      │               │               │
      └───────────────┴───────────────┘
                    │
                    ▼
            ┌───────────────┐
            │  STUN Server  │
            └───────────────┘
```

**Requirements**:

- UPnP enabled router or STUN server
- No port forwarding needed
- Works behind most NATs

**Pros**:

- No manual port forwarding
- Works in most home networks
- Good performance
- Simple for users

**Cons**:

- May not work in corporate networks
- Still exposes IP address
- Some ISPs block UPnP

### 3. Tor Network (When Needed)

```
┌─────────┐     ┌─────────┐     ┌─────────┐
│  Node A │◄───►│  Node B │◄───►│  Node C │
└─────────┘     └─────────┘     └─────────┘
      ▲               ▲               ▲
      │               │               │
      └───────────────┴───────────────┘
                    │
                    ▼
            ┌───────────────┐
            │   Tor Network │
            └───────────────┘
```

**When to Use Tor**:

- Behind strict firewalls
- In countries with internet restrictions
- When privacy is crucial
- When ISP blocks P2P

**Requirements**:

- Tor installed
- More bandwidth
- Higher latency acceptable
- Privacy-focused setup

**Pros**:

- Works everywhere
- Hides IP address
- Bypasses restrictions
- Enhanced privacy

**Cons**:

- Slower speeds
- More complex setup
- Higher resource usage
- May be blocked in some countries

### 4. Hybrid Approach (Recommended)

```
┌─────────┐     ┌─────────┐     ┌─────────┐
│  Node A │◄───►│  Node B │◄───►│  Node C │
└─────────┘     └─────────┘     └─────────┘
      ▲               ▲               ▲
      │               │               │
      └───────────────┴───────────────┘
                    │
                    ▼
            ┌───────────────┐
            │  Connection   │
            │   Manager     │
            └───────────────┘
                    │
                    ▼
            ┌───────────────┐
            │  Tor (if needed) │
            └───────────────┘
```

**How It Works**:

1. Try direct P2P first
2. If that fails, try NAT traversal
3. If that fails, use Tor
4. Automatically switch between methods

**Implementation**:

```typescript
class ConnectionManager {
  async connect() {
    // Try direct P2P first
    if (await this.tryDirectP2P()) {
      return "direct";
    }

    // Try NAT traversal
    if (await this.tryNATTraversal()) {
      return "nat";
    }

    // Fall back to Tor
    return await this.connectViaTor();
  }
}
```

### 5. Connection Setup

1. **Initial Connection**:

   - App starts
   - Tries direct P2P
   - Falls back to NAT traversal
   - Uses Tor if needed

2. **Peer Discovery**:

   - DHT for peer lookup
   - Bootstrap nodes for initial connection
   - Peer exchange for finding more peers
   - Automatic reconnection

3. **Bandwidth Management**:
   - Configurable upload/download limits
   - Automatic throttling
   - Connection pooling
   - Resource optimization

### 6. User Experience

1. **Automatic Mode**:

   - App tries all methods
   - Uses best available
   - No user configuration needed

2. **Manual Mode**:
   - User can choose method
   - Set connection preferences
   - Configure bandwidth
   - Monitor connections

### 7. Technical Requirements

1. **Network**:

   - TCP/UDP support
   - Configurable ports
   - Bandwidth control
   - Connection management

2. **Security**:
   - Encrypted connections
   - Peer verification
   - Content integrity
   - Basic privacy

## 🔄 Network Switching & Tor Toggle

### 1. Simple Tor Toggle

```
┌─────────────────────────────────┐
│  Network Settings               │
├─────────────────────────────────┤
│  [x] Enable Tor Network         │
│      (Slower but more private)  │
│                                │
│  Current Network:               │
│  ► Tor Network (Active)        │
│                                │
│  Connected Peers: 12           │
│  Download Speed: 2.5 MB/s      │
│  Upload Speed: 1.8 MB/s        │
│                                │
│  [Apply Changes]               │
└─────────────────────────────────┘
```

### 2. Network Switching Implementation

```typescript
class NetworkManager {
  private isTorEnabled: boolean = false;
  private activePeers: Set<string> = new Set();
  private connectionManager: ConnectionManager;

  constructor() {
    this.connectionManager = new ConnectionManager();
  }

  // Toggle Tor network
  async toggleTor(enabled: boolean) {
    // Store current peers
    const currentPeers = Array.from(this.activePeers);

    // Disconnect from current network
    await this.connectionManager.disconnect();

    // Enable/disable Tor
    this.isTorEnabled = enabled;

    // Reconnect to new network
    await this.connectionManager.connect(this.isTorEnabled);

    // Restore peer connections
    await this.restorePeers(currentPeers);
  }

  // Restore peer connections
  private async restorePeers(peers: string[]) {
    for (const peer of peers) {
      try {
        await this.connectionManager.connectToPeer(peer);
        this.activePeers.add(peer);
      } catch (error) {
        console.warn(`Failed to reconnect to peer ${peer}`);
      }
    }
  }

  // Get current network status
  getNetworkStatus() {
    return {
      isTorEnabled: this.isTorEnabled,
      activePeers: this.activePeers.size,
      currentMethod: this.connectionManager.getCurrentMethod(),
      speeds: this.connectionManager.getSpeeds(),
    };
  }
}

// Usage in UI
const networkManager = new NetworkManager();

// Toggle button handler
async function handleTorToggle(enabled: boolean) {
  try {
    // Show loading state
    updateUIState("switching");

    // Switch networks
    await networkManager.toggleTor(enabled);

    // Update UI with new status
    const status = networkManager.getNetworkStatus();
    updateUIWithStatus(status);
  } catch (error) {
    showError("Failed to switch networks");
  } finally {
    updateUIState("ready");
  }
}
```

### 3. Seamless Network Switching

1. **Before Switching**:

   - Store current peer list
   - Save active downloads/uploads
   - Cache current network state

2. **During Switch**:

   - Show loading indicator
   - Maintain file transfers
   - Keep search results

3. **After Switching**:
   - Restore peer connections
   - Resume transfers
   - Update UI status

### 4. User Experience

```
┌─────────────────────────────────┐
│  Switching Networks...          │
├─────────────────────────────────┤
│  ► Storing current state       │
│  ► Disconnecting from Tor      │
│  ► Connecting to Direct P2P    │
│  ► Restoring peer connections  │
│  ► Resuming transfers          │
└─────────────────────────────────┘
```

### 5. Network State Management

```typescript
interface NetworkState {
  isTorEnabled: boolean;
  activePeers: string[];
  currentTransfers: Transfer[];
  searchResults: SearchResult[];
}

class NetworkStateManager {
  private state: NetworkState;

  // Save current state
  async saveState() {
    this.state = {
      isTorEnabled: networkManager.isTorEnabled,
      activePeers: Array.from(networkManager.activePeers),
      currentTransfers: transferManager.getActiveTransfers(),
      searchResults: searchManager.getCurrentResults(),
    };
  }

  // Restore previous state
  async restoreState() {
    // Restore peer connections
    await networkManager.restorePeers(this.state.activePeers);

    // Resume transfers
    await transferManager.resumeTransfers(this.state.currentTransfers);

    // Restore search results
    searchManager.restoreResults(this.state.searchResults);
  }
}
```

### 6. Implementation Details

1. **State Preservation**:

   - Save peer connections
   - Cache search results
   - Store transfer states
   - Remember user preferences

2. **Smooth Transition**:

   - Gradual peer reconnection
   - Background state restoration
   - Progress indicators
   - Error handling

3. **User Feedback**:

   - Network status updates
   - Connection progress
   - Speed indicators
   - Error messages

4. **Error Recovery**:
   - Automatic retry
   - Fallback options
   - State recovery
   - User notifications

### 7. Code Example: UI Implementation

```typescript
// Tor Toggle Component
function TorToggle() {
  const [isTorEnabled, setIsTorEnabled] = useState(false);
  const [isSwitching, setIsSwitching] = useState(false);

  const handleToggle = async (enabled: boolean) => {
    setIsSwitching(true);
    try {
      await networkManager.toggleTor(enabled);
      setIsTorEnabled(enabled);
    } catch (error) {
      showError("Failed to switch networks");
    } finally {
      setIsSwitching(false);
    }
  };

  return (
    <div className="network-settings">
      <Switch
        checked={isTorEnabled}
        onChange={handleToggle}
        disabled={isSwitching}
      />
      <span>Enable Tor Network</span>
      {isSwitching && <LoadingIndicator />}
    </div>
  );
}
```

---

This simplified P2P architecture ensures:

- Easy to use
- Simple file sharing
- Automatic distribution
- Basic security
- Resource efficient
- User controlled
