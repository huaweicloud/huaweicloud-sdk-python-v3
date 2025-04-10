# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UnbindGlobalEipsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'connect_gateway_id': 'str',
        'body': 'CreateUnbindingGeipRequestBody'
    }

    attribute_map = {
        'connect_gateway_id': 'connect_gateway_id',
        'body': 'body'
    }

    def __init__(self, connect_gateway_id=None, body=None):
        r"""UnbindGlobalEipsRequest

        The model defined in huaweicloud sdk

        :param connect_gateway_id: 互联网关ID
        :type connect_gateway_id: str
        :param body: Body of the UnbindGlobalEipsRequest
        :type body: :class:`huaweicloudsdkdc.v3.CreateUnbindingGeipRequestBody`
        """
        
        

        self._connect_gateway_id = None
        self._body = None
        self.discriminator = None

        self.connect_gateway_id = connect_gateway_id
        if body is not None:
            self.body = body

    @property
    def connect_gateway_id(self):
        r"""Gets the connect_gateway_id of this UnbindGlobalEipsRequest.

        互联网关ID

        :return: The connect_gateway_id of this UnbindGlobalEipsRequest.
        :rtype: str
        """
        return self._connect_gateway_id

    @connect_gateway_id.setter
    def connect_gateway_id(self, connect_gateway_id):
        r"""Sets the connect_gateway_id of this UnbindGlobalEipsRequest.

        互联网关ID

        :param connect_gateway_id: The connect_gateway_id of this UnbindGlobalEipsRequest.
        :type connect_gateway_id: str
        """
        self._connect_gateway_id = connect_gateway_id

    @property
    def body(self):
        r"""Gets the body of this UnbindGlobalEipsRequest.

        :return: The body of this UnbindGlobalEipsRequest.
        :rtype: :class:`huaweicloudsdkdc.v3.CreateUnbindingGeipRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UnbindGlobalEipsRequest.

        :param body: The body of this UnbindGlobalEipsRequest.
        :type body: :class:`huaweicloudsdkdc.v3.CreateUnbindingGeipRequestBody`
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
        if not isinstance(other, UnbindGlobalEipsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
