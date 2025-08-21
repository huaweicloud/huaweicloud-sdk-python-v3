# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MemberAccess:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'access_level': 'int',
        'notification_level': 'int'
    }

    attribute_map = {
        'access_level': 'access_level',
        'notification_level': 'notification_level'
    }

    def __init__(self, access_level=None, notification_level=None):
        r"""MemberAccess

        The model defined in huaweicloud sdk

        :param access_level: **参数解释：** 访问级别。 **约束限制：** 不涉及。
        :type access_level: int
        :param notification_level: **参数解释：** 通知级别。 **约束限制：** 不涉及。
        :type notification_level: int
        """
        
        

        self._access_level = None
        self._notification_level = None
        self.discriminator = None

        if access_level is not None:
            self.access_level = access_level
        if notification_level is not None:
            self.notification_level = notification_level

    @property
    def access_level(self):
        r"""Gets the access_level of this MemberAccess.

        **参数解释：** 访问级别。 **约束限制：** 不涉及。

        :return: The access_level of this MemberAccess.
        :rtype: int
        """
        return self._access_level

    @access_level.setter
    def access_level(self, access_level):
        r"""Sets the access_level of this MemberAccess.

        **参数解释：** 访问级别。 **约束限制：** 不涉及。

        :param access_level: The access_level of this MemberAccess.
        :type access_level: int
        """
        self._access_level = access_level

    @property
    def notification_level(self):
        r"""Gets the notification_level of this MemberAccess.

        **参数解释：** 通知级别。 **约束限制：** 不涉及。

        :return: The notification_level of this MemberAccess.
        :rtype: int
        """
        return self._notification_level

    @notification_level.setter
    def notification_level(self, notification_level):
        r"""Sets the notification_level of this MemberAccess.

        **参数解释：** 通知级别。 **约束限制：** 不涉及。

        :param notification_level: The notification_level of this MemberAccess.
        :type notification_level: int
        """
        self._notification_level = notification_level

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
        if not isinstance(other, MemberAccess):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
