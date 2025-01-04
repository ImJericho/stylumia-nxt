The workflow looks like:


DataIngestion Page pe ek button hoga -> find new products types  -> Displays product
                                                                              -> Save product to ../backend/data_ingestion_engine/data
                                                                                    -> After saving img2txt2txt_engine will do feature_extraction and save the file in ../backend/img2txt2txt_engine/data


Verification Page will take data from ../backend/img2txt2txt_engine/data and will display all the rows in that file along with a checkbox  -> If checkbox got ticked then send add that row in the ../backend/verification_engine/data
                ->After saving the trend engine will take the data from ../backend/verification_engine/data and do the analysis
                ->After saving the ontology_engine will take the data from ../backend/verification_engine/data and update the ontology




                                                                       