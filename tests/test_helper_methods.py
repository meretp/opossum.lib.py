# SPDX-FileCopyrightText: 2023 TNG Technology Consulting GmbH <https://www.tngtech.com>
#
# SPDX-License-Identifier: Apache-2.0
from unittest import TestCase

from networkx import DiGraph

from opossum_lib.helper_methods import (
    _create_file_path_from_graph_path,
    _replace_node_ids_with_labels,
)


def test_create_file_path_from_graph_path() -> None:
    graph = _create_simple_graph()
    path = ["root", "node", "leaf"]

    file_path = _create_file_path_from_graph_path(path, graph)

    assert file_path == "/root/node/with/path/leaf"


def test_replace_node_ids_with_labels() -> None:
    graph = _create_simple_graph()
    path = ["root", "node", "leaf"]

    file_path = _replace_node_ids_with_labels(path, graph)

    TestCase().assertCountEqual(file_path, ["root", "node", "with", "path", "leaf"])


def _create_simple_graph() -> DiGraph:
    graph = DiGraph()
    graph.add_nodes_from(
        [
            ("root", {"label": "root"}),
            ("node", {"label": "node/with/path"}),
            ("leaf", {"label": "leaf"}),
        ]
    )
    return graph