# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CloseProtectionInfoRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_id_list': 'list[str]',
        'agent_id_list': 'list[str]',
        'close_protection_type': 'str'
    }

    attribute_map = {
        'host_id_list': 'host_id_list',
        'agent_id_list': 'agent_id_list',
        'close_protection_type': 'close_protection_type'
    }

    def __init__(self, host_id_list=None, agent_id_list=None, close_protection_type=None):
        r"""CloseProtectionInfoRequestInfo

        The model defined in huaweicloud sdk

        :param host_id_list: **参数解释**: 需要关闭勒索防护的主机ID列表，您可以通过[查询勒索防护服务器列表](ListProtectionServer.xml)接口获取HostID。 **约束限制**: 不涉及 **取值范围**: 列表条数0-64 **默认取值**: 不涉及 
        :type host_id_list: list[str]
        :param agent_id_list: **参数解释**: 需要关闭勒索防护的agentID列表，您可以通过[查询勒索防护服务器列表](ListProtectionServer.xml)接口获取AgentID。 **约束限制**: 不涉及 **取值范围**: 列表条数0-64 **默认取值**: 不涉及 
        :type agent_id_list: list[str]
        :param close_protection_type: **参数解释**: 关闭防护类型  **约束限制**: 不涉及 **取值范围**: - close_anti : 关闭勒索防护；暂不支持关闭备份防护，若需要解绑存储库，请前往cbr服务进行操作。 **默认取值**: 不涉及
        :type close_protection_type: str
        """
        
        

        self._host_id_list = None
        self._agent_id_list = None
        self._close_protection_type = None
        self.discriminator = None

        self.host_id_list = host_id_list
        self.agent_id_list = agent_id_list
        self.close_protection_type = close_protection_type

    @property
    def host_id_list(self):
        r"""Gets the host_id_list of this CloseProtectionInfoRequestInfo.

        **参数解释**: 需要关闭勒索防护的主机ID列表，您可以通过[查询勒索防护服务器列表](ListProtectionServer.xml)接口获取HostID。 **约束限制**: 不涉及 **取值范围**: 列表条数0-64 **默认取值**: 不涉及 

        :return: The host_id_list of this CloseProtectionInfoRequestInfo.
        :rtype: list[str]
        """
        return self._host_id_list

    @host_id_list.setter
    def host_id_list(self, host_id_list):
        r"""Sets the host_id_list of this CloseProtectionInfoRequestInfo.

        **参数解释**: 需要关闭勒索防护的主机ID列表，您可以通过[查询勒索防护服务器列表](ListProtectionServer.xml)接口获取HostID。 **约束限制**: 不涉及 **取值范围**: 列表条数0-64 **默认取值**: 不涉及 

        :param host_id_list: The host_id_list of this CloseProtectionInfoRequestInfo.
        :type host_id_list: list[str]
        """
        self._host_id_list = host_id_list

    @property
    def agent_id_list(self):
        r"""Gets the agent_id_list of this CloseProtectionInfoRequestInfo.

        **参数解释**: 需要关闭勒索防护的agentID列表，您可以通过[查询勒索防护服务器列表](ListProtectionServer.xml)接口获取AgentID。 **约束限制**: 不涉及 **取值范围**: 列表条数0-64 **默认取值**: 不涉及 

        :return: The agent_id_list of this CloseProtectionInfoRequestInfo.
        :rtype: list[str]
        """
        return self._agent_id_list

    @agent_id_list.setter
    def agent_id_list(self, agent_id_list):
        r"""Sets the agent_id_list of this CloseProtectionInfoRequestInfo.

        **参数解释**: 需要关闭勒索防护的agentID列表，您可以通过[查询勒索防护服务器列表](ListProtectionServer.xml)接口获取AgentID。 **约束限制**: 不涉及 **取值范围**: 列表条数0-64 **默认取值**: 不涉及 

        :param agent_id_list: The agent_id_list of this CloseProtectionInfoRequestInfo.
        :type agent_id_list: list[str]
        """
        self._agent_id_list = agent_id_list

    @property
    def close_protection_type(self):
        r"""Gets the close_protection_type of this CloseProtectionInfoRequestInfo.

        **参数解释**: 关闭防护类型  **约束限制**: 不涉及 **取值范围**: - close_anti : 关闭勒索防护；暂不支持关闭备份防护，若需要解绑存储库，请前往cbr服务进行操作。 **默认取值**: 不涉及

        :return: The close_protection_type of this CloseProtectionInfoRequestInfo.
        :rtype: str
        """
        return self._close_protection_type

    @close_protection_type.setter
    def close_protection_type(self, close_protection_type):
        r"""Sets the close_protection_type of this CloseProtectionInfoRequestInfo.

        **参数解释**: 关闭防护类型  **约束限制**: 不涉及 **取值范围**: - close_anti : 关闭勒索防护；暂不支持关闭备份防护，若需要解绑存储库，请前往cbr服务进行操作。 **默认取值**: 不涉及

        :param close_protection_type: The close_protection_type of this CloseProtectionInfoRequestInfo.
        :type close_protection_type: str
        """
        self._close_protection_type = close_protection_type

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
        if not isinstance(other, CloseProtectionInfoRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
