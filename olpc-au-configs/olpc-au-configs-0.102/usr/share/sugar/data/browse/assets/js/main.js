$(".container").fadeIn(2000);

$('img').bind('mouseover',function(){
	$(this).animate({
		height: "210px",
		width: "210px"
	}, 100)
});

$('img').bind('mouseout',function(){
    $(this).animate({
    	height: "200px",
    	width: "200px"
    }, 100)
})	