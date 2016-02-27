(function (ng) {
    var mod = ng.module('independentsModule');

    mod.controller('independentsCtrl', ['$scope', 'independentsService', '$window', function ($scope, independentsService, $window) {

        function responseError(response) {
            console.log(response);
        }

        this.getIndependents = function () {
            return independentsService.getIndependents().then(function (response) {
                $scope.independents = response.data;
            }, responseError);
        };

        this.registerIndependent = function(){
            var name = angular.element('#name').val();
            var lastName = angular.element('#last_name').val();
            var job = angular.element('#job').val();
            var yearsOfExperience = angular.element('#years_of_experience').val();
            var phoneNumber = angular.element('#phone_number').val();
            var email = angular.element('#email').val();
            var imageFileUrl = angular.element('#imageFileUrl').val();
            var username = angular.element('#username').val();
            var password = angular.element('#password').val();

            if (name && lastName && job && yearsOfExperience && phoneNumber && email && imageFileUrl && username && password){
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
