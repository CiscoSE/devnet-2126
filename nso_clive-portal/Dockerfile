# Dockerfile

# FROM directive instructing base image to build upon
FROM python:3-onbuild

ADD . /usr/src/app/

# EXPOSE port 8080 to allow communication to/from server
EXPOSE 8080

# CMD specifcies the command to execute to start the server running.
CMD ["/usr/src/app/web_start.sh"]
# done!
