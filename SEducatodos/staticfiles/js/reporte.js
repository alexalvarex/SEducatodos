var tab_text;
var data_type = 'data:application/vnd.ms-excel';


function CreateHiddenTable(ListOfMessages)
{
var ColumnHead = "SECRETARÍA DE EDUCACION";
var subColumnHead = "PROGRAMA EDUCATODOS";
var thirdColumnHead = "PROGRAMA EDUCATODOS";
var TableMarkUp='<table id="myModifiedTable" class="visibilityHide"><thead><tr><td><b>'+ColumnHead+'</b></td><td><b>'+subColumnHead+'</b></td><td><b>'+thirdColumnHead+'</b></td>  </tr></thead><tbody>';

for(i=0; i<ListOfMessages.length; i++){
    TableMarkUp += '<tr><td>' + ListOfMessages[i] +'</td></tr>';
}
TableMarkUp += "</tbody></table>";
$('#MessageHolder').append(TableMarkUp);
}

function fnExcelReport() {
var Messages = "\n Departamento.\n Municipio.\n Alde.\n Municipio.";
var ListOfMessages = Messages.split(".");

CreateHiddenTable(ListOfMessages);

    tab_text = '<html xmlns:x="urn:schemas-microsoft-com:office:excel">';
    tab_text = tab_text + '<head><xml><x:ExcelWorkbook><x:ExcelWorksheets><x:ExcelWorksheet>';

    tab_text = tab_text + '<x:Name>Constancia</x:Name>';

    tab_text = tab_text + '<x:WorksheetOptions><x:Panes></x:Panes></x:WorksheetOptions></x:ExcelWorksheet>';
    tab_text = tab_text + '</x:ExcelWorksheets></x:ExcelWorkbook></xml></head><body>';

    tab_text = tab_text + "<table border='1px'>";
    tab_text = tab_text + $('#example').html();;
    tab_text = tab_text + '</table></body></html>';

    data_type = 'data:application/vnd.ms-excel';
    
    var ua = window.navigator.userAgent;
    var msie = ua.indexOf("MSIE ");
    
    if (msie > 0 || !!navigator.userAgent.match(/Trident.*rv\:11\./)) {
        if (window.navigator.msSaveBlob) {
            var blob = new Blob([tab_text], {
                type: "application/csv;charset=utf-8;"
            });
            navigator.msSaveBlob(blob, 'Test file.xlsx');
        }
    } else {
    console.log(data_type);
console.log(tab_text);
      $('#testAnchor')[0].click()
    }
$('#MessageHolder').html("");
}
$($("#testAnchor")[0]).click(function(){
console.log(data_type);
console.log(tab_text);
  $('#testAnchor').attr('href', data_type + ', ' + encodeURIComponent(tab_text));
        $('#testAnchor').attr('download', 'Test file.xls');
});