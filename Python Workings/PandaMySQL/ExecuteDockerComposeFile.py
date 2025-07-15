import subprocess

# Path to your Docker Compose file
docker_compose_file = "docker-compose.yml"

try:
    # Run the Docker Compose up command
    subprocess.run(["docker-compose", "-f", docker_compose_file, "up", "-d"], check=True)
    print("Docker Compose executed successfully!")
except subprocess.CalledProcessError as e:
    print(f"Error occurred while executing Docker Compose: {e}")
