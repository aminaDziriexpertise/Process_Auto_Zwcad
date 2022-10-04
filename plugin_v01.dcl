Justification : dialog
              { label =  "Plugin Zwcad V0.1";
             
                spacer;
           
                
                : row {
                  : boxed_column {
                    label = "Charger les elements du Plugin";
                    : row {
                   // : edit_box {	key = "insert" ;label = "&Insert URL ticket Odoo" : ;	edit_width = 100 ;	edit_limit = 20000 ;		}	 
                    : edit_box {	key = "insert" ;label = "&Insert URL ticket Odoo" : ;	edit_width = 100 ;		}	
                    :column {
                       : button {label = "Charger le plan" ; key = "next";fixed_width=true;is_cancel=true;width=18;}
                       : button { label = "Insert URL Odoo";key = "insert1";fixed_width=true;is_cancel=true;width=18;}
                    }              
                    
                    }
                    spacer;
                  }
              
                }
                :row{
                     : boxed_column {  
                    label = "&Calques";
                    width = 7;      
                : toggle {key = "2-tremie"  ; label = "GEX_EDS_sdp_2-tremie.";}  
                : toggle {key = "3-h-180"  ; label = "GEX_EDS_sdp_3-h-180.";}    
                : toggle {key = "5-pk" ; label = "GEX_EDS_sdp_5-pk.";}   
                : toggle {key = "6-combles" ; label = "GEX_EDS_sdp_6-combles.";}        
                : toggle {key = "7-lt"  ; label = "GEX_EDS_sdp_7-lt.";}          
                : toggle {key = "8-cave"  ; label = "GEX_EDS_sdp_8-cave.";}       
                : toggle {key = "teinte_contour"  ; label = "GEX_EDS_sdp_teinte_contour.";}
                : toggle {key = "sdp_SDP_su"  ; label = "GEX_EDS_sdp_SDP_su.";}
              
                  }

                         : boxed_column {  
                   
                    width = 7;      
                : toggle {key = "2-tremie_su"  ; label = "GEX_EDS_sdp_2-tremie_su.";}  
                : toggle {key = "3-h-180_su"  ; label = "GEX_EDS_sdp_3-h-180_su.";}    
                : toggle {key = "5-pk_su" ; label = "GEX_EDS_sdp_5-pk_su.";}          
                : toggle {key = "6-combles_su"  ; label = "GEX_EDS_sdp_6-combles_su.";}          
                : toggle {key = "7-lt_su"  ; label = "GEX_EDS_sdp_7-lt_su.";}       
                : toggle {key = "8-cave_su"  ; label = "GEX_EDS_sdp_8-cave_su.";}
              
                  }
                }
               
                                
              : column {                
                : boxed_column {
                   label = "&Options";
               :row {                 
                    spacer;
                    : boxed_radio_column {      
                            label = "&Style" ;   
                           :radio_button {key = "SwissBlack" ;label = "SwissBlack.ttf" ;}			
                            :radio_button { key = "Arial" ;	 label = "Arial" ; }	
                            :radio_button { key = "Roman" ;	label = "Roman" ;}		    
                    spacer;
                 }   
                
                                
                      : boxed_radio_column {	
                              label = "&Types de Hachure" ;    
                              : radio_button {	 key = "type1" ; label =" Predetermine" ;	}			
                              : radio_button {	key = "type2" ;	 label = "Defini par l'utilisateur" ; }
                              : radio_button {	key = "type3" ;	label = "Personnalise" ; }
                    spacer;
                 }	
                                
                       :boxed_radio_column {	 
                              label = "&Motif de Hachure" ;	key = "motif_hash"; 
                              : radio_button {		key = "SOLID" ;		label = "SOLID" ;}		       
                              : radio_button {		key = "ANGLE" ;	label = "ANGLE" ;	 }			   	 
                              : radio_button {		key = "ANSI32" ;	label = "ANSI32" ; }				 
                             }				 

              
                                
                 : column{
                     
                         : button {label = "Extract";key ="extract";fixed_width=true;is_cancel=true;width=14;fixed_width=true;}  
                         : button { label = "SDP";key = "SDP";fixed_width=true;is_cancel=true;width=14;}
                         : button { label = "SDT";key = "SDT";fixed_width=true;is_cancel=true;width=14;}
                         : button {label = "Export";key = "export";fixed_width=true;is_cancel=true;width=14;fixed_width=true;} 
                        
                             }				                                       
                             }				 
                  }
                  }
                spacer;
                spacer;
                    spacer;
             :row {
                        ok_button;fixed_width=true;is_cancel=true;width=40;
                        cancel_button;fixed_width=true;is_cancel=true;width=40;
                }
                spacer;
                spacer;
              }


diag_alert : dialog 
{
  label =  "Identification du type de Batiment";
	key = "main";
  spacer;

  :boxed_radio_column {	 
                              label = "&Identification du type de batiment " ; 
                              : radio_button {		key = "M" ;		label = "Batiments Mixtes(M)" ;}	       
                              : radio_button {		key = "L" ;	label = "Batiments Locaux(L)" ;	 }			   	 
                              : radio_button {		key = "H" ;	label = "Batiments Habitation(H) " ; }				 
                             }	
	: button {
	label = "OK";
	key = "accept";
	width = 12;
	fixed_width = true;
	mnemonic = "O";
	is_default = true;
	}

	: button {
	label = "Cancel";
	key = "cancel";
	width = 12;
	fixed_width = true;
	mnemonic = "C";
	is_cancel = true;
  	}
	: spacer { width = 1;}
	}
input_superficie: dialog { 
         label = "Pesquisa de Projetos"; 
         : column { 
           : boxed_column { 
             : edit_box {
               key = "superficie";
               label = "Entrer la superficie de locaux d'habitation ::";
               edit_width = 50;
               value = "";
               initial_focus = true;
             }
             :boxed_row{
              : button {
                  label = "OK";
                  key = "accept";
                  width = 12;
                  fixed_width = true;
                  mnemonic = "O";
                  is_default = true;
                  }

                  : button {
                  label = "Cancel";
                  key = "cancel";
                  width = 12;
                  fixed_width = true;
                  mnemonic = "C";
                  is_cancel = true;
                    }
                  : spacer { width = 1;}


             }
                

           }}}