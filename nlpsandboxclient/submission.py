"""Submission module"""
import re

from synapseclient import Submission, Synapse


def _find_docker_repo_by_name(syn: Synapse, docker_image: str,
                              project_id: str) -> str:
    """Find Docker repository by name and return synid"""
    docker_repos = syn.getChildren(project_id, includeTypes=['dockerrepo'])

    for docker_repo in docker_repos:
        docker_ent = syn.get(docker_repo['id'])
        if docker_ent.repositoryName == docker_image:
            synid = docker_repo['id']
            return synid


def submit(syn: Synapse, docker_image: str,
           annotator_type: str, team: str = None) -> Submission:
    """Submit nlpsandbox docker submission

    Args:
        syn: Synapse connection
        docker_image: Must be in the format of
                      docker.synapse.org/synXXXXX/your-image-name:your-tag
        annotator_type: Type of annotator, can be date, person or address.
        team: Name or Id of Synapse team. Optional, if left out, submission
              will be submitted as the user.
    """
    docker_components = re.match("docker.synapse.org/(syn.+)/(.+):(.+)",
                                 docker_image)
    if not docker_components:
        raise ValueError(
            "Docker image must follow "
            "docker.synapse.org/synXXXXX/your-image-name:your-tag convention"
        )
    # Checks if Synapse team exists
    if team is not None:
        team = syn.getTeam(team)

    project_id = docker_components[1]
    docker_repo = docker_image.split(":")[0]
    docker_tag = docker_components[3]
    synid = _find_docker_repo_by_name(syn, docker_repo, project_id)
    if synid is None:
        raise ValueError("Docker repository not found.")
    evaluation_queue_map = {
        "date": "9614654",
        "person": "9614685",
        "address": "9614684"
    }
    queue_id = evaluation_queue_map[annotator_type]
    return syn.submit(evaluation=queue_id, entity=synid, team=team,
                      dockerTag=docker_tag)
