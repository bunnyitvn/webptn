(function ($) {


  /* ------------------------------- */
  $(function(){
  	
  	if($('div').is('#slideshow')){slide_function();}
  	if($('div').is('#aside')){aside_function();}
  	if($('div').is('#news_section')){news_function();}
    // load_event();

    /*slidescroll*/
    // $("a[href*='#']").slideScroll();
/**/
$("#topics dt:even").addClass("bg_b");
  });

})(jQuery);

/*image rollover*/
// var load_event = function(){
  // $('a>img[src*="-out-"],input[src*="-out-"]').each(function(){
    // var $$ = $(this);
    // $$.mouseover(function(){ $(this).attr('src', $(this).attr('src').replace(/-out-/,'-on-')) });
    // $$.mouseout (function(){
      // if ( $(this).attr('wws') != 'current' ) { $(this).attr('src', $(this).attr('src').replace(/-on-/,'-out-')) }
    // });
  // });
// 
  // $('a[subwin]').die('click').click(subwin_func);
// 
// }

/*sub window*/
// var subwin_func = function () {
  // var $$ = $(this);
  // var param = $$.attr('subwin').split(/\D+/);
  // var w = param[0] || 300;
  // var h = param[1] || 300;
  // var s = ($$.attr('subwin').match(/slim/))?'no':'yes';
  // var r = ($$.attr('subwin').match(/fix/) )?'no':'yes';
  // var t = $$.attr('target') || '_blank' ;
  // window.open( $$.attr('href'), t, "resizable="+r+",scrollbars="+s+",width="+w+",height="+h ).focus();
  // return false;
// }

var slide_function = function () {	
	var $slideshow= $('#slideshow_content');
	var $control=$('#slideshow #slideshow_control .control_navi');
	var $control_item = $('#slideshow #slideshow_control .control_navi li');
	var $control_next = $('#slideshow .control_right');
	var $control_prev = $('#slideshow .control_left');
	var $slide_item = $('#slideshow #slideshow_inner p');
	var size=$slide_item.size()
	var speedTime = 1000;
	var waitTime = 1000;
	var flag = true;
	var slide_function=function (next) {
		if(flag){
			flag=false;
			clearTimeout(timer);
			var current = $slide_item.index($slideshow.find(".active:first"));
			var active;
			if(next=='next' || next=='auto'){active=current+1;if(active>=size){active=0;}}
			else if(next=='prev'){
				active=current-1;if(active<0){active=size-1;}
			}
			else{active= next;}	
			$slide_item.removeClass('active');
			$control_item.removeClass('active');
			$control_item.eq(active).addClass('active');
			$slide_item.eq(current).fadeOut(speedTime,function () {
				$slide_item.eq(active).fadeIn(speedTime,function () {
					$(this).addClass('active');flag = true;
					if(next=='auto')
						timer = setTimeout(function(){slide_function("next");}, waitTime);
					})})
		}
	}
	var initslide = function () {
		if(size>1){
			// $control_manager.hide();
			$('#slideshow #slideshow_control .control_navi').css({width:(parseFloat($control_item.width())+parseFloat($control_item.css('margin-left'))+parseFloat($control_item.css('margin-right')))*($control_item.size())});
			$slide_item.removeClass('active').hide();
			$slide_item.eq(0).addClass('active').fadeOut(waitTime,function () {
				$control_item.each(function(i){		
					$(this).bind("click",{index:i}, function(e){
						clearTimeout(timer);
						var current = $control_item.index($control.find(".active:first"));
						
						if(e.data.index !== current){
							slide_function(e.data.index);
							}
						})
				})
			});
			$control_item.removeClass('active');
			$control_item.eq(0).addClass('active');	
			timer = setTimeout(function(){slide_function("auto");}, waitTime);
			$control_next.unbind('click').bind("click", function(){
				console.log("next")
				clearTimeout(timer);
				slide_function("next");
				});
			$control_prev.unbind('click').bind("click", function(){
				clearTimeout(timer);
				slide_function("prev");
				});
			$slideshow.bind("mouseout", function(){
				clearTimeout(timer);timer = setTimeout(function(){slide_function("auto");}, waitTime);
				});
			$slideshow.bind("mouseover", function(){
				clearTimeout(timer);
				});
			
		}
	}
	initslide();	  
}
var aside_function= function () {
	var $aside_slide_view = $('#inner_aside');
	var $aside_slide_mask = $('#inner_aside .navi_aside');
	var $aside_slide_item = $('#inner_aside .navi_aside li');
	var size_aside_item=$aside_slide_item.size();
	var width_aside_item=$aside_slide_item.width()+50;
	var max_width_aside_item=size_aside_item*width_aside_item;
	var mask_width=max_width_aside_item*3;
	var start_aside=null;
	var speed = 3;
	var auto_Speed=speed;
	var interval = 35;
	var waitTime = 5000 ;
	var flag = false;
	var loop_aside = function () {	
		asidetimer = setTimeout(function(){
			var start_aside=parseInt($aside_slide_mask.css('left'));
			if(start_aside<-1*(max_width_aside_item*2) || start_aside>0){
				start_aside=-max_width_aside_item;
			}
			var move_Auto = start_aside - auto_Speed;
			$aside_slide_mask.css({left:move_Auto});	
			loop_aside();
		}, interval);
	}
	var init_multi_function= function () {		
		$aside_slide_mask.css({width : mask_width,left : -max_width_aside_item});      
		$aside_slide_item.clone().prependTo($aside_slide_mask);
		$aside_slide_item.clone().appendTo($aside_slide_mask);
		loop_aside();
		$aside_slide_view.bind("mouseover",function(){
			clearInterval(asidetimer);	
		});
		$aside_slide_view.bind("mouseout",function(){
			loop_aside();
		});
	}
	init_multi_function();
}
var news_function= function () {
	var $news_slide_view = $('#news_section');
	var $news_slide_mask = $('#news_section .navi_section');
	var $news_slide_item = $('#news_section .navi_section li');
	var size_news_item=$news_slide_item.size();
	var height_news_item=$news_slide_item.height()+20;
	var max_height_news_item=size_news_item*height_news_item;
	var mask_height=max_height_news_item*3;
	var start_news=null;
	var speed = 2;
	var auto_Speed=speed;
	var interval = 35;
	var waitTime = 5000 ;
	var flag = false;
	var loop_news = function () {	
		newstimer = setTimeout(function(){
			var start_news=parseInt($news_slide_mask.css('top'));
			if(start_news<-1*(max_height_news_item*2) || start_news>0){
				start_news=-max_height_news_item;
			}
			var move_Auto = start_news - auto_Speed;
			$news_slide_mask.css({top:move_Auto});	
			loop_news();
		}, interval);
	}
	var init_multi_function= function () {		
		$news_slide_mask.css({height : mask_height,top : -max_height_news_item});      
		$news_slide_item.clone().prependTo($news_slide_mask);
		$news_slide_item.clone().appendTo($news_slide_mask);
		loop_news();
		$news_slide_view.bind("mouseover",function(){
			clearInterval(newstimer);	
		});
		$news_slide_view.bind("mouseout",function(){
			loop_news();
		});
	}
	init_multi_function();
}