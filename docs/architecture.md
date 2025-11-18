# NexusShield Architecture

## Overview

NexusShield is a Graph Neural Network (GNN) system for detecting fraud rings in financial transaction data. This document describes the high-level architecture and design decisions.

## System Components

### Data Layer
- **Loaders**: Load raw CSV/Parquet tables (transactions, accounts, devices, merchants, labels)
- **Preprocessing**: Clean data and engineer features for each entity type
- **Graph Builder**: Construct heterogeneous graph from processed tables

### Model Layer
- **Encoders**: Transform raw features into node/edge embeddings
- **GNN Layers**: Perform message passing (GCN, GAT, GraphSAGE)
- **Classifier Heads**: Produce fraud predictions (node classification, link prediction)

### Training Layer
- **Node Classification Training**: Train models to classify accounts/devices as fraud/legitimate
- **Link Prediction Training**: Train models to predict suspicious relationships
- **Evaluation**: Compute metrics (AUC-ROC, AUC-PR, etc.)

### Pipeline Layer
- **Graph Construction Pipeline**: Chains loaders → preprocess → graph_builder
- **Train-Eval Pipeline**: Chains graph building → training → evaluation

### Inference Layer
- **Scorer**: Load trained models and score accounts/devices for fraud risk

## Graph Structure

The system constructs a heterogeneous graph with:
- **Node Types**: Account, Device, IP, Transaction, Merchant
- **Edge Types**: Account-uses-Device, Account-makes-Transaction, Transaction-from-IP, etc.

## Message Passing

GNN layers aggregate information from neighboring nodes through message passing:
1. Each node collects messages from its neighbors
2. Messages are aggregated (mean, max, attention-weighted)
3. Aggregated messages are combined with node's own features
4. Multiple layers enable multi-hop relationship learning

## Fraud Ring Detection

Fraud rings are detected by:
1. Learning node embeddings that capture structural and behavioral patterns
2. Identifying clusters of nodes with similar embeddings
3. Scoring nodes based on learned patterns and cluster membership
4. Flagging high-risk clusters as potential fraud rings

