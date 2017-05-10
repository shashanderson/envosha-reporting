$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-parameter").modal("show");
      },
      success: function (data) {
        $("#modal-parameter .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#parameter-table tbody").html(data.html_book_list);
          $("#modal-parameter").modal("hide");
        }
        else {
          $("#modal-parameter .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create book
  $(".js-create-parameter").click(loadForm);
  $("#modal-parameter").on("submit", ".js-parameter-create-form", saveForm);

  // Update book
  $("#parameter-table").on("click", ".js-update-parameter", loadForm);
  $("#modal-parameter").on("submit", ".js-parameter-update-form", saveForm);

  // Delete book
  $("#parameter-table").on("click", ".js-delete-parameter", loadForm);
  $("#modal-parameter").on("submit", ".js-parameter-delete-form", saveForm);

});
