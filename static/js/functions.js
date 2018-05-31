/**
   @var {JSON} global_data  variable donde se almacena la información recojida de las peticiones ajax 
   @var {Array} platillos_carrito  array donde se almacenan los platillos para cargar el carrito con js  */
   var platillos_carrito = new Array();
   var global_data = [{}];
/**
 * @function peticionAJAX Peticion ajax determinada por:
 * @param {String} url dirección url a la que se solicita el request ej: "ajax/get_platillo/"
 * @param {Boolean} async especificando si la peticion ajax es sincrona o asincrona (como hilo)
 * @param {String} type GET ó POST
 * @param {JSON} data_object Informacón para realizar el request ej: { 'getData': Platillo_pk } el info debe ser en json no objeto
 * @param {Boolean} is_return Especifica si la petición espera datos del servidor
 */
function peticionAJAX(url,async,type,data_object,is_return) {
	$.ajax({
		url: url,
		async : async,
		type: type,
		data: data_object,
		dataType: 'json',
		success: function (data) {
			if (is_return) {
				set_global_data(data);
			}
			return data;
		}
	});
}
/**
 * @function getPlatillo retorno de los atributos y el objeto platillo a travez de una peticion ajax
 * @param {Integer} Platillo_pk identificador del platillo que se quiere recibir por parametro
 */
function getPlatillo(Platillo_pk) {
	peticionAJAX("ajax/get_platillo/", false, "POST", {'getData': Platillo_pk },true);
}
// TODO: arreglar el tamaño de los platillos de acuerdo al precio
// TODO: añadir adiconales a la BD
// TODO: actualizar los datos del global data cuando se edita en pantalla la información
function loadPlatillo(Platillo_pk) {
	getPlatillo(Platillo_pk);
	// console.log(global_data.fields);
	document.getElementById("namePL").innerText = global_data.fields.nombre;
	document.getElementById("descPL").innerText = global_data.fields.descripcion;
	document.getElementById("costPL").innerText = "COP $" + global_data.fields.precio;
}


function saveToCart(){
	platillos_carrito.push(global_data.fields);
	peticionAJAX("ajax/save_to_cart/", true, "POST", { 'getData': JSON.stringify(global_data.fields)},false);
	loadCart();
	
}
function cleanCart(){
	peticionAJAX("ajax/clean_cart/", true, "GET", { 'getData': JSON.stringify(global_data.fields) }, false);
	platillos_carrito = new Array();
	// seenTotals(false, "", "");
	loadCart();
}

function seenTotals(isSeen,total,descuento) {
	if (isSeen) {
		document.getElementById("sub-total-cart").innerText = "COL $" + total;
		document.getElementById("discount-cart").innerText = "COL $" + descuento;
		document.getElementById("total-cart").innerText = "COL $" + (total - descuento);
		document.getElementById("label-sub-total-cart").innerText = "Subtotal:";
		document.getElementById("label-discount-cart").innerText = "Descuento:";
		document.getElementById("label-total-cart").innerText = "Total:";
		document.getElementById("global-total").innerText = "$"+(total - descuento);
	}else{
		document.getElementById("sub-total-cart").innerText = "";
		document.getElementById("discount-cart").innerText = "";
		document.getElementById("total-cart").innerText = "";
		document.getElementById("label-sub-total-cart").innerText = "";
		document.getElementById("label-discount-cart").innerText = "";
		document.getElementById("label-total-cart").innerText = "";
		document.getElementById("global-total").innerText = "$0.0";
	}
	
}

function loadSesion() {
	peticionAJAX("ajax/load_sesion/", false, "GET", { 'getData': JSON.stringify(global_data.fields)}, true);
	loadCart();
	// TODO: Se carga la sesion ahora hay que 
	// cargar los platillos visualmente y arreglar lo del PK para identificar y cargar las ediciones
	// revisar como se carga con el pk o como cargar el pk a las variables de sesion
}

function loadCart() {
	// loadSesion();	
	// console.log(platillos_carrito.length);	
	setNotification(platillos_carrito.length);
	// console.log(platillos_carrito)
	var table = document.getElementById("table-cart");
	table.innerHTML = '';
	for (var i = 0; i < platillos_carrito.length; i++) {
		// Crea las hileras de la tabla
		var hilera = document.createElement("tr");

		for (var j = 0; j < 3; j++) {
			// Crea un elemento <td> y un nodo de texto, haz que el nodo de
			// texto sea el contenido de <td>, ubica el elemento <td> al final
			// de la hilera de la tabla
			var celda = document.createElement("td");
			var textoCelda = ""
			if (j == 0) {
				 textoCelda = document.createTextNode("1");
			}if (j == 1) {
				textoCelda = document.createTextNode(platillos_carrito[i].nombre);
				
			}if (j == 2) {
				textoCelda = document.createTextNode(platillos_carrito[i].precio);
			}
			celda.appendChild(textoCelda);
			hilera.appendChild(celda);
		}
		// agrega la hilera al final de la tabla (al final del elemento tblbody)
		table.appendChild(hilera);
	} if(platillos_carrito.length>0){
		calcularPrecio(100);
	}else{
		seenTotals(false,"","")
	}
}

function calcularPrecio(descuento) {
	var total = 0;
	for (var i = 0; i < platillos_carrito.length; i++) {
		total += parseInt(platillos_carrito[i].precio)
	}
	seenTotals(true,total,descuento);
}


function checkout() {
	
}

// sets and getters
function set_global_data(data) {
	try {
		global_data = JSON.parse(JSON.parse(data['content']).getData)[0];
	} catch (error) {
		platillos_carrito = data.getData
	}
	// console.log("seting global data to: " + global_data.fields.nombre);
}

function setNotification(notify) {
	document.getElementById("notificationCart").innerText = notify;
	document.getElementById("notificationCartMobile").innerText = notify;
}
/**
 * @function btn_go_top esta función se ejecuta al cargaar el body (onload) renderiza y 
 * realiza un scroll al top del body al presionar el boton (class = ir-arriba)
 */
function btn_go_top() {
	$(document).ready(function () {
		$('.ir-arriba').click(function () {
			$('body, html').animate({
				scrollTop: '0px'
			}, 300);
		});
		$(window).scroll(function () {
			if ($(this).scrollTop() > 0) {
				$('.ir-arriba').slideDown(20);
			} else {
				$('.ir-arriba').slideUp(20);
			}
		});
	});
}


function alerta() {
	//un alert
	swal("Gracias por usar SwiftService, traeremons tu pedido en breve!").then((value) => {
		switch (value) {
			default:
				location.href = window.location;
		}
	});
}



function checkMeal() {
	document.getElementById("mesa").innerText = "";
	document.getElementById("platillo").innerText = "";
	document.getElementById("btn").innerText = "";
}

function redirecionar() {
	location.href = "http://192.168.0.2:8000/manager/";
}