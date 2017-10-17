$(function(){

	$('#slide-submenu').on('click',function() {			        
        $(this).closest('.list-group').fadeOut('slide',function(){
        	$('.mini-submenu').fadeIn();	
        });
        
      });

	$('.mini-submenu').on('click',function(){		
        $(this).next('.list-group').toggle('slide');
        $('.mini-submenu').hide();
	})

	$('#example').DataTable();
    $('select').addClass('mdb-select');
    $('.mdb-select').material_select();


$(document).ready(function(){
        var sexo = {
                exportEnabled: true,
                animationEnabled: true,
                title: {
                    text: "Gráfico de Alumnos por su Sexo"
                },
                data: [
                {
                    type: "pie", //change it to line, area, bar, pie, etc
                    startAngle: 240,
                    yValueFormatString: "##0",
                    indexLabel: "{label} {y}",
                    dataPoints: [
                        { y: $('#masculino').val(), label: "Masculino" },
                        { y: $('#femenino').val(), label: "Femenino" }
                    ]
                }
                ]
            };
            $("#chartContainer").CanvasJSChart(sexo);
    
        var grado = {
                exportEnabled: true,
                animationEnabled: true,
                title: {
                    text: "Gráfico de Alumnos por su Grado"
                },
                data: [
                {
                    type: "pie", //change it to line, area, bar, pie, etc
                    startAngle: 240,
                    yValueFormatString: "##0",
                    indexLabel: "{label} {y}",
                    dataPoints: [
                        { y: $('#primero').val(), label: "Primero" },
                        { y: $('#segundo').val(), label: "Segundo" },
                        { y: $('#tercero').val(), label: "Tercero" },
                        { y: $('#cuarto').val(), label: "Cuarto" },
                        { y: $('#quinto').val(), label: "Quinto" },
                        { y: $('#sexto').val(), label: "Sexto" },
                        { y: $('#septimo').val(), label: "Septimo" },
                        { y: $('#octavo').val(), label: "Octavo" },
                        { y: $('#noveno').val(), label: "Noveno" }
                    ]
                }
                ]
            };
            $("#grado").CanvasJSChart(grado);
    
        })

            $('.button-collapse').sideNav({
                edge: 'left',
                closeOnClick: true 
              });
            
        })