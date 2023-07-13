# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StartKibanaPublicReqElbWhitelist:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable_white_list': 'bool',
        'white_list': 'str'
    }

    attribute_map = {
        'enable_white_list': 'enableWhiteList',
        'white_list': 'whiteList'
    }

    def __init__(self, enable_white_list=None, white_list=None):
        """StartKibanaPublicReqElbWhitelist

        The model defined in huaweicloud sdk

        :param enable_white_list: 是否开启白名单。 - true: 开启白名单。 - false: 关闭白名单。
        :type enable_white_list: bool
        :param white_list: 白名单。
        :type white_list: str
        """
        
        

        self._enable_white_list = None
        self._white_list = None
        self.discriminator = None

        self.enable_white_list = enable_white_list
        self.white_list = white_list

    @property
    def enable_white_list(self):
        """Gets the enable_white_list of this StartKibanaPublicReqElbWhitelist.

        是否开启白名单。 - true: 开启白名单。 - false: 关闭白名单。

        :return: The enable_white_list of this StartKibanaPublicReqElbWhitelist.
        :rtype: bool
        """
        return self._enable_white_list

    @enable_white_list.setter
    def enable_white_list(self, enable_white_list):
        """Sets the enable_white_list of this StartKibanaPublicReqElbWhitelist.

        是否开启白名单。 - true: 开启白名单。 - false: 关闭白名单。

        :param enable_white_list: The enable_white_list of this StartKibanaPublicReqElbWhitelist.
        :type enable_white_list: bool
        """
        self._enable_white_list = enable_white_list

    @property
    def white_list(self):
        """Gets the white_list of this StartKibanaPublicReqElbWhitelist.

        白名单。

        :return: The white_list of this StartKibanaPublicReqElbWhitelist.
        :rtype: str
        """
        return self._white_list

    @white_list.setter
    def white_list(self, white_list):
        """Sets the white_list of this StartKibanaPublicReqElbWhitelist.

        白名单。

        :param white_list: The white_list of this StartKibanaPublicReqElbWhitelist.
        :type white_list: str
        """
        self._white_list = white_list

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
        if not isinstance(other, StartKibanaPublicReqElbWhitelist):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
