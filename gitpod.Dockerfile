# You can find the new timestamped tags here: https://hub.docker.com/r/gitpod/workspace-full/tags
FROM gitpod/workspace-full

USER root

# Install custom tools, runtime, etc.
RUN sudo apt-get update && sudo apt-get install -y python3-pyqt5