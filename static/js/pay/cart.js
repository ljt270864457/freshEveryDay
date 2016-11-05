$(function() {
	var name = $('#userName').html();
	if (name) {
		$('#welcome').show();
		$('#login').hide();
	} else {
		$('#welcome').hide();
	}

	$('.cart_list_td #del').bind('click', function() {
		var goodsID = $(this).parent().next('li').html();
		// $.ajax({
		// 		url: '/delGoodsHandeler/',
		// 		type: 'POST',
		// 		dataType: 'json',
		// 		data: {
		// 			'goodsID': goodsID
		// 		},
		// 	})
		// 	.done(function() {
		// 		alert('删除成功')
		// 	})
		var count = parseInt($('.total_count em').text());
		count -= 1;
		$('.total_count em').text(count);
		$('.settlements .col03 b').text(count);
		$(this).parent().parent().remove();
		$('.settlements .col03 em').text(getFinalPrice());
	})

	$('.add').bind('click', function() {
		var num = parseInt($(this).next('input').val());
		num += 1;
		$(this).next('input').val(num);
		var pricestr = $(this).parent().parent().prev().html();
		var patt = '^[1-9]+[0-9]*.?[0-9]*';
		var price = parseFloat(pricestr.match(patt));
		var sumPrice = (num * price).toFixed(2);
		$(this).parent().parent().next().html(sumPrice + '元');
		$('.settlements .col03 em').text(getFinalPrice());

	})
	$('.minus').bind('click', function() {
		var num = parseInt($(this).prev('input').val());
		if (num <= 1) {
			$(this).prev('input').val(1);
		} else {
			num -= 1;
			$(this).prev('input').val(num);
		}
		var pricestr = $(this).parent().parent().prev().html();
		var patt = '^[1-9]+[0-9]*.?[0-9]*';
		var price = parseFloat(pricestr.match(patt));
		var sumPrice = (num * price).toFixed(2);
		$(this).parent().parent().next().html(sumPrice + '元');
		$('.settlements .col03 em').text(getFinalPrice());
	})

	$('.num_show').bind('keyup', function() {
		var num = $(this).val();
		if (parseInt(num) && parseInt(num) > 0) {
			var pricestr = $(this).parent().parent().prev().html();
			var patt = '^[1-9]+[0-9]*.?[0-9]*';
			var price = parseFloat(pricestr.match(patt));
			var sumPrice = (num * price).toFixed(2);
			$(this).parent().parent().next().html(sumPrice + '元');
		} else {
			$(this).html(1);
		}
		$('.settlements .col03 em').text(getFinalPrice());

	})

	$('.settlements .col01 input').bind('click', function() {
		if ($(this).prop('checked')) {

			$('.cart_list_td .col01 input').each(function() {
				$(this).prop('checked', true);
			})
		} else {
			$('.cart_list_td .col01 input').each(function() {
				$(this).prop('checked', false);
			})
		}
		$('.settlements .col03 em').text(getFinalPrice());
	})

	function getFinalPrice() {
		var sumPrice = 0;
		if ($('.cart_list_td .col01 input').prop('checked')) {
			var priceStrList = $('.cart_list_td .col01 input').parent().siblings('.col07').text().split("元");
			for (item in priceStrList) {
				if (priceStrList[item].length > 0) {
					sumPrice += parseFloat(priceStrList[item]);
				}
			}
		}
		return sumPrice.toFixed(2);
	}

})