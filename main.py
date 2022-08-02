FROM ubuntu:20.04
RUN apt update
RUN apt install -y default-jdk
RUN apt install -y tomcat9
RUN apt install -y maven
RUN apt install -y git
RUN git clone https://github.com/boxfuse/boxfuse-sample-java-war-hello.git
WORKDIR /boxfuse-sample-java-war-hello
RUN mvn package
WORKDIR /target
RUN cp hello-1.0.war /var/lib/tomcat9/webapps/
EXPOSE 8085
CMD ["catalina.sh", "run"]