<?php
/**
 * ERROR HANDLER
 * ----------------------------------------------
 * Show or not errors ?
 * What kind of error to show ?
 */
ini_set('display_errors', 1); //0 to hide errors
error_reporting(E_ALL & ~(E_STRICT|E_NOTICE)); //E_STRICT|E_NOTICE|E_WARNING



/**
 * GLOBALS
 * ----------------------------------------------
 * Globally available variables & init stuff
 * We store the values to "inject" into our functions 
 */
/*#region GLOBALS*/
/* BASE VARS
---------------------------------*/
$debug_arr  = [];
$site_data  = site_data();                  //debug($site_data);
$pages      = $site_data['pages'];          //debug($pages);
$get_page   = router(array_keys($pages));   //debug('Page: '.$get_page);   



/* PARAMS FOR DEPENDENCY INJECTION
----------------------------------*/
$params = [
  'get_page'    => $get_page,
  'site_info'   => $site_data['site_info'],
  'pages'       => $pages,
  'page_data'   => $pages[$get_page]
];
/*#endregion*/



/**
 * SITE DATA
 * ----------------------------------------------
 * A minimalist example of data storage
 * For this example we use a file of type "json"
 * In a typical CMS the data is stored in a database
 */
/*#region SITE DATA*/
function site_data() {

  $json_file = 'site_data.json';

  //IF FILE EXIST STORE THE CONTENTS INTO A VAR
  $site_data_json = (file_exists($json_file)) ? file_get_contents($json_file) : '';
  
  //IF NOT EMPTY CONVERT JSON TO ARRAY
  $site_data = (trim($site_data_json) !== false) ? json_decode($site_data_json, true) : [];

  //RETURN DATA []
  return $site_data;

}
/*#endregion*/



/**
 * ROUTER - GET CURRENT PAGE FROM URL
 * ----------------------------------------------
 * A minimalist example of "router"
 * It is used to retrieve data from URI and serve the correct page
 * The code below will only work if a .htaccess file exists
 * The "security" part is still to be done.
 */
/*#region ROUTER*/
function router($pages_keys = []) {

  $from_root    = str_replace('/index.php', '', $_SERVER['PHP_SELF']).'/';	//debug('From root: '.$from_root);

  $uri          = $_SERVER['REQUEST_URI'];                        					//debug('URI: '.$uri);
  $uri_page     = str_replace($from_root, '', $uri);              					//debug('URI Page: '.$uri_page);
  $get_page     = !empty($uri_page) ? $uri_page : $pages_keys[0]; 					//debug('Page: '.$get_page);
  
  return $get_page;

}
/*#endregion*/


/**
 * MENU (HTML)
 * ----------------------------------------------
 * An example of a dynamic menu
 * Check the active page and add a CSS class
 * The "echo" at the end will display the contents of what you call this function
 */
/*#region MENU*/
function menu_html($params = []) {

  $pages = $params['pages'];
  $get_page = $params['get_page'];

  //If pages array is empty stop here with a message
  if(empty($pages)) {
    return "You don't have any pages.";
  }

  //INIT
  $html = '';

  //START MENU
  $html .= '<ul class="menu">'.PHP_EOL;


  //START LOOP
  foreach($pages as $page_key => $page_info) {

    $menu = $page_info['menu'];
    $active = $page_key === $get_page ? ' active' : '';

    //Add to menu html
    $html .= '<li class="menu-item'.$active.'"><a href="'.$page_key.'">'.$menu.'</a></li>'.PHP_EOL;

  } //END LOOP


  $html .= '</ul>'.PHP_EOL; //END MENU


  return $html;

}
/*#endregion*/



/**
 * PAGE TITLE(S)
 * ----------------------------------------------
 * Returns a <head> or content title
 */
/*#region PAGE TITLE(S)*/
function title($params = [], $return = '') {

  $global_title = $params['site_info']['global_title'];
  $page_title = $params['page_data']['title'];
  $title = '';

  if($return === 'content') {
    $title = $page_title;
  }
  elseif($return === 'head') {
    $title = $page_title . ' | ' . $global_title;
  }
  else {
    $title = $global_title;
  }

  //If not global return this...
  return $title;

}
/*#endregion*/




/**
 * PAGE CONTENT
 * ----------------------------------------------
 * Displays the content of the current page
 * For this kind of storage we'll search an external file
 */
/*#region PAGE CONTENT*/
function content($params = []) {

  //PREPARE FILE PATH
  $html_file        = $params['page_data']['content']; 
  $html_file_path   = 'html/'.$html_file; //echo $html_file_path;


  //GET FILE CONTENT
  if(file_exists($html_file_path)) {
    $content = file_get_contents($html_file_path);
  }
  else {
    $content = '404. The page you are looking for is not here.';
  }


  return $content;

}
/*#endregion*/



/**
 * DEBUGGER
 * ----------------------------------------------
 * An elaborate debug function to display test code
 */
/*#region DEBUGGER*/
//COLLECT DEBUG DATA
function debug($data = '') {

  if(empty($data)) {
    return false;
  }

  $bt         = debug_backtrace();
  $file_arr   = explode(DIRECTORY_SEPARATOR, $bt[0]['file']);
  $file       = array_pop($file_arr);
  $line       = $bt[0]['line'];

  $GLOBALS['debug_arr'][] = [
    'file' => $file,
    'line' => $line,
    'data' => $data
  ];

}

//DISPLAY DEBUG
function debug_view($debug_arr) {
 
  if(empty($debug_arr)) {
    return false;
  }
  
  $tot_items = count($debug_arr);
  $n = 0;

  echo '<div style="position:absolute;left:0;bottom:0;width:50%;max-width:600px;max-height:50%;overflow:auto;padding:.5em;background:#fff;">';
  echo '<h3 style="font-size:1em;color:#f00;">Debug items</h3>';
  
  echo '<ul style="background-color:rgba(240,240,240,.5);font-size:.9em;padding:1em;border:solid 1px #ddd;">';
  
  //START LOOP
  foreach($debug_arr as $item) {
    
    $n++;

    $style = ($n < $tot_items) ? ' style="padding:0 0 1em 0;margin:0 0 1em 0;border-bottom:dotted 1px #ccc;"' : '';
    echo '<li'.$style.'>';
   
    //DATA
    echo '<pre>';
    print_r($item['data']);
    echo '</pre>';
    
    //FILE INFO
    echo PHP_EOL.'<em style="color:#ccc;font-family:serif;font-style:italic;">' . $item['file'] . ':' . $item['line'] . '</em>' . PHP_EOL;
    
    echo '</li>';
    
  } //END LOOP

  echo '</ul>';
  echo '</div>';

}
/*#endregion*/
