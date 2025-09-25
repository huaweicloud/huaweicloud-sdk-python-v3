# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VerifyOrderRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'number': 'str',
        'body': 'VerifyOrderRequestBody'
    }

    attribute_map = {
        'number': 'number',
        'body': 'body'
    }

    def __init__(self, number=None, body=None):
        r"""VerifyOrderRequest

        The model defined in huaweicloud sdk

        :param number: 服务单号
        :type number: str
        :param body: Body of the VerifyOrderRequest
        :type body: :class:`huaweicloudsdkdcos.v1.VerifyOrderRequestBody`
        """
        
        

        self._number = None
        self._body = None
        self.discriminator = None

        self.number = number
        if body is not None:
            self.body = body

    @property
    def number(self):
        r"""Gets the number of this VerifyOrderRequest.

        服务单号

        :return: The number of this VerifyOrderRequest.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        r"""Sets the number of this VerifyOrderRequest.

        服务单号

        :param number: The number of this VerifyOrderRequest.
        :type number: str
        """
        self._number = number

    @property
    def body(self):
        r"""Gets the body of this VerifyOrderRequest.

        :return: The body of this VerifyOrderRequest.
        :rtype: :class:`huaweicloudsdkdcos.v1.VerifyOrderRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this VerifyOrderRequest.

        :param body: The body of this VerifyOrderRequest.
        :type body: :class:`huaweicloudsdkdcos.v1.VerifyOrderRequestBody`
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
        if not isinstance(other, VerifyOrderRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
