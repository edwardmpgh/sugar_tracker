$('#common-meal').on('change', function() {
  if(this.value > 0) {
      console.log( this.value );
      $.get( '/get/meal/'+this.value, function( data ) {
          $( ".result" ).html( data );
          $('#id_proteins').val(data['protein'])
          $('#id_fat').val(data['fat'])
          $('#id_carbohydrates').val(data['carbohydrates'])

      });
  }
});