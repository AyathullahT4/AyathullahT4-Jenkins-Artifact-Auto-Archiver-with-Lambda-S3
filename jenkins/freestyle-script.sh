# 1. Archive the artifact in Jenkins
mkdir -p artifacts
cp "$JENKINS_HOME/jobs/$JOB_NAME/builds/$BUILD_NUMBER/log" artifacts/build-log.txt

