# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProductTextInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'title': 'str',
        'text': 'str'
    }

    attribute_map = {
        'title': 'title',
        'text': 'text'
    }

    def __init__(self, title=None, text=None):
        r"""ProductTextInfo

        The model defined in huaweicloud sdk

        :param title: 文本标题
        :type title: str
        :param text: 文本
        :type text: str
        """
        
        

        self._title = None
        self._text = None
        self.discriminator = None

        if title is not None:
            self.title = title
        if text is not None:
            self.text = text

    @property
    def title(self):
        r"""Gets the title of this ProductTextInfo.

        文本标题

        :return: The title of this ProductTextInfo.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this ProductTextInfo.

        文本标题

        :param title: The title of this ProductTextInfo.
        :type title: str
        """
        self._title = title

    @property
    def text(self):
        r"""Gets the text of this ProductTextInfo.

        文本

        :return: The text of this ProductTextInfo.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        r"""Sets the text of this ProductTextInfo.

        文本

        :param text: The text of this ProductTextInfo.
        :type text: str
        """
        self._text = text

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
        if not isinstance(other, ProductTextInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
