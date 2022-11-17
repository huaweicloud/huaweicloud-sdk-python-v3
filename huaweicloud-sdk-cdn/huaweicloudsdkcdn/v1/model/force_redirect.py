# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ForceRedirect:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'switch': 'int',
        'redirect_type': 'str'
    }

    attribute_map = {
        'switch': 'switch',
        'redirect_type': 'redirect_type'
    }

    def __init__(self, switch=None, redirect_type=None):
        """ForceRedirect

        The model defined in huaweicloud sdk

        :param switch: 强制跳转开关。1打开。0关闭。
        :type switch: int
        :param redirect_type: 强制跳转类型。http：强制跳转HTTP。https：强制跳转HTTPS。
        :type redirect_type: str
        """
        
        

        self._switch = None
        self._redirect_type = None
        self.discriminator = None

        self.switch = switch
        if redirect_type is not None:
            self.redirect_type = redirect_type

    @property
    def switch(self):
        """Gets the switch of this ForceRedirect.

        强制跳转开关。1打开。0关闭。

        :return: The switch of this ForceRedirect.
        :rtype: int
        """
        return self._switch

    @switch.setter
    def switch(self, switch):
        """Sets the switch of this ForceRedirect.

        强制跳转开关。1打开。0关闭。

        :param switch: The switch of this ForceRedirect.
        :type switch: int
        """
        self._switch = switch

    @property
    def redirect_type(self):
        """Gets the redirect_type of this ForceRedirect.

        强制跳转类型。http：强制跳转HTTP。https：强制跳转HTTPS。

        :return: The redirect_type of this ForceRedirect.
        :rtype: str
        """
        return self._redirect_type

    @redirect_type.setter
    def redirect_type(self, redirect_type):
        """Sets the redirect_type of this ForceRedirect.

        强制跳转类型。http：强制跳转HTTP。https：强制跳转HTTPS。

        :param redirect_type: The redirect_type of this ForceRedirect.
        :type redirect_type: str
        """
        self._redirect_type = redirect_type

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
        if not isinstance(other, ForceRedirect):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
