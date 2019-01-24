// Copyright (c) 2019, PT DAS and contributors
// For license information, please see license.txt
cur_frm.add_fetch("id_alat", "kode_objek", "kode_objek");
cur_frm.add_fetch("id_alat", "unit_produksi", "unit_produksi");
cur_frm.add_fetch("id_alat", "badan_usaha", "badan_usaha");
cur_frm.add_fetch("batch", "satuan", "satuan");

frappe.ui.form.on('Data Produksi', {
        validate: function(frm){
                frm.doc.total=0;
                if (frm.doc.sn_def!=null && frm.doc.sn_def>0){
                        frm.doc.total = frm.doc.qty * frm.doc.sn_def;
                }else if (frm.doc.sn_tak!=null && frm.doc.sn_tak>0){
                        frm.doc.total = frm.doc.qty * frm.doc.sn_tak;
                }else if (frm.doc.sn_est!=null && frm.doc.sn_est>0){
                        frm.doc.total = frm.doc.qty * frm.doc.sn_est;
                }
                frm.refresh_field("total");
        }
});