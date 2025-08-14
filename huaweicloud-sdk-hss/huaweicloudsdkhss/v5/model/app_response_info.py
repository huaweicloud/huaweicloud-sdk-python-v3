# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agent_id': 'str',
        'host_id': 'str',
        'host_name': 'str',
        'host_ip': 'str',
        'app_name': 'str',
        'version': 'str',
        'update_time': 'int',
        'recent_scan_time': 'int',
        'container_id': 'str',
        'container_name': 'str'
    }

    attribute_map = {
        'agent_id': 'agent_id',
        'host_id': 'host_id',
        'host_name': 'host_name',
        'host_ip': 'host_ip',
        'app_name': 'app_name',
        'version': 'version',
        'update_time': 'update_time',
        'recent_scan_time': 'recent_scan_time',
        'container_id': 'container_id',
        'container_name': 'container_name'
    }

    def __init__(self, agent_id=None, host_id=None, host_name=None, host_ip=None, app_name=None, version=None, update_time=None, recent_scan_time=None, container_id=None, container_name=None):
        r"""AppResponseInfo

        The model defined in huaweicloud sdk

        :param agent_id: **参数解释**: Agent ID **取值范围**: 字符长度1-64位 
        :type agent_id: str
        :param host_id: **参数解释**： 主机ID **取值范围**： 字符长度1-64位 
        :type host_id: str
        :param host_name: **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 
        :type host_name: str
        :param host_ip: **参数解释**: 主机IP **取值范围**: 字符长度1-128位 
        :type host_ip: str
        :param app_name: **参数解释**: 软件名称 **取值范围**: 字符长度1-256位 
        :type app_name: str
        :param version: **参数解释**: 版本号 **取值范围**: 字符长度1-128位 
        :type version: str
        :param update_time: **参数解释**: 更新时间，最近一次更新的时间，用毫秒表示 **取值范围**: 最小值0，最大值9223372036854775807 
        :type update_time: int
        :param recent_scan_time: **参数解释**: 最近扫描时间，用毫秒表示 **取值范围**: 最小值0，最大值9223372036854775807 
        :type recent_scan_time: int
        :param container_id: **参数解释**: 容器ID **取值范围**: 字符长度1-128位 
        :type container_id: str
        :param container_name: **参数解释**： 容器实例名称，只有容器类型的告警有 **取值范围**： 字符长度1-256位 
        :type container_name: str
        """
        
        

        self._agent_id = None
        self._host_id = None
        self._host_name = None
        self._host_ip = None
        self._app_name = None
        self._version = None
        self._update_time = None
        self._recent_scan_time = None
        self._container_id = None
        self._container_name = None
        self.discriminator = None

        if agent_id is not None:
            self.agent_id = agent_id
        if host_id is not None:
            self.host_id = host_id
        if host_name is not None:
            self.host_name = host_name
        if host_ip is not None:
            self.host_ip = host_ip
        if app_name is not None:
            self.app_name = app_name
        if version is not None:
            self.version = version
        if update_time is not None:
            self.update_time = update_time
        if recent_scan_time is not None:
            self.recent_scan_time = recent_scan_time
        if container_id is not None:
            self.container_id = container_id
        if container_name is not None:
            self.container_name = container_name

    @property
    def agent_id(self):
        r"""Gets the agent_id of this AppResponseInfo.

        **参数解释**: Agent ID **取值范围**: 字符长度1-64位 

        :return: The agent_id of this AppResponseInfo.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this AppResponseInfo.

        **参数解释**: Agent ID **取值范围**: 字符长度1-64位 

        :param agent_id: The agent_id of this AppResponseInfo.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def host_id(self):
        r"""Gets the host_id of this AppResponseInfo.

        **参数解释**： 主机ID **取值范围**： 字符长度1-64位 

        :return: The host_id of this AppResponseInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this AppResponseInfo.

        **参数解释**： 主机ID **取值范围**： 字符长度1-64位 

        :param host_id: The host_id of this AppResponseInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        r"""Gets the host_name of this AppResponseInfo.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 

        :return: The host_name of this AppResponseInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this AppResponseInfo.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 

        :param host_name: The host_name of this AppResponseInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_ip(self):
        r"""Gets the host_ip of this AppResponseInfo.

        **参数解释**: 主机IP **取值范围**: 字符长度1-128位 

        :return: The host_ip of this AppResponseInfo.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        r"""Sets the host_ip of this AppResponseInfo.

        **参数解释**: 主机IP **取值范围**: 字符长度1-128位 

        :param host_ip: The host_ip of this AppResponseInfo.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def app_name(self):
        r"""Gets the app_name of this AppResponseInfo.

        **参数解释**: 软件名称 **取值范围**: 字符长度1-256位 

        :return: The app_name of this AppResponseInfo.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this AppResponseInfo.

        **参数解释**: 软件名称 **取值范围**: 字符长度1-256位 

        :param app_name: The app_name of this AppResponseInfo.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def version(self):
        r"""Gets the version of this AppResponseInfo.

        **参数解释**: 版本号 **取值范围**: 字符长度1-128位 

        :return: The version of this AppResponseInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this AppResponseInfo.

        **参数解释**: 版本号 **取值范围**: 字符长度1-128位 

        :param version: The version of this AppResponseInfo.
        :type version: str
        """
        self._version = version

    @property
    def update_time(self):
        r"""Gets the update_time of this AppResponseInfo.

        **参数解释**: 更新时间，最近一次更新的时间，用毫秒表示 **取值范围**: 最小值0，最大值9223372036854775807 

        :return: The update_time of this AppResponseInfo.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this AppResponseInfo.

        **参数解释**: 更新时间，最近一次更新的时间，用毫秒表示 **取值范围**: 最小值0，最大值9223372036854775807 

        :param update_time: The update_time of this AppResponseInfo.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def recent_scan_time(self):
        r"""Gets the recent_scan_time of this AppResponseInfo.

        **参数解释**: 最近扫描时间，用毫秒表示 **取值范围**: 最小值0，最大值9223372036854775807 

        :return: The recent_scan_time of this AppResponseInfo.
        :rtype: int
        """
        return self._recent_scan_time

    @recent_scan_time.setter
    def recent_scan_time(self, recent_scan_time):
        r"""Sets the recent_scan_time of this AppResponseInfo.

        **参数解释**: 最近扫描时间，用毫秒表示 **取值范围**: 最小值0，最大值9223372036854775807 

        :param recent_scan_time: The recent_scan_time of this AppResponseInfo.
        :type recent_scan_time: int
        """
        self._recent_scan_time = recent_scan_time

    @property
    def container_id(self):
        r"""Gets the container_id of this AppResponseInfo.

        **参数解释**: 容器ID **取值范围**: 字符长度1-128位 

        :return: The container_id of this AppResponseInfo.
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        r"""Sets the container_id of this AppResponseInfo.

        **参数解释**: 容器ID **取值范围**: 字符长度1-128位 

        :param container_id: The container_id of this AppResponseInfo.
        :type container_id: str
        """
        self._container_id = container_id

    @property
    def container_name(self):
        r"""Gets the container_name of this AppResponseInfo.

        **参数解释**： 容器实例名称，只有容器类型的告警有 **取值范围**： 字符长度1-256位 

        :return: The container_name of this AppResponseInfo.
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        r"""Sets the container_name of this AppResponseInfo.

        **参数解释**： 容器实例名称，只有容器类型的告警有 **取值范围**： 字符长度1-256位 

        :param container_name: The container_name of this AppResponseInfo.
        :type container_name: str
        """
        self._container_name = container_name

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
        if not isinstance(other, AppResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
