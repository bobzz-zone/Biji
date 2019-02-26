// Copyright (c) 2019, PT DAS and contributors
// For license information, please see license.txt

frappe.ui.form.on('Pengiriman Batch', {
	refresh: function(frm) {
		cur_frm.add_fetch("batch", "total", "total");
	},onload: function(frm) {
		cur_frm.set_query("batch", function() {
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
