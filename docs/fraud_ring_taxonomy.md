# Fraud Ring Taxonomy

## Overview

This document describes different types of fraud rings that NexusShield is designed to detect.

## Fraud Ring Types

### 1. Device-Sharing Rings
- **Pattern**: Multiple accounts sharing the same device(s)
- **Indicators**: High device reuse across accounts, rapid account creation on same device
- **Graph Signature**: Dense connections between Account and Device nodes

### 2. IP-Sharing Rings
- **Pattern**: Multiple accounts using the same IP address(es)
- **Indicators**: Geographic inconsistencies, VPN/proxy usage, high IP reuse
- **Graph Signature**: Dense connections between Account and IP nodes

### 3. Transaction Pattern Rings
- **Pattern**: Coordinated transaction behaviors (similar amounts, timing, merchants)
- **Indicators**: Synchronized transactions, similar transaction patterns
- **Graph Signature**: Similar transaction node features, temporal clustering

### 4. Merchant Collusion Rings
- **Pattern**: Multiple accounts transacting with the same merchant(s) in suspicious patterns
- **Indicators**: Unusual merchant-account relationships, high-value transactions
- **Graph Signature**: Dense connections between Account, Transaction, and Merchant nodes

### 5. Hybrid Rings
- **Pattern**: Combination of above patterns
- **Indicators**: Multiple suspicious signals across different entity types
- **Graph Signature**: Complex multi-hop patterns connecting multiple entity types

## Detection Strategy

Different fraud ring types may require different GNN architectures:
- **Device/IP sharing**: Link prediction tasks
- **Transaction patterns**: Node classification on transaction nodes
- **Hybrid rings**: Multi-task learning combining node classification and link prediction

