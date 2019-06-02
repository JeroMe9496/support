<?php
if( !defined('IS_ADMIN_INDEX')) {
  exit();
}


//WHAT FUNCTION TO CALL ?
if(empty($action) || $action === 'pages') {
  pages();
}
else {
  page_detail($action);
}



/**
 * PAGES LIST
 * ========================================================
 */
/*#region PAGES*/
function pages() {


  /* PAGES QUERY
  ----------------------------------------*/
  $sql = "SELECT id, title, menu FROM pages ORDER BY position ASC";
        
  try {

    $sth = db()->prepare($sql);
    $sth->execute($params);
    $pages = $sth->fetchAll();
    //$results = array_map('reset', $results); //debug($results);
    
  } catch(PDOException $e) {
    debug($e->getMessage());
  }
  //$pages = crud('pages_list');


  /* TABLE ROWS
  ----------------------------------------*/
  //INIT VAR
  $rows = '';

  //START LOOP
  foreach($pages as $key => $page) {
    
    $id			= (int)$page['id'];
    $title  = $page['title'];
    $menu   = $page['menu'];

    $edit_link = '?page=pages&action=edit-page&id='.$id;

    $rows .= '
    <tr>
      <td>'.$id.'</td>
      <td><a href="'.$edit_link.'" title="Edit page">'.$title.'</a></td>
      <td>'.$menu.'</td>
      <td class="tools">
        <a class="tool edit uk-margin-right" uk-icon="icon: pencil" href="'.$edit_link.'"></a>
        <a class="tool edit" uk-icon="icon: trash" href="?crud-action=delete-page&id='.$id.'"></a>
      </td>
    </tr>
    ';
    
  } //END LOOP


  /* HTML DISPLAY
  ----------------------------------------*/
  $html = admin_header([
    'title' => 'Pages list',
    'buttons' => '<a href="?page=pages&amp;action=new-page" class="uk-button uk-button-default">New Page</a>'
  ]);
  
  $html .= '
  <table id="pages-list" class="uk-table uk-table-hover uk-table-middle uk-table-divider">
    <thead>
      <tr>
        <th class="uk-table-shrink">#id</th>
        <th class="country uk-width-xlarge">Title</th>
        <th class="name">Menu</th>
        <th class="tools uk-width-small">Tools</th>
      </tr>
    </thead>
    <tbody>
      '.$rows.'
    </tbody>
  </table>
  ';

  echo $html;

}
/*#endregion PAGES*/



/**
 * PAGE DETAIL
 * ========================================================
 * For edit / new page
 */
/*#region PAGE DETAIL*/
function page_detail($action = 'edit-page') {


  /* INIT VARS
  ----------------------------------------*/
  $id       = (int)req('id');
  $is_edit  = $action === 'edit-page' && $id > 0;
  $is_new   = $action === 'new-page' && !$id;

  $page     = [];


  /* IS EDIT OR NEW CONDITIONAL CONTENT
  ----------------------------------------*/
  if($is_edit) {

    //QUERY - GET PAGE DATA
    $sql = "SELECT id, page_key, title, menu, slug, content FROM pages WHERE id = ?";
    $params = [$id];
          
    try {

      $sth = db()->prepare($sql);
      $sth->execute($params);
      $page = $sth->fetch(); //debug($page);
      
    } catch(PDOException $e) {
      debug($e->getMessage());
    }
    
    $page_title = 'Edit page: <span class="uk-text-primary">' . $page['title'].'</span>';

  }

  else {

    $page_title = 'New page';

  }

  
  /* CREATE FORM ITEMS
  ----------------------------------------*/
  //EDITABLE ITEMS ARRAY
  $editable_items = [
    
    'title'     => $page['title'],
    'menu'      => $page['menu'],
    'page_key'  => $page['page_key'],
    'slug'      => $page['slug'],
    'content'   => $page['content'],

  ];

  $form_items = '';

  //START LOOP
  foreach($editable_items as $key => $value) {

    //FORM INPUT
    if($key !== 'content') {
      $form_input = '<input class="uk-input" id="'.$key.'" type="text" value="'.$page[$key].'">';
    }
    else {
      $form_input = '<textarea class="uk-textarea" id="'.$key.'" rows="8">'.$page[$key].'</textarea>';
    }

    $form_items .= '
    <div class="uk-margin uk-flex">
      <label class="uk-form-label W10p" for="'.$key.'">'.ucfirst($key).':</label>
      <div class="uk-form-controls DB W90p">
        '.$form_input.'
      </div>
    </div>
    ';

  } //END LOOP


  /* HTML DISPLAY
  ----------------------------------------*/
  $html = admin_header([
    'title' => $page_title,
    'buttons' => '<a href="?page=pages" class="uk-button uk-button-default"><span class="uk-close" uk-close></span> Close</a>'
  ]);

  $html .= '
  <form class="uk-form-stacked" action="crud.php" method="post">
  
  '.$form_items .'
  
  <div class="uk-margin uk-flex uk-flex-right">
    <button class="uk-button uk-button-primary">Submit</button>
  </div>

  </form>

  <script src="https://cdnjs.cloudflare.com/ajax/libs/tinymce/4.9.4/tinymce.min.js"></script>
  <script src="js/tinymce-init.js"></script>  
  ';


  echo $html;


}
/*#endregion PAGE DETAIL*/
