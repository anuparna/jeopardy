<html> 
	<head>
		<title>Jeopardy - Game database</title> 
		<link rel="stylesheet" href="css/layout.css"/> 
	</head>
	<body>
		
		<form name="index" method="POST" action="results.php">
		<input type="hidden" value="<?=$_POST['choice']?>" name="question"/>
		<table class="box">
			<tr>
				<td>
					<center>
						<br/><br/>
						<img src="images/jeopardy_logo.jpg" height="30%" width="70%"/>
						<h4>With the questions, I also want to see </h4>
						<br/>
					</center>
				</td>
			</tr>
			<tr>
				<td>
					<input type="checkbox" name="answer" value="A"><b>Answer</b><br/><br/>
					<input type="checkbox" name="season" value="S"><b>Season</b><br/><br/>
					<input type="checkbox" name="round" value="R"><b>Type of Round (e.g. Jeopardy, Double Jeopardy, Final)</b><br/><br/>
				</td>
			</tr>
			<tr>
				<td  align="center">
					<input type="reset" align="center" value="Clear" class="search"/>
					<input type="submit" align="center" value="View Results" class="search"/>
				</td>
			</tr>
			
		</table>
		</form>
	</body>
</html>