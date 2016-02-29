(function (ng) {
    var mod = ng.module('loginModule');

    mod.controller('loginCtrl', ['$scope', 'loginService', function ($scope, loginService) {

        $scope.user = {};

        $scope.error = false;

        function responseError(response) {
            console.log(response);
        }

        this.logIn = function () {
            return loginService.logIn($scope.user.username,$scope.user.password).then(function (response) {
                $scope.message = response.data;
                console.log($scope.message)
                if($scope.message.message === 'OK'){
                    console.log('Cargando pagina..')
                    window.location.assign('#/independents');
                    window.location.reload(true);
                    console.log('Cargando pagina.. despues')
                }else{
                    console.log('error')
                    $scope.error = true;
                }
            }, responseError);
        };

    }]);
})(window.angular);
