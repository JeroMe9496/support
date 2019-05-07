/* ATTENTION !
   CETTE PAGE UTILISE jQuery ET LES FONCTIONS DU FICHIER "functions.js"
   VEILLEZ A INSERER "jQuery" et "functions.js" AVANT D'UTILISER LES SCRIPTS CI-DESSOUS
*/


/**
 * jQuery
 * --------------------------------------------------------------
 * On document ready, do this...
 * Avant d'utiliser le code ci-dessous il faut installer jQuery !
 */
/*START jQuery Code*/
$(function() {
	
	
	/* OPEN/CLOSE MENU ON CLICK
	-----------------------------------------------------*/
	// OPEN MENU
	$("#open-menu").on("click", function(e) {

		$("#header").addClass("menu-is-open");
		$(window).disableScroll();
		
	});
	
	
	// CLOSE MENU
	$("#close-menu").on("click", function(e) {
		
		$("#header").removeClass("menu-is-open");
		$(window).enableScroll();
		
	});
	
	
});