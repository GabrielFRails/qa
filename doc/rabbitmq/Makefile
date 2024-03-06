base_install:
	bash install.sh

set_user_and_password:
	sudo rabbitmqctl add_user user password && \
	sudo rabbitmqctl set_user_tags user administrator && \
	sudo rabbitmqctl set_permissions -p / user "." "." "."

pipinstall_pika:
	pip install pika

runall: base_install set_user_and_password pipinstall_pika
	echo "all done"