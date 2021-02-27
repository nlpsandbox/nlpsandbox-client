# Remove datanode database first
docker volume rm data-node_database-data
# Start data node

cd examples
python push_dataset.py

# Get annotation store
nlp-cli community get-annotation-store --dataset_id test-dataset --annotation_store_id goldstandard --data_node_host http://localhost:8080/api/v1

# List annotations
nlp-cli community list-annotations --dataset_id test-dataset --annotation_store_id goldstandard --data_node_host http://localhost:8080/api/v1

# list notes
nlp-cli community list-notes --dataset_id test-dataset \
                             --fhir_store_id evaluation \
                             --data_node_host http://localhost:8080/api/v1

nlp-cli community list-notes --dataset_id test-dataset --fhir_store_id evaluation --data_node_host http://localhost:8080/api/v1 --output example_note.json

# get annotation
nlp-cli community get-annotation --annotation_id 110-01 \
                                 --dataset_id test-dataset \
                                 --annotation_store_id goldstandard \
                                 --data_node_host http://localhost:8080/api/v1 

# Get json
nlp-cli community get-annotation --annotation_id 110-01 \
                                 --dataset_id test-dataset \
                                 --annotation_store_id goldstandard \
                                 --data_node_host http://localhost:8080/api/v1 \
                                 --output test.json


# Store annotations
# Must remove "name" key from test.json
nlp-cli community store-annotations --dataset_id test-dataset \
                                    --annotation_store_id goldstandard \
                                    --annotation_json test.json \
                                    --data_node_host http://localhost:8080/api/v1


# Start date-annotator-example
nlp-cli evaluate get-tool --annotator_host http://localhost:80/api/v1

nlp-cli evaluate check-url --url http://localhost:80/api/v1/ui

nlp-cli evaluate annotate-note --annotator_host http://localhost:80/api/v1 \
                               --note_json example_note.json \
                               --annotator_type date

nlp-cli evaluate prediction --pred_filepath test/data/new_prediction.json \
                            --gold_filepath test/data/new_goldstandard.json \
                            --eval_type person