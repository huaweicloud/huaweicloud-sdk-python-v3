# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WtpProtectHostResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_name': 'str',
        'host_id': 'str',
        'public_ip': 'str',
        'private_ip': 'str',
        'group_id': 'str',
        'group_name': 'str',
        'asset_value': 'str',
        'os_bit': 'str',
        'os_type': 'str',
        'protect_status': 'str',
        'charging_mode': 'str',
        'resource_id': 'str',
        'rasp_protect_status': 'str',
        'anti_tampering_times': 'int',
        'detect_tampering_times': 'int',
        'os_name': 'str',
        'os_version': 'str',
        'host_status': 'str',
        'agent_status': 'str',
        'protect_dir_num': 'int',
        'abnormal_dir_list': 'list[str]',
        'abnormal_reason': 'int',
        'backup_host_id': 'str',
        'interrupt_reason': 'str'
    }

    attribute_map = {
        'host_name': 'host_name',
        'host_id': 'host_id',
        'public_ip': 'public_ip',
        'private_ip': 'private_ip',
        'group_id': 'group_id',
        'group_name': 'group_name',
        'asset_value': 'asset_value',
        'os_bit': 'os_bit',
        'os_type': 'os_type',
        'protect_status': 'protect_status',
        'charging_mode': 'charging_mode',
        'resource_id': 'resource_id',
        'rasp_protect_status': 'rasp_protect_status',
        'anti_tampering_times': 'anti_tampering_times',
        'detect_tampering_times': 'detect_tampering_times',
        'os_name': 'os_name',
        'os_version': 'os_version',
        'host_status': 'host_status',
        'agent_status': 'agent_status',
        'protect_dir_num': 'protect_dir_num',
        'abnormal_dir_list': 'abnormal_dir_list',
        'abnormal_reason': 'abnormal_reason',
        'backup_host_id': 'backup_host_id',
        'interrupt_reason': 'interrupt_reason'
    }

    def __init__(self, host_name=None, host_id=None, public_ip=None, private_ip=None, group_id=None, group_name=None, asset_value=None, os_bit=None, os_type=None, protect_status=None, charging_mode=None, resource_id=None, rasp_protect_status=None, anti_tampering_times=None, detect_tampering_times=None, os_name=None, os_version=None, host_status=None, agent_status=None, protect_dir_num=None, abnormal_dir_list=None, abnormal_reason=None, backup_host_id=None, interrupt_reason=None):
        r"""WtpProtectHostResponseInfo

        The model defined in huaweicloud sdk

        :param host_name: **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 
        :type host_name: str
        :param host_id: **参数解释**： 主机ID **取值范围**： 字符长度1-64位 
        :type host_id: str
        :param public_ip: **参数解释**： 弹性公网IP地址 **取值范围**： 字符长度1-256位 
        :type public_ip: str
        :param private_ip: **参数解释**： 服务器私有IP **取值范围**： 字符长度1-128位 
        :type private_ip: str
        :param group_id: **参数解释**： 策略组ID **取值范围**： 字符长度36-64位
        :type group_id: str
        :param group_name: **参数解释**: 服务器组名称 **取值范围**: 字符长度0-256位 
        :type group_name: str
        :param asset_value: 资产重要性，包含如下3种   - important ：重要资产   - common ：一般资产   - test ：测试资产
        :type asset_value: str
        :param os_bit: **参数解释**： 操作系统位数 **取值范围**： 字符长度1-64位 
        :type os_bit: str
        :param os_type: **参数解释**： 操作系统类型 **取值范围**： - Linux：Linux。 - Windows：Windows。 
        :type os_type: str
        :param protect_status: **参数解释**: 网页防篡改防护状态 **取值范围**: - opening : 开启中。 - opened : 防护中。 - closed : 未防护。 - open_failed : 防护失败。 - partial_protection : 部分防护。 - protection_interruption : 防护中断。 - protection_pause : 防护暂停。 
        :type protect_status: str
        :param charging_mode: **参数解释**： 计费模式 **取值范围**： - packet_cycle ：包年/包月。 - on_demand ：按需计费。
        :type charging_mode: str
        :param resource_id: **参数解释**： 资源ID **取值范围**： 字符长度0-128位
        :type resource_id: str
        :param rasp_protect_status: **参数解释**: 动态网页防篡改防护开启状态 **取值范围**: - opened ：已开启动态网页防篡改防护。 - closed ：未开启动态网页防篡改防护。 
        :type rasp_protect_status: str
        :param anti_tampering_times: **参数解释**: 近7天静态网页防篡改攻击次数 **取值范围**: 最小值0，最大值2000000000 
        :type anti_tampering_times: int
        :param detect_tampering_times: **参数解释**: 近7天动态网页防篡改攻击次数 **取值范围**: 最小值0，最大值2000000000 
        :type detect_tampering_times: int
        :param os_name: **参数解释**： 操作系统名称 **取值范围**： 字符长度0-128位 
        :type os_name: str
        :param os_version: **参数解释**： 操作系统版本 **取值范围**： 字符长度0-256位 
        :type os_version: str
        :param host_status: **参数解释**: 服务器状态 **取值范围**: - ACTIVE ：运行中。 - SHUTOFF ：关机。 - BUILDING ：创建中。 - ERROR ：故障。
        :type host_status: str
        :param agent_status: **参数解释**: Agent状态 **取值范围**: - not_installed：未安装。 - online：在线。 - offline：离线。 
        :type agent_status: str
        :param protect_dir_num: **参数解释**: 防护目录数 **取值范围**: 最小值0，最大值50 
        :type protect_dir_num: int
        :param abnormal_dir_list: **参数解释**: 防护状态是防护失败的防护目录列表，仅当存在防护状态是防护失败的防护目录时返回。 **取值范围**: 最少0条，最多50条 
        :type abnormal_dir_list: list[str]
        :param abnormal_reason: **参数解释**: 防护失败原因，仅当存在防护状态是防护失败的防护目录时返回。 **取值范围**: - 1 ：某一个防护目录的路径不存在。 - 2 ：多个防护目录的路径不存在。 - 7 ：某一个防护目录未防护。 - 8 ：多个防护目录未防护。 - 10 ：某一个防护目录是网络文件系统。 - 11 ：多个防护目录是网络文件系统。 
        :type abnormal_reason: int
        :param backup_host_id: **参数解释**： 远端备份服务器ID，仅当Linux服务器开启远端备份功能时返回。 **取值范围**： 字符长度0-64位 
        :type backup_host_id: str
        :param interrupt_reason: **参数解释**： 防护中断原因，仅当防护状态是防护中断时返回。 **取值范围**： 字符长度0-256位 
        :type interrupt_reason: str
        """
        
        

        self._host_name = None
        self._host_id = None
        self._public_ip = None
        self._private_ip = None
        self._group_id = None
        self._group_name = None
        self._asset_value = None
        self._os_bit = None
        self._os_type = None
        self._protect_status = None
        self._charging_mode = None
        self._resource_id = None
        self._rasp_protect_status = None
        self._anti_tampering_times = None
        self._detect_tampering_times = None
        self._os_name = None
        self._os_version = None
        self._host_status = None
        self._agent_status = None
        self._protect_dir_num = None
        self._abnormal_dir_list = None
        self._abnormal_reason = None
        self._backup_host_id = None
        self._interrupt_reason = None
        self.discriminator = None

        if host_name is not None:
            self.host_name = host_name
        if host_id is not None:
            self.host_id = host_id
        if public_ip is not None:
            self.public_ip = public_ip
        if private_ip is not None:
            self.private_ip = private_ip
        if group_id is not None:
            self.group_id = group_id
        if group_name is not None:
            self.group_name = group_name
        if asset_value is not None:
            self.asset_value = asset_value
        if os_bit is not None:
            self.os_bit = os_bit
        if os_type is not None:
            self.os_type = os_type
        if protect_status is not None:
            self.protect_status = protect_status
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if resource_id is not None:
            self.resource_id = resource_id
        if rasp_protect_status is not None:
            self.rasp_protect_status = rasp_protect_status
        if anti_tampering_times is not None:
            self.anti_tampering_times = anti_tampering_times
        if detect_tampering_times is not None:
            self.detect_tampering_times = detect_tampering_times
        if os_name is not None:
            self.os_name = os_name
        if os_version is not None:
            self.os_version = os_version
        if host_status is not None:
            self.host_status = host_status
        if agent_status is not None:
            self.agent_status = agent_status
        if protect_dir_num is not None:
            self.protect_dir_num = protect_dir_num
        if abnormal_dir_list is not None:
            self.abnormal_dir_list = abnormal_dir_list
        if abnormal_reason is not None:
            self.abnormal_reason = abnormal_reason
        if backup_host_id is not None:
            self.backup_host_id = backup_host_id
        if interrupt_reason is not None:
            self.interrupt_reason = interrupt_reason

    @property
    def host_name(self):
        r"""Gets the host_name of this WtpProtectHostResponseInfo.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 

        :return: The host_name of this WtpProtectHostResponseInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this WtpProtectHostResponseInfo.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 

        :param host_name: The host_name of this WtpProtectHostResponseInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_id(self):
        r"""Gets the host_id of this WtpProtectHostResponseInfo.

        **参数解释**： 主机ID **取值范围**： 字符长度1-64位 

        :return: The host_id of this WtpProtectHostResponseInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this WtpProtectHostResponseInfo.

        **参数解释**： 主机ID **取值范围**： 字符长度1-64位 

        :param host_id: The host_id of this WtpProtectHostResponseInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def public_ip(self):
        r"""Gets the public_ip of this WtpProtectHostResponseInfo.

        **参数解释**： 弹性公网IP地址 **取值范围**： 字符长度1-256位 

        :return: The public_ip of this WtpProtectHostResponseInfo.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this WtpProtectHostResponseInfo.

        **参数解释**： 弹性公网IP地址 **取值范围**： 字符长度1-256位 

        :param public_ip: The public_ip of this WtpProtectHostResponseInfo.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def private_ip(self):
        r"""Gets the private_ip of this WtpProtectHostResponseInfo.

        **参数解释**： 服务器私有IP **取值范围**： 字符长度1-128位 

        :return: The private_ip of this WtpProtectHostResponseInfo.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this WtpProtectHostResponseInfo.

        **参数解释**： 服务器私有IP **取值范围**： 字符长度1-128位 

        :param private_ip: The private_ip of this WtpProtectHostResponseInfo.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def group_id(self):
        r"""Gets the group_id of this WtpProtectHostResponseInfo.

        **参数解释**： 策略组ID **取值范围**： 字符长度36-64位

        :return: The group_id of this WtpProtectHostResponseInfo.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this WtpProtectHostResponseInfo.

        **参数解释**： 策略组ID **取值范围**： 字符长度36-64位

        :param group_id: The group_id of this WtpProtectHostResponseInfo.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def group_name(self):
        r"""Gets the group_name of this WtpProtectHostResponseInfo.

        **参数解释**: 服务器组名称 **取值范围**: 字符长度0-256位 

        :return: The group_name of this WtpProtectHostResponseInfo.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this WtpProtectHostResponseInfo.

        **参数解释**: 服务器组名称 **取值范围**: 字符长度0-256位 

        :param group_name: The group_name of this WtpProtectHostResponseInfo.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def asset_value(self):
        r"""Gets the asset_value of this WtpProtectHostResponseInfo.

        资产重要性，包含如下3种   - important ：重要资产   - common ：一般资产   - test ：测试资产

        :return: The asset_value of this WtpProtectHostResponseInfo.
        :rtype: str
        """
        return self._asset_value

    @asset_value.setter
    def asset_value(self, asset_value):
        r"""Sets the asset_value of this WtpProtectHostResponseInfo.

        资产重要性，包含如下3种   - important ：重要资产   - common ：一般资产   - test ：测试资产

        :param asset_value: The asset_value of this WtpProtectHostResponseInfo.
        :type asset_value: str
        """
        self._asset_value = asset_value

    @property
    def os_bit(self):
        r"""Gets the os_bit of this WtpProtectHostResponseInfo.

        **参数解释**： 操作系统位数 **取值范围**： 字符长度1-64位 

        :return: The os_bit of this WtpProtectHostResponseInfo.
        :rtype: str
        """
        return self._os_bit

    @os_bit.setter
    def os_bit(self, os_bit):
        r"""Sets the os_bit of this WtpProtectHostResponseInfo.

        **参数解释**： 操作系统位数 **取值范围**： 字符长度1-64位 

        :param os_bit: The os_bit of this WtpProtectHostResponseInfo.
        :type os_bit: str
        """
        self._os_bit = os_bit

    @property
    def os_type(self):
        r"""Gets the os_type of this WtpProtectHostResponseInfo.

        **参数解释**： 操作系统类型 **取值范围**： - Linux：Linux。 - Windows：Windows。 

        :return: The os_type of this WtpProtectHostResponseInfo.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this WtpProtectHostResponseInfo.

        **参数解释**： 操作系统类型 **取值范围**： - Linux：Linux。 - Windows：Windows。 

        :param os_type: The os_type of this WtpProtectHostResponseInfo.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def protect_status(self):
        r"""Gets the protect_status of this WtpProtectHostResponseInfo.

        **参数解释**: 网页防篡改防护状态 **取值范围**: - opening : 开启中。 - opened : 防护中。 - closed : 未防护。 - open_failed : 防护失败。 - partial_protection : 部分防护。 - protection_interruption : 防护中断。 - protection_pause : 防护暂停。 

        :return: The protect_status of this WtpProtectHostResponseInfo.
        :rtype: str
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        r"""Sets the protect_status of this WtpProtectHostResponseInfo.

        **参数解释**: 网页防篡改防护状态 **取值范围**: - opening : 开启中。 - opened : 防护中。 - closed : 未防护。 - open_failed : 防护失败。 - partial_protection : 部分防护。 - protection_interruption : 防护中断。 - protection_pause : 防护暂停。 

        :param protect_status: The protect_status of this WtpProtectHostResponseInfo.
        :type protect_status: str
        """
        self._protect_status = protect_status

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this WtpProtectHostResponseInfo.

        **参数解释**： 计费模式 **取值范围**： - packet_cycle ：包年/包月。 - on_demand ：按需计费。

        :return: The charging_mode of this WtpProtectHostResponseInfo.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this WtpProtectHostResponseInfo.

        **参数解释**： 计费模式 **取值范围**： - packet_cycle ：包年/包月。 - on_demand ：按需计费。

        :param charging_mode: The charging_mode of this WtpProtectHostResponseInfo.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def resource_id(self):
        r"""Gets the resource_id of this WtpProtectHostResponseInfo.

        **参数解释**： 资源ID **取值范围**： 字符长度0-128位

        :return: The resource_id of this WtpProtectHostResponseInfo.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this WtpProtectHostResponseInfo.

        **参数解释**： 资源ID **取值范围**： 字符长度0-128位

        :param resource_id: The resource_id of this WtpProtectHostResponseInfo.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def rasp_protect_status(self):
        r"""Gets the rasp_protect_status of this WtpProtectHostResponseInfo.

        **参数解释**: 动态网页防篡改防护开启状态 **取值范围**: - opened ：已开启动态网页防篡改防护。 - closed ：未开启动态网页防篡改防护。 

        :return: The rasp_protect_status of this WtpProtectHostResponseInfo.
        :rtype: str
        """
        return self._rasp_protect_status

    @rasp_protect_status.setter
    def rasp_protect_status(self, rasp_protect_status):
        r"""Sets the rasp_protect_status of this WtpProtectHostResponseInfo.

        **参数解释**: 动态网页防篡改防护开启状态 **取值范围**: - opened ：已开启动态网页防篡改防护。 - closed ：未开启动态网页防篡改防护。 

        :param rasp_protect_status: The rasp_protect_status of this WtpProtectHostResponseInfo.
        :type rasp_protect_status: str
        """
        self._rasp_protect_status = rasp_protect_status

    @property
    def anti_tampering_times(self):
        r"""Gets the anti_tampering_times of this WtpProtectHostResponseInfo.

        **参数解释**: 近7天静态网页防篡改攻击次数 **取值范围**: 最小值0，最大值2000000000 

        :return: The anti_tampering_times of this WtpProtectHostResponseInfo.
        :rtype: int
        """
        return self._anti_tampering_times

    @anti_tampering_times.setter
    def anti_tampering_times(self, anti_tampering_times):
        r"""Sets the anti_tampering_times of this WtpProtectHostResponseInfo.

        **参数解释**: 近7天静态网页防篡改攻击次数 **取值范围**: 最小值0，最大值2000000000 

        :param anti_tampering_times: The anti_tampering_times of this WtpProtectHostResponseInfo.
        :type anti_tampering_times: int
        """
        self._anti_tampering_times = anti_tampering_times

    @property
    def detect_tampering_times(self):
        r"""Gets the detect_tampering_times of this WtpProtectHostResponseInfo.

        **参数解释**: 近7天动态网页防篡改攻击次数 **取值范围**: 最小值0，最大值2000000000 

        :return: The detect_tampering_times of this WtpProtectHostResponseInfo.
        :rtype: int
        """
        return self._detect_tampering_times

    @detect_tampering_times.setter
    def detect_tampering_times(self, detect_tampering_times):
        r"""Sets the detect_tampering_times of this WtpProtectHostResponseInfo.

        **参数解释**: 近7天动态网页防篡改攻击次数 **取值范围**: 最小值0，最大值2000000000 

        :param detect_tampering_times: The detect_tampering_times of this WtpProtectHostResponseInfo.
        :type detect_tampering_times: int
        """
        self._detect_tampering_times = detect_tampering_times

    @property
    def os_name(self):
        r"""Gets the os_name of this WtpProtectHostResponseInfo.

        **参数解释**： 操作系统名称 **取值范围**： 字符长度0-128位 

        :return: The os_name of this WtpProtectHostResponseInfo.
        :rtype: str
        """
        return self._os_name

    @os_name.setter
    def os_name(self, os_name):
        r"""Sets the os_name of this WtpProtectHostResponseInfo.

        **参数解释**： 操作系统名称 **取值范围**： 字符长度0-128位 

        :param os_name: The os_name of this WtpProtectHostResponseInfo.
        :type os_name: str
        """
        self._os_name = os_name

    @property
    def os_version(self):
        r"""Gets the os_version of this WtpProtectHostResponseInfo.

        **参数解释**： 操作系统版本 **取值范围**： 字符长度0-256位 

        :return: The os_version of this WtpProtectHostResponseInfo.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        r"""Sets the os_version of this WtpProtectHostResponseInfo.

        **参数解释**： 操作系统版本 **取值范围**： 字符长度0-256位 

        :param os_version: The os_version of this WtpProtectHostResponseInfo.
        :type os_version: str
        """
        self._os_version = os_version

    @property
    def host_status(self):
        r"""Gets the host_status of this WtpProtectHostResponseInfo.

        **参数解释**: 服务器状态 **取值范围**: - ACTIVE ：运行中。 - SHUTOFF ：关机。 - BUILDING ：创建中。 - ERROR ：故障。

        :return: The host_status of this WtpProtectHostResponseInfo.
        :rtype: str
        """
        return self._host_status

    @host_status.setter
    def host_status(self, host_status):
        r"""Sets the host_status of this WtpProtectHostResponseInfo.

        **参数解释**: 服务器状态 **取值范围**: - ACTIVE ：运行中。 - SHUTOFF ：关机。 - BUILDING ：创建中。 - ERROR ：故障。

        :param host_status: The host_status of this WtpProtectHostResponseInfo.
        :type host_status: str
        """
        self._host_status = host_status

    @property
    def agent_status(self):
        r"""Gets the agent_status of this WtpProtectHostResponseInfo.

        **参数解释**: Agent状态 **取值范围**: - not_installed：未安装。 - online：在线。 - offline：离线。 

        :return: The agent_status of this WtpProtectHostResponseInfo.
        :rtype: str
        """
        return self._agent_status

    @agent_status.setter
    def agent_status(self, agent_status):
        r"""Sets the agent_status of this WtpProtectHostResponseInfo.

        **参数解释**: Agent状态 **取值范围**: - not_installed：未安装。 - online：在线。 - offline：离线。 

        :param agent_status: The agent_status of this WtpProtectHostResponseInfo.
        :type agent_status: str
        """
        self._agent_status = agent_status

    @property
    def protect_dir_num(self):
        r"""Gets the protect_dir_num of this WtpProtectHostResponseInfo.

        **参数解释**: 防护目录数 **取值范围**: 最小值0，最大值50 

        :return: The protect_dir_num of this WtpProtectHostResponseInfo.
        :rtype: int
        """
        return self._protect_dir_num

    @protect_dir_num.setter
    def protect_dir_num(self, protect_dir_num):
        r"""Sets the protect_dir_num of this WtpProtectHostResponseInfo.

        **参数解释**: 防护目录数 **取值范围**: 最小值0，最大值50 

        :param protect_dir_num: The protect_dir_num of this WtpProtectHostResponseInfo.
        :type protect_dir_num: int
        """
        self._protect_dir_num = protect_dir_num

    @property
    def abnormal_dir_list(self):
        r"""Gets the abnormal_dir_list of this WtpProtectHostResponseInfo.

        **参数解释**: 防护状态是防护失败的防护目录列表，仅当存在防护状态是防护失败的防护目录时返回。 **取值范围**: 最少0条，最多50条 

        :return: The abnormal_dir_list of this WtpProtectHostResponseInfo.
        :rtype: list[str]
        """
        return self._abnormal_dir_list

    @abnormal_dir_list.setter
    def abnormal_dir_list(self, abnormal_dir_list):
        r"""Sets the abnormal_dir_list of this WtpProtectHostResponseInfo.

        **参数解释**: 防护状态是防护失败的防护目录列表，仅当存在防护状态是防护失败的防护目录时返回。 **取值范围**: 最少0条，最多50条 

        :param abnormal_dir_list: The abnormal_dir_list of this WtpProtectHostResponseInfo.
        :type abnormal_dir_list: list[str]
        """
        self._abnormal_dir_list = abnormal_dir_list

    @property
    def abnormal_reason(self):
        r"""Gets the abnormal_reason of this WtpProtectHostResponseInfo.

        **参数解释**: 防护失败原因，仅当存在防护状态是防护失败的防护目录时返回。 **取值范围**: - 1 ：某一个防护目录的路径不存在。 - 2 ：多个防护目录的路径不存在。 - 7 ：某一个防护目录未防护。 - 8 ：多个防护目录未防护。 - 10 ：某一个防护目录是网络文件系统。 - 11 ：多个防护目录是网络文件系统。 

        :return: The abnormal_reason of this WtpProtectHostResponseInfo.
        :rtype: int
        """
        return self._abnormal_reason

    @abnormal_reason.setter
    def abnormal_reason(self, abnormal_reason):
        r"""Sets the abnormal_reason of this WtpProtectHostResponseInfo.

        **参数解释**: 防护失败原因，仅当存在防护状态是防护失败的防护目录时返回。 **取值范围**: - 1 ：某一个防护目录的路径不存在。 - 2 ：多个防护目录的路径不存在。 - 7 ：某一个防护目录未防护。 - 8 ：多个防护目录未防护。 - 10 ：某一个防护目录是网络文件系统。 - 11 ：多个防护目录是网络文件系统。 

        :param abnormal_reason: The abnormal_reason of this WtpProtectHostResponseInfo.
        :type abnormal_reason: int
        """
        self._abnormal_reason = abnormal_reason

    @property
    def backup_host_id(self):
        r"""Gets the backup_host_id of this WtpProtectHostResponseInfo.

        **参数解释**： 远端备份服务器ID，仅当Linux服务器开启远端备份功能时返回。 **取值范围**： 字符长度0-64位 

        :return: The backup_host_id of this WtpProtectHostResponseInfo.
        :rtype: str
        """
        return self._backup_host_id

    @backup_host_id.setter
    def backup_host_id(self, backup_host_id):
        r"""Sets the backup_host_id of this WtpProtectHostResponseInfo.

        **参数解释**： 远端备份服务器ID，仅当Linux服务器开启远端备份功能时返回。 **取值范围**： 字符长度0-64位 

        :param backup_host_id: The backup_host_id of this WtpProtectHostResponseInfo.
        :type backup_host_id: str
        """
        self._backup_host_id = backup_host_id

    @property
    def interrupt_reason(self):
        r"""Gets the interrupt_reason of this WtpProtectHostResponseInfo.

        **参数解释**： 防护中断原因，仅当防护状态是防护中断时返回。 **取值范围**： 字符长度0-256位 

        :return: The interrupt_reason of this WtpProtectHostResponseInfo.
        :rtype: str
        """
        return self._interrupt_reason

    @interrupt_reason.setter
    def interrupt_reason(self, interrupt_reason):
        r"""Sets the interrupt_reason of this WtpProtectHostResponseInfo.

        **参数解释**： 防护中断原因，仅当防护状态是防护中断时返回。 **取值范围**： 字符长度0-256位 

        :param interrupt_reason: The interrupt_reason of this WtpProtectHostResponseInfo.
        :type interrupt_reason: str
        """
        self._interrupt_reason = interrupt_reason

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WtpProtectHostResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
