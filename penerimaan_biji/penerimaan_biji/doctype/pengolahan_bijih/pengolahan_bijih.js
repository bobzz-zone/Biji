// Copyright (c) 2019, PT DAS and contributors
// For license information, please see license.txt
cur_frm.add_fetch("batch", "objek_produksi", "kode_objek");
cur_frm.add_fetch("batch", "id_alat", "id_alat");

cur_frm.add_fetch("batch", "kelas", "kelas");

cur_frm.add_fetch("batch", "unit_produksi", "unit_produksi");

cur_frm.add_fetch("batch", "badan_usaha", "badan_usaha");

cur_frm.add_fetch("batch", "satuan", "satuan");

cur_frm.add_fetch("batch", "sn_est", "sn_est");
//cur_frm.add_fetch("batch", "tak_percent", "sn_tak");
//cur_frm.add_fetch("batch", "def_percent", "sn_def");
//cur_frm.add_fetch("batch", "total", "qty");



// cur_frm.add_fetch("batch", "total_final", "total");

// cur_frm.add_fetch("batch", "tara", "tara");
// cur_frm.add_fetch("batch", "kadar_air", "kadar_air");
// cur_frm.add_fetch("batch", "berat_air", "berat_air");
// cur_frm.add_fetch("batch", "berat_ore", "berat_ore");
// cur_frm.add_fetch("batch", "netto", "netto");
// cur_frm.add_fetch("batch", "bruto", "bruto");
frappe.ui.form.on('Pengolahan Bijih', {
	refresh: function(frm) {

	},
	onload: function(frm) {
		frm.set_query("batch", function() {
			return {
					"filters": {
						"used": "0",
						"status": "Closed"
					}
				};
		});
	},
	type : function(frm){
		if(frm.doc.type == "Input"){
			frm.set_query("batch", function() {
			return {
					"filters": {
						"used": "0",
						"status": "Closed"
					}
				};
			});	
		}
		else {
			frm.set_value('qty', 0);
			frm.set_query("batch", function() {
			return {
					"filters": {
						"used": "1",
						"status": "Closed"
					}
				};
			});		
		}
		frm.set_df_property("kadar_air", "read_only", frm.doc.type=="Input");
		frm.set_df_property("bruto", "read_only", frm.doc.type=="Input");
		frm.set_df_property("tara", "read_only", frm.doc.type=="Input");
		frm.set_df_property("sn_tak", "read_only", frm.doc.type=="Input");
		frm.set_df_property("sn_def", "read_only", frm.doc.type=="Input");
		get_batch_value(frm);
	},
	batch: function(frm) {
		get_batch_value(frm);
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
function get_batch_value(frm){
	if (frm.doc.batch){
    frappe.call({
        "method": "frappe.client.get",
        "args": {
             "doctype": "Kode Batch",
             "name": frm.doc.batch
        },
        "callback": function(response) {
             var batch = response.message;
             if (batch) {
             	  if (frm.doc.type == "Input"){
             	  	frm.set_value('qty', batch.total);
             	  	frm.set_value('sn_tak', batch.tak_percent);
             	  	frm.set_value('sn_def', batch.def_percent);
             	  	frm.set_value('tara', batch.tara);
             	  	frm.set_value('kadar_air', batch.kadar_air);
             	  	frm.set_value('berat_air', batch.berat_air);
             	  	frm.set_value('berat_ore', batch.berat_ore);
             	  	frm.set_value('netto', batch.netto);
             	  	frm.set_value('bruto', batch.bruto);
             	  	frm.set_value('total', batch.total_final);
             	  } 
             	  else{
             	  	frm.set_value('qty', 0);
             	  	frm.set_value('sn_tak', 0);
             	  	frm.set_value('sn_def', 0);
             	  	frm.set_value('tara', 0);
             	  	frm.set_value('kadar_air', 0);
             	  	frm.set_value('berat_air', 0);
             	  	frm.set_value('berat_ore', 0);
             	  	frm.set_value('netto', 0);
             	  	frm.set_value('bruto', 0);
             	  	frm.set_value('total', 0);
             	  }
             }
             else{
             	  	frm.set_value('qty', 0);
             	  	frm.set_value('sn_tak', 0);
             	  	frm.set_value('sn_def', 0);
             	  	frm.set_value('tara', 0);
             	  	frm.set_value('kadar_air', 0);
             	  	frm.set_value('berat_air', 0);
             	  	frm.set_value('berat_ore', 0);
             	  	frm.set_value('netto', 0);
             	  	frm.set_value('bruto', 0);
             	  	frm.set_value('total', 0);
             } 
        }
    }); }
}
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
		ka = frm.doc.kadar_air * frm.doc.netto/100;
		frm.doc.berat_air = ka;
	}
	frm.doc.berat_ore = frm.doc.netto - ka;

	frm.doc.total=0;
	if (frm.doc.sn_def!=null && frm.doc.sn_def>0){
		frm.doc.total = frm.doc.berat_ore * frm.doc.sn_def/100;
	}else if (frm.doc.sn_tak!=null && frm.doc.sn_tak>0){
		frm.doc.total = frm.doc.berat_ore * frm.doc.sn_tak/100;
	}else if (frm.doc.sn_est!=null && frm.doc.sn_est>0){
		frm.doc.total = frm.doc.qty * frm.doc.sn_est;
	}
	frm.refresh_field("total");
	frm.refresh_field("netto");
	frm.refresh_field("berat_air");
}
