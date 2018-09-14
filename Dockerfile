FROM nginx:1.14

RUN apt-get -y update && apt-get install -y build-essential python python-dev \
python-pip

RUN pip install appdirs doxypypy

RUN useradd -m tempuser

COPY . /home/tempuser/python-app

RUN chown -R tempuser:tempuser /home/tempuser/python-app

WORKDIR /home/tempuser/python-app/

USER tempuser

RUN doxygen Doxyfile

USER root

RUN cp -r ./html/* /usr/share/nginx/html/

