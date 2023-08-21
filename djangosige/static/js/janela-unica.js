console.log("Janela única carregada com sucesso!");
$(document).ready(function () {
    // Mover o formulário de cadastro de multiplos documentos para o formulário de cadastro de documento único
    try {
        $("#documento_unico_arquivo-group").detach().appendTo("fieldset.documento_unico_arquivo-group");
    } catch (error) {
        console.log("Erro ao mover o campo documento_unico_arquivo-group");
        console.log(error);
    }
    try {
        $("#documento_unico_avaliacao-group").detach().appendTo("fieldset.documento_unico_avaliacao-group");
    } catch (error) {
        console.log("Erro ao mover o campo documento_unico_avaliacao-group");
        console.log(error);
    }
    
    //
    try {
        $("input.vTextField").addClass('form-control').removeClass('vTextField');
    } catch (error) {
        console.log("Erro ao ajustar css do campo vTextField");
        console.log(error);
    }

    // try {
    //     $("#documento_unico_arquivo-empty").hide();
    // } catch (error) {
    //     console.log("Erro ao ajustar css do campo vTextField");
    //     console.log(error);
    // }

    try {
        // $("#id_forma_pagamento").hide();
    }catch (error) {
        console.log("Erro ao ajustar css do campo vTextField");
        console.log(error);
    }

    
});
// https://stackoverflow.com/questions/2596833/how-to-move-child-element-from-one-parent-to-another-using-jquery