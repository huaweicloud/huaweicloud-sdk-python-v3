# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessControl:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'black': 'list[str]',
        'white': 'list[str]'
    }

    attribute_map = {
        'black': 'black',
        'white': 'white'
    }

    def __init__(self, black=None, white=None):
        """AccessControl

        The model defined in huaweicloud sdk

        :param black: 黑名单数组。 - 每行一个IP地址或网段，以回车结束。 - 每个IP地址组最多可添加300个IP地址或网段。 
        :type black: list[str]
        :param white: 白名单数组。 - 每行一个IP地址或网段，以回车结束。 - 每个IP地址组最多可添加300个IP地址或网段。 
        :type white: list[str]
        """
        
        

        self._black = None
        self._white = None
        self.discriminator = None

        if black is not None:
            self.black = black
        if white is not None:
            self.white = white

    @property
    def black(self):
        """Gets the black of this AccessControl.

        黑名单数组。 - 每行一个IP地址或网段，以回车结束。 - 每个IP地址组最多可添加300个IP地址或网段。 

        :return: The black of this AccessControl.
        :rtype: list[str]
        """
        return self._black

    @black.setter
    def black(self, black):
        """Sets the black of this AccessControl.

        黑名单数组。 - 每行一个IP地址或网段，以回车结束。 - 每个IP地址组最多可添加300个IP地址或网段。 

        :param black: The black of this AccessControl.
        :type black: list[str]
        """
        self._black = black

    @property
    def white(self):
        """Gets the white of this AccessControl.

        白名单数组。 - 每行一个IP地址或网段，以回车结束。 - 每个IP地址组最多可添加300个IP地址或网段。 

        :return: The white of this AccessControl.
        :rtype: list[str]
        """
        return self._white

    @white.setter
    def white(self, white):
        """Sets the white of this AccessControl.

        白名单数组。 - 每行一个IP地址或网段，以回车结束。 - 每个IP地址组最多可添加300个IP地址或网段。 

        :param white: The white of this AccessControl.
        :type white: list[str]
        """
        self._white = white

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
        if not isinstance(other, AccessControl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
