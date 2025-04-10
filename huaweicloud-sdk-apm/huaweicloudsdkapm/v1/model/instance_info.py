# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'int',
        'business_name': 'str',
        'business_id': 'int',
        'app_name': 'str',
        'host_name': 'str',
        'instance_name': 'str',
        'ip_address': 'str',
        'env_id': 'int',
        'agent_version': 'str',
        'last_heartbeat': 'int',
        'register_time': 'int',
        'last_modify_user_id': 'str',
        'instance_status': 'int',
        'last_modify_user_name': 'str',
        'last_modify_time': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'business_name': 'business_name',
        'business_id': 'business_id',
        'app_name': 'app_name',
        'host_name': 'host_name',
        'instance_name': 'instance_name',
        'ip_address': 'ip_address',
        'env_id': 'env_id',
        'agent_version': 'agent_version',
        'last_heartbeat': 'last_heartbeat',
        'register_time': 'register_time',
        'last_modify_user_id': 'last_modify_user_id',
        'instance_status': 'instance_status',
        'last_modify_user_name': 'last_modify_user_name',
        'last_modify_time': 'last_modify_time'
    }

    def __init__(self, instance_id=None, business_name=None, business_id=None, app_name=None, host_name=None, instance_name=None, ip_address=None, env_id=None, agent_version=None, last_heartbeat=None, register_time=None, last_modify_user_id=None, instance_status=None, last_modify_user_name=None, last_modify_time=None):
        r"""InstanceInfo

        The model defined in huaweicloud sdk

        :param instance_id: 实例id。
        :type instance_id: int
        :param business_name: 应用名称。
        :type business_name: str
        :param business_id: 应用id。
        :type business_id: int
        :param app_name: 组件名称。
        :type app_name: str
        :param host_name: 主机名称。
        :type host_name: str
        :param instance_name: 实例名称。
        :type instance_name: str
        :param ip_address: 主机ip地址。
        :type ip_address: str
        :param env_id: 环境ID。
        :type env_id: int
        :param agent_version: Javaagent版本。
        :type agent_version: str
        :param last_heartbeat: 最后心跳时间。
        :type last_heartbeat: int
        :param register_time: 注册时间。
        :type register_time: int
        :param last_modify_user_id: 最后修改用户id。
        :type last_modify_user_id: str
        :param instance_status: 实例状态。
        :type instance_status: int
        :param last_modify_user_name: 最后修改用户名称。
        :type last_modify_user_name: str
        :param last_modify_time: 最后修改时间。
        :type last_modify_time: int
        """
        
        

        self._instance_id = None
        self._business_name = None
        self._business_id = None
        self._app_name = None
        self._host_name = None
        self._instance_name = None
        self._ip_address = None
        self._env_id = None
        self._agent_version = None
        self._last_heartbeat = None
        self._register_time = None
        self._last_modify_user_id = None
        self._instance_status = None
        self._last_modify_user_name = None
        self._last_modify_time = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if business_name is not None:
            self.business_name = business_name
        if business_id is not None:
            self.business_id = business_id
        if app_name is not None:
            self.app_name = app_name
        if host_name is not None:
            self.host_name = host_name
        if instance_name is not None:
            self.instance_name = instance_name
        if ip_address is not None:
            self.ip_address = ip_address
        if env_id is not None:
            self.env_id = env_id
        if agent_version is not None:
            self.agent_version = agent_version
        if last_heartbeat is not None:
            self.last_heartbeat = last_heartbeat
        if register_time is not None:
            self.register_time = register_time
        if last_modify_user_id is not None:
            self.last_modify_user_id = last_modify_user_id
        if instance_status is not None:
            self.instance_status = instance_status
        if last_modify_user_name is not None:
            self.last_modify_user_name = last_modify_user_name
        if last_modify_time is not None:
            self.last_modify_time = last_modify_time

    @property
    def instance_id(self):
        r"""Gets the instance_id of this InstanceInfo.

        实例id。

        :return: The instance_id of this InstanceInfo.
        :rtype: int
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this InstanceInfo.

        实例id。

        :param instance_id: The instance_id of this InstanceInfo.
        :type instance_id: int
        """
        self._instance_id = instance_id

    @property
    def business_name(self):
        r"""Gets the business_name of this InstanceInfo.

        应用名称。

        :return: The business_name of this InstanceInfo.
        :rtype: str
        """
        return self._business_name

    @business_name.setter
    def business_name(self, business_name):
        r"""Sets the business_name of this InstanceInfo.

        应用名称。

        :param business_name: The business_name of this InstanceInfo.
        :type business_name: str
        """
        self._business_name = business_name

    @property
    def business_id(self):
        r"""Gets the business_id of this InstanceInfo.

        应用id。

        :return: The business_id of this InstanceInfo.
        :rtype: int
        """
        return self._business_id

    @business_id.setter
    def business_id(self, business_id):
        r"""Sets the business_id of this InstanceInfo.

        应用id。

        :param business_id: The business_id of this InstanceInfo.
        :type business_id: int
        """
        self._business_id = business_id

    @property
    def app_name(self):
        r"""Gets the app_name of this InstanceInfo.

        组件名称。

        :return: The app_name of this InstanceInfo.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this InstanceInfo.

        组件名称。

        :param app_name: The app_name of this InstanceInfo.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def host_name(self):
        r"""Gets the host_name of this InstanceInfo.

        主机名称。

        :return: The host_name of this InstanceInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this InstanceInfo.

        主机名称。

        :param host_name: The host_name of this InstanceInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def instance_name(self):
        r"""Gets the instance_name of this InstanceInfo.

        实例名称。

        :return: The instance_name of this InstanceInfo.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this InstanceInfo.

        实例名称。

        :param instance_name: The instance_name of this InstanceInfo.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def ip_address(self):
        r"""Gets the ip_address of this InstanceInfo.

        主机ip地址。

        :return: The ip_address of this InstanceInfo.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        r"""Sets the ip_address of this InstanceInfo.

        主机ip地址。

        :param ip_address: The ip_address of this InstanceInfo.
        :type ip_address: str
        """
        self._ip_address = ip_address

    @property
    def env_id(self):
        r"""Gets the env_id of this InstanceInfo.

        环境ID。

        :return: The env_id of this InstanceInfo.
        :rtype: int
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        r"""Sets the env_id of this InstanceInfo.

        环境ID。

        :param env_id: The env_id of this InstanceInfo.
        :type env_id: int
        """
        self._env_id = env_id

    @property
    def agent_version(self):
        r"""Gets the agent_version of this InstanceInfo.

        Javaagent版本。

        :return: The agent_version of this InstanceInfo.
        :rtype: str
        """
        return self._agent_version

    @agent_version.setter
    def agent_version(self, agent_version):
        r"""Sets the agent_version of this InstanceInfo.

        Javaagent版本。

        :param agent_version: The agent_version of this InstanceInfo.
        :type agent_version: str
        """
        self._agent_version = agent_version

    @property
    def last_heartbeat(self):
        r"""Gets the last_heartbeat of this InstanceInfo.

        最后心跳时间。

        :return: The last_heartbeat of this InstanceInfo.
        :rtype: int
        """
        return self._last_heartbeat

    @last_heartbeat.setter
    def last_heartbeat(self, last_heartbeat):
        r"""Sets the last_heartbeat of this InstanceInfo.

        最后心跳时间。

        :param last_heartbeat: The last_heartbeat of this InstanceInfo.
        :type last_heartbeat: int
        """
        self._last_heartbeat = last_heartbeat

    @property
    def register_time(self):
        r"""Gets the register_time of this InstanceInfo.

        注册时间。

        :return: The register_time of this InstanceInfo.
        :rtype: int
        """
        return self._register_time

    @register_time.setter
    def register_time(self, register_time):
        r"""Sets the register_time of this InstanceInfo.

        注册时间。

        :param register_time: The register_time of this InstanceInfo.
        :type register_time: int
        """
        self._register_time = register_time

    @property
    def last_modify_user_id(self):
        r"""Gets the last_modify_user_id of this InstanceInfo.

        最后修改用户id。

        :return: The last_modify_user_id of this InstanceInfo.
        :rtype: str
        """
        return self._last_modify_user_id

    @last_modify_user_id.setter
    def last_modify_user_id(self, last_modify_user_id):
        r"""Sets the last_modify_user_id of this InstanceInfo.

        最后修改用户id。

        :param last_modify_user_id: The last_modify_user_id of this InstanceInfo.
        :type last_modify_user_id: str
        """
        self._last_modify_user_id = last_modify_user_id

    @property
    def instance_status(self):
        r"""Gets the instance_status of this InstanceInfo.

        实例状态。

        :return: The instance_status of this InstanceInfo.
        :rtype: int
        """
        return self._instance_status

    @instance_status.setter
    def instance_status(self, instance_status):
        r"""Sets the instance_status of this InstanceInfo.

        实例状态。

        :param instance_status: The instance_status of this InstanceInfo.
        :type instance_status: int
        """
        self._instance_status = instance_status

    @property
    def last_modify_user_name(self):
        r"""Gets the last_modify_user_name of this InstanceInfo.

        最后修改用户名称。

        :return: The last_modify_user_name of this InstanceInfo.
        :rtype: str
        """
        return self._last_modify_user_name

    @last_modify_user_name.setter
    def last_modify_user_name(self, last_modify_user_name):
        r"""Sets the last_modify_user_name of this InstanceInfo.

        最后修改用户名称。

        :param last_modify_user_name: The last_modify_user_name of this InstanceInfo.
        :type last_modify_user_name: str
        """
        self._last_modify_user_name = last_modify_user_name

    @property
    def last_modify_time(self):
        r"""Gets the last_modify_time of this InstanceInfo.

        最后修改时间。

        :return: The last_modify_time of this InstanceInfo.
        :rtype: int
        """
        return self._last_modify_time

    @last_modify_time.setter
    def last_modify_time(self, last_modify_time):
        r"""Sets the last_modify_time of this InstanceInfo.

        最后修改时间。

        :param last_modify_time: The last_modify_time of this InstanceInfo.
        :type last_modify_time: int
        """
        self._last_modify_time = last_modify_time

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
        if not isinstance(other, InstanceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
