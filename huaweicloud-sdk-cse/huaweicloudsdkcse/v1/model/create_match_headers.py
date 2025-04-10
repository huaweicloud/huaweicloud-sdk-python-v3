# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateMatchHeaders:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'header': 'CreateMatchHeadersHeader'
    }

    attribute_map = {
        'header': '&lt;header&gt;'
    }

    def __init__(self, header=None):
        r"""CreateMatchHeaders

        The model defined in huaweicloud sdk

        :param header: 
        :type header: :class:`huaweicloudsdkcse.v1.CreateMatchHeadersHeader`
        """
        
        

        self._header = None
        self.discriminator = None

        if header is not None:
            self.header = header

    @property
    def header(self):
        r"""Gets the header of this CreateMatchHeaders.

        :return: The header of this CreateMatchHeaders.
        :rtype: :class:`huaweicloudsdkcse.v1.CreateMatchHeadersHeader`
        """
        return self._header

    @header.setter
    def header(self, header):
        r"""Sets the header of this CreateMatchHeaders.

        :param header: The header of this CreateMatchHeaders.
        :type header: :class:`huaweicloudsdkcse.v1.CreateMatchHeadersHeader`
        """
        self._header = header

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
        if not isinstance(other, CreateMatchHeaders):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
