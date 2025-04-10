# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTokenRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'business_id': 'str',
        'x_business_id': 'int'
    }

    attribute_map = {
        'business_id': 'business_id',
        'x_business_id': 'x-business-id'
    }

    def __init__(self, business_id=None, x_business_id=None):
        r"""ShowTokenRequest

        The model defined in huaweicloud sdk

        :param business_id: 应用id。
        :type business_id: str
        :param x_business_id: 应用id。
        :type x_business_id: int
        """
        
        

        self._business_id = None
        self._x_business_id = None
        self.discriminator = None

        self.business_id = business_id
        self.x_business_id = x_business_id

    @property
    def business_id(self):
        r"""Gets the business_id of this ShowTokenRequest.

        应用id。

        :return: The business_id of this ShowTokenRequest.
        :rtype: str
        """
        return self._business_id

    @business_id.setter
    def business_id(self, business_id):
        r"""Sets the business_id of this ShowTokenRequest.

        应用id。

        :param business_id: The business_id of this ShowTokenRequest.
        :type business_id: str
        """
        self._business_id = business_id

    @property
    def x_business_id(self):
        r"""Gets the x_business_id of this ShowTokenRequest.

        应用id。

        :return: The x_business_id of this ShowTokenRequest.
        :rtype: int
        """
        return self._x_business_id

    @x_business_id.setter
    def x_business_id(self, x_business_id):
        r"""Sets the x_business_id of this ShowTokenRequest.

        应用id。

        :param x_business_id: The x_business_id of this ShowTokenRequest.
        :type x_business_id: int
        """
        self._x_business_id = x_business_id

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
        if not isinstance(other, ShowTokenRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
