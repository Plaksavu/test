ansible-playbook -i "192.168.100.24," -u имя_пользователя_с_доступом_к_sudo -kK имя_плейбука.yaml

Пример

ansible-playbook -i "192.168.100.24," -u administrator -kK ansible-playbook.yaml