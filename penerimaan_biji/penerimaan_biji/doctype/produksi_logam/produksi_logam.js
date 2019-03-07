// Copyright (c) 2019, PT DAS and contributors
// For license information, please see license.txt
cur_frm.add_fetch("batch", "def_percent", "sn");
cur_frm.add_fetch("batch", "netto", "bruto");
cur_frm.add_fetch("batch", "total_final", "netto");
frappe.ui.form.on('Produksi Logam', {
	refresh: function(frm) {

	}
});
