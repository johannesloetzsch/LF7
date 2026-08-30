# Node-RED
Low-code programming for event-driven applications

![](examples/rest/nodered/nodered_rest_openapi.png)

> **💻** Beispiel [flow.json](./examples/rest/nodered/nodered_flow_html.json)


## [Setup](https://nodered.org/docs/getting-started/)

### [via Docker](https://nodered.org/docs/getting-started/docker)

```
docker volume create --name node_red_data
docker run -it -p 1880:1880 -v node_red_data:/data --name mynodered nodered/node-red --dns 8.8.8.8
```

## Documentation
* [Tutorials](https://nodered.org/docs/tutorials/)
* [Cookbook](https://cookbook.nodered.org/)
* [User Guide](https://nodered.org/docs/user-guide/)

## Swagger

### Setup

`Menü` -> `User Settings` -> `Palette` -> `Install`

* [`openapi-red`](https://flows.nodered.org/node/openapi-red) (Client)
* [`node-red-node-swagger`](https://flows.nodered.org/node/node-red-node-swagger) (Documentation Generator)


### Benutzung Client

* `openApi-red` Node statt `http request` Node benutzen

### Benutzung Documentation Generator

1. `http in` Node nutzen und optional `Docs` Property editieren

2. [http://localhost:1880/http-api/swagger.json](http://localhost:1880/http-api/swagger.json)

3. [Swagger UI (Live Demo)](https://petstore.swagger.io/) starten
* `http://localhost:1880/http-api/swagger.json` eintragen
* mit `Explore` laden
