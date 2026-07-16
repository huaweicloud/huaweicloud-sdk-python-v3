# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPoolRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pool_name': 'str',
        'x_model_arts_user_id': 'str'
    }

    attribute_map = {
        'pool_name': 'pool_name',
        'x_model_arts_user_id': 'X-ModelArts-User-ID'
    }

    def __init__(self, pool_name=None, x_model_arts_user_id=None):
        r"""ShowPoolRequest

        The model defined in huaweicloud sdk

        :param pool_name: **参数解释**：资源池的ID，取值自资源池详情的metadata.name字段。 **约束限制**：不涉及。 **取值范围**：只能以小写字母开头，数字、中划线组成，不能以中划线结尾，且长度为36-63。 **默认取值**：不涉及。
        :type pool_name: str
        :param x_model_arts_user_id: **参数解释**：租户ID，传递该参数鉴权以该租户ID为准。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type x_model_arts_user_id: str
        """
        
        

        self._pool_name = None
        self._x_model_arts_user_id = None
        self.discriminator = None

        self.pool_name = pool_name
        if x_model_arts_user_id is not None:
            self.x_model_arts_user_id = x_model_arts_user_id

    @property
    def pool_name(self):
        r"""Gets the pool_name of this ShowPoolRequest.

        **参数解释**：资源池的ID，取值自资源池详情的metadata.name字段。 **约束限制**：不涉及。 **取值范围**：只能以小写字母开头，数字、中划线组成，不能以中划线结尾，且长度为36-63。 **默认取值**：不涉及。

        :return: The pool_name of this ShowPoolRequest.
        :rtype: str
        """
        return self._pool_name

    @pool_name.setter
    def pool_name(self, pool_name):
        r"""Sets the pool_name of this ShowPoolRequest.

        **参数解释**：资源池的ID，取值自资源池详情的metadata.name字段。 **约束限制**：不涉及。 **取值范围**：只能以小写字母开头，数字、中划线组成，不能以中划线结尾，且长度为36-63。 **默认取值**：不涉及。

        :param pool_name: The pool_name of this ShowPoolRequest.
        :type pool_name: str
        """
        self._pool_name = pool_name

    @property
    def x_model_arts_user_id(self):
        r"""Gets the x_model_arts_user_id of this ShowPoolRequest.

        **参数解释**：租户ID，传递该参数鉴权以该租户ID为准。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The x_model_arts_user_id of this ShowPoolRequest.
        :rtype: str
        """
        return self._x_model_arts_user_id

    @x_model_arts_user_id.setter
    def x_model_arts_user_id(self, x_model_arts_user_id):
        r"""Sets the x_model_arts_user_id of this ShowPoolRequest.

        **参数解释**：租户ID，传递该参数鉴权以该租户ID为准。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param x_model_arts_user_id: The x_model_arts_user_id of this ShowPoolRequest.
        :type x_model_arts_user_id: str
        """
        self._x_model_arts_user_id = x_model_arts_user_id

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
        if not isinstance(other, ShowPoolRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
