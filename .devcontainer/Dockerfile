FROM mcr.microsoft.com/devcontainers/python:1-3.12-bookworm

# OCI labels
LABEL org.opencontainers.image.source="https://github.com/sysengquick-yt/yaml-2024"
LABEL org.opencontainers.image.description="Devcontainer for sysengquick YAML tutorial 2024"
LABEL org.opencontainers.image.licenses="GPL-3.0"

# install python packages
RUN python3 -m pip install pyyaml~=6.0.1 ruamel-yaml~=0.18.6

# install yq
ARG YQ_VERSION=4.44.1
RUN curl https://github.com/mikefarah/yq/releases/download/v${YQ_VERSION}/yq_linux_amd64 -Lo /usr/bin/yq \
    && chmod +x /usr/bin/yq

# enable bash completion for git
RUN ln -s /usr/share/bash-completion/completions/git /usr/share/bash-completion/bash_completion
