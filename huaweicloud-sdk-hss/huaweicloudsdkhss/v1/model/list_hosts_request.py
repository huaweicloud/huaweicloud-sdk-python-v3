# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHostsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version': 'str',
        'agent_status': 'str',
        'host_status': 'str',
        'protect_status': 'str',
        'detect_result': 'str',
        'host_name': 'str',
        'host_ip': 'str',
        'public_ip': 'str',
        'os_type': 'str',
        'charging_mode': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'version': 'version',
        'agent_status': 'agent_status',
        'host_status': 'host_status',
        'protect_status': 'protect_status',
        'detect_result': 'detect_result',
        'host_name': 'host_name',
        'host_ip': 'host_ip',
        'public_ip': 'public_ip',
        'os_type': 'os_type',
        'charging_mode': 'charging_mode',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, version=None, agent_status=None, host_status=None, protect_status=None, detect_result=None, host_name=None, host_ip=None, public_ip=None, os_type=None, charging_mode=None, limit=None, offset=None):
        """ListHostsRequest

        The model defined in huaweicloud sdk

        :param version: 主机开通的版本，包含如下5种输入。   - hss.version.null ：无。   - hss.version.basic ：基础版。   - hss.version.enterprise ：企业版。   - hss.version.premium ：旗舰版。   - hss.version.wtp ：网页防篡改版。
        :type version: str
        :param agent_status: Agent状态，包含如下3种。   - not_register ：未注册。   - online ：在线。   - offline ：离线。
        :type agent_status: str
        :param host_status: Agent状态，包含如下4种。   - ACTIVE ：正在运行。   - SHUTOFF ：关机。   - BUILDING ：创建中。   - ERROR ：故障。
        :type host_status: str
        :param protect_status: 防护状态，包含如下2种。   - closed ：关闭。   - opened ：开启。
        :type protect_status: str
        :param detect_result: 防护状态，包含如下3种。   - undetect ：未检测。   - clean ：无风险。   - risk ：有风险。
        :type detect_result: str
        :param host_name: 云主机名称
        :type host_name: str
        :param host_ip: 云主机私有IP
        :type host_ip: str
        :param public_ip: 云主机公网IP
        :type public_ip: str
        :param os_type: 操作系统类型
        :type os_type: str
        :param charging_mode: 收费模式，包含如下2种。   - packet_cycle ：包年/包月。   - on_demand ：按需。
        :type charging_mode: str
        :param limit: 默认10
        :type limit: int
        :param offset: 默认0
        :type offset: int
        """
        
        

        self._version = None
        self._agent_status = None
        self._host_status = None
        self._protect_status = None
        self._detect_result = None
        self._host_name = None
        self._host_ip = None
        self._public_ip = None
        self._os_type = None
        self._charging_mode = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if agent_status is not None:
            self.agent_status = agent_status
        if host_status is not None:
            self.host_status = host_status
        if protect_status is not None:
            self.protect_status = protect_status
        if detect_result is not None:
            self.detect_result = detect_result
        if host_name is not None:
            self.host_name = host_name
        if host_ip is not None:
            self.host_ip = host_ip
        if public_ip is not None:
            self.public_ip = public_ip
        if os_type is not None:
            self.os_type = os_type
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def version(self):
        """Gets the version of this ListHostsRequest.

        主机开通的版本，包含如下5种输入。   - hss.version.null ：无。   - hss.version.basic ：基础版。   - hss.version.enterprise ：企业版。   - hss.version.premium ：旗舰版。   - hss.version.wtp ：网页防篡改版。

        :return: The version of this ListHostsRequest.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ListHostsRequest.

        主机开通的版本，包含如下5种输入。   - hss.version.null ：无。   - hss.version.basic ：基础版。   - hss.version.enterprise ：企业版。   - hss.version.premium ：旗舰版。   - hss.version.wtp ：网页防篡改版。

        :param version: The version of this ListHostsRequest.
        :type version: str
        """
        self._version = version

    @property
    def agent_status(self):
        """Gets the agent_status of this ListHostsRequest.

        Agent状态，包含如下3种。   - not_register ：未注册。   - online ：在线。   - offline ：离线。

        :return: The agent_status of this ListHostsRequest.
        :rtype: str
        """
        return self._agent_status

    @agent_status.setter
    def agent_status(self, agent_status):
        """Sets the agent_status of this ListHostsRequest.

        Agent状态，包含如下3种。   - not_register ：未注册。   - online ：在线。   - offline ：离线。

        :param agent_status: The agent_status of this ListHostsRequest.
        :type agent_status: str
        """
        self._agent_status = agent_status

    @property
    def host_status(self):
        """Gets the host_status of this ListHostsRequest.

        Agent状态，包含如下4种。   - ACTIVE ：正在运行。   - SHUTOFF ：关机。   - BUILDING ：创建中。   - ERROR ：故障。

        :return: The host_status of this ListHostsRequest.
        :rtype: str
        """
        return self._host_status

    @host_status.setter
    def host_status(self, host_status):
        """Sets the host_status of this ListHostsRequest.

        Agent状态，包含如下4种。   - ACTIVE ：正在运行。   - SHUTOFF ：关机。   - BUILDING ：创建中。   - ERROR ：故障。

        :param host_status: The host_status of this ListHostsRequest.
        :type host_status: str
        """
        self._host_status = host_status

    @property
    def protect_status(self):
        """Gets the protect_status of this ListHostsRequest.

        防护状态，包含如下2种。   - closed ：关闭。   - opened ：开启。

        :return: The protect_status of this ListHostsRequest.
        :rtype: str
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        """Sets the protect_status of this ListHostsRequest.

        防护状态，包含如下2种。   - closed ：关闭。   - opened ：开启。

        :param protect_status: The protect_status of this ListHostsRequest.
        :type protect_status: str
        """
        self._protect_status = protect_status

    @property
    def detect_result(self):
        """Gets the detect_result of this ListHostsRequest.

        防护状态，包含如下3种。   - undetect ：未检测。   - clean ：无风险。   - risk ：有风险。

        :return: The detect_result of this ListHostsRequest.
        :rtype: str
        """
        return self._detect_result

    @detect_result.setter
    def detect_result(self, detect_result):
        """Sets the detect_result of this ListHostsRequest.

        防护状态，包含如下3种。   - undetect ：未检测。   - clean ：无风险。   - risk ：有风险。

        :param detect_result: The detect_result of this ListHostsRequest.
        :type detect_result: str
        """
        self._detect_result = detect_result

    @property
    def host_name(self):
        """Gets the host_name of this ListHostsRequest.

        云主机名称

        :return: The host_name of this ListHostsRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this ListHostsRequest.

        云主机名称

        :param host_name: The host_name of this ListHostsRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_ip(self):
        """Gets the host_ip of this ListHostsRequest.

        云主机私有IP

        :return: The host_ip of this ListHostsRequest.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        """Sets the host_ip of this ListHostsRequest.

        云主机私有IP

        :param host_ip: The host_ip of this ListHostsRequest.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def public_ip(self):
        """Gets the public_ip of this ListHostsRequest.

        云主机公网IP

        :return: The public_ip of this ListHostsRequest.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """Sets the public_ip of this ListHostsRequest.

        云主机公网IP

        :param public_ip: The public_ip of this ListHostsRequest.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def os_type(self):
        """Gets the os_type of this ListHostsRequest.

        操作系统类型

        :return: The os_type of this ListHostsRequest.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this ListHostsRequest.

        操作系统类型

        :param os_type: The os_type of this ListHostsRequest.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def charging_mode(self):
        """Gets the charging_mode of this ListHostsRequest.

        收费模式，包含如下2种。   - packet_cycle ：包年/包月。   - on_demand ：按需。

        :return: The charging_mode of this ListHostsRequest.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        """Sets the charging_mode of this ListHostsRequest.

        收费模式，包含如下2种。   - packet_cycle ：包年/包月。   - on_demand ：按需。

        :param charging_mode: The charging_mode of this ListHostsRequest.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def limit(self):
        """Gets the limit of this ListHostsRequest.

        默认10

        :return: The limit of this ListHostsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListHostsRequest.

        默认10

        :param limit: The limit of this ListHostsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListHostsRequest.

        默认0

        :return: The offset of this ListHostsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListHostsRequest.

        默认0

        :param offset: The offset of this ListHostsRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListHostsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
