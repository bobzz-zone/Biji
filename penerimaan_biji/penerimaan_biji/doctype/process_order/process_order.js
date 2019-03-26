// Copyright (c) 2019, PT DAS and contributors
// For license information, please see license.txt

frappe.ui.form.on('Process Order', {
	refresh: function(frm) {
		frm.set_query("s_loc", function() {
			return {
					"filters": [
						 ["Lokasi Penyimpanan": "type", "IN", "PPBT,BPM,All Type"]
					]
				};
			});	
	}
});
