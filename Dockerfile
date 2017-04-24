FROM continuumio/miniconda3

MAINTAINER Brynjar Smári Bjarnason <binni@binnisb.com>

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

# Set the ENTRYPOINT to use bash
# (this is also where you’d set SHELL,
# if your version of docker supports this)
ENTRYPOINT ["/bin/bash", "-c" ]

# Use the environment.yml to create the conda environment.
ADD environment.yml /tmp/environment.yml
WORKDIR /tmp
RUN ["conda", "env", "create" ]

ADD . /code

# Use bash to source our new environment for setting up
# private dependencies—note that /bin/bash is called in
# exec mode directly
WORKDIR /code
RUN ["/bin/bash", "-c", "source activate test_stuff && python setup.py install" ]

# We set ENTRYPOINT, so while we still use exec mode, we don’t
# explicitly call /bin/bash
CMD [ "source activate test_stuff && exec python test.py" ]
