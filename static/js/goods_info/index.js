$(function(){
	var name = $('#userName').html();
	if(name.length)
	{
		$('#welcome').show(); 
		$('#login').hide();
	}
	else
	{
		$('#welcome').hide();
	}

	$('#userCenter').bind('click',function(){
		if(!name)
		{
			$(this).attr('href','/login/');
		}
		
	})
	$('#myOrder').bind('click',function(){
		if(!name)
		{
			$(this).attr('href','/login/');
		}		
	})
	$('#cart').bind('click',function(){
		if(!name)
		{
			$(this).attr('href','/login/');
		}		
	})
	$('.cart_name').bind('click',function(){
		if(!name)
		{
			$(this).attr('href','/login/');
		}		
	})
})