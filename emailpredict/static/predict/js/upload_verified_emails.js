$(document).ready(function () {
    $('input[type=file]').bootstrapFileInput();
    $('.file-inputs').bootstrapFileInput();
    $('input[type=file]').attr('data-filename-placement', 'inside');
    $('.file-inputs').attr('data-filename-placement', 'inside');
});