// Copyright (c) 2018, PT DAS and contributors
// For license information, please see license.txt

frappe.ui.form.on('ID Alat', {
	refresh: function(frm) {
		frm.set_df_property("kode_objek", "read_only", frm.doc.__islocal ? 0 : 1);
		frm.set_df_property("kode_alat", "read_only", frm.doc.__islocal ? 0 : 1);
		frm.set_df_property("lokasi", "read_only", frm.doc.__islocal ? 0 : 1);
		frm.set_df_property("iup", "read_only", frm.doc.__islocal ? 0 : 1);
	}
});
