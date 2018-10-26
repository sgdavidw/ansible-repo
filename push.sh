echo "test $1" > github_file$1.txt
git add .
git commit -m "$1th commit"
git push

