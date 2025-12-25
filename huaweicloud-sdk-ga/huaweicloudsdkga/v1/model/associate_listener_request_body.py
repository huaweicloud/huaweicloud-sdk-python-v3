# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssociateListenerRequestBody:

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
        'type': 'str'
    }

    attribute_map = {
        'listener_id': 'listener_id',
        'type': 'type'
    }

    def __init__(self, listener_id=None, type=None):
        r"""AssociateListenerRequestBody

        The model defined in huaweicloud sdk

        :param listener_id: 监听器ID。
        :type listener_id: str
        :param type: 访问控制策略类型,即黑名单还是白名单, 取值： - BLACK：黑名单 - WHITE：白名单
        :type type: str
        """
        
        

        self._listener_id = None
        self._type = None
        self.discriminator = None

        self.listener_id = listener_id
        self.type = type

    @property
    def listener_id(self):
        r"""Gets the listener_id of this AssociateListenerRequestBody.

        监听器ID。

        :return: The listener_id of this AssociateListenerRequestBody.
        :rtype: str
        """
        return self._listener_id

    @listener_id.setter
    def listener_id(self, listener_id):
        r"""Sets the listener_id of this AssociateListenerRequestBody.

        监听器ID。

        :param listener_id: The listener_id of this AssociateListenerRequestBody.
        :type listener_id: str
        """
        self._listener_id = listener_id

    @property
    def type(self):
        r"""Gets the type of this AssociateListenerRequestBody.

        访问控制策略类型,即黑名单还是白名单, 取值： - BLACK：黑名单 - WHITE：白名单

        :return: The type of this AssociateListenerRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this AssociateListenerRequestBody.

        访问控制策略类型,即黑名单还是白名单, 取值： - BLACK：黑名单 - WHITE：白名单

        :param type: The type of this AssociateListenerRequestBody.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, AssociateListenerRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
