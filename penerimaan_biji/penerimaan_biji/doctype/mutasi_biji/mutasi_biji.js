// Copyright (c) 2019, PT DAS and contributors
// For license information, please see license.txt

cur_frm.add_fetch("to_loc", "type", "type");
frappe.ui.form.on('Mutasi Biji', {
	refresh: function(frm) {

	},
	bruto: function(frm) {
		netto_calc(frm);
	},
	tara: function(frm) {
		netto_calc(frm);
	}
});
function netto_calc(frm){

}