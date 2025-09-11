# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAuditDbAgentRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'agent_id': 'str',
        'body': 'AgentEditRequest'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'agent_id': 'agent_id',
        'body': 'body'
    }

    def __init__(self, instance_id=None, agent_id=None, body=None):
        r"""CreateAuditDbAgentRequest

        The model defined in huaweicloud sdk

        :param instance_id: **参数解释**： 实例ID。可通过查询实例列表接口ID字段获取 **约束限制**： 不涉及 **取值范围**： 以查询实例列表接口值为准，字符长度32-64。 **默认取值**： 不涉及 
        :type instance_id: str
        :param agent_id: **参数解释**： 审计Agent ID。可通过获取agent列表接口agent_id字段获取 **约束限制**： 不涉及 **取值范围**： 以获取agent列表接口agent_id值为准，字符长度16-64。 **默认取值**： 不涉及 
        :type agent_id: str
        :param body: Body of the CreateAuditDbAgentRequest
        :type body: :class:`huaweicloudsdkdbss.v1.AgentEditRequest`
        """
        
        

        self._instance_id = None
        self._agent_id = None
        self._body = None
        self.discriminator = None

        self.instance_id = instance_id
        self.agent_id = agent_id
        if body is not None:
            self.body = body

    @property
    def instance_id(self):
        r"""Gets the instance_id of this CreateAuditDbAgentRequest.

        **参数解释**： 实例ID。可通过查询实例列表接口ID字段获取 **约束限制**： 不涉及 **取值范围**： 以查询实例列表接口值为准，字符长度32-64。 **默认取值**： 不涉及 

        :return: The instance_id of this CreateAuditDbAgentRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this CreateAuditDbAgentRequest.

        **参数解释**： 实例ID。可通过查询实例列表接口ID字段获取 **约束限制**： 不涉及 **取值范围**： 以查询实例列表接口值为准，字符长度32-64。 **默认取值**： 不涉及 

        :param instance_id: The instance_id of this CreateAuditDbAgentRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def agent_id(self):
        r"""Gets the agent_id of this CreateAuditDbAgentRequest.

        **参数解释**： 审计Agent ID。可通过获取agent列表接口agent_id字段获取 **约束限制**： 不涉及 **取值范围**： 以获取agent列表接口agent_id值为准，字符长度16-64。 **默认取值**： 不涉及 

        :return: The agent_id of this CreateAuditDbAgentRequest.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this CreateAuditDbAgentRequest.

        **参数解释**： 审计Agent ID。可通过获取agent列表接口agent_id字段获取 **约束限制**： 不涉及 **取值范围**： 以获取agent列表接口agent_id值为准，字符长度16-64。 **默认取值**： 不涉及 

        :param agent_id: The agent_id of this CreateAuditDbAgentRequest.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def body(self):
        r"""Gets the body of this CreateAuditDbAgentRequest.

        :return: The body of this CreateAuditDbAgentRequest.
        :rtype: :class:`huaweicloudsdkdbss.v1.AgentEditRequest`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CreateAuditDbAgentRequest.

        :param body: The body of this CreateAuditDbAgentRequest.
        :type body: :class:`huaweicloudsdkdbss.v1.AgentEditRequest`
        """
        self._body = body

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
        if not isinstance(other, CreateAuditDbAgentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
