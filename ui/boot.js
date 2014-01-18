


$(function(){
	collapse();
});


$.fn.isTextless = function() {
   var txt = this.first()
                 .clone()
                 .find('style')
                 .remove()
                 .end()
                 .text();

   return $.trim(txt).length === 0; 
}

function collapse(){
	
	
    $('._collapse').each(function(){
	if ( $(this).isTextless() ) {
		$(this).remove();
	}	
    });
    
    if($('.pageContainer').isTextless()){
	$('#bottombar').hide();
    }
}