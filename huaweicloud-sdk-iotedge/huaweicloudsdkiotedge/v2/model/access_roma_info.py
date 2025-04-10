# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessRomaInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_key': 'str',
        'app_secret': 'str'
    }

    attribute_map = {
        'app_key': 'app_key',
        'app_secret': 'app_secret'
    }

    def __init__(self, app_key=None, app_secret=None):
        r"""AccessRomaInfo

        The model defined in huaweicloud sdk

        :param app_key: 认证key，加密存储
        :type app_key: str
        :param app_secret: 认证secret，加密存储
        :type app_secret: str
        """
        
        

        self._app_key = None
        self._app_secret = None
        self.discriminator = None

        if app_key is not None:
            self.app_key = app_key
        if app_secret is not None:
            self.app_secret = app_secret

    @property
    def app_key(self):
        r"""Gets the app_key of this AccessRomaInfo.

        认证key，加密存储

        :return: The app_key of this AccessRomaInfo.
        :rtype: str
        """
        return self._app_key

    @app_key.setter
    def app_key(self, app_key):
        r"""Sets the app_key of this AccessRomaInfo.

        认证key，加密存储

        :param app_key: The app_key of this AccessRomaInfo.
        :type app_key: str
        """
        self._app_key = app_key

    @property
    def app_secret(self):
        r"""Gets the app_secret of this AccessRomaInfo.

        认证secret，加密存储

        :return: The app_secret of this AccessRomaInfo.
        :rtype: str
        """
        return self._app_secret

    @app_secret.setter
    def app_secret(self, app_secret):
        r"""Sets the app_secret of this AccessRomaInfo.

        认证secret，加密存储

        :param app_secret: The app_secret of this AccessRomaInfo.
        :type app_secret: str
        """
        self._app_secret = app_secret

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
        if not isinstance(other, AccessRomaInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
