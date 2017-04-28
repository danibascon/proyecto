%include('header.tpl')
<br>
	<h1>Resultado de la busqueda<strong>{{buscar}}</strong> son:</h1>
	% for a,b,c in zip(lista_ti,lista_id,lista_foto):
		<p>Enlace: <a href="https://www.youtube.com/channel/{{b}}"><strong>{{a}}</strong></a></p>
		<form action="/twittear" method="post">
    		<p><textarea name="tweet" id="textbox" rows="3" cols="50"></textarea></p>
    		<p><input type="submit" class="button" value="Enviar" /></p>
		</form>		
		<img aria-hidden="true" width="64" alt="" height="64" src="{{c}}" >

	%end
</br>
%include('footer.tpl')
