# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IndependentReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'IndependentBodyReq',
        'is_auto_pay': 'int'
    }

    attribute_map = {
        'type': 'type',
        'is_auto_pay': 'is_auto_pay'
    }

    def __init__(self, type=None, is_auto_pay=None):
        r"""IndependentReq

        The model defined in huaweicloud sdk

        :param type: 
        :type type: :class:`huaweicloudsdkcss.v1.IndependentBodyReq`
        :param is_auto_pay: 是否自动支付。下单订购后，是否自动从客户的华为云账户中支付，而不需要客户手动去进行支付。
        :type is_auto_pay: int
        """
        
        

        self._type = None
        self._is_auto_pay = None
        self.discriminator = None

        self.type = type
        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay

    @property
    def type(self):
        r"""Gets the type of this IndependentReq.

        :return: The type of this IndependentReq.
        :rtype: :class:`huaweicloudsdkcss.v1.IndependentBodyReq`
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this IndependentReq.

        :param type: The type of this IndependentReq.
        :type type: :class:`huaweicloudsdkcss.v1.IndependentBodyReq`
        """
        self._type = type

    @property
    def is_auto_pay(self):
        r"""Gets the is_auto_pay of this IndependentReq.

        是否自动支付。下单订购后，是否自动从客户的华为云账户中支付，而不需要客户手动去进行支付。

        :return: The is_auto_pay of this IndependentReq.
        :rtype: int
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        r"""Sets the is_auto_pay of this IndependentReq.

        是否自动支付。下单订购后，是否自动从客户的华为云账户中支付，而不需要客户手动去进行支付。

        :param is_auto_pay: The is_auto_pay of this IndependentReq.
        :type is_auto_pay: int
        """
        self._is_auto_pay = is_auto_pay

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
        if not isinstance(other, IndependentReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
