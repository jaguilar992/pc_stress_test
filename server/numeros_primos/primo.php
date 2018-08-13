<?php  
  $resp = [];
  if (isset($_POST['valor'])){
    $num = $_POST['valor'];
    $retorno=0;
    $cont=0;
    for($i = 1; $i <= $num; $i++){
      if($num % $i == 0){
        $cont++;
      }
    }
    $resp['resultado'] = $retorno!=2;
    echo json_encode($resp);
  }else{
    $resp['resultado'] = 'No se encontró valor';
    echo json_encode($resp);
  }
?>