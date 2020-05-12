## Going edit script where if ping is alive, send payload, "menu" was just for testing


### Random NOTES
function loadPayload(slotValue) {

    bufPayloadIndex = 0; // reset
    bufPayload = []; // reset
    user_addresses = [720896, 737280, 753664, 770048, 786432, 802816, 819200];
    buff_len = 1024;
    for (let i = 0; i < 16; i++) {
      user_addr = user_addresses[slotValue] + (i*1024);
      cmd = "FR" + user_addr + "\t" + buff_len;
      QueueOperation(cmd, loadPayloadCallback);
    }
}

wx FR 720896 1024

function REBOOT() {
  killGroup(1);
  hud(1,"ghost",1);
  command_line = "CR1\t";
  QueueOperation(command_line);
}
load
FR + user address/payload address

1 on | 0 off
CR1 = reboot cable
CE = run payload?
CU = usb interrubt
CJ = jiggler
CS0\t =  scan networks

WS API calls

API uses ASCII encoded commands, arguments are separated with `\t`.

API responses contain complete request data and optional additional
response data (again separated with `\t`).

----encode payload------
line 2871 -  line 5925
