(function (ng) {
    var mod = ng.module('commentsModule');

    mod.controller('commentsCtrl', ['$scope', '$routeParams', 'commentsService', '$window', function ($scope, $routeParams, commentsService, $window) {
        var mensaje = "";
        function validarEmail(valor) {
          if (/^\w+([\.\+\-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/.test(valor)){
           return true;
          } else {
              mensaje="La dirección de email es incorrecta, debe tener el formato usuario@dominio <br />";
              document.getElementById('areaMensaje').innerHTML=mensaje;
            }
        }

        function responseError(response) {
            console.log(response);
        }

        this.registerComment = function(){
            var comentario = angular.element('#comment').val();
            var emailUsuario = angular.element('#userEmail').val();
            
            if(comentario && validarEmail(emailUsuario)==true){
                 console.log('antes de enviar correo');
                document.getElementById('areaMensaje').innerHTML="Enviando...<br />";
                return commentsService.registerComment({
                    'idIndependent':$routeParams.idIndependent,
                    'comment':comentario,
                    'userEmail':emailUsuario
                }).then(function (response) {
                     console.log('Despues de enviar el comentario');
                     alert("Su comentario fue enviado con éxito.");
                    $window.location.href = '/#/independents';
                }, responseError);
            }
        };

    }]);
})(window.angular);