# SPDX-License-Identifier: MIT
# (c) 2019 The TJHSST Director 4.0 Development Team & Contributors

import json
import traceback
from typing import Tuple, Union

from flask import Blueprint, request

from ...docker.images import build_custom_docker_image
from ...docker.services import (
    remove_director_service,
    restart_director_service,
    update_director_service,
)
from ...docker.utils import create_client
from ...exceptions import OrchestratorActionError
from ...files import ensure_site_directories_exist

docker_blueprint = Blueprint("docker", __name__)


@docker_blueprint.route("/sites/<int:site_id>/update-docker-service", methods=["POST"])
def update_docker_service_page(site_id: int) -> Union[str, Tuple[str, int]]:
    """Updates the Docker service for a given site.

    Based on the provided site_id and data, updates
    the Docker service to reflect the site's new state.
    Returns "Success" if successful, else an appropriate
    error.
    """

    if "data" not in request.form:
        return "Error", 400

    try:
        ensure_site_directories_exist(site_id)

        update_director_service(create_client(), site_id, json.loads(request.form["data"]))
    except OrchestratorActionError as ex:
        traceback.print_exc()
        return str(ex), 500
    except BaseException:  # pylint: disable=broad-except
        traceback.print_exc()
        return "Error", 500
    else:
        return "Success"


@docker_blueprint.route("/sites/<int:site_id>/restart-docker-service", methods=["POST"])
def restart_docker_service_page(site_id: int) -> Union[str, Tuple[str, int]]:
    """Restarts the Docker service for a given site."""

    try:
        restart_director_service(create_client(), site_id)
    except OrchestratorActionError as ex:
        traceback.print_exc()
        return str(ex), 500
    except BaseException:  # pylint: disable=broad-except
        traceback.print_exc()
        return "Error", 500
    else:
        return "Success"


@docker_blueprint.route("/sites/<int:site_id>/remove-docker-service", methods=["POST"])
def remove_docker_service_page(site_id: int) -> Union[str, Tuple[str, int]]:
    """Removes the Docker service for a given site."""

    try:
        remove_director_service(create_client(), site_id)
    except OrchestratorActionError as ex:
        traceback.print_exc()
        return str(ex), 500
    except BaseException:  # pylint: disable=broad-except
        traceback.print_exc()
        return "Error", 500
    else:
        return "Success"


@docker_blueprint.route("/sites/build-docker-image", methods=["POST"])
def build_custom_docker_image_page() -> Union[str, Tuple[str, int]]:
    """Builds a Docker image based on provided parameters."""

    try:
        build_custom_docker_image(create_client(), json.loads(request.form["data"]))
    except OrchestratorActionError as ex:
        traceback.print_exc()
        return str(ex), 500
    except BaseException:  # pylint: disable=broad-except
        traceback.print_exc()
        return "Error", 500
    else:
        return "Success"
