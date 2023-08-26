$(document).ready(function() {
    var flag = true
    var selectedSector

    $('#setor').change(function() {
      flag = true
      selectedSector = parseInt($(this).val());
      var options = '';
      data = cleanString('tipoProbJson')
      options += '<option value=" " selected>Selecione o tipo</option>';

      for (var i = 0; i < data.length; i++) {
        var item = data[i];
        var id = item.id
        var tipoProb = item.tipoProb
        var setorId = item.setorId

        if(setorId == selectedSector){
        options += '<option value="' + id + '">' + tipoProb + '</option>';
        }
      }

      $('#tipoProblema').html(options);
      options += '<option value=" " selected>Selecione o problema</option>';
    });

    $('#tipoProblema').click(function() {
      $('#tipoProblema').change(function() {

        if (!isNaN(parseInt($(this).val()))) {
          idSelected = parseInt($(this).val())
        }

        if (flag == true) {
          var options
          options += '<option value=" " selected>Selecione o problema</option>';
          dataProb = cleanString('probJson')

          for (var i = 0; i < dataProb.length; i++) {
            var item = dataProb[i];
            var id = item.id
            var problema = item.problema
            var tProblema = item.tipoProblema

            if (idSelected == tProblema) {
              options += '<option value="' + id + '">' + problema + '</option>';
            }

          }
          flag = false
          $('#tipoProblema').html(options);
        }
      });
    });

    function cleanString(elementId) {
      // Troca os none da string para null e aspas simples '' para aspas duplas ""
      // Transforma string em json para manipulação
      var inputElement = document.getElementById(elementId);
      var data = inputElement.value;
      var cleanedString = data.replace(/'/g, '"');
      var cleanedString = data.replace(/None/g, 'null').replace(/'/g, '"');
      data = JSON.parse(cleanedString)
      return data
    }
});