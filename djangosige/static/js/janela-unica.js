console.log("Janela única carregada com sucesso!");
$(document).ready(function () {
    try {
        $("#documento_unico_arquivo-group").detach().appendTo("fieldset.replacein");
    } catch (error) {
        console.log("Erro ao mover o campo documento_unico_arquivo-group");
        console.log(error);
    }
});
// https://stackoverflow.com/questions/2596833/how-to-move-child-element-from-one-parent-to-another-using-jquery