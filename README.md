```
pip install virtualenv
```

```
virtualenv .env
```

```
source .env/bin/activate
```

or in windows 
```
py \Scripts\activate
```

```
.gitignore
```

```
pip install -r requirements.txt
```

# Build the Docker Image
Now that all the files are in place, let's build the container image.

 - Go to the project directory (in where your Dockerfile is, containing your app directory).
 - Build your FastAPI image:
```
docker build -t myimage .
```

## Start the Docker Container
Run a container based on your image:
```
docker run -d --name mycontainer -p 80:80 myimage
```