%include('header.tpl')
<br>
	<form action="/formulario" method="post">
		<label>Nombre que buscar:</label>
		<input type="text" name="buscar" required/>
		<input type="text" name="artista" required/>
		<label>Numero de videos:</label>
		<input type="number" name="cantidad" min='1' value='1' max='10' required/>
		<input type="submit" value="Enviar">
	</form>
<br>
%include('footer.tpl')




