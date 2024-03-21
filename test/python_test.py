
data = "POST /submit_form HTTP/1.1\r\nHost: example.com\r\n Connection: keep-alive\r\n User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36\r\n Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n Accept-Encoding: gzip, deflate\r\n Accept-Language: en-US,en;q=0.9\r\n Content-Length: 12\r\n Content-Type: application/x-www-form-urlencoded\r\n\r\n Hello, World!"

index = data.find('Content-Length:') # 검색

length_line = data[index:] # 문자열이니까

print(length_line)

length = int(length_line.split(' ')[1])

print(length)

body_start_index = data.find('\r\n\r\n') + 4

print(body_start_index)

body = data[body_start_index:body_start_index + length]

print(body)


