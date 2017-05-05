%include('header.tpl')
<br>
	<h1>BUSCADOR DE VIDEOS</h1>
	<h1>Resultado de la busqueda <strong>{{buscar}}</strong> son:</h1>
	% for a,b in zip(lista_ti,lista_id):
		<p>Enlace: <a href="https://www.youtube.com/watch?v={{b}}"><strong>{{a}}</strong></a></p>
		<form action="/twitter" method="post">
			<input type="hidden" name="url" value="https://www.youtube.com/watch?v={{b}}"/>
    		<p><input type="submit" class="button" value="Enviar" /></p>
		</form>
		<iframe width="854" height="480" src="https://www.youtube.com/embed/{{b}}" frameborder="0" allowfullscreen></iframe>
	%end
<br>
%include('footer.tpl')
