# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AgentUpgradeParam:

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
        'agent_list': 'list[SingleAgentParam]'
    }

    attribute_map = {
        'version': 'version',
        'agent_list': 'agent_list'
    }

    def __init__(self, version=None, agent_list=None):
        r"""AgentUpgradeParam

        The model defined in huaweicloud sdk

        :param version: UniAgent升级的版本号。
        :type version: str
        :param agent_list: UniAgent主机列表信息。
        :type agent_list: list[:class:`huaweicloudsdkaom.v4.SingleAgentParam`]
        """
        
        

        self._version = None
        self._agent_list = None
        self.discriminator = None

        self.version = version
        self.agent_list = agent_list

    @property
    def version(self):
        r"""Gets the version of this AgentUpgradeParam.

        UniAgent升级的版本号。

        :return: The version of this AgentUpgradeParam.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this AgentUpgradeParam.

        UniAgent升级的版本号。

        :param version: The version of this AgentUpgradeParam.
        :type version: str
        """
        self._version = version

    @property
    def agent_list(self):
        r"""Gets the agent_list of this AgentUpgradeParam.

        UniAgent主机列表信息。

        :return: The agent_list of this AgentUpgradeParam.
        :rtype: list[:class:`huaweicloudsdkaom.v4.SingleAgentParam`]
        """
        return self._agent_list

    @agent_list.setter
    def agent_list(self, agent_list):
        r"""Sets the agent_list of this AgentUpgradeParam.

        UniAgent主机列表信息。

        :param agent_list: The agent_list of this AgentUpgradeParam.
        :type agent_list: list[:class:`huaweicloudsdkaom.v4.SingleAgentParam`]
        """
        self._agent_list = agent_list

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
        if not isinstance(other, AgentUpgradeParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
