Vagrant.configure(2) do |config|

  config.vm.define "OpenSuse13", autostart: true do |m0|
    m0.vm.box = "default-machine"
    m0.vm.box = "webhippie/opensuse-13.2"
    m0.vm.network "private_network", ip: "192.168.33.11"

    m0.vm.provider "virtualbox" do |vb|
        vb.gui = true
        vb.memory = "1024"
        vb.cpus = 2
    end
  end

  config.vm.define "Ubuntu14", autostart: true do |m0|
    m0.vm.box = "default-machine"
    m0.vm.box = "ubuntu/trusty64"
    m0.vm.network "private_network", ip: "192.168.33.12"

    m0.vm.provider "virtualbox" do |vb|
        vb.gui = true
        vb.memory = "1024"
        vb.cpus = 2
    end
  end

  config.vm.define "CentOS7", autostart: true do |m0|
    m0.vm.box = "default-machine"
#    m0.vm.box = "centos/7" # Duh, no guest additions
    m0.vm.box = "bento/centos-7.1"
    m0.vm.network "private_network", ip: "192.168.33.13"
    #m0.vm.synced_folder ".", "/srv/website" # trying to fix rsync only synced folder

    m0.vm.provider "virtualbox" do |vb|
        vb.gui = true
        vb.memory = "1024"
        vb.cpus = 2
    end
  end
end
