console.log("Janela única carregada com sucesso!");
$(document).ready(function () {
    try {
        $("input.vTextField").addClass('form-control').removeClass('vTextField');
    } catch (error) {
        console.log("Erro ao ajustar css do campo vTextField");
        console.log(error);
    }
    try {
        $("input.vIntegerField").addClass('form-control').removeClass('vIntegerField');
    } catch (error) {
        console.log("Erro ao ajustar css do campo vTextField");
        console.log(error);
    }
    try {
        $("select:not(.form-class)").addClass("form-control");
    } catch (error) {
        console.log("Erro ao ajustar css do campo vTextField");
        console.log(error);
    }   
    
});
// https://stackoverflow.com/questions/2596833/how-to-move-child-element-from-one-parent-to-another-using-jquery