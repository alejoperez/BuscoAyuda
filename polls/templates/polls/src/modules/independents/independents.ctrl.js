(function (ng) {
    var mod = ng.module('independentsModule');

    mod.controller('independentsCtrl', ['$scope', 'independentsService', function ($scope, independentsService) {

        function responseError(response) {
            console.log(response);
        }

        this.getIndependents = function () {
            return independentsService.getIndependents().then(function (response) {
                $scope.independents = response.data;
            }, responseError);
        };

    }]);
})(window.angular);
