if [ "setup project" = $1 ]; then
    echo "Running microservice setup"
    exec pip install -r microservice/scrapping_datbase_api/requirements.txt
    exit;
fi

if [ "makemigrations" = $1 ]; then
    echo "Running migrations"
    exec python3 microservice/scrapping_datbase_api/manage.py makemigrations
    exit;
fi

if [ "migrate" = $1 ]; then
    echo "Migrate database configuration"
    exec python3 microservice/scrapping_datbase_api/manage.py migrate
    exit;
fi

if [ "microservice" = $1 ]; then
    echo "Running microservice"
    exec python3 microservice/scrapping_datbase_api/manage.py runserver
    exit;
fi


echo "Your first argument must be either 'setup', 'microservice'"
exit 5;