<?php  
	$num = $_POST['valor'];
	$retorno=0;
    $cont=0;
	for($i = 1; $i <= $num; $i++){
		if($num % $i == 0){
			$cont++;
	};
	if($cont==2){
		$retorno = 1;
	}else{
		$retorno=0;
	};
    echo $retorno;
?>