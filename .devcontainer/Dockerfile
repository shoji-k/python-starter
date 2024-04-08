FROM python:3.12.2

RUN pip install --upgrade pip && pip install poetry
# RUN poetry config virtualenvs.in-project true

# https://code.visualstudio.com/remote/advancedcontainers/add-nonroot-user
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME
    #
    # [Optional] Add sudo support. Omit if you don't need to install software after connecting.
    # && apt-get update \
    # && apt-get install -y sudo \
    # && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    # && chmod 0440 /etc/sudoers.d/$USERNAME

# ********************************************************
# * Anything else you want to do like clean up goes here *
# ********************************************************

# [Optional] Set the default user. Omit if you want to keep the default as root.
USER $USERNAME

# set the work directory
WORKDIR /app

# change home directory to /app
# ENV HOME /app

# copy the poetry files
# COPY poetry.lock pyproject.toml /app/

# # install the dependencies
# RUN poetry install

# copy the application
# COPY . /app

# start the application
# CMD ["poetry", "run", "python", "app.py"]
