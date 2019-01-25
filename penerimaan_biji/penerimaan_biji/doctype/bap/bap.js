// Copyright (c) 2019, PT DAS and contributors
// For license information, please see license.txt
cur_frm.add_fetch("batch", "objek_produksi", "kode_objek");
cur_frm.add_fetch("batch", "unit_produksi", "unit_produksi");
cur_frm.add_fetch("batch", "badan_usaha", "badan_usaha");
cur_frm.add_fetch("batch", "kelas", "kelas");
cur_frm.add_fetch("batch", "satuan", "satuan");
cur_frm.add_fetch("batch", "id_alat", "id_alat");

frappe.ui.form.on('BAP', {
	refresh: function(frm) {

	}
});
