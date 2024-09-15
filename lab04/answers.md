# Lab 4: Docker Tutorial

**Before you begin...**
1. Ensure that Docker is running and that you can access the Docker Dashboard
1. Open the command prompt
2. Run the following command: `docker run -dp 80:80 docker/getting-started`
3. Open [http://localhost](http://localhost) in your browser to complete the tutorial.


Complete the following tutorial sections (note that #4 and #9 are optional) and answer the questions below:

## 1. Getting Started
Consider the command you just ran: `docker run -d -p 80:80 docker/getting-started`

Answer the following:
1. Explain what the -p flag is doing (in your own words)
2. How do you think [http://localhost](http://localhost) is communicating with Docker?

The -p flag in the docker run command is used to map a port on your local machine (host) to a port inside the Docker container. In the case of -p 80:80, the first 80 refers to the port on the host machine , and the second 80 refers to the port inside the Docker container.

This means that any traffic sent to port 80 on your local machine will be forwarded to port 80 inside the container. 
## 2. Our Application
When you download and unzip `app`, save it inside of the `lab04` directory (while on your `lab04` branch). Then follow the instructions for this section. When you're done, answer the following questions about the `Dockerfile` you just made:
1. What is `node:18-alpine` and where did it come from?

node:18-alpine is a Docker image that serves as a lightweight version of the Node.js environment (version 18) based on the Alpine Linux distribution. 

2. Which commands in the Dockerfile instructed Docker to copy the code from `app` onto the Docker image? Explain.
COPY: This command copies files or directories from the host system into the Docker image.
./app: This refers to the app directory on your local machine.
/app: This is the target directory inside the Docker image where the files are being copied.
COPY ./app /app
COPY: This command copies files or directories from the host system into the Docker image.
./app: This refers to the app directory on your local machine.
/app: This is the target directory inside the Docker image where the files are being copied.

3. What do you think would happen if you forgot to add `CMD ["node", "src/index.js"]` in your Dockerfile? Why?

If you forgot to add CMD ["node", "src/index.js"], Docker would not know what command to run when the container starts. The CMD instruction specifies the default command to be executed when the container runs.

Without this, the container might start but then immediately exit, as there would be no process running to keep it active. In this case, the Node.js application wouldn't start.

## 3. Updating Our App
In this section, you learned that if you make a change to the code, you have to 
* Rebuild the Docker image,
* Delete the container that you previously made (which is still running), and
* Create a brand new container

Answer the following:
1. What are two ways you can delete a container?
docker rm & docker rm -f
## 4. Sharing Our App (Optional)
You don't have to complete this section, but I do want you to navigate to the Docker Image repository and take a look: [https://hub.docker.com/search?q=&type=image&image_filter=official](https://hub.docker.com/search?q=&type=image&image_filter=official). These are all of the potential Docker Images you can utilize to build your own containers (which will save you a lot of time)!

## 5. Persisting our DB

1. What is the difference between the `run` and the `exec` command?
docker run creates and starts a new container.
docker exec runs commands inside an existing, running container.

2. What does the `docker exec -it` command do, exactly. Try asking ChatGPT!
The docker exec -it command allows you to interactively execute a command inside a running container.

3. What was the purpose of creating a volume?

Volumes are particularly useful for databases, log storage, and any case where persistent data is important, regardless of the container's lifecycle.







4. Optional: How does the TODO app code know to use the volume you just made? Hint: open `app/src/persistence/sqlite.js` and see if you can figure it out.

## 6. Using Bind Mounts
1. Why are bind mounts useful?

Bind mounts are useful in Docker because they allow you to link a specific directory on your host machine to a directory inside the container
 
2. Note that the commands below can also be represented in a Dockerfile (instead of in one big string of commands on the terminal). What are the advantages of using a Dockerfile?

```
docker run -dp 3000:3000 \
    -w /app -v "$(pwd):/app" \
    node:18-alpine \
    sh -c "yarn install && yarn run dev"
```
Using a Dockerfile makes containerization workflows more efficient, reliable, and maintainable, while ensuring that environments are consistently reproducible across teams and machines.

## 7. Multi-Container Apps
If you have never worked with network applications, this section may be confusing. That said, try to answer this question as best you can:

1. If you have two containers running that are sandboxed (i.e., one container can't reach into another container and see its internal state or code), how did you get your two containers to communicate with one another? In other words, how was the web application container able to communicate with the database container?

To get two containers to communicate, you place them on the same Docker network (preferably a custom network). Once they are on the same network, they can resolve each other's names and communicate using their container names (e.g., db_container for the database). This allows the web application container to communicate with the database container.
## 8. Using Docker Compose
1. What is the purpose of the `docker-compose.yml` file?

 Its purpose is to simplify the orchestration of services by allowing you to describe your application’s services, networks, and volumes in a single file.
## 9. Image Building Best Practices (Optional)
Optional section. Only complete if you want to.


## What to turn in
After answering all of the questions above...
1. Make sure that your `app` folder is inside of your `lab04` folder (including your `Dockerfile` and `docker-compose.yml` files).
1. Then, stage, commit, and push your 'lab04' branch to GitHub. 
1. Create a Pull Request (but do not merge your pull request -- that doesn't happen until Sarah reviews it).
1. Paste a link to your pull request in the Lab04 submission
