$(window).on('scroll', function(event) {
    var scrollValue = $(window).scrollTop();
    if (scrollValue > 70) {
         $('.header_menu').addClass('fixed-top animated slideInDown');
    } else{
      $('.header_menu').removeClass('fixed-top animated slideInDown');
    } 
});


  
"use strict";


/*======== Doucument Ready Function =========*/
jQuery(document).ready(function () {

    /**
     * Highlight current top-level navigation item.
     */
    (function setActiveNavigation() {
      var currentPage = window.location.pathname.split('/').pop() || 'index.html';
      var sectionMap = {
        'aboutus.html': 'aboutus.html',
        'restaurant.html': 'restaurant.html',
        'restaurant-menu.html': 'restaurant.html',
        'restaurant-reserve.html': 'restaurant.html',
        'restaurant-about.html': 'restaurant.html',
        'blog-full.html': 'blog-full.html',
        'blog-right.html': 'blog-full.html',
        'single-left.html': 'blog-full.html',
        'single-right.html': 'blog-full.html',
        'single-full.html': 'blog-full.html',
        'contact.html': 'contact.html',
        'room.html': 'room.html',
        'Deluxeroom.html': 'room.html',
        'Familyroom.html': 'room.html',
        'Lakeviewroom.html': 'room.html',
        'roomlist-1.html': 'room.html',
        'roomlist-2.html': 'room.html',
        'room-select.html': 'room.html',
        'detail-full.html': 'room.html',
        'detail-sidebar.html': 'room.html',
        'availability.html': 'room.html',
        'booking.html': 'room.html'
      };
      var activeHref = sectionMap[currentPage] || currentPage;
      var navMenus = $('#responsive-menu, .responsive-menu');

      navMenus.find('li').removeClass('active');

      navMenus.each(function () {
        var menu = $(this);
        var activeLink = menu.find('a').filter(function () {
          var href = $(this).attr('href');
          return href && href.split('/').pop() === activeHref;
        }).first();

        if (!activeLink.length && (currentPage === '' || currentPage === 'index.html')) {
          activeLink = menu.find('a[href="index.html"]').first();
        }

        if (activeLink.length) {
          activeLink.closest('li').addClass('active');
          activeLink.parents('li.submenu').first().addClass('active');
        }
      });
    }());

      // slicknav
    /**
     * Slicknav - a Mobile Menu
     */
    var $slicknav_label;
    $('.responsive-menu').slicknav({
      duration: 500,
      easingOpen: 'easeInExpo',
      easingClose: 'easeOutExpo',
      closedSymbol: '<i class="fa fa-plus"></i>',
      openedSymbol: '<i class="fa fa-minus"></i>',
      prependTo: '#slicknav-mobile',
      allowParentLinks: true,
      label:"" 
    });

    var $slicknav_label;
    $('#responsive-menu').slicknav({
      duration: 500,
      easingOpen: 'easeInExpo',
      easingClose: 'easeOutExpo',
      closedSymbol: '<i class="fa fa-plus"></i>',
      openedSymbol: '<i class="fa fa-minus"></i>',
      prependTo: '#slicknav-mobile',
      allowParentLinks: true,
      label:"" 
    });

    
    /**
     * Sticky Header
     */
        
    $(window).scroll(function(){

      if( $(window).scrollTop() > 10 ){

        $('.navbar').addClass('navbar-sticky-in')

      } else {
        $('.navbar').removeClass('navbar-sticky-in')
      }

    })
    
    /**
     * Main Menu Slide Down Effect
     */
     
    var selected = $('#navbar li');
    // Mouse-enter dropdown
    selected.on("mouseenter", function() {
        $(this).find('ul').first().stop(true, true).delay(350).slideDown(500, 'easeInOutQuad');
    });

    // Mouse-leave dropdown
    selected.on("mouseleave", function() {
        $(this).find('ul').first().stop(true, true).delay(100).slideUp(150, 'easeInOutQuad');
    });

    /**
     *  Arrow for Menu has sub-menu
     */
    if ($(window).width() > 992) {
      $(".navbar-arrow ul ul > li").has("ul").children("a").append("<i class='arrow-indicator fa fa-angle-right'></i>");
    }

});
