# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MasterEIPResponseSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'spec': 'MasterEIPResponseSpecSpec',
        'elastic_ip': 'str'
    }

    attribute_map = {
        'action': 'action',
        'spec': 'spec',
        'elastic_ip': 'elasticIp'
    }

    def __init__(self, action=None, spec=None, elastic_ip=None):
        r"""MasterEIPResponseSpec

        The model defined in huaweicloud sdk

        :param action: **参数解释**： 绑定动作 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type action: str
        :param spec: 
        :type spec: :class:`huaweicloudsdkcce.v3.MasterEIPResponseSpecSpec`
        :param elastic_ip: **参数解释**： 弹性公网IP **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type elastic_ip: str
        """
        
        

        self._action = None
        self._spec = None
        self._elastic_ip = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if spec is not None:
            self.spec = spec
        if elastic_ip is not None:
            self.elastic_ip = elastic_ip

    @property
    def action(self):
        r"""Gets the action of this MasterEIPResponseSpec.

        **参数解释**： 绑定动作 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The action of this MasterEIPResponseSpec.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this MasterEIPResponseSpec.

        **参数解释**： 绑定动作 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param action: The action of this MasterEIPResponseSpec.
        :type action: str
        """
        self._action = action

    @property
    def spec(self):
        r"""Gets the spec of this MasterEIPResponseSpec.

        :return: The spec of this MasterEIPResponseSpec.
        :rtype: :class:`huaweicloudsdkcce.v3.MasterEIPResponseSpecSpec`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        r"""Sets the spec of this MasterEIPResponseSpec.

        :param spec: The spec of this MasterEIPResponseSpec.
        :type spec: :class:`huaweicloudsdkcce.v3.MasterEIPResponseSpecSpec`
        """
        self._spec = spec

    @property
    def elastic_ip(self):
        r"""Gets the elastic_ip of this MasterEIPResponseSpec.

        **参数解释**： 弹性公网IP **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The elastic_ip of this MasterEIPResponseSpec.
        :rtype: str
        """
        return self._elastic_ip

    @elastic_ip.setter
    def elastic_ip(self, elastic_ip):
        r"""Sets the elastic_ip of this MasterEIPResponseSpec.

        **参数解释**： 弹性公网IP **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param elastic_ip: The elastic_ip of this MasterEIPResponseSpec.
        :type elastic_ip: str
        """
        self._elastic_ip = elastic_ip

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MasterEIPResponseSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
