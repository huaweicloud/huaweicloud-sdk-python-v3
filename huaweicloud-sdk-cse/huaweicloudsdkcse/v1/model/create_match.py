# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateMatch:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'headers': 'CreateMatchHeaders'
    }

    attribute_map = {
        'headers': 'headers'
    }

    def __init__(self, headers=None):
        r"""CreateMatch

        The model defined in huaweicloud sdk

        :param headers: 
        :type headers: :class:`huaweicloudsdkcse.v1.CreateMatchHeaders`
        """
        
        

        self._headers = None
        self.discriminator = None

        if headers is not None:
            self.headers = headers

    @property
    def headers(self):
        r"""Gets the headers of this CreateMatch.

        :return: The headers of this CreateMatch.
        :rtype: :class:`huaweicloudsdkcse.v1.CreateMatchHeaders`
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        r"""Sets the headers of this CreateMatch.

        :param headers: The headers of this CreateMatch.
        :type headers: :class:`huaweicloudsdkcse.v1.CreateMatchHeaders`
        """
        self._headers = headers

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
        if not isinstance(other, CreateMatch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
