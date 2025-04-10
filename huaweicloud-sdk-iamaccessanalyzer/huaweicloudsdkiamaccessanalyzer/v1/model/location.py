# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Location:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'path': 'list[PathElement]',
        'span': 'Span'
    }

    attribute_map = {
        'path': 'path',
        'span': 'span'
    }

    def __init__(self, path=None, span=None):
        r"""Location

        The model defined in huaweicloud sdk

        :param path: 策略中的路径，表示为路径元素的有序序列。
        :type path: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.PathElement`]
        :param span: 
        :type span: :class:`huaweicloudsdkiamaccessanalyzer.v1.Span`
        """
        
        

        self._path = None
        self._span = None
        self.discriminator = None

        self.path = path
        self.span = span

    @property
    def path(self):
        r"""Gets the path of this Location.

        策略中的路径，表示为路径元素的有序序列。

        :return: The path of this Location.
        :rtype: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.PathElement`]
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this Location.

        策略中的路径，表示为路径元素的有序序列。

        :param path: The path of this Location.
        :type path: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.PathElement`]
        """
        self._path = path

    @property
    def span(self):
        r"""Gets the span of this Location.

        :return: The span of this Location.
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.Span`
        """
        return self._span

    @span.setter
    def span(self, span):
        r"""Sets the span of this Location.

        :param span: The span of this Location.
        :type span: :class:`huaweicloudsdkiamaccessanalyzer.v1.Span`
        """
        self._span = span

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
        if not isinstance(other, Location):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
