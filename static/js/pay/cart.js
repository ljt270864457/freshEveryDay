$(function() {
	var name = $('#userName').html();
	if (name) {
		$('#welcome').show();
		$('#login').hide();
	}

	$('.cart_list_td #del').bind('click', function() {
		var goodsID = $(this).parent().next('li').html();
		$(this).parent().parent().remove();
		$.ajax({
				url: '/delGoodsHandeler/',
				type: 'POST',
				dataType: 'json',
				data: {
					'goodsID': goodsID
				},


			})
			.done(function() {
				alert('删除成功')
			})


	})
})