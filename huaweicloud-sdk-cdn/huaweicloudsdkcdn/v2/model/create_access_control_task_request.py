# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAccessControlTaskRequest:

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
        'body': 'UrlAccessControlTaskRequestBody'
    }

    attribute_map = {
        'action': 'action',
        'body': 'body'
    }

    def __init__(self, action=None, body=None):
        r"""CreateAccessControlTaskRequest

        The model defined in huaweicloud sdk

        :param action: **参数解释：** 操作类型， **约束限制：** 不涉及 **取值范围：** - ban：禁用 - unban：解禁  **默认取值：** 不涉及
        :type action: str
        :param body: Body of the CreateAccessControlTaskRequest
        :type body: :class:`huaweicloudsdkcdn.v2.UrlAccessControlTaskRequestBody`
        """
        
        

        self._action = None
        self._body = None
        self.discriminator = None

        self.action = action
        if body is not None:
            self.body = body

    @property
    def action(self):
        r"""Gets the action of this CreateAccessControlTaskRequest.

        **参数解释：** 操作类型， **约束限制：** 不涉及 **取值范围：** - ban：禁用 - unban：解禁  **默认取值：** 不涉及

        :return: The action of this CreateAccessControlTaskRequest.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this CreateAccessControlTaskRequest.

        **参数解释：** 操作类型， **约束限制：** 不涉及 **取值范围：** - ban：禁用 - unban：解禁  **默认取值：** 不涉及

        :param action: The action of this CreateAccessControlTaskRequest.
        :type action: str
        """
        self._action = action

    @property
    def body(self):
        r"""Gets the body of this CreateAccessControlTaskRequest.

        :return: The body of this CreateAccessControlTaskRequest.
        :rtype: :class:`huaweicloudsdkcdn.v2.UrlAccessControlTaskRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CreateAccessControlTaskRequest.

        :param body: The body of this CreateAccessControlTaskRequest.
        :type body: :class:`huaweicloudsdkcdn.v2.UrlAccessControlTaskRequestBody`
        """
        self._body = body

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
        if not isinstance(other, CreateAccessControlTaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
