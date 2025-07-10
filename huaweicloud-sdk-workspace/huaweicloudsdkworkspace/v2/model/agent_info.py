# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AgentInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agent_name': 'str',
        'agent_version': 'str',
        'is_installed': 'bool'
    }

    attribute_map = {
        'agent_name': 'agent_name',
        'agent_version': 'agent_version',
        'is_installed': 'is_installed'
    }

    def __init__(self, agent_name=None, agent_version=None, is_installed=None):
        r"""AgentInfo

        The model defined in huaweicloud sdk

        :param agent_name: 插件名称。
        :type agent_name: str
        :param agent_version: 插件版本。
        :type agent_version: str
        :param is_installed: 是否安装插件（是否）。
        :type is_installed: bool
        """
        
        

        self._agent_name = None
        self._agent_version = None
        self._is_installed = None
        self.discriminator = None

        if agent_name is not None:
            self.agent_name = agent_name
        if agent_version is not None:
            self.agent_version = agent_version
        if is_installed is not None:
            self.is_installed = is_installed

    @property
    def agent_name(self):
        r"""Gets the agent_name of this AgentInfo.

        插件名称。

        :return: The agent_name of this AgentInfo.
        :rtype: str
        """
        return self._agent_name

    @agent_name.setter
    def agent_name(self, agent_name):
        r"""Sets the agent_name of this AgentInfo.

        插件名称。

        :param agent_name: The agent_name of this AgentInfo.
        :type agent_name: str
        """
        self._agent_name = agent_name

    @property
    def agent_version(self):
        r"""Gets the agent_version of this AgentInfo.

        插件版本。

        :return: The agent_version of this AgentInfo.
        :rtype: str
        """
        return self._agent_version

    @agent_version.setter
    def agent_version(self, agent_version):
        r"""Sets the agent_version of this AgentInfo.

        插件版本。

        :param agent_version: The agent_version of this AgentInfo.
        :type agent_version: str
        """
        self._agent_version = agent_version

    @property
    def is_installed(self):
        r"""Gets the is_installed of this AgentInfo.

        是否安装插件（是否）。

        :return: The is_installed of this AgentInfo.
        :rtype: bool
        """
        return self._is_installed

    @is_installed.setter
    def is_installed(self, is_installed):
        r"""Sets the is_installed of this AgentInfo.

        是否安装插件（是否）。

        :param is_installed: The is_installed of this AgentInfo.
        :type is_installed: bool
        """
        self._is_installed = is_installed

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
        if not isinstance(other, AgentInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
