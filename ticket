import requests
import time

def check_ticket_availability():
    # 发送请求检查票是否可用
    response = requests.get('https://ticketwebsite.com/check_ticket')
    data = response.json()
    return data['available']

def book_ticket():
    # 发送请求预订票
    payload = {'ticket_id': '12345', 'quantity': 1}
    response = requests.post('https://ticketwebsite.com/book_ticket', data=payload)
    data = response.json()
    if data['success']:
        print('成功预订票！')
    else:
        print('预订失败。')

def main():
    available = False
    while not available:
        available = check_ticket_availability()
        if available:
            book_ticket()
        else:
            print('票暂时不可用，继续尝试...')
            time.sleep(5)  # 每隔5秒钟重新检查票的可用性

if __name__ == '__main__':
    main()
