(function (ng) {
    var mod = ng.module('commentsModule');

    mod.controller('commentsCtrl', ['$scope', 'commentsService', '$window', function ($scope, commentsService, $window) {

        function responseError(response) {
            console.log(response);
        }

        this.registerComment = function(){
            return commentsService.registerComment({
                'independent':angular.element('#independent').val(),
                'comment':angular.element('#comment').val(),
                'userEmail':angular.element('#userEmail').val()
            }).then(function (response) {
                $window.location.href = '/#/independents';
            }, responseError);
        };

    }]);
})(window.angular);