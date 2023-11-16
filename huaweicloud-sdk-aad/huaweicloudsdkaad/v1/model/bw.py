# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Bw:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'black_ip_list': 'list[str]',
        'white_ip_list': 'list[str]'
    }

    attribute_map = {
        'black_ip_list': 'black_ip_list',
        'white_ip_list': 'white_ip_list'
    }

    def __init__(self, black_ip_list=None, white_ip_list=None):
        """Bw

        The model defined in huaweicloud sdk

        :param black_ip_list: 黑名单列表
        :type black_ip_list: list[str]
        :param white_ip_list: 白名单列表
        :type white_ip_list: list[str]
        """
        
        

        self._black_ip_list = None
        self._white_ip_list = None
        self.discriminator = None

        self.black_ip_list = black_ip_list
        self.white_ip_list = white_ip_list

    @property
    def black_ip_list(self):
        """Gets the black_ip_list of this Bw.

        黑名单列表

        :return: The black_ip_list of this Bw.
        :rtype: list[str]
        """
        return self._black_ip_list

    @black_ip_list.setter
    def black_ip_list(self, black_ip_list):
        """Sets the black_ip_list of this Bw.

        黑名单列表

        :param black_ip_list: The black_ip_list of this Bw.
        :type black_ip_list: list[str]
        """
        self._black_ip_list = black_ip_list

    @property
    def white_ip_list(self):
        """Gets the white_ip_list of this Bw.

        白名单列表

        :return: The white_ip_list of this Bw.
        :rtype: list[str]
        """
        return self._white_ip_list

    @white_ip_list.setter
    def white_ip_list(self, white_ip_list):
        """Sets the white_ip_list of this Bw.

        白名单列表

        :param white_ip_list: The white_ip_list of this Bw.
        :type white_ip_list: list[str]
        """
        self._white_ip_list = white_ip_list

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
        if not isinstance(other, Bw):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
