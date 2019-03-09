// Copyright (c) 2019, PT DAS and contributors
// For license information, please see license.txt
cur_frm.add_fetch("batch", "objek_produksi", "kode_objek");
cur_frm.add_fetch("batch", "unit_produksi", "unit_produksi");
cur_frm.add_fetch("batch", "badan_usaha", "badan_usaha");
cur_frm.add_fetch("batch", "kelas", "kelas");
cur_frm.add_fetch("batch", "satuan", "satuan");
cur_frm.add_fetch("batch", "id_alat", "id_alat");
cur_frm.add_fetch("saksi1_nama", "email", "email1");
cur_frm.add_fetch("saksi1_nama", "sign", "saksi1_sign");
cur_frm.add_fetch("saksi2_nama", "email", "email2");
cur_frm.add_fetch("saksi2_nama", "sign", "saksi2_sign");
cur_frm.add_fetch("saksi3_nama", "email", "email3");
cur_frm.add_fetch("saksi3_nama", "sign", "saksi3_sign");
cur_frm.add_fetch("vendor", "vendor", "penyedia_jasa_nama");
frappe.ui.form.on('BAP', {
	onload : function(frm) {
		cur_frm.set_query("batch", function() {
			return {
					"filters": {
						"status": "Open"
					}
				};
		});
	},
	refresh: function(frm): {
		frm.set_df_property("unit_produksi", "read_only", frm.doc.__islocal ? 0 : 1);
		if (frm.doc.docstatus==0){
			frappe.call({
				method:"penerimaan_biji.penerimaan_biji.doctype.bap.bap.get_harga",
				callback: function(r) {
					cur_frm.set_value("harga", r.message);
				}
			});
		}
	},
	bruto: function(frm) {
		if (frm.doc.tara){
			frm.doc.netto = frm.doc.bruto - frm.doc.tara;
		}else{
			frm.doc.netto = frm.doc.bruto;
		}
		if (frm.doc.kadar_air && frm.doc.netto){
			frm.doc.total = frm.doc.netto - (frm.doc.netto * frm.doc.kadar_air / 100);
			frm.doc.rekomendasi =  frm.doc.total * frm.doc.harga
		}
		frm.refresh_field("total");
		frm.refresh_field("rekomendasi")
		frm.refresh_field("netto");
	},
	tara: function(frm) {
		if (frm.doc.bruto){
			frm.doc.netto = frm.doc.bruto - frm.doc.tara;
		}else{
			frm.doc.netto = 0;
		}
		if (frm.doc.kadar_air && frm.doc.netto){
			frm.doc.total = frm.doc.netto - (frm.doc.netto * frm.doc.kadar_air / 100);
			frm.doc.rekomendasi =  frm.doc.total * frm.doc.harga
		}
		frm.refresh_field("total");
		frm.refresh_field("rekomendasi")
		frm.refresh_field("netto");
	},
	kadar_air: function(frm) {
		if (frm.doc.kadar_air && frm.doc.netto){
			frm.doc.total = frm.doc.netto - (frm.doc.netto * frm.doc.kadar_air / 100);
			frm.doc.rekomendasi =  frm.doc.total * frm.doc.harga
		}
		frm.refresh_field("rekomendasi")
		frm.refresh_field("total");
	}
});
