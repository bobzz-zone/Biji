// Copyright (c) 2019, PT DAS and contributors
// For license information, please see license.txt

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
			frm.set_query("batch", function() {
			return {
					"filters": {
						"used": "1",
						"status": "Closed"
					}
				};
			});		
		}
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
