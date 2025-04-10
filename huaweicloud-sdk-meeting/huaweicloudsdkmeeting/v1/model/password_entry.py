# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PasswordEntry:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'conference_role': 'str',
        'password': 'str'
    }

    attribute_map = {
        'conference_role': 'conferenceRole',
        'password': 'password'
    }

    def __init__(self, conference_role=None, password=None):
        r"""PasswordEntry

        The model defined in huaweicloud sdk

        :param conference_role: 会议角色。 - chair: 会议主持人 - general: 普通与会者
        :type conference_role: str
        :param password: 会议中角色的密码（明文）。
        :type password: str
        """
        
        

        self._conference_role = None
        self._password = None
        self.discriminator = None

        if conference_role is not None:
            self.conference_role = conference_role
        if password is not None:
            self.password = password

    @property
    def conference_role(self):
        r"""Gets the conference_role of this PasswordEntry.

        会议角色。 - chair: 会议主持人 - general: 普通与会者

        :return: The conference_role of this PasswordEntry.
        :rtype: str
        """
        return self._conference_role

    @conference_role.setter
    def conference_role(self, conference_role):
        r"""Sets the conference_role of this PasswordEntry.

        会议角色。 - chair: 会议主持人 - general: 普通与会者

        :param conference_role: The conference_role of this PasswordEntry.
        :type conference_role: str
        """
        self._conference_role = conference_role

    @property
    def password(self):
        r"""Gets the password of this PasswordEntry.

        会议中角色的密码（明文）。

        :return: The password of this PasswordEntry.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        r"""Sets the password of this PasswordEntry.

        会议中角色的密码（明文）。

        :param password: The password of this PasswordEntry.
        :type password: str
        """
        self._password = password

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
        if not isinstance(other, PasswordEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
