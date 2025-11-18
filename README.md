# NexusShield

**NexusShield** is an advanced fraud detection system that leverages Graph Neural Networks (GNNs) to identify coordinated fraud patterns. By modeling accounts, devices, IPs, and transactions as an interconnected graph, it uncovers hidden fraud rings and generates actionable cluster-level alerts to prevent organized attacks before they cause significant financial damage.

## 🎯 Overview

Traditional fraud detection systems analyze transactions in isolation, missing coordinated attacks that span multiple entities. NexusShield takes a fundamentally different approach by understanding the **connections** between entities. When fraudsters coordinate their activities, they leave behind a trail of relationships—shared devices, IP addresses, payment methods, and transaction patterns. NexusShield models these relationships as a graph and uses deep learning to identify suspicious clusters and patterns that would otherwise remain invisible.

## ✨ Key Features

- **Graph-Based Modeling**: Represents accounts, devices, IPs, and transactions as nodes in a heterogeneous graph
- **GNN-Powered Detection**: Uses Graph Neural Networks to learn complex patterns and relationships
- **Fraud Ring Detection**: Identifies coordinated fraud networks that traditional systems miss
- **Risk Scoring**: Assigns risk scores to individual nodes and entire clusters
- **Real-Time Alerts**: Generates actionable alerts at the cluster level for rapid response
- **Scalable Architecture**: Designed to handle large-scale transaction volumes
- **Early Detection**: Catches organized attacks before they escalate

## 🏗️ Architecture

NexusShield operates on a graph-based architecture that transforms raw transaction data into actionable fraud insights:

```
┌─────────────────────────────────────────────────────────┐
│                    Data Ingestion                        │
│  (Accounts, Devices, IPs, Transactions)                  │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              Graph Construction Layer                    │
│  • Node Creation (Accounts, Devices, IPs, Transactions)  │
│  • Edge Creation (Relationships & Connections)          │
│  • Feature Engineering                                  │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│            Graph Neural Network Model                    │
│  • Node Embedding Generation                            │
│  • Graph Convolutional Layers                           │
│  • Cluster Detection                                    │
│  • Risk Score Computation                               │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              Alert & Action System                       │
│  • High-Risk Node Identification                        │
│  • Fraud Ring Clustering                                │
│  • Actionable Alert Generation                          │
└─────────────────────────────────────────────────────────┘
```

## 📁 Project Structure

The project is organized into a modular structure that separates concerns and enables scalable development:

```
NexusShield/
├── config/                    # Configuration files
│   ├── config.yaml           # Main configuration
│   └── schema.json           # Data schema definitions
│
├── data/                      # Data directories
│   ├── raw/                  # Raw input data
│   ├── processed/            # Processed datasets
│   └── external/             # External data sources
│
├── src/nexusshield/          # Core source code
│   ├── __init__.py
│   ├── utils/                # Utility functions
│   │   ├── logging.py       # Logging configuration
│   │   ├── io.py            # I/O operations
│   │   └── graph_ops.py     # Graph operations
│   ├── data/                 # Data processing
│   │   ├── preprocess.py    # Data preprocessing
│   │   ├── feature_engineering.py  # Feature creation
│   │   └── graph_builder.py # Graph construction
│   ├── models/               # ML models
│   │   ├── gnn.py           # Graph Neural Network
│   │   ├── trainer.py       # Model training
│   │   └── evaluator.py     # Model evaluation
│   ├── pipelines/            # End-to-end pipelines
│   │   ├── train_pipeline.py      # Training pipeline
│   │   ├── inference_pipeline.py  # Inference pipeline
│   │   └── monitoring_pipeline.py # Monitoring pipeline
│   └── api/                  # API layer
│       ├── __init__.py
│       ├── server.py         # API server
│       └── schemas.py        # API schemas
│
├── notebooks/                # Jupyter notebooks
│   ├── EDA.ipynb            # Exploratory data analysis
│   ├── Graph_Construction.ipynb  # Graph building experiments
│   ├── Model_Experiments.ipynb   # Model experimentation
│   └── Monitoring_Demo.ipynb     # Monitoring demonstrations
│
├── scripts/                  # Standalone scripts
│   ├── run_training.py      # Training script
│   ├── run_inference.py     # Inference script
│   ├── build_graph.py       # Graph building script
│   └── export_model.py      # Model export script
│
├── tests/                    # Test suite
│   ├── test_data.py         # Data processing tests
│   ├── test_graph_builder.py # Graph builder tests
│   ├── test_gnn.py          # GNN model tests
│   └── test_api.py          # API tests
│
├── docker/                   # Docker configuration
│   ├── Dockerfile           # Container definition
│   ├── docker-compose.yaml  # Multi-container setup
│   └── start.sh             # Startup script
│
└── nexusshield/              # Package metadata
    ├── README.md
    ├── requirements.txt     # Python dependencies
    └── pyproject.toml        # Project configuration
```

### How the Project Unfolds

