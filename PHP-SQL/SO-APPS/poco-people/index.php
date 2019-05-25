<?php
require_once('php/config.php');
require_once('php/functions.php');


/* QUERY - GET PEOPLE
----------------------------------------*/
$sth = db()->prepare("SELECT first_name, last_name, country_id, birth_year FROM people ORDER BY last_name ASC");
$sth->execute();
$people = $sth->fetchAll(); //show($people);

$sth = db()->prepare("SELECT country_id, name FROM countries");
$sth->execute();
$countries = $sth->fetchAll(PDO::FETCH_KEY_PAIR); //show($countries);
//$countries = array_map('reset', $countries); show($countries);


/* PEOPLE ITEMS LIST
----------------------------------------*/
//INIT VAR
$list_items = '';

//START LOOP
foreach($people as $item) {
	
	$name = $item['last_name'].', '.$item['first_name'];
	$country = $countries[ $item['country_id'] ];
	$age = (int)date('Y') - $item['birth_year'] ?? false;
	
	$list_items .= '<tr>';
	$list_items .= '<td>'.$name.'</td>'.PHP_EOL;
	$list_items .= '<td>'.$country.'</td>'.PHP_EOL;
	$list_items .= '<td>'.$age.'</td>'.PHP_EOL;
	$list_items .= '</tr>';
	
} //END LOOP
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Poco People - Coming soon</title>
</head>
<body>

  <h1>PoCo People - LIST</h1>
  
  <table id="people-list" class="table">
  <thead>
  	<tr>
      <th>Name</th>
      <th>Country</th>
      <th>Age</th>
    </tr>
  </thead>
  <?php echo $list_items; ?>
  </table>
  
</body>
</html>