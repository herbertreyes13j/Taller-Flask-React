function eliminar(libro){
  fetch('http://localhost:5000/libros/' +libro, {
  method: 'DELETE',
})
.then(res => res.text()) // or res.json()
.then(res => {
  alert(res)
  actualizar()
})
}

function agregarlibro(){
  var titulo = document.getElementById("titulo");
  var autor = document.getElementById("autor");
  var descripcion = document.getElementById("descripcion");
  var imagen = document.getElementById("imagen")
  let headers = new Headers();
	headers.append('Content-Type', 'application/json');
	headers.append('Accept', 'application/json');
  fetch('http://localhost:5000/libros', {
    method: 'POST',
    headers,
    body: `{
        "titulo":"${titulo.value}",
        "autor":"${autor.value}",
        "descripcion":"${descripcion.value}",
        "imagen":"${imagen.value}"
      }`,
  })
  .then(response => response.json())
  .then(result => {
    console.log('Success:', result);
    actualizar()

    titulo.value=''
    autor.value=''
    descripcion.value=''
    imagen.value=''
  })
  .catch(error => {
    console.error('Error:', error);
  });

  

}

function modificarlibro(){
  var titulo_o = document.getElementById("vtitulo");
  var titulo = document.getElementById("ntitulo");
  var autor = document.getElementById("nautor");
  var descripcion = document.getElementById("ndescripcion");
  var imagen = document.getElementById("nimagen")
  let headers = new Headers();
	headers.append('Content-Type', 'application/json');
	headers.append('Accept', 'application/json');

  let reque = `{
    "titulo":"${titulo.value}",
    "autor":"${autor.value}",
    "descripcion":"${descripcion.value}",
    "imagen":"${imagen.value}"
  }`

  console.log(reque)
  fetch('http://localhost:5000/libros/'+titulo_o.value, {
    method: 'PUT',
    headers,
    body: reque,
  })
  .then(response => response.json())
  .then(result => {
    console.log('Success:', result);
    actualizar()
    titulo_o.value=''
    titulo.value=''
    autor.value=''
    descripcion.value=''
    imagen.value=''
    
  })
  .catch(error => {
    console.error('Error:', error);
  });

  

}


function actualizar(){
  document.getElementById("cardsc").innerHTML = '';
  let text="";
  fetch('http://localhost:5000/obtenerlibros')
  .then(response => response.json())
  .then(data =>{
      var i;
      for(i=0;i<data.length;i++){
          text+= `<br>
                  <div class="col-sm-3" style="margin-top: 25px;">
                  <div class="card bg-light" style="width: 18rem;">
                  <img class="card-img-top" src="${data[i].imagen}" alt="Card image cap">
                  <div class="card-body">
                      <h4 class="card-title">${data[i].titulo}</h4>
                      <h5 class="card-title">${data[i].autor}</h5>
                      <p class="card-text">${data[i].descripcion}</p>
                      <button href="#" class="btn btn btn-danger" onclick="eliminar('${data[i].titulo}')">Eliminar</button>
                  </div>
                  </div>
                  </div>
                  <br>`
          console.log(data[i].nombre,'prueba')
      }
      document.getElementById("cardsc").innerHTML = text;
  });


}