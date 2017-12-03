<?php
	 
	// Database connection 
	$db = new mysqli('localhost', 'jeopardyAdmin', 'AlexTribeaks', 'jeopardy');

	if($db->connect_errno > 0){
		die('Unable to connect to database [' . $db->connect_error . ']');
	}
	
	
	// SQL Query execution
	$sql = <<<SQL
				SELECT q.question_text as question, 
					   q.answer, 
					   q.round_name,
					   g.season_number as season
				FROM question q, 
				     game g 
			    WHERE g.game_id = q.game_id 
				      AND q.round_name='Final'
SQL;

	if(!$result = $db->query($sql)){
		die('There was an error running the query [' . $db->error . ']');
	}

?>
<head> 
	<title>Jeopardy - Game database</title> 
	<link rel="stylesheet" href="css/layout.css"/> 
	<script src="js/navigation.js"></script>
</head>
<body>
	<table class="box">
		<tr>
			<td>
				<center>
					<br/><br/>
					<img src="images/jeopardy_logo.jpg" height="30%" width="70%"/>
					<h4>Your Results </h4>
				</center>
			</td>
		</tr>
	</table>
	<table class="result_box">
		<tr>
			<td>
				<div class="scroller"> 
				<table border="1" width="100%" align="center"  cellpadding="0">
					<thead>
						<tr>
							<th bgcolor="#f4bc42">Sr. No.</th>
							<th bgcolor="#f4bc42">Question</th>
							<?php

								if(isset($_POST['answer'])){
									print("<th bgcolor='#f4bc42'>Answer</th>");
								}
								if(isset($_POST['season'])){
									print("<th bgcolor='#f4bc42'>Season</th>");
								}
								if(isset($_POST['round'])){
									print("<th bgcolor='#f4bc42'>Round Name</th>");
								}
							?>
						</tr>
					</thead>
					<tbody>
					<?php
						$counter = 0;
						while($row = $result->fetch_assoc()){
							$counter = $counter + 1;
							print("<tr>");
							print("<td align='center'>".$counter."</td>");
							print("<td>".$row['question']."</td>");
							if(isset($_POST['answer'])){
								print("<td>".$row['answer']."</td>");
							}
							if(isset($_POST['season'])){
								print("<td>".$row['season']."</td>");
							}
							if(isset($_POST['round'])){
								print("<td>".$row['round_name']."</td>");
							}
							print("</tr>");	
						} 
					?>
					
					</tbody>
				</table>
				</div>	
				<br/>
				<center>
					<input type="button" value="Back" name="back" onclick="goBack()" class="search"/>
				</center>						
			</td>
		</tr>
		
	</table>
	
</body>