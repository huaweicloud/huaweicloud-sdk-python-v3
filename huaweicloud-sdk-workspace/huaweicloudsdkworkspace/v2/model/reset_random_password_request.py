# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResetRandomPasswordRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_id': 'str',
        'notification_type': 'str'
    }

    attribute_map = {
        'user_id': 'user_id',
        'notification_type': 'notification_type'
    }

    def __init__(self, user_id=None, notification_type=None):
        """ResetRandomPasswordRequest

        The model defined in huaweicloud sdk

        :param user_id: 用户ID。
        :type user_id: str
        :param notification_type: 通知用户类型，现在有“email”和“phone”两种，用\&quot;,\&quot;分开，用户为用户激活模式时必须要带上通知类型，以便接收到密码通知。
        :type notification_type: str
        """
        
        

        self._user_id = None
        self._notification_type = None
        self.discriminator = None

        self.user_id = user_id
        if notification_type is not None:
            self.notification_type = notification_type

    @property
    def user_id(self):
        """Gets the user_id of this ResetRandomPasswordRequest.

        用户ID。

        :return: The user_id of this ResetRandomPasswordRequest.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ResetRandomPasswordRequest.

        用户ID。

        :param user_id: The user_id of this ResetRandomPasswordRequest.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def notification_type(self):
        """Gets the notification_type of this ResetRandomPasswordRequest.

        通知用户类型，现在有“email”和“phone”两种，用\",\"分开，用户为用户激活模式时必须要带上通知类型，以便接收到密码通知。

        :return: The notification_type of this ResetRandomPasswordRequest.
        :rtype: str
        """
        return self._notification_type

    @notification_type.setter
    def notification_type(self, notification_type):
        """Sets the notification_type of this ResetRandomPasswordRequest.

        通知用户类型，现在有“email”和“phone”两种，用\",\"分开，用户为用户激活模式时必须要带上通知类型，以便接收到密码通知。

        :param notification_type: The notification_type of this ResetRandomPasswordRequest.
        :type notification_type: str
        """
        self._notification_type = notification_type

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
        if not isinstance(other, ResetRandomPasswordRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
