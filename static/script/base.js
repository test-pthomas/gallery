String.prototype.endsWith = function(str) {
  var lastIndex = this.lastIndexOf(str);
  return (lastIndex != -1) && (lastIndex + str.length == this.length);
}

function trimSlash(url) {
  if (url.endsWith("/")) {
    return url.substr(0, url.length - 1);
  } else {
    return url;
  }
}
jQuery(document).ready(function() {    
  //set the current page in the menu
  var trimUrl = trimSlash(location.pathname); 
  //use this to check contains safely
  jQuery('#menu li a').each(function() {
    var trimLink = trimSlash(jQuery(this).attr('href'));
    if (trimLink == "") {
      if (trimUrl == "") {
        jQuery(this).parent().addClass('current');
      }
    } else if (trimUrl.endsWith(trimLink)) {
      jQuery(this).parent().addClass('current');
    }
  });
  
  jQuery("#menu").fadeIn();
  jQuery("#content").fadeIn();
  
  //like I note elsewhere, this is a goofy thing to do
  //but it looks cool so all non outgoing links have fade effects
  jQuery("a[target!='blank']").click(function(e) {
    var link = jQuery(this);
    
    //don't go to the page until we fade out
    e.preventDefault();
    
    jQuery("#menu").fadeOut();
    jQuery("#content").fadeOut(function() {
      //NOW you can go to the page
      location.href = link.attr("href");
    })  
  });
});
