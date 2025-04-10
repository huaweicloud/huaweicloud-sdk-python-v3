# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteLivePlatformRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'platform_id': 'str',
        'x_app_user_id': 'str'
    }

    attribute_map = {
        'platform_id': 'platform_id',
        'x_app_user_id': 'X-App-UserId'
    }

    def __init__(self, platform_id=None, x_app_user_id=None):
        r"""DeleteLivePlatformRequest

        The model defined in huaweicloud sdk

        :param platform_id: 直播平台ID。
        :type platform_id: str
        :param x_app_user_id: 第三方用户ID。不允许输入中文。
        :type x_app_user_id: str
        """
        
        

        self._platform_id = None
        self._x_app_user_id = None
        self.discriminator = None

        self.platform_id = platform_id
        if x_app_user_id is not None:
            self.x_app_user_id = x_app_user_id

    @property
    def platform_id(self):
        r"""Gets the platform_id of this DeleteLivePlatformRequest.

        直播平台ID。

        :return: The platform_id of this DeleteLivePlatformRequest.
        :rtype: str
        """
        return self._platform_id

    @platform_id.setter
    def platform_id(self, platform_id):
        r"""Sets the platform_id of this DeleteLivePlatformRequest.

        直播平台ID。

        :param platform_id: The platform_id of this DeleteLivePlatformRequest.
        :type platform_id: str
        """
        self._platform_id = platform_id

    @property
    def x_app_user_id(self):
        r"""Gets the x_app_user_id of this DeleteLivePlatformRequest.

        第三方用户ID。不允许输入中文。

        :return: The x_app_user_id of this DeleteLivePlatformRequest.
        :rtype: str
        """
        return self._x_app_user_id

    @x_app_user_id.setter
    def x_app_user_id(self, x_app_user_id):
        r"""Sets the x_app_user_id of this DeleteLivePlatformRequest.

        第三方用户ID。不允许输入中文。

        :param x_app_user_id: The x_app_user_id of this DeleteLivePlatformRequest.
        :type x_app_user_id: str
        """
        self._x_app_user_id = x_app_user_id

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
        if not isinstance(other, DeleteLivePlatformRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
