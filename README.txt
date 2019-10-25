1. Reference
https://towardsdatascience.com/step-by-step-guide-to-creating-r-and-python-libraries-e81bbea87911
2. Download Docker Image
docker pull jupyter/datascience-notebook
3. Start Jupyterlab Container
docker run -it -v `pwd`:/home/jovyan/work -p 8888:8888 jupyter/datascience-notebook start.sh jupyter lab
4. Use Notebooks
Copy URL and open in a browser
Run Nootebooks
