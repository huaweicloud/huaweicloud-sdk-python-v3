# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyUser:

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
        'attached_at': 'datetime'
    }

    attribute_map = {
        'user_id': 'user_id',
        'attached_at': 'attached_at'
    }

    def __init__(self, user_id=None, attached_at=None):
        r"""PolicyUser

        The model defined in huaweicloud sdk

        :param user_id: IAM用户ID。
        :type user_id: str
        :param attached_at: 身份策略的附加时间。
        :type attached_at: datetime
        """
        
        

        self._user_id = None
        self._attached_at = None
        self.discriminator = None

        self.user_id = user_id
        self.attached_at = attached_at

    @property
    def user_id(self):
        r"""Gets the user_id of this PolicyUser.

        IAM用户ID。

        :return: The user_id of this PolicyUser.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this PolicyUser.

        IAM用户ID。

        :param user_id: The user_id of this PolicyUser.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def attached_at(self):
        r"""Gets the attached_at of this PolicyUser.

        身份策略的附加时间。

        :return: The attached_at of this PolicyUser.
        :rtype: datetime
        """
        return self._attached_at

    @attached_at.setter
    def attached_at(self, attached_at):
        r"""Sets the attached_at of this PolicyUser.

        身份策略的附加时间。

        :param attached_at: The attached_at of this PolicyUser.
        :type attached_at: datetime
        """
        self._attached_at = attached_at

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
        if not isinstance(other, PolicyUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
