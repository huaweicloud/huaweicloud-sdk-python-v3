# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppCodeCreate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_code': 'str'
    }

    attribute_map = {
        'app_code': 'app_code'
    }

    def __init__(self, app_code=None):
        """AppCodeCreate

        The model defined in huaweicloud sdk

        :param app_code: App Code值  支持英文、数字，+_!@#$%-/&#x3D;，且只能以英文、数字和+、/开头，64-180个字符。
        :type app_code: str
        """
        
        

        self._app_code = None
        self.discriminator = None

        self.app_code = app_code

    @property
    def app_code(self):
        """Gets the app_code of this AppCodeCreate.

        App Code值  支持英文、数字，+_!@#$%-/=，且只能以英文、数字和+、/开头，64-180个字符。

        :return: The app_code of this AppCodeCreate.
        :rtype: str
        """
        return self._app_code

    @app_code.setter
    def app_code(self, app_code):
        """Sets the app_code of this AppCodeCreate.

        App Code值  支持英文、数字，+_!@#$%-/=，且只能以英文、数字和+、/开头，64-180个字符。

        :param app_code: The app_code of this AppCodeCreate.
        :type app_code: str
        """
        self._app_code = app_code

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
        if not isinstance(other, AppCodeCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
