VAGRANT_IMAGE_NAME = "ashleykleynhans/jammy64"

ELASTIC_NODES = 1
ELASTIC_IP_START = 20
PRIVATE_IP_NW = "10.10.10."

Vagrant.configure("2") do |config|
    config.vm.box = VAGRANT_IMAGE_NAME
    config.vm.box_check_update = false
    config.ssh.insert_key = false

    # Provision Elastis Stack Nodes
    (1..ELASTIC_NODES).each do |server_id|
        config.vm.define "elk-#{server_id}" do |node|
            node.vm.provider "virtualbox" do |vb|
                vb.name = "elk-#{server_id}"
                vb.memory = 4096
                vb.cpus = 2
                vb.customize ["modifyvm", :id, "--cpuexecutioncap", "50"]
            end
            node.vm.hostname = "elk-#{server_id}"
            node.vm.network :private_network, ip: PRIVATE_IP_NW + "#{ELASTIC_IP_START + server_id}"
            node.vm.provision "ansible" do |ansible|
                ansible.compatibility_mode = "2.0"
                ansible.playbook = "ansible/playbooks/provision_elastic_stack.yml"
                ansible.extra_vars = {
                    node_ip: PRIVATE_IP_NW + "#{ELASTIC_IP_START + server_id}",
                }
            end
        end
    end
end
