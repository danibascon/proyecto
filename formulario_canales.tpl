%include('header.tpl')
<br>
	<h1>Resultado de la busqueda<strong>{{buscar}}</strong> son:</h1>
	% for a,b,c in zip(lista_ti,lista_id,lista_foto):
		<p>Enlace: <a href="https://www.youtube.com/channel/{{b}}"><strong>{{a}}</strong></a></p> 
		<img aria-hidden="true" width="64" alt="" height="64" src="{{c}}" >

	%end
</br>
%include('footer.tpl')
