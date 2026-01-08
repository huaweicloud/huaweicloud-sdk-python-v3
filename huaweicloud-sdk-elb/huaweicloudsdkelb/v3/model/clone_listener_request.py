# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CloneListenerRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'listener_id': 'str',
        'body': 'CloneListenerRequestBody'
    }

    attribute_map = {
        'listener_id': 'listener_id',
        'body': 'body'
    }

    def __init__(self, listener_id=None, body=None):
        r"""CloneListenerRequest

        The model defined in huaweicloud sdk

        :param listener_id: **参数解释**：被复制监听器ID（UUID）。  **约束限制**：不涉及  **取值范围**：标准的UUID格式，长度为36个字符。  **默认取值**：不涉及
        :type listener_id: str
        :param body: Body of the CloneListenerRequest
        :type body: :class:`huaweicloudsdkelb.v3.CloneListenerRequestBody`
        """
        
        

        self._listener_id = None
        self._body = None
        self.discriminator = None

        self.listener_id = listener_id
        if body is not None:
            self.body = body

    @property
    def listener_id(self):
        r"""Gets the listener_id of this CloneListenerRequest.

        **参数解释**：被复制监听器ID（UUID）。  **约束限制**：不涉及  **取值范围**：标准的UUID格式，长度为36个字符。  **默认取值**：不涉及

        :return: The listener_id of this CloneListenerRequest.
        :rtype: str
        """
        return self._listener_id

    @listener_id.setter
    def listener_id(self, listener_id):
        r"""Sets the listener_id of this CloneListenerRequest.

        **参数解释**：被复制监听器ID（UUID）。  **约束限制**：不涉及  **取值范围**：标准的UUID格式，长度为36个字符。  **默认取值**：不涉及

        :param listener_id: The listener_id of this CloneListenerRequest.
        :type listener_id: str
        """
        self._listener_id = listener_id

    @property
    def body(self):
        r"""Gets the body of this CloneListenerRequest.

        :return: The body of this CloneListenerRequest.
        :rtype: :class:`huaweicloudsdkelb.v3.CloneListenerRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CloneListenerRequest.

        :param body: The body of this CloneListenerRequest.
        :type body: :class:`huaweicloudsdkelb.v3.CloneListenerRequestBody`
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
        if not isinstance(other, CloneListenerRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
