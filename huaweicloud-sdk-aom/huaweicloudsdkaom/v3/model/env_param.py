# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EnvParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'component_id': 'str',
        'description': 'str',
        'env_name': 'str',
        'env_type': 'str',
        'os_type': 'str',
        'region': 'str',
        'register_type': 'str'
    }

    attribute_map = {
        'component_id': 'component_id',
        'description': 'description',
        'env_name': 'env_name',
        'env_type': 'env_type',
        'os_type': 'os_type',
        'region': 'region',
        'register_type': 'register_type'
    }

    def __init__(self, component_id=None, description=None, env_name=None, env_type=None, os_type=None, region=None, register_type=None):
        """EnvParam

        The model defined in huaweicloud sdk

        :param component_id: 环境关联组件id
        :type component_id: str
        :param description: 描述
        :type description: str
        :param env_name: 环境名称
        :type env_name: str
        :param env_type: 环境类型，取值：DEV、TEST、PRE、ONLINE
        :type env_type: str
        :param os_type: OS类型，取值：LINUX、WINDOWS
        :type os_type: str
        :param region: 环境关联region
        :type region: str
        :param register_type: 注册类型，取值：API、SERVICE_DISCOVERY、CONSOLE，默认值：API
        :type register_type: str
        """
        
        

        self._component_id = None
        self._description = None
        self._env_name = None
        self._env_type = None
        self._os_type = None
        self._region = None
        self._register_type = None
        self.discriminator = None

        if component_id is not None:
            self.component_id = component_id
        if description is not None:
            self.description = description
        self.env_name = env_name
        self.env_type = env_type
        if os_type is not None:
            self.os_type = os_type
        self.region = region
        if register_type is not None:
            self.register_type = register_type

    @property
    def component_id(self):
        """Gets the component_id of this EnvParam.

        环境关联组件id

        :return: The component_id of this EnvParam.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        """Sets the component_id of this EnvParam.

        环境关联组件id

        :param component_id: The component_id of this EnvParam.
        :type component_id: str
        """
        self._component_id = component_id

    @property
    def description(self):
        """Gets the description of this EnvParam.

        描述

        :return: The description of this EnvParam.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EnvParam.

        描述

        :param description: The description of this EnvParam.
        :type description: str
        """
        self._description = description

    @property
    def env_name(self):
        """Gets the env_name of this EnvParam.

        环境名称

        :return: The env_name of this EnvParam.
        :rtype: str
        """
        return self._env_name

    @env_name.setter
    def env_name(self, env_name):
        """Sets the env_name of this EnvParam.

        环境名称

        :param env_name: The env_name of this EnvParam.
        :type env_name: str
        """
        self._env_name = env_name

    @property
    def env_type(self):
        """Gets the env_type of this EnvParam.

        环境类型，取值：DEV、TEST、PRE、ONLINE

        :return: The env_type of this EnvParam.
        :rtype: str
        """
        return self._env_type

    @env_type.setter
    def env_type(self, env_type):
        """Sets the env_type of this EnvParam.

        环境类型，取值：DEV、TEST、PRE、ONLINE

        :param env_type: The env_type of this EnvParam.
        :type env_type: str
        """
        self._env_type = env_type

    @property
    def os_type(self):
        """Gets the os_type of this EnvParam.

        OS类型，取值：LINUX、WINDOWS

        :return: The os_type of this EnvParam.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this EnvParam.

        OS类型，取值：LINUX、WINDOWS

        :param os_type: The os_type of this EnvParam.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def region(self):
        """Gets the region of this EnvParam.

        环境关联region

        :return: The region of this EnvParam.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this EnvParam.

        环境关联region

        :param region: The region of this EnvParam.
        :type region: str
        """
        self._region = region

    @property
    def register_type(self):
        """Gets the register_type of this EnvParam.

        注册类型，取值：API、SERVICE_DISCOVERY、CONSOLE，默认值：API

        :return: The register_type of this EnvParam.
        :rtype: str
        """
        return self._register_type

    @register_type.setter
    def register_type(self, register_type):
        """Sets the register_type of this EnvParam.

        注册类型，取值：API、SERVICE_DISCOVERY、CONSOLE，默认值：API

        :param register_type: The register_type of this EnvParam.
        :type register_type: str
        """
        self._register_type = register_type

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
        if not isinstance(other, EnvParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