**Data Flow**: Raw data enters through `data/raw/`, gets preprocessed in `src/nexusshield/data/preprocess.py`, and features are engineered in `feature_engineering.py`. The `graph_builder.py` module constructs the heterogeneous graph that serves as the foundation for all analysis.

**Model Development**: The GNN architecture lives in `src/nexusshield/models/gnn.py`, trained via `trainer.py` and evaluated with `evaluator.py`. The `notebooks/` directory provides interactive environments for experimentation and analysis.

**Production Deployment**: End-to-end pipelines in `src/nexusshield/pipelines/` orchestrate the complete workflow. The `api/` layer exposes REST endpoints for real-time fraud detection, while `scripts/` provide command-line interfaces for batch operations.

**Infrastructure**: Docker configurations in `docker/` enable containerized deployment, while `config/` centralizes all configuration management.

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip or conda package manager
- (Optional) CUDA-enabled GPU for faster training

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/NexusShield.git
   cd NexusShield
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r nexusshield/requirements.txt
   ```

4. **Configure the system**
   ```bash
   # Edit config/config.yaml with your settings
   ```

### Configuration

The `config/config.yaml` file contains all system configuration:

```yaml
data:
  input_path: "data/raw/transactions.csv"
  account_path: "data/raw/accounts.csv"
  
model:
  embedding_dim: 128
  num_layers: 3
  learning_rate: 0.001
  
detection:
  risk_threshold: 0.7
  cluster_min_size: 3
  alert_enabled: true
```

## 📖 Usage

### Command Line Interface

```bash
# Build the graph from raw data
python scripts/build_graph.py --input data/raw/transactions.csv

# Train the model
python scripts/run_training.py --config config/config.yaml

# Run inference
python scripts/run_inference.py --input data/processed/test_data.csv

# Export trained model
python scripts/export_model.py --output models/nexusshield_model.pth
```

### Python API

```python
from src.nexusshield.pipelines import inference_pipeline
from src.nexusshield.utils.io import load_config

# Load configuration
config = load_config("config/config.yaml")

# Run inference pipeline
results = inference_pipeline.run(
    input_path="data/processed/test_data.csv",
    config=config
)

# Access results
alerts = results.get_alerts()
risk_scores = results.get_risk_scores()
```

### API Server

```bash
# Start the API server
python -m src.nexusshield.api.server

# The API will be available at http://localhost:8000
```

## 🔍 How It Works

1. **Data Preprocessing** (`src/nexusshield/data/preprocess.py`): Raw transaction data is cleaned, validated, and normalized using the schema defined in `config/schema.json`.

2. **Feature Engineering** (`src/nexusshield/data/feature_engineering.py`): Each entity (account, device, IP, transaction) is enriched with features capturing behavioral patterns, temporal dynamics, and contextual information.

3. **Graph Construction** (`src/nexusshield/data/graph_builder.py`): A heterogeneous graph is built where nodes represent entities and edges represent relationships. This graph structure enables the system to capture complex multi-entity interactions.

4. **GNN Processing** (`src/nexusshield/models/gnn.py`): Graph Neural Networks propagate information through the graph, allowing nodes to aggregate information from their neighbors. Multiple layers capture complex multi-hop relationships, and learned embeddings capture both structural and behavioral patterns.

5. **Risk Assessment** (`src/nexusshield/models/evaluator.py`): The model computes individual node risk scores, cluster-level risk metrics, and anomaly detection scores.

6. **Alert Generation** (`src/nexusshield/pipelines/monitoring_pipeline.py`): High-risk clusters trigger alerts with affected entities, risk scores, evidence, and recommended actions.

## 📊 Example Output

```
Alert ID: ALERT-2024-001
Risk Level: HIGH
Cluster Size: 15 entities
Affected Accounts: 8
Shared Devices: 3
Shared IPs: 2
Risk Score: 0.87

Entities:
- Account: ACC-12345 (Risk: 0.92)
- Account: ACC-67890 (Risk: 0.89)
- Device: DEV-ABC123 (Risk: 0.85)
- IP: 192.168.1.100 (Risk: 0.78)

Recommended Action: Block cluster and investigate
```

## 🛠️ Development

### Running Tests

```bash
# Run all tests
pytest tests/

# Run specific test suite
pytest tests/test_gnn.py
pytest tests/test_api.py
```

### Development Workflow

1. **Exploration**: Use notebooks in `notebooks/` for interactive analysis
2. **Implementation**: Add features in `src/nexusshield/`
3. **Testing**: Write tests in `tests/` following the existing patterns
4. **Integration**: Use pipelines in `src/nexusshield/pipelines/` for end-to-end validation

### Docker Deployment

```bash
# Build and run with Docker Compose
cd docker
docker-compose up --build

# Or use the startup script
./start.sh
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Built with PyTorch Geometric for graph neural network operations
- Inspired by research in graph-based fraud detection

---

**Note**: This is an active development project. Features and APIs may change as the system evolves.
