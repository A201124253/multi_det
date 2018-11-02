curl -X PUT --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{ } ' 'http://169.254.49.115/api/v1/nodes/rc_april_tag_detect/services/start'
curl -X PUT --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{"tags": [  { "id": "string","size": "float64" } ] } 
 ' 'http://169.254.49.115/api/v1/nodes/rc_april_tag_detect/services/detect' >info_april.txt
curl -X PUT --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{ } ' 'http://169.254.49.115/api/v1/nodes/rc_april_tag_detect/services/stop'
python3 multi_det.py
#gedit info_file.txt info_april.txt
