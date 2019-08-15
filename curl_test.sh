if curl "$1" > HTML
then rm HTML && echo "200" && exit 0
else rm HTML && echo "404" && exit 1
fi
