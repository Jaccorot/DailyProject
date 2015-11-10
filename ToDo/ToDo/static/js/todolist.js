/**
 * Created by Administrator on 2015/11/10.
 */
/*global $, test, equal */
$(document).ready(function(){
    $('input').on('keypress', function(){
        $('.has-error').hide();
    })
})

//
//test("smoke test", function(){
//    equal($('.has-error').is(':visible'), true);
//    $('.has-error').hide();
//    equal($('.has-error').is(':visible'), false);
//});
//
//
//test("errors should be hidden on keypress", function(){
//    $('input').trigger('keypress');
//    //$('.has-error').hide()
//    equal($('.has-error').is(':visible'), false);
//});
//
//test("errors not be hidden unless there is a keypress", function(){
//    equal($('.has-error').is(":visible"), true);
//})

