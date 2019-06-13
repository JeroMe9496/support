# WordPress
Optimisation, Recommended plugins, Learning ressources

<br>

## Optimisation

**functions.php**
```php
<?php
//MAIN CONTSTANTS - FOR REQUIRES
define('TEMPLATE_DIR', str_replace('\\', '/', get_template_directory()).'/'); //reverse slashes for Windows
define( 'TEMPLATE_INC_DIR', TEMPLATE_DIR.'inc/' );


//GET PATH TO MISC DIRS - FOR NORMAL LINKS
function get_path_to($end_path = '', $dir = 'theme') {

	$wp_content		= '/wp-content/';

	if($dir === 'theme') {
		$active_theme	= get_template_directory_uri().'/';
		return $active_theme.$end_path;
	}
	elseif($dir === 'uploads') {
		$upload_dir = wp_upload_dir();
		$uploads_dir = $upload_dir['baseurl'];
		return $uploads_dir.'/'.$end_path;
	}
	
}


//ADD TITLE TAG IN HEAD
add_theme_support( 'title-tag' );


//DISABLE DEFAULT EMBED SCRIPTS
add_action( 'init', function() {

    // Remove the REST API endpoint.
    remove_action('rest_api_init', 'wp_oembed_register_route');

    // Turn off oEmbed auto discovery.
    // Don't filter oEmbed results.
    remove_filter('oembed_dataparse', 'wp_filter_oembed_result', 10);

    // Remove oEmbed discovery links.
    remove_action('wp_head', 'wp_oembed_add_discovery_links');

    // Remove oEmbed-specific JavaScript from the front-end and back-end.
    remove_action('wp_head', 'wp_oembed_add_host_js');
}, PHP_INT_MAX - 1 );


//DISABLE (SOME ?) WP HEAD AUTO SHIT
remove_action( 'wp_head', 'feed_links_extra', 3); //disable feeds
remove_action ('wp_head', 'rsd_link'); //disable EditURI/RSD Weblog Client Link
remove_action('wp_head', 'wp_generator'); //disable meta "generator"
remove_action( 'wp_head', 'wlwmanifest_link'); //disable Windows Live Writer Manifest Link


//DISABLE WP EMOJI SHIT !
function disable_wp_emojicons() {

  // all actions related to emojis
  remove_action( 'admin_print_styles', 'print_emoji_styles' );
  remove_action( 'wp_head', 'print_emoji_detection_script', 7 );
  remove_action( 'admin_print_scripts', 'print_emoji_detection_script' );
  remove_action( 'wp_print_styles', 'print_emoji_styles' );
  remove_filter( 'wp_mail', 'wp_staticize_emoji_for_email' );
  remove_filter( 'the_content_feed', 'wp_staticize_emoji' );
  remove_filter( 'comment_text_rss', 'wp_staticize_emoji' );

  // filter to remove TinyMCE emojis
  add_filter( 'tiny_mce_plugins', 'disable_emojicons_tinymce' );
}
add_action( 'init', 'disable_wp_emojicons' );

function disable_emojicons_tinymce( $plugins ) {
  if ( is_array( $plugins ) ) {
    return array_diff( $plugins, array( 'wpemoji' ) );
  } else {
    return array();
  }
}
add_filter( 'emoji_svg_url', '__return_false' );


//DISABLE Gutenberg CSS
function wps_deregister_styles() {
	wp_dequeue_style( 'wp-block-library' );
}
add_action( 'wp_print_styles', 'wps_deregister_styles', 100 );


//Show REST API only for admin - Require Authentication for All Reque​sts
add_filter('rest_authentication_errors', function($result) {
	if(!empty($result)) {
		return $result;
	}
	if(!is_user_logged_in()) {
		return new WP_Error( 'rest_not_logged_in', 'You are not currently logged in.', array( 'status' => 401 ) );
	}
	return $result;
});


//DISABLE REST API
add_filter('rest_enabled', '__return_false');
add_filter('rest_jsonp_enabled', '__return_false');

remove_action( 'xmlrpc_rsd_apis', 'rest_output_rsd' );
remove_action( 'wp_head', 'rest_output_link_wp_head', 10 );
remove_action( 'template_redirect', 'rest_output_link_header', 11 );


//ADMIN - Show only published post/pages BY DEFAULT
// change post link to display published posts only
function wcs_change_admin_post_link() {
  global $submenu;
  $submenu['edit.php'][5][2] = 'edit.php?post_status=publish';
}
add_action( 'admin_menu', 'wcs_change_admin_post_link' );


//ADMIN - change page link to display published pages only
function wcs_change_admin_page_link() {
  global $submenu;
  $submenu['edit.php?post_type=page'][5][2] = 'edit.php?post_type=page&post_status=publish';
}
add_action( 'admin_menu', 'wcs_change_admin_page_link' );
?> 
```


## Inheritance :

```php

```
