# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessRomaBriefInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_key': 'str'
    }

    attribute_map = {
        'app_key': 'app_key'
    }

    def __init__(self, app_key=None):
        """AccessRomaBriefInfo

        The model defined in huaweicloud sdk

        :param app_key: 认证key，加密存储
        :type app_key: str
        """
        
        

        self._app_key = None
        self.discriminator = None

        if app_key is not None:
            self.app_key = app_key

    @property
    def app_key(self):
        """Gets the app_key of this AccessRomaBriefInfo.

        认证key，加密存储

        :return: The app_key of this AccessRomaBriefInfo.
        :rtype: str
        """
        return self._app_key

    @app_key.setter
    def app_key(self, app_key):
        """Sets the app_key of this AccessRomaBriefInfo.

        认证key，加密存储

        :param app_key: The app_key of this AccessRomaBriefInfo.
        :type app_key: str
        """
        self._app_key = app_key

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
        if not isinstance(other, AccessRomaBriefInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
