# SOLID CHALLENGE

## Ambiente de desenvolvimento - Ubuntu
### Requisitos
- python 3.9.12
```
$ sudo apt-get install python3
$ sudo apt-get install make
```

### Instalar pyenv
```
$ curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
$ exec $SHELL
```
editar o arquivo "~/.bashrc" adicionando os comandos abaixo
```
$ sudo nano ~/.bashrc
export PATH="/home/$USER/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

### Instalar Docker
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04

#
## Criando ambiente de desenvolvimento
```
make create-venv
```

#
## Iniciar o projeto
```
make run-server
```

### URL do projeto
- /api/v1/products/create
