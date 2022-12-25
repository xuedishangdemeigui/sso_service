FROM sso_serv:1.0.3
EXPOSE 5000
ENTRYPOINT [ "bash","/app/sso_service/run.sh" ]