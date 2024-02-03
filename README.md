# Previsão do clima com Flask


<p align="center">
<img src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge">
</p>

Um APP que busca através da [API  ClimaTempo](https://www.dropbox.com/developers/documentation/http/documentation) previsões para o clima de qualquer uma cidade ou região de todo o Brasil utilizando Flask.
### Deploy da APP: https://clima-8ba6fda2cfe4.herokuapp.com/

# 🔨 Funcionalidades do projeto:

### - ` 1`:  Pesquisar a temperatura e o clima atual de uma cidade, desde que a mesma tenha sido definida como padrão. (como usei API gratuita, só é possível definir uma cidade padrão por dia)

### - ` 2`:  Pesquisar a previsão de todos os horário do dia para a determinada cidade padrão

### - ` 3`: Pesquisar a previsão para os próximos 3 dias de uma determinada região do Brasil (está região não precisa ser padrão, podemos pesquisar sem limitações)

### - `EXTRA:`: O APP também conta com login e autenticação de usuários e administradores (que podemos editar e excluir qualquer usuário).


# 🛠️ Limitações da v1.2:   
- Por conta da API ser gratuita, é permitido pesquisar apenas por uma cidade a cada 24h, mas os services e as rotas já conseguem buscar qualquer cidade, caso a API não seja mais gratuita.


## ✔️ Tecnologias utilizadas

- ``Flask``
- ``HTML + CSS + JS + BOOTSTRAP``
- ``SQLALCHEMY ``

[<img loading="lazy" src="https://avatars.githubusercontent.com/u/88624922?v=4" width=115><br><sub>João Pedro</sub>](https://github.com/JoaoPedro8807)
