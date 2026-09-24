# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SwitchMySqlProxyEipRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'public_ip': 'str',
        'public_ip_id': 'str',
        'bind': 'str'
    }

    attribute_map = {
        'public_ip': 'public_ip',
        'public_ip_id': 'public_ip_id',
        'bind': 'bind'
    }

    def __init__(self, public_ip=None, public_ip_id=None, bind=None):
        r"""SwitchMySqlProxyEipRequestBody

        The model defined in huaweicloud sdk

        :param public_ip: **参数解释**：  待绑定的弹性公网IP地址。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type public_ip: str
        :param public_ip_id: **参数解释**：  弹性公网IP地址对应的ID。请求为绑定弹性公网IP时需传入该参数，请求为解绑弹性公网IP时无需传入。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type public_ip_id: str
        :param bind: **参数解释**：  请求是否为绑定弹性公网IP。  **约束限制**：  不涉及。  **取值范围**：  - true：表示请求为绑定弹性公网IP。 - false：表示请求为解绑弹性公网IP。  **默认取值**：  不涉及。
        :type bind: str
        """
        
        

        self._public_ip = None
        self._public_ip_id = None
        self._bind = None
        self.discriminator = None

        self.public_ip = public_ip
        if public_ip_id is not None:
            self.public_ip_id = public_ip_id
        self.bind = bind

    @property
    def public_ip(self):
        r"""Gets the public_ip of this SwitchMySqlProxyEipRequestBody.

        **参数解释**：  待绑定的弹性公网IP地址。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The public_ip of this SwitchMySqlProxyEipRequestBody.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this SwitchMySqlProxyEipRequestBody.

        **参数解释**：  待绑定的弹性公网IP地址。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param public_ip: The public_ip of this SwitchMySqlProxyEipRequestBody.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def public_ip_id(self):
        r"""Gets the public_ip_id of this SwitchMySqlProxyEipRequestBody.

        **参数解释**：  弹性公网IP地址对应的ID。请求为绑定弹性公网IP时需传入该参数，请求为解绑弹性公网IP时无需传入。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The public_ip_id of this SwitchMySqlProxyEipRequestBody.
        :rtype: str
        """
        return self._public_ip_id

    @public_ip_id.setter
    def public_ip_id(self, public_ip_id):
        r"""Sets the public_ip_id of this SwitchMySqlProxyEipRequestBody.

        **参数解释**：  弹性公网IP地址对应的ID。请求为绑定弹性公网IP时需传入该参数，请求为解绑弹性公网IP时无需传入。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param public_ip_id: The public_ip_id of this SwitchMySqlProxyEipRequestBody.
        :type public_ip_id: str
        """
        self._public_ip_id = public_ip_id

    @property
    def bind(self):
        r"""Gets the bind of this SwitchMySqlProxyEipRequestBody.

        **参数解释**：  请求是否为绑定弹性公网IP。  **约束限制**：  不涉及。  **取值范围**：  - true：表示请求为绑定弹性公网IP。 - false：表示请求为解绑弹性公网IP。  **默认取值**：  不涉及。

        :return: The bind of this SwitchMySqlProxyEipRequestBody.
        :rtype: str
        """
        return self._bind

    @bind.setter
    def bind(self, bind):
        r"""Sets the bind of this SwitchMySqlProxyEipRequestBody.

        **参数解释**：  请求是否为绑定弹性公网IP。  **约束限制**：  不涉及。  **取值范围**：  - true：表示请求为绑定弹性公网IP。 - false：表示请求为解绑弹性公网IP。  **默认取值**：  不涉及。

        :param bind: The bind of this SwitchMySqlProxyEipRequestBody.
        :type bind: str
        """
        self._bind = bind

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
        if not isinstance(other, SwitchMySqlProxyEipRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
