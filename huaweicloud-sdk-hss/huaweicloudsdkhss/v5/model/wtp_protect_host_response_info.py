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
        'ipv6': 'str',
        'group_name': 'str',
        'asset_value': 'str',
        'os_bit': 'str',
        'os_type': 'str',
        'protect_status': 'str',
        'rasp_protect_status': 'str',
        'anti_tampering_times': 'int',
        'detect_tampering_times': 'int',
        'last_detect_time': 'int',
        'scheduled_shutdown_status': 'str',
        'os_name': 'str',
        'os_version': 'str',
        'host_status': 'str',
        'agent_status': 'str',
        'protect_dir_num': 'int',
        'remote_backbup_info': 'WtpRemoteBackupResponseInfo'
    }

    attribute_map = {
        'host_name': 'host_name',
        'host_id': 'host_id',
        'public_ip': 'public_ip',
        'private_ip': 'private_ip',
        'ipv6': 'ipv6',
        'group_name': 'group_name',
        'asset_value': 'asset_value',
        'os_bit': 'os_bit',
        'os_type': 'os_type',
        'protect_status': 'protect_status',
        'rasp_protect_status': 'rasp_protect_status',
        'anti_tampering_times': 'anti_tampering_times',
        'detect_tampering_times': 'detect_tampering_times',
        'last_detect_time': 'last_detect_time',
        'scheduled_shutdown_status': 'scheduled_shutdown_status',
        'os_name': 'os_name',
        'os_version': 'os_version',
        'host_status': 'host_status',
        'agent_status': 'agent_status',
        'protect_dir_num': 'protect_dir_num',
        'remote_backbup_info': 'remote_backbup_info'
    }

    def __init__(self, host_name=None, host_id=None, public_ip=None, private_ip=None, ipv6=None, group_name=None, asset_value=None, os_bit=None, os_type=None, protect_status=None, rasp_protect_status=None, anti_tampering_times=None, detect_tampering_times=None, last_detect_time=None, scheduled_shutdown_status=None, os_name=None, os_version=None, host_status=None, agent_status=None, protect_dir_num=None, remote_backbup_info=None):
        r"""WtpProtectHostResponseInfo

        The model defined in huaweicloud sdk

        :param host_name: 服务器名称
        :type host_name: str
        :param host_id: 主机ID
        :type host_id: str
        :param public_ip: 弹性公网IP
        :type public_ip: str
        :param private_ip: 私有IP
        :type private_ip: str
        :param ipv6: 私有IPv6地址
        :type ipv6: str
        :param group_name: 服务器组名称
        :type group_name: str
        :param asset_value: 资产重要性，包含如下3种   - important ：重要资产   - common ：一般资产   - test ：测试资产
        :type asset_value: str
        :param os_bit: 操作系统位数
        :type os_bit: str
        :param os_type: 操作系统（linux，windows）
        :type os_type: str
        :param protect_status: 防护状态   - opening : 正在开启   - opened : 防护中   - open_failed : 防护失败   - partial_protection : 部分防护   - protection_interruption : 防护中断
        :type protect_status: str
        :param rasp_protect_status: 动态网页防篡改状态   - closed : 未开启   - opened : 防护中
        :type rasp_protect_status: str
        :param anti_tampering_times: 已防御篡改攻击次数
        :type anti_tampering_times: int
        :param detect_tampering_times: 已发现篡改攻击
        :type detect_tampering_times: int
        :param last_detect_time: 最近检测时间(ms)
        :type last_detect_time: int
        :param scheduled_shutdown_status: 定时关闭防护开关状态   - opened : 开启   - closed : 未开启
        :type scheduled_shutdown_status: str
        :param os_name: 系统名称
        :type os_name: str
        :param os_version: 系统版本
        :type os_version: str
        :param host_status: 服务器状态，包含如下4种。   - ACTIVE ：运行中。   - SHUTOFF ：关机。   - BUILDING ：创建中。   - ERROR ：故障。
        :type host_status: str
        :param agent_status: Agent状态   - not_installed : agent未安装   - online : agent在线   - offline : agent不在线
        :type agent_status: str
        :param protect_dir_num: 防护目录数
        :type protect_dir_num: int
        :param remote_backbup_info: 
        :type remote_backbup_info: :class:`huaweicloudsdkhss.v5.WtpRemoteBackupResponseInfo`
        """
        
        

        self._host_name = None
        self._host_id = None
        self._public_ip = None
        self._private_ip = None
        self._ipv6 = None
        self._group_name = None
        self._asset_value = None
        self._os_bit = None
        self._os_type = None
        self._protect_status = None
        self._rasp_protect_status = None
        self._anti_tampering_times = None
        self._detect_tampering_times = None
        self._last_detect_time = None
        self._scheduled_shutdown_status = None
        self._os_name = None
        self._os_version = None
        self._host_status = None
        self._agent_status = None
        self._protect_dir_num = None
        self._remote_backbup_info = None
        self.discriminator = None

        if host_name is not None:
            self.host_name = host_name
        if host_id is not None:
            self.host_id = host_id
        if public_ip is not None:
            self.public_ip = public_ip
        if private_ip is not None:
            self.private_ip = private_ip
        if ipv6 is not None:
            self.ipv6 = ipv6
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
        if rasp_protect_status is not None:
            self.rasp_protect_status = rasp_protect_status
        if anti_tampering_times is not None:
            self.anti_tampering_times = anti_tampering_times
        if detect_tampering_times is not None:
            self.detect_tampering_times = detect_tampering_times
        if last_detect_time is not None:
            self.last_detect_time = last_detect_time
        if scheduled_shutdown_status is not None:
            self.scheduled_shutdown_status = scheduled_shutdown_status
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
        if remote_backbup_info is not None:
            self.remote_backbup_info = remote_backbup_info

    @property
    def host_name(self):
        r"""Gets the host_name of this WtpProtectHostResponseInfo.

        服务器名称

        :return: The host_name of this WtpProtectHostResponseInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this WtpProtectHostResponseInfo.

        服务器名称

        :param host_name: The host_name of this WtpProtectHostResponseInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_id(self):
        r"""Gets the host_id of this WtpProtectHostResponseInfo.

        主机ID

        :return: The host_id of this WtpProtectHostResponseInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this WtpProtectHostResponseInfo.

        主机ID

        :param host_id: The host_id of this WtpProtectHostResponseInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def public_ip(self):
        r"""Gets the public_ip of this WtpProtectHostResponseInfo.

        弹性公网IP

        :return: The public_ip of this WtpProtectHostResponseInfo.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this WtpProtectHostResponseInfo.

        弹性公网IP

        :param public_ip: The public_ip of this WtpProtectHostResponseInfo.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def private_ip(self):
        r"""Gets the private_ip of this WtpProtectHostResponseInfo.

        私有IP

        :return: The private_ip of this WtpProtectHostResponseInfo.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this WtpProtectHostResponseInfo.

        私有IP

        :param private_ip: The private_ip of this WtpProtectHostResponseInfo.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def ipv6(self):
        r"""Gets the ipv6 of this WtpProtectHostResponseInfo.

        私有IPv6地址

        :return: The ipv6 of this WtpProtectHostResponseInfo.
        :rtype: str
        """
        return self._ipv6

    @ipv6.setter
    def ipv6(self, ipv6):
        r"""Sets the ipv6 of this WtpProtectHostResponseInfo.

        私有IPv6地址

        :param ipv6: The ipv6 of this WtpProtectHostResponseInfo.
        :type ipv6: str
        """
        self._ipv6 = ipv6

    @property
    def group_name(self):
        r"""Gets the group_name of this WtpProtectHostResponseInfo.

        服务器组名称

        :return: The group_name of this WtpProtectHostResponseInfo.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this WtpProtectHostResponseInfo.

        服务器组名称

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

        操作系统位数

        :return: The os_bit of this WtpProtectHostResponseInfo.
        :rtype: str
        """
        return self._os_bit

    @os_bit.setter
    def os_bit(self, os_bit):
        r"""Sets the os_bit of this WtpProtectHostResponseInfo.

        操作系统位数

        :param os_bit: The os_bit of this WtpProtectHostResponseInfo.
        :type os_bit: str
        """
        self._os_bit = os_bit

    @property
    def os_type(self):
        r"""Gets the os_type of this WtpProtectHostResponseInfo.

        操作系统（linux，windows）

        :return: The os_type of this WtpProtectHostResponseInfo.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this WtpProtectHostResponseInfo.

        操作系统（linux，windows）

        :param os_type: The os_type of this WtpProtectHostResponseInfo.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def protect_status(self):
        r"""Gets the protect_status of this WtpProtectHostResponseInfo.

        防护状态   - opening : 正在开启   - opened : 防护中   - open_failed : 防护失败   - partial_protection : 部分防护   - protection_interruption : 防护中断

        :return: The protect_status of this WtpProtectHostResponseInfo.
        :rtype: str
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        r"""Sets the protect_status of this WtpProtectHostResponseInfo.

        防护状态   - opening : 正在开启   - opened : 防护中   - open_failed : 防护失败   - partial_protection : 部分防护   - protection_interruption : 防护中断

        :param protect_status: The protect_status of this WtpProtectHostResponseInfo.
        :type protect_status: str
        """
        self._protect_status = protect_status

    @property
    def rasp_protect_status(self):
        r"""Gets the rasp_protect_status of this WtpProtectHostResponseInfo.

        动态网页防篡改状态   - closed : 未开启   - opened : 防护中

        :return: The rasp_protect_status of this WtpProtectHostResponseInfo.
        :rtype: str
        """
        return self._rasp_protect_status

    @rasp_protect_status.setter
    def rasp_protect_status(self, rasp_protect_status):
        r"""Sets the rasp_protect_status of this WtpProtectHostResponseInfo.

        动态网页防篡改状态   - closed : 未开启   - opened : 防护中

        :param rasp_protect_status: The rasp_protect_status of this WtpProtectHostResponseInfo.
        :type rasp_protect_status: str
        """
        self._rasp_protect_status = rasp_protect_status

    @property
    def anti_tampering_times(self):
        r"""Gets the anti_tampering_times of this WtpProtectHostResponseInfo.

        已防御篡改攻击次数

        :return: The anti_tampering_times of this WtpProtectHostResponseInfo.
        :rtype: int
        """
        return self._anti_tampering_times

    @anti_tampering_times.setter
    def anti_tampering_times(self, anti_tampering_times):
        r"""Sets the anti_tampering_times of this WtpProtectHostResponseInfo.

        已防御篡改攻击次数

        :param anti_tampering_times: The anti_tampering_times of this WtpProtectHostResponseInfo.
        :type anti_tampering_times: int
        """
        self._anti_tampering_times = anti_tampering_times

    @property
    def detect_tampering_times(self):
        r"""Gets the detect_tampering_times of this WtpProtectHostResponseInfo.

        已发现篡改攻击

        :return: The detect_tampering_times of this WtpProtectHostResponseInfo.
        :rtype: int
        """
        return self._detect_tampering_times

    @detect_tampering_times.setter
    def detect_tampering_times(self, detect_tampering_times):
        r"""Sets the detect_tampering_times of this WtpProtectHostResponseInfo.

        已发现篡改攻击

        :param detect_tampering_times: The detect_tampering_times of this WtpProtectHostResponseInfo.
        :type detect_tampering_times: int
        """
        self._detect_tampering_times = detect_tampering_times

    @property
    def last_detect_time(self):
        r"""Gets the last_detect_time of this WtpProtectHostResponseInfo.

        最近检测时间(ms)

        :return: The last_detect_time of this WtpProtectHostResponseInfo.
        :rtype: int
        """
        return self._last_detect_time

    @last_detect_time.setter
    def last_detect_time(self, last_detect_time):
        r"""Sets the last_detect_time of this WtpProtectHostResponseInfo.

        最近检测时间(ms)

        :param last_detect_time: The last_detect_time of this WtpProtectHostResponseInfo.
        :type last_detect_time: int
        """
        self._last_detect_time = last_detect_time

    @property
    def scheduled_shutdown_status(self):
        r"""Gets the scheduled_shutdown_status of this WtpProtectHostResponseInfo.

        定时关闭防护开关状态   - opened : 开启   - closed : 未开启

        :return: The scheduled_shutdown_status of this WtpProtectHostResponseInfo.
        :rtype: str
        """
        return self._scheduled_shutdown_status

    @scheduled_shutdown_status.setter
    def scheduled_shutdown_status(self, scheduled_shutdown_status):
        r"""Sets the scheduled_shutdown_status of this WtpProtectHostResponseInfo.

        定时关闭防护开关状态   - opened : 开启   - closed : 未开启

        :param scheduled_shutdown_status: The scheduled_shutdown_status of this WtpProtectHostResponseInfo.
        :type scheduled_shutdown_status: str
        """
        self._scheduled_shutdown_status = scheduled_shutdown_status

    @property
    def os_name(self):
        r"""Gets the os_name of this WtpProtectHostResponseInfo.

        系统名称

        :return: The os_name of this WtpProtectHostResponseInfo.
        :rtype: str
        """
        return self._os_name

    @os_name.setter
    def os_name(self, os_name):
        r"""Sets the os_name of this WtpProtectHostResponseInfo.

        系统名称

        :param os_name: The os_name of this WtpProtectHostResponseInfo.
        :type os_name: str
        """
        self._os_name = os_name

    @property
    def os_version(self):
        r"""Gets the os_version of this WtpProtectHostResponseInfo.

        系统版本

        :return: The os_version of this WtpProtectHostResponseInfo.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        r"""Sets the os_version of this WtpProtectHostResponseInfo.

        系统版本

        :param os_version: The os_version of this WtpProtectHostResponseInfo.
        :type os_version: str
        """
        self._os_version = os_version

    @property
    def host_status(self):
        r"""Gets the host_status of this WtpProtectHostResponseInfo.

        服务器状态，包含如下4种。   - ACTIVE ：运行中。   - SHUTOFF ：关机。   - BUILDING ：创建中。   - ERROR ：故障。

        :return: The host_status of this WtpProtectHostResponseInfo.
        :rtype: str
        """
        return self._host_status

    @host_status.setter
    def host_status(self, host_status):
        r"""Sets the host_status of this WtpProtectHostResponseInfo.

        服务器状态，包含如下4种。   - ACTIVE ：运行中。   - SHUTOFF ：关机。   - BUILDING ：创建中。   - ERROR ：故障。

        :param host_status: The host_status of this WtpProtectHostResponseInfo.
        :type host_status: str
        """
        self._host_status = host_status

    @property
    def agent_status(self):
        r"""Gets the agent_status of this WtpProtectHostResponseInfo.

        Agent状态   - not_installed : agent未安装   - online : agent在线   - offline : agent不在线

        :return: The agent_status of this WtpProtectHostResponseInfo.
        :rtype: str
        """
        return self._agent_status

    @agent_status.setter
    def agent_status(self, agent_status):
        r"""Sets the agent_status of this WtpProtectHostResponseInfo.

        Agent状态   - not_installed : agent未安装   - online : agent在线   - offline : agent不在线

        :param agent_status: The agent_status of this WtpProtectHostResponseInfo.
        :type agent_status: str
        """
        self._agent_status = agent_status

    @property
    def protect_dir_num(self):
        r"""Gets the protect_dir_num of this WtpProtectHostResponseInfo.

        防护目录数

        :return: The protect_dir_num of this WtpProtectHostResponseInfo.
        :rtype: int
        """
        return self._protect_dir_num

    @protect_dir_num.setter
    def protect_dir_num(self, protect_dir_num):
        r"""Sets the protect_dir_num of this WtpProtectHostResponseInfo.

        防护目录数

        :param protect_dir_num: The protect_dir_num of this WtpProtectHostResponseInfo.
        :type protect_dir_num: int
        """
        self._protect_dir_num = protect_dir_num

    @property
    def remote_backbup_info(self):
        r"""Gets the remote_backbup_info of this WtpProtectHostResponseInfo.

        :return: The remote_backbup_info of this WtpProtectHostResponseInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.WtpRemoteBackupResponseInfo`
        """
        return self._remote_backbup_info

    @remote_backbup_info.setter
    def remote_backbup_info(self, remote_backbup_info):
        r"""Sets the remote_backbup_info of this WtpProtectHostResponseInfo.

        :param remote_backbup_info: The remote_backbup_info of this WtpProtectHostResponseInfo.
        :type remote_backbup_info: :class:`huaweicloudsdkhss.v5.WtpRemoteBackupResponseInfo`
        """
        self._remote_backbup_info = remote_backbup_info

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
