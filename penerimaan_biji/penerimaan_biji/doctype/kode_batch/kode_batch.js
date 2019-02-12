// Copyright (c) 2019, PT DAS and contributors
// For license information, please see license.txt
cur_frm.add_fetch("id_alat", "kode_objek", "objek_produksi");
cur_frm.add_fetch("id_alat", "unit_produksi", "unit_produksi");
cur_frm.add_fetch("id_alat", "badan_usaha", "badan_usaha");
cur_frm.add_fetch("id_alat", "kelas", "kelas");
frappe.ui.form.on('Kode Batch', {
	refresh: function(frm) {
		if(frm.doc.docstatus==1 && frm.doc.closing == null) {
			var doc = frm.doc;
			frappe.ui.form.is_saving = true;
			frappe.call({
				method: "penerimaan_biji.penerimaan_biji.doctype.kode_batch.kode_batch.close_batch",
				args: {name: doc.name},
				callback: function(r){
					me.frm.reload_doc();
				},
				always: function() {
					frappe.ui.form.is_saving = false;
				}
			});
		}
	}
});
