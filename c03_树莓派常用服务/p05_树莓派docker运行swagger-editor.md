# 树莓派docker运行swagger-editor

该镜像在树莓派本地构建，构建过程：

### Building and running an image locally

To build and run a docker image with the code checked out on your machine, run the following from the root directory of the project:

```shell
# Install npm packages (if needed)
npm install

# Build the app
npm run build

# Build an image
docker build -t swagger-editor .

# Run the container
docker run -d \
    --name swagger-editor \
    --restart always \
    -p 30080:8080 swagger-editor
```

You can then view the app by navigating to `http://localhost` in your browser.

更多信息见：<https://github.com/swagger-api/swagger-editor>
