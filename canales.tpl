%include('header.tpl')
<br>
	<form action="/canal" method="post">
		<label>Nombre del canal:</label>
		<input type="text" name="buscar" required/>
		<label>Numero de videos:</label>
		<input type="number" name="cantidad" min='1' max='10'required/>
		<input type="submit" value="Enviar">
	</form>
</br>
%include('footer.tpl')
