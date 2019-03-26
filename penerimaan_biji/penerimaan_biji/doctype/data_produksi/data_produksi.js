// Copyright (c) 2019, PT DAS and contributors
// For license information, please see license.txt
cur_frm.add_fetch("batch", "objek_produksi", "kode_objek");
cur_frm.add_fetch("batch", "unit_produksi", "unit_produksi");
cur_frm.add_fetch("batch", "badan_usaha", "badan_usaha");
cur_frm.add_fetch("batch", "kelas", "kelas");
cur_frm.add_fetch("batch", "satuan", "satuan");
cur_frm.add_fetch("batch", "id_alat", "id_alat");

cur_frm.add_fetch("batch", "sn_est", "sn_est");
frappe.ui.form.on('Data Produksi', {
	onload : function(frm) {
		cur_frm.set_query("batch", function() {
			return {
					"filters": {
						"status": "Open"
					}
				};
		});
	},
        validate: function(frm){
        	if (frm.doc.status=="Closed"){
        		frappe.throw("Data Produksi Sudah Tidak Boleh di Update");
        		return false;
        	}
            frm.doc.total=0;
            if (frm.doc.sn_def!=null && frm.doc.sn_def>0){
                    frm.doc.total = frm.doc.qty * frm.doc.sn_def;
            }else if (frm.doc.sn_tak!=null && frm.doc.sn_tak>0){
                    frm.doc.total = frm.doc.qty * frm.doc.sn_tak;
            }else if (frm.doc.sn_est!=null && frm.doc.sn_est>0){
                    frm.doc.total = frm.doc.qty * frm.doc.sn_est;
            }
            frm.refresh_field("total");
        },refresh:function(frm){
        	frm.set_df_property("batch", "read_only", frm.doc.__islocal ? 0 : 1);
            if (frm.doc.status=="Closed"){
            frm.set_df_property("date", "read_only", 1);
            frm.set_df_property("qty", "read_only", 1);
            }
        }

});