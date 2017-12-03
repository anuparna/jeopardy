<?php
    
    $question_asked = $_POST['question'];   
	if($question_asked == 'FR'){
		include 'final_round_questions.php';
	}
	else if($question_asked == 'KJ'){
		
	}
	else if($question_asked == 'BR'){
		
	}
	else{
	   print("Please select an option in the previous page to proceed further.");
	}
?>