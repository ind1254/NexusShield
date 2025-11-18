"""
Tests for training modules.
"""

import pytest

from src.nexusshield.training.train_node_classification import (
    train_node_classification,
    train_epoch,
    validate
)
from src.nexusshield.training.train_link_prediction import (
    train_link_prediction,
    sample_negative_edges
)
from src.nexusshield.training.evaluation import (
    compute_node_classification_metrics,
    compute_link_prediction_metrics,
    compute_auc_roc,
    compute_auc_pr
)


def test_train_node_classification():
    """
    Test node classification training.

    TODO: Implement test:
    - Create sample model and data
    - Run training for a few epochs
    - Assert metrics are computed
    """
    pass


def test_train_link_prediction():
    """
    Test link prediction training.

    TODO: Implement test
    """
    pass


def test_compute_node_classification_metrics():
    """
    Test node classification metrics computation.

    TODO: Implement test
    """
    pass


def test_compute_link_prediction_metrics():
    """
    Test link prediction metrics computation.

    TODO: Implement test
    """
    pass

