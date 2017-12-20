docker-compose exec redis redis-cli flushall > /dev/null

curl_output=$(curl -s http://localhost:5000/test; curl -s -X POST http://localhost:5000/test; curl -s http://localhost:5000/test)

expected_curl_output='{
  "value": null
}
{
  "success": true
}
{
  "value": "value"
}'

if [ "$curl_output" == "$expected_curl_output" ]; then
	echo "Success!"
else
	echo "Something went wrong"
	echo "$curl_output"
fi
