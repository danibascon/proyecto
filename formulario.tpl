%include('header.tpl')
<br>
	<h1>Resultado de la busqueda<strong>{{buscar}}</strong> son:</h1>
	% for a,b in zip(lista_ti,lista_id):
		<p>Enlace: <a href="https://www.youtube.com/watch?v={{["videoId"]}}"><strong>{{a}}</strong></a></p> 
		<iframe width="854" height="480" src="https://www.youtube.com/embed/{{b}}" frameborder="0" allowfullscreen></iframe>
	%end
</br>
%include('footer.tpl')
