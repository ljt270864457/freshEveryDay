$(function(){
	$('.add_goods').click(function(){
		var goodName = $(this).parent().prev().children('.goods_name').text()
		$.ajax({
			url: '/addGoodsHanderler/',
			type: 'POST',
			dataType: 'json',
			data: {'name': goodName},
		})
		
	})
})