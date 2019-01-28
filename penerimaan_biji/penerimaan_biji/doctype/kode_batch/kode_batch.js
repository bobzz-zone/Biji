// Copyright (c) 2019, PT DAS and contributors
// For license information, please see license.txt
cur_frm.add_fetch("id_alat", "kode_objek", "objek_produksi");
cur_frm.add_fetch("id_alat", "unit_produksi", "unit_produksi");
cur_frm.add_fetch("id_alat", "badan_usaha", "badan_usaha");
cur_frm.add_fetch("id_alat", "kelas", "kelas");
cur_frm.add_fetch("id_alat", "s_loc", "s_loc");
frappe.ui.form.on('Kode Batch', {
	refresh: function(frm) {

	}
});
