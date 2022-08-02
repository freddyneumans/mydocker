FROM ubuntu:18.04
RUN apt-get update
RUN apt-get install -y default-jdk
RUN apt-get install -y tomcat9
RUN apt-get install -y maven
RUN apt-get install -y git
RUN git clone https://github.com/boxfuse/boxfuse-sample-java-war-hello.git
WORKDIR /boxfuse-sample-java-war-hello
RUN mvn package
WORKDIR /boxfuse-sample-java-war-hello/target
RUN cp hello-1.0.war /var/lib/tomcat9/webapps/
EXPOSE 8085
CMD ["catalina.sh", "run"]