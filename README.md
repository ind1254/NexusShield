# NexusShield GNN Fraud Ring Detector

**NexusShield** is a production-ready Graph Neural Network (GNN) system designed to detect coordinated fraud rings in financial transaction data. By modeling accounts, devices, IPs, transactions, and merchants as nodes in a heterogeneous graph, NexusShield identifies hidden fraud networks through message passing and node embedding techniques.

## Overview

Traditional fraud detection systems analyze transactions in isolation, missing coordinated attacks that span multiple entities. NexusShield leverages Graph Neural Networks to understand the **connections** between entities. When fraudsters coordinate their activities, they create patterns of shared devices, IP addresses, and transaction behaviors that form detectable fraud rings in the graph structure.

## Key Features

- **Heterogeneous Graph Modeling**: Represents multiple entity types (accounts, devices, IPs, transactions, merchants) as nodes with type-specific features
- **GNN-Powered Detection**: Uses Graph Convolutional Networks (GCN), Graph Attention Networks (GAT), and GraphSAGE layers for message passing
- **Dual Learning Objectives**: Supports both node classification (fraud/legitimate) and link prediction (suspicious relationships)
- **Production-Ready Pipelines**: Modular pipelines for graph construction, training, and inference
- **Comprehensive Evaluation**: Metrics for AUC-ROC, AUC-PR, and fraud ring detection performance

## Project Structure

```
NexusShield/
├── configs/                    # Configuration files
│   └── config.yaml            # Baseline YAML configs
├── data/                       # Data directories
│   ├── raw/                   # Raw input data
│   ├── interim/               # Intermediate processed data
│   └── processed/             # Final processed datasets
├── docs/                       # Documentation
│   ├── architecture.md        # System architecture
│   ├── fraud_ring_taxonomy.md # Fraud ring types
│   └── api_design.md          # API design docs
├── notebooks/                  # Jupyter notebooks
│   ├── EDA.ipynb              # Exploratory data analysis
│   ├── Graph_Construction.ipynb  # Graph building experiments
│   ├── Model_Experiments.ipynb   # Model experimentation
│   └── Monitoring_Demo.ipynb     # Monitoring demonstrations
├── src/nexusshield/           # Core source code
│   ├── data/                  # Data processing
│   │   ├── loaders.py        # Load CSV/Parquet tables
│   │   ├── preprocess.py     # Data cleaning and feature engineering
│   │   └── graph_builder.py   # Construct heterogeneous graph
│   ├── models/                # GNN models
│   │   ├── gnn_layers.py     # GCN/GAT/GraphSAGE layers
│   │   ├── encoders.py       # Node/edge type encoders
│   │   ├── classifier_head.py # MLP classification heads
│   │   └── nexusshield_gnn.py # Main model class
│   ├── training/             # Training modules
│   │   ├── train_node_classification.py
│   │   ├── train_link_prediction.py
│   │   └── evaluation.py
│   ├── pipelines/             # End-to-end pipelines
│   │   ├── build_graph_pipeline.py
│   │   └── train_eval_pipeline.py
│   ├── inference/            # Inference
│   │   └── scorer.py         # Model scoring interface
│   └── utils/                # Utilities
│       ├── logging_utils.py
│       ├── metrics.py
│       └── visualization.py
└── tests/                      # Test suite
    ├── test_data.py
    ├── test_graph_builder.py
    └── test_gnn.py
```

## Getting Started

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
   pip install -r requirements.txt
   ```

4. **Configure the system**
   ```bash
   # Edit configs/config.yaml with your settings
   ```

## How It Works

1. **Data Loading** (`src/nexusshield/data/loaders.py`): Loads transaction, account, device, merchant, and label tables from CSV/Parquet files.

2. **Preprocessing** (`src/nexusshield/data/preprocess.py`): Cleans data and engineers features for each entity type.

3. **Graph Construction** (`src/nexusshield/data/graph_builder.py`): Builds a heterogeneous graph where nodes represent entities and edges represent relationships (e.g., account-uses-device, transaction-from-account).

4. **GNN Processing** (`src/nexusshield/models/`): 
   - Node/edge encoders transform raw features into embeddings
   - GNN layers perform message passing to aggregate neighbor information
   - Multiple layers capture multi-hop relationships
   - Classifier heads produce fraud predictions

5. **Training** (`src/nexusshield/training/`): Trains models for node classification (fraud detection) and link prediction (suspicious relationship detection).

6. **Inference** (`src/nexusshield/inference/scorer.py`): Loads trained models and scores accounts/devices for fraud risk.

## Development

This is a scaffolded repository with stub implementations. All modules contain:
- Type-hinted function signatures
- Docstrings explaining purpose and conceptual approach
- TODO comments marking where implementation will go
- No actual implementation code

## License

This project is licensed under the MIT License.
