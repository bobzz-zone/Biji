// Copyright (c) 2019, PT DAS and contributors
// For license information, please see license.txt
cur_frm.add_fetch("batch", "objek_produksi", "kode_objek");
cur_frm.add_fetch("batch", "unit_produksi", "unit_produksi");
cur_frm.add_fetch("batch", "badan_usaha", "badan_usaha");
cur_frm.add_fetch("batch", "kelas", "kelas");
cur_frm.add_fetch("batch", "satuan", "satuan");
cur_frm.add_fetch("batch", "id_alat", "id_alat");
frappe.ui.form.on('BAP', {
	bruto: function(frm) {
		if (frm.doc.tara){
			frm.doc.netto = frm.doc.bruto - frm.doc.tara;
		}else{
			frm.doc.netto = frm.doc.bruto;
		}
		if (frm.doc.kadar_air && frm.doc.netto){
			frm.doc.total = frm.doc.netto - (frm.doc.netto * frm.doc.kadar_air);
		}
		frm.refresh_field("total");
		frm.refresh_field("netto");
	},
	tara: function(frm) {
		if (frm.doc.bruto){
			frm.doc.netto = frm.doc.bruto - frm.doc.tara;
		}else{
			frm.doc.netto = 0;
		}
		if (frm.doc.kadar_air && frm.doc.netto){
			frm.doc.total = frm.doc.netto - (frm.doc.netto * frm.doc.kadar_air);
		}
		frm.refresh_field("total");
		frm.refresh_field("netto");
	},
	kadar_air: function(frm) {
		if (frm.doc.kadar_air && frm.doc.netto){
			frm.doc.total = frm.doc.netto - (frm.doc.netto * frm.doc.kadar_air);
		}
		frm.refresh_field("total");
	}
});
