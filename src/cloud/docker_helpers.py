import subprocess

def build_and_run_docker():
    """
    Builds and runs Docker containers using docker-compose.
    """
    print("🔧 Building and starting Docker containers...")
    subprocess.run(["docker-compose", "up", "--build"])

def stop_and_clean_docker():
    """
    Stops containers and removes them with volumes.
    """
    print("🧹 Stopping and cleaning Docker containers...")
    subprocess.run(["docker-compose", "down", "--volumes", "--remove-orphans"])

def prune_docker_system():
    """
    Removes unused Docker images, containers, and volumes.
    """
    print("🧼 Pruning Docker system...")
    subprocess.run(["docker", "system", "prune", "-f"])
