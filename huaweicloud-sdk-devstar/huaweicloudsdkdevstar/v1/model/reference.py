# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Reference:

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
        'url': 'str',
        'type': 'int',
        'productshort': 'str',
        'is_valid': 'bool'
    }

    attribute_map = {
        'title': 'title',
        'url': 'url',
        'type': 'type',
        'productshort': 'productshort',
        'is_valid': 'is_valid'
    }

    def __init__(self, title=None, url=None, type=None, productshort=None, is_valid=None):
        """Reference

        The model defined in huaweicloud sdk

        :param title: 标题名称。
        :type title: str
        :param url: 链接地址。
        :type url: str
        :param type: 关联类型。
        :type type: int
        :param productshort: 产品短名。
        :type productshort: str
        :param is_valid: 是否有效
        :type is_valid: bool
        """
        
        

        self._title = None
        self._url = None
        self._type = None
        self._productshort = None
        self._is_valid = None
        self.discriminator = None

        if title is not None:
            self.title = title
        if url is not None:
            self.url = url
        if type is not None:
            self.type = type
        if productshort is not None:
            self.productshort = productshort
        if is_valid is not None:
            self.is_valid = is_valid

    @property
    def title(self):
        """Gets the title of this Reference.

        标题名称。

        :return: The title of this Reference.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Reference.

        标题名称。

        :param title: The title of this Reference.
        :type title: str
        """
        self._title = title

    @property
    def url(self):
        """Gets the url of this Reference.

        链接地址。

        :return: The url of this Reference.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Reference.

        链接地址。

        :param url: The url of this Reference.
        :type url: str
        """
        self._url = url

    @property
    def type(self):
        """Gets the type of this Reference.

        关联类型。

        :return: The type of this Reference.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Reference.

        关联类型。

        :param type: The type of this Reference.
        :type type: int
        """
        self._type = type

    @property
    def productshort(self):
        """Gets the productshort of this Reference.

        产品短名。

        :return: The productshort of this Reference.
        :rtype: str
        """
        return self._productshort

    @productshort.setter
    def productshort(self, productshort):
        """Sets the productshort of this Reference.

        产品短名。

        :param productshort: The productshort of this Reference.
        :type productshort: str
        """
        self._productshort = productshort

    @property
    def is_valid(self):
        """Gets the is_valid of this Reference.

        是否有效

        :return: The is_valid of this Reference.
        :rtype: bool
        """
        return self._is_valid

    @is_valid.setter
    def is_valid(self, is_valid):
        """Sets the is_valid of this Reference.

        是否有效

        :param is_valid: The is_valid of this Reference.
        :type is_valid: bool
        """
        self._is_valid = is_valid

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
        if not isinstance(other, Reference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
