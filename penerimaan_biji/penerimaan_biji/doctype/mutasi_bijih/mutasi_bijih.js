// Copyright (c) 2019, PT DAS and contributors
// For license information, please see license.txt
cur_frm.add_fetch("batch", "objek_produksi", "kode_objek");
cur_frm.add_fetch("batch", "unit_produksi", "unit_produksi");
cur_frm.add_fetch("batch", "badan_usaha", "badan_usaha");
cur_frm.add_fetch("batch", "kelas", "kelas");
cur_frm.add_fetch("batch", "satuan", "satuan");
cur_frm.add_fetch("batch", "id_alat", "id_alat");
cur_frm.add_fetch("batch", "sn_est", "sn_est");
cur_frm.add_fetch("batch", "sn_tak", "sn_tak");
cur_frm.add_fetch("batch", "sn_def", "sn_def");
cur_frm.add_fetch("batch", "total", "qty");
cur_frm.add_fetch("batch", "total_final", "total");
cur_frm.add_fetch("to_loc", "type", "type");
frappe.ui.form.on('Mutasi Bijih', {
	on_load: function(frm) {
		cur_frm.set_query("batch", function() {
			return {
					"filters": {
					"status": "Closed"
					}
				};
		});
	},
	bruto: function(frm) {
		netto_calc(frm);
	},
	tara: function(frm) {
		netto_calc(frm);
	},
	kadar_air: function(frm) {
		netto_calc(frm);
	},
	sn_tak: function(frm) {
		netto_calc(frm);
	},
	sn_def: function(frm) {
		netto_calc(frm);
	}
});


function netto_calc(frm){
	var br = 0;
	var ta = 0;
	if (frm.doc.bruto){
		br = frm.doc.bruto;
	}
	if (frm.doc.tara){
		ta = frm.doc.tara;
	}
	frm.doc.netto = br - ta;
	var ka = 0;
	if (frm.doc.kadar_air){
		ka = frm.doc.kadar_air * frm.doc.netto;
		frm.doc.berat_air = ka;
	}
	frm.doc.berat_ore = frm.doc.netto - ka;

	frm.doc.total=0;
	if (frm.doc.sn_def!=null && frm.doc.sn_def>0){
		frm.doc.total = frm.doc.berat_ore * frm.doc.sn_def;
	}else if (frm.doc.sn_tak!=null && frm.doc.sn_tak>0){
		frm.doc.total = frm.doc.berat_ore * frm.doc.sn_tak;
	}else if (frm.doc.sn_est!=null && frm.doc.sn_est>0){
		frm.doc.total = frm.doc.qty * frm.doc.sn_est;
	}
	frm.refresh_field("total");
	frm.refresh_field("netto");
	frm.refresh_field("berat_air");
}