# SOLID CHALLENGE

## Ambiente de desenvolvimento - Ubuntu
### Requisitos
`python 3.9.12
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
$ sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl git
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