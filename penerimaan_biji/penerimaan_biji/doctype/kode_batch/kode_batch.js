// Copyright (c) 2019, PT DAS and contributors
// For license information, please see license.txt
cur_frm.add_fetch("id_alat", "kode_objek", "objek_produksi");
cur_frm.add_fetch("id_alat", "unit_produksi", "unit_produksi");
cur_frm.add_fetch("id_alat", "badan_usaha", "badan_usaha");
cur_frm.add_fetch("id_alat", "kelas", "kelas");
cur_frm.add_fetch("s_loc", "type", "type_simpan");
frappe.ui.form.on('Kode Batch', {
	refresh: function(frm) {
		frm.set_df_property("sn_est", "read_only", frm.doc.__islocal ? 0 : 1);
		frm.set_df_property("s_loc", "read_only", frm.doc.docstatus==1);
		if(frm.doc.docstatus==1 && frm.doc.status == "Open") {
			frm.add_custom_button(__('Close'), function () {
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
			});
		}
	}
});
