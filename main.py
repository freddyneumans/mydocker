FROM tomcat:9.0
MAINTAINER freddy
RUN apt-get update
RUN apt-get install -y maven
RUN apt-get install -y git
RUN git clone https://github.com/boxfuse/boxfuse-sample-java-war-hello.git
WORKDIR /usr/local/tomcat/boxfuse-sample-java-war-hello
RUN mvn package
WORKDIR /usr/local/tomcat/boxfuse-sample-java-war-hello/target
RUN cp hello-1.0.war /usr/local/tomcat/webapps/
EXPOSE 8080
CMD ["catalina.sh","run"]