// Copyright (c) 2019, PT DAS and contributors
// For license information, please see license.txt

frappe.ui.form.on('Pengiriman Batch', {
	refresh: function(frm) {
		cur_frm.add_fetch("batch", "total_final", "total");
		cur_frm.add_fetch("s_loc", "type", "type");
		cur_frm.set_query("batch", "batch_list", function(doc, cdt, cdn) {
			return {
					"filters": {
						"status": "Closed",
						"jalan":0,
						"used":0
					}
				};
		});
	}
});
