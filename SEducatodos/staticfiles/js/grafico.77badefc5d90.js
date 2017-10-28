$(function(){
	grafico()
});

function grafico(tipo = "pie")
{
	var hc = Highcharts.chart('chart-grafico', {
		data: 	 { table: 'data-grafico' },
		chart: 	 { type: tipo },
		title: 	 { text: 'Alumnos por Sexo' },
		yAxis: 	 { allowDecimals: true, title: 'Sexo' },
		tooltip: {
			formatter: function(){
				return '<strong>' + this.series.name + '</strong> <br/>' + this.point.y + ' ' + this.point.name.toLowerCase;
			}
		},
		plotOptions: {
			line: { dataLabels: true },
			enableMouseTracking: false
		}
	});
}