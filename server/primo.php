<?php  
  $resp = [];
  if (isset($_POST['valor'])){
    $num = $_POST['valor'];
    $num = intval($num);
    $cont=0;
    for($i = 2; $i < $num; $i++){
      if($num % $i == 0){
        $cont++;
      }
    }
    $resp['es_primo'] = $cont==0;
    $resp['factores'] = $cont + 2;
    echo json_encode($resp);
  }else{
    $resp['result'] = 'No se encontró valor';
  }
?>
