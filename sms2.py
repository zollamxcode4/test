import clx.xms
import time
import requests

message=raw_input('Pesan  : ')
numbers=raw_input('Nomor  : ')
banyak =raw_input('Banyak : ')

def send(message, number):
    service_plan_id='d1a45bd91cf34d88ace81625ca18ceb0'
    token='371bb47502c64097909b01fc7cb674b9'
    client = clx.xms.Client(service_plan_id, token)

    create = clx.xms.api.MtBatchTextSmsCreate()
    create.sender = '447537404817'
    create.recipients = {number}
    create.body = message

    try:
      batch = client.create_batch(create)
      print 'Coba Mengirim Ke %s'%(number)
    except (requests.exceptions.RequestException,
      clx.xms.exceptions.ApiException) as ex:
      print('Failed to communicate with XMS: %s' % str(ex))

if __name__ == '__main__':
    for x in range(int(banyak)):
        send(message, numbers)
        time.sleep(2)
