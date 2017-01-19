@echo off
echo python manage.py collectstatic
echo gsutil rsync -R static/ gs://legendary-online/static
exit /B