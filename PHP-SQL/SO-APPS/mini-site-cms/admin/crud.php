<?php
require_once('admin_functions.php');


//STOP HERE IF NO SESSION ADMIN
if( !is_admin() ) {
	exit("Hey dude, only admin can access this page!");
}


//MERGE POST AND GET METHODS
$crud_action = req('crud-action'); show($crud_action); exit();


//CALL CRUD FUNCTION
crud($crud_action);



/**
 * CREATE - READ - UPDATE - DELETE
 * -----------------------------------------------------------------------------
 * ...
 * ...
 */
function crud($crud_action) {


	if(empty($crud_action)) {
		return false;
	}


	//START SWITCH
	switch($crud_action) {


		/* UPDATE/NEW PAGE
		-----------------------------------------------------------*/
		case 'update-page' :
		case 'insert-page' :

			$sql = "SELECT id, title, menu FROM pages ORDER BY position ASC";
			
			try {

				$sth = db()->prepare($sql);
				$sth->execute($params);
				$results = $sth->fetchAll();
				//$results = array_map('reset', $results); //debug($results);
				
			} catch(PDOException $e) {
				debug($e->getMessage());
			}

		break;



		/* PAGE DATA
		-----------------------------------------------------------*/
		case 'page' :

			$sql = "SELECT title, page_key, content_type, content FROM pages WHERE slug = ?";
			
			try {

				$sth = db()->prepare($sql);
				$sth->execute($params);
				$results = $sth->fetch(); //debug($results);
				
			} catch(PDOException $e) {
				debug($e->getMessage());
			}

		break;
		
		
		
		/* HOME SLUG (Default page)
		-----------------------------------------------------------*/
		case 'home_slug' :

			$sql = "SELECT slug FROM pages WHERE is_home = ?";
			
			try {

				$sth = db()->prepare($sql);
				$sth->execute($params);
				$results = $sth->fetch(); //debug($results);
				
			} catch(PDOException $e) {
				debug($e->getMessage());
			}

		break;


	} //END SWITCH


	return $results;


}