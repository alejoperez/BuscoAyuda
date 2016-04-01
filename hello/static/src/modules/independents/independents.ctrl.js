(function (ng) {
    var mod = ng.module('independentsModule');

    mod.controller('independentsCtrl', ['$scope', 'independentsService', '$window', function ($scope, independentsService, $window) {
        function validarEmail(valor) {
          if (/^\w+([\.\+\-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/.test(valor)){
           return true;
          } else {
           alert("La dirección de email es incorrecta, debe tener el formato usuario@dominio");
          }
        }
        
        function responseError(response) {
            console.log(response);
        }

        this.getIndependents = function () {
            return independentsService.getIndependents().then(function (response) {
                $scope.independents = response.data;
            }, responseError);
        };

        this.registerIndependent = function(){
            var name = angular.element('#id_name').val();
            var lastName = angular.element('#id_last_name').val();
            var job = angular.element('#id_job').val().trim();
            var yearsOfExperience = angular.element('#id_years_of_experience').val();
            var phoneNumber = angular.element('#id_phone_number').val();
            var email = angular.element('#id_email').val();
            var imageFileUrl = angular.element('#id_imageFileUrl').val();
            var username = angular.element('#id_username').val();
            var password = angular.element('#id_password').val();
            console.log(job);
            if (name && lastName && job && yearsOfExperience && phoneNumber && validarEmail(email)==true && imageFileUrl && username && password){
                console.log('antes de regirto 2');
                return independentsService.registerIndependent({
                                'name': name,
                                'lastName': lastName,
                                'job': job,
                                'yearsOfExperience': yearsOfExperience,
                                'phoneNumber': phoneNumber,
                                'email': email,
                                'imageFileUrl': imageFileUrl,
                                'username': username,
                                'password': password
                        }).then(function (response) {
                        console.log('retorna registro');
                                $window.location.href = '/#/independents';
                            }, responseError);
                }
        };

        this.getJobs = function () {
            return independentsService.getJobs().then(function (response) {
                $scope.jobs = response.data;
            }, responseError);
        };

    }]);
})(window.angular);
