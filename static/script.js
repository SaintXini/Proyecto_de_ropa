function mostrarFormularioEdicion(id) {
    var form = document.getElementById('edit-form-' + id);
    if (form.style.display === 'none') {
      form.style.display = 'table-row';
    } else {
      form.style.display = 'none';
    }
  }