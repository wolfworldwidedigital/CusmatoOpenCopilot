import json
import yaml
from typing import Dict, List
from flask import Request
from prance import ResolvingParser
from shared.utils.opencopilot_utils.get_vector_store import get_vector_store
from shared.utils.opencopilot_utils import StoreOptions
from langchain.docstore.document import Document
from utils.llm_consts import initialize_qdrant_client

client = initialize_qdrant_client()


def save_swagger_paths_to_qdrant(swagger_doc: ResolvingParser, bot_id: str):
    vector_store = get_vector_store(StoreOptions("apis"))
    try:
        # delete documents with metadata in api with the current bot id, before reingesting
        documents: List[Document] = []
        paths = swagger_doc.specification.get("paths", {})

        for path, operations in paths.items():
            for method, operation in operations.items():
                try:
                    operation["method"] = method
                    operation["path"] = path
                    del operation["responses"]

                    # Check if "summary" key is present before accessing it
                    summary = operation.get("summary", "")
                    description = operation.get("description", "")

                    document = Document(page_content=f"{summary}; {description}")
                    document.metadata["bot_id"] = bot_id
                    document.metadata["operation"] = operation

                    documents.append(document)
                except KeyError as e:
                    # Handle the specific key error, log, or take necessary action
                    raise e

        point_ids = vector_store.add_documents(documents)
        return point_ids
    except Exception as e:
        # Handle other exceptions
        raise e
