"""
Data loaders for NexusShield GNN Fraud Ring Detector.

This module provides functions to load raw CSV/Parquet tables containing
transaction data, account information, device records, merchant data, and fraud labels.
All loaders return pandas DataFrames for downstream processing.
"""

from typing import Optional, Union
import pandas as pd
from pathlib import Path


def load_transactions(
    file_path: Union[str, Path],
    file_format: Optional[str] = None
) -> pd.DataFrame:
    """
    Load transaction data from CSV or Parquet file.

    Args:
        file_path: Path to the transaction data file
        file_format: File format ('csv' or 'parquet'). If None, inferred from extension.

    Returns:
        DataFrame containing transaction records with columns such as:
        - transaction_id
        - account_id
        - device_id
        - ip_address
        - merchant_id
        - amount
        - timestamp
        - status
        - etc.

    TODO: Implement file format detection and loading logic
    TODO: Add data validation and schema checking
    TODO: Handle missing values and data type conversions
    """
    pass


def load_accounts(
    file_path: Union[str, Path],
    file_format: Optional[str] = None
) -> pd.DataFrame:
    """
    Load account data from CSV or Parquet file.

    Args:
        file_path: Path to the account data file
        file_format: File format ('csv' or 'parquet'). If None, inferred from extension.

    Returns:
        DataFrame containing account records with columns such as:
        - account_id
        - created_at
        - account_type
        - verification_status
        - country
        - etc.

    TODO: Implement file format detection and loading logic
    TODO: Add data validation and schema checking
    """
    pass


def load_devices(
    file_path: Union[str, Path],
    file_format: Optional[str] = None
) -> pd.DataFrame:
    """
    Load device data from CSV or Parquet file.

    Args:
        file_path: Path to the device data file
        file_format: File format ('csv' or 'parquet'). If None, inferred from extension.

    Returns:
        DataFrame containing device records with columns such as:
        - device_id
        - device_type
        - os
        - browser
        - device_fingerprint
        - etc.

    TODO: Implement file format detection and loading logic
    TODO: Add data validation and schema checking
    """
    pass


def load_merchants(
    file_path: Union[str, Path],
    file_format: Optional[str] = None
) -> pd.DataFrame:
    """
    Load merchant data from CSV or Parquet file.

    Args:
        file_path: Path to the merchant data file
        file_format: File format ('csv' or 'parquet'). If None, inferred from extension.

    Returns:
        DataFrame containing merchant records with columns such as:
        - merchant_id
        - merchant_name
        - merchant_category
        - country
        - etc.

    TODO: Implement file format detection and loading logic
    TODO: Add data validation and schema checking
    """
    pass


def load_labels(
    file_path: Union[str, Path],
    file_format: Optional[str] = None
) -> pd.DataFrame:
    """
    Load fraud labels from CSV or Parquet file.

    Args:
        file_path: Path to the labels file
        file_format: File format ('csv' or 'parquet'). If None, inferred from extension.

    Returns:
        DataFrame containing fraud labels with columns such as:
        - entity_id (account_id or device_id)
        - entity_type ('account' or 'device')
        - is_fraud (binary label)
        - fraud_type (optional: type of fraud)
        - etc.

    TODO: Implement file format detection and loading logic
    TODO: Add data validation and schema checking
    TODO: Handle missing labels (semi-supervised learning scenario)
    """
    pass

