"""Deploy Mosip in Cloudlab"""

import geni.portal as portal
import geni.rspec.pg as pg
import geni.rspec.emulab as emulab

# Create a portal object,
pc = portal.Context()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()

CENTOS_ARN = "urn:publicid:IDN+emulab.net+image+emulab-ops:CENTOS7-64-STD"

node = request.XenVM("console")
node.disk_image = CENTOS_ARN
node.ram = 16 * 1024
node.cores = 4
node.disk = 256

node = request.XenVM("mz-master")
node.disk_image = CENTOS_ARN
node.ram = 8 * 1024
node.cores = 4
node.disk = 64

for i in range(9):
    node = request.XenVM("mz-worker-" + str(i))
    node.disk_image = CENTOS_ARN
    node.ram = 16 * 1024
    node.cores = 4
    node.disk = 64

node = request.XenVM(f"dmz-master")
node.disk_image = CENTOS_ARN
node.ram = 8 * 1024
node.cores = 4
node.disk = 64

node = request.XenVM(f"dmz-worker")
node.disk_image = CENTOS_ARN
node.ram = 16 * 1024
node.cores = 4
node.disk = 64

pc.printRequestRSpec(request)
