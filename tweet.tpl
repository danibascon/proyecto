%include('header.tpl')

    <title>.::Usando la API de twitter::.</title>
  </head>
  <body>
    <p>Buen momento para un tweet:{{text}}</p>
    <br />
    <form action="/twittear" method="post">
      <p><textarea name="tweet" id="textbox" rows="3" cols="50" maxlength="140">
        Me ha gustado el vídeo: {{text}}


      </textarea></p>
      <p><input type="submit" class="button" value="Enviar" /></p>
    </form>
    <a href="/twitter_logout">Desconectar</a>
  </body>
%include('footer.tpl')