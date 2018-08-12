function evaluar() {
	$num = document.getElementById("txt_numero").value;;
  	$retorno=0;
    $cont=0;
  	for($i = 1; $i <= $num; $i++){
    	if($num % $i == 0){
      		$cont++;
  		};
  	};	
  	if($cont==2){
    	alert("Es un numero primo");
  	}else{
    	alert("No es un numero primo");
  	};
}