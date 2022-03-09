FROM python:3.10.2
# Last version check: 09 mar 2022. 
# Newer versions may be available, and info is available at https://www.python.org/downloads/
# Note that Python 2.7 is end of life. End of support was 01 Jan 2020, see https://www.python.org/dev/peps/pep-0373/

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
        procps \
        iputils-ping \
        net-tools \
        lsb-release
# procps: to support command 'ps'
# iputils-ping: to support command 'ping' (https://linuxconfig.org/ping-command-not-found-on-ubuntu-20-04-focal-fossa-linux) [Manfred, 19sep2021]
# net-tools: to support command such as 'arp', 'ifconfig', 'netstat', etc. (https://helpmanual.io/packages/apt/net-tools/) [Manfred, 26sep2021]
# lsb-release: to support commmand 'lsb_release -a' [Manfred, 15jan2022]
# You can safely remove the packages you don't want. [Manfred, 08oct2021]

# Create non-root user (zero trust principle, least privileged principle)
RUN groupadd -g 1000 -r dev && \
    useradd -u 1000 -r -g dev -m -s $(which bash) dev
# Option '-m' to create home directory (see https://askubuntu.com/a/393470)
# Option '-s' to set shell for this user (see comment in https://askubuntu.com/a/393470)
# Option '-r' creates a system user which does not expire (see https://linuxize.com/post/how-to-create-users-in-linux-using-the-useradd-command/)

# How to add sudo support for the non-root user is described at https://code.visualstudio.com/remote/advancedcontainers/add-nonroot-user#_creating-a-nonroot-user
# However, standard practice is not to add sudo support for security reasons. VS Code will connect
# to the running dev container as the user specified in file ".devcontainer/devcontainer.json" in
# property "remoteUser". If you need to run commands as root to set up the dev container, use the
# "RUN" directive in Dockerfile or add suitable code to the script ".devcontainer/entrypoint.sh". 
# [Manfred, 16jan2022]

# Create working directory. Ownership will be changed in entrypoint.sh which
# executes *after* the volume has been mounted.
RUN mkdir /src

# Copy entrypoint script into container, make it executable, then make it the entrypoint for the
#  container:
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
# Option '+x' adds executable flag to the file
ENTRYPOINT ["/entrypoint.sh"]
