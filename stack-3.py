import re

data = {
 ' cAVDNIIB ': ' pattern not matched: "[2022-07-25 06:40:51.147] [Information] LW () <RDP> Bot execution completed - JOBNAME:\\"TEST_NAME_1\\" JOBID:\\"2022072564027\\" TYPE:\\"Desktop\\" startTime:\\"1658731228\\" endTime:\\"1658731251\\" botMachineName:\\"LW\\" botMachineIP:\\"SOME_IP\\" state:\\"completed\\" status:\\"successful\\" Action:\\"run\\"" ',
 ' cQVDNIIB ': ' pattern not matched: "[2022-07-25 07:30:11.711] [Information] LW () <RDP> Bot consumer listening for messages." ',
 ' cgVDNIIB ': ' pattern not matched: "[2022-07-25 07:30:11.714] [Information] LW () <RDP> Message received from queue - JOBNAME:\\"TEST_NAME\\" JOBID:\\"2022072573011\\" TYPE:\\"Desktop\\" startTime:\\"1658734211\\" Action:\\"run\\"" ',
 ' cwVDNIIB ': ' pattern not matched: "[2022-07-25 07:30:11.717] [Information] LW () <RDP> Bot action:\\"run\\"" ',
 ' dAVDNIIB ': ' pattern not matched: "[2022-07-25 07:30:11.717] [Information] LW () <RDP>  [x] \\"{\\\\\\"JOBNAME\\\\\\":\\\\\\"TEST_NAME\\\\\\",\\\\\\"TYPE\\\\\\":\\\\\\"Desktop\\\\\\",\\\\\\"rdpRequired\\\\\\":false,\\\\\\"state\\\\\\":\\\\\\"Running\\\\\\",\\\\\\"status\\\\\\":\\\\\\"Running\\\\\\",\\\\\\"requestorId\\\\\\":null,\\\\\\"JOBID\\\\\\":\\\\\\"2022072573011\\\\\\",\\\\\\"startTime\\\\\\":null,\\\\\\"endTime\\\\\\":null,\\\\\\"botstatus\\\\\\":null,\\\\\\"action\\\\\\":\\\\\\"run\\\\\\"}\\"" ',
 ' dQVDNIIB ': ' pattern not matched: "[2022-07-25 07:30:11.718] [Information] LW () <RDP> Creating background process \'\\"C:\\\\Tools\\\\Flows\\\\Desktop\\\\TEST_NAME\\\\Simulator.exe\\"\'" ',
 ' gQVENIIB ': ' pattern not matched: "[2022-07-25 07:30:11.743] [Information] LW () <RDP> Bot execution started - JOBNAME:\\"TEST_NAME\\" JOBID:\\"2022072573011\\" TYPE:\\"Desktop\\" startTime:\\"1658734211\\" botMachineName:\\"LW\\" botMachineIP:\\"SOME_IP\\" state:\\"Running\\" status:\\"Running\\" Action:\\"run\\"" ',
 ' ggVENIIB ': ' pattern not matched: "[2022-07-25 07:31:23.368] [Information] LW () <RDP> Published message to response queue: ExchangeName:\\"liteportal.exchange\\", Message:\\"{\\\\\\"requestorId\\\\\\":null,\\\\\\"rdpRequired\\\\\\":false,\\\\\\"JOBNAME\\\\\\":\\\\\\"TEST_NAME\\\\\\",\\\\\\"JOBID\\\\\\":\\\\\\"2022072573011\\\\\\",\\\\\\"TYPE\\\\\\":\\\\\\"Desktop\\\\\\",\\\\\\"startTime\\\\\\":\\\\\\"1658734211\\\\\\",\\\\\\"endTime\\\\\\":\\\\\\"1658734283\\\\\\",\\\\\\"status\\\\\\":\\\\\\"successful\\\\\\",\\\\\\"action\\\\\\":\\\\\\"run\\\\\\",\\\\\\"state\\\\\\":\\\\\\"completed\\\\\\",\\\\\\"botMachineName\\\\\\":\\\\\\"LW\\\\\\",\\\\\\"botMachineOS\\\\\\":\\\\\\"WindowsXP 6.2.9200.0\\\\\\",\\\\\\"botMachineIP\\\\\\":\\\\\\"SOME_IP\\\\\\",\\\\\\"Message\\\\\\":null}\\" " ',
 ' gwVENIIB ': ' pattern not matched: "[2022-07-25 07:31:23.373] [Information] LW () <RDP> Log file path: \\"C:\\\\Tools\\\\Flows\\\\Desktop\\\\TEST_NAME\\\\logs\\\\Logs-2022_07_25.log\\"" ',
 ' hAVENIIB ': ' pattern not matched: "[2022-07-25 07:31:23.374] [Information] LW () <RDP> Log file exists" ',
 ' hgVENIIB ': ' pattern not matched: "[2022-07-25 07:31:23.384] [Information] LW () <RDP> Bot log file deleted: \\"C:\\\\Tools\\\\Flows\\\\Desktop\\\\TEST_NAME\\\\logs\\\\Logs-2022_07_25.log\\"" '}

# keys = list(data.keys())
# string0 = data[keys[0]]

# search0 = re.search('JOBID',data[keys[0]])

# if re.search('JOBID',string0) != None:
#     string1 = string0[search0.span()[1]:]
#     jobid = re.search('\d+', string1).group(0)
#     print(jobid)

jobid_temp = []

for k,v in data.items():
    search0 = re.search('JOBID',data[k])

    if re.search('JOBID',v) == None:
        jobid_temp.append("NaN")

        ## for illustration purpose
        print(k, 'Nothing Exist')

    else:
        string1 = v[search0.span()[1]:]
        jobid = re.search('\d+', string1).group(0)
        jobid_temp.append(jobid)

        ## for illustration purpose
        print(k, jobid)
    
