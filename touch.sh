git init
git remote add origin https://github.com/pavanyendluri588/hospital_management_system.git
git remote -v  --force
git add . --force
git commit -m "april_2nd_upload"
git config --global push.autoSetupRemote true
git pull --rebase origin master

git push -f origin master

