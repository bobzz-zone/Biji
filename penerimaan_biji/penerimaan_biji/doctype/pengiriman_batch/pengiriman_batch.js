// Copyright (c) 2019, PT DAS and contributors
// For license information, please see license.txt

frappe.ui.form.on('Pengiriman Batch', {
	refresh: function(frm) {
		cur_frm.add_fetch("batch", "total", "total");
		cur_frm.add_fetch("batch", "berat_temp", "ton");
		cur_frm.add_fetch("s_loc", "type", "type");
		if (frm.doc.s_loc){
			frm.set_df_property("s_loc", "hidden", true);
		}
		cur_frm.set_query("batch", "batch_list", function(doc, cdt, cdn) {
			return {
					"filters": {
						"status": "Closed",
						"jalan":0,
						"used":0,
						"is_end":0
					}
				};
		});
	}
});
