# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePublicZoneInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'email': 'str',
        'ttl': 'int'
    }

    attribute_map = {
        'description': 'description',
        'email': 'email',
        'ttl': 'ttl'
    }

    def __init__(self, description=None, email=None, ttl=None):
        r"""UpdatePublicZoneInfo

        The model defined in huaweicloud sdk

        :param description: **参数解释：** 域名的描述信息。 **约束限制：** 不涉及。 **取值范围：** 长度不超过255个字符。 **默认取值：** 默认为空，表示维持原值。
        :type description: str
        :param email: **参数解释：** 管理该域名的管理员邮箱，用于生成该域名的SOA记录。   **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 默认为空，表示维持原值。
        :type email: str
        :param ttl: **参数解释：** 用于填写默认生成的SOA记录中有效缓存时间，以秒为单位。 **约束限制：** 不涉及。 **取值范围：** 1~2147483647。 **默认取值：** 默认为空，表示维持原值。
        :type ttl: int
        """
        
        

        self._description = None
        self._email = None
        self._ttl = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if email is not None:
            self.email = email
        if ttl is not None:
            self.ttl = ttl

    @property
    def description(self):
        r"""Gets the description of this UpdatePublicZoneInfo.

        **参数解释：** 域名的描述信息。 **约束限制：** 不涉及。 **取值范围：** 长度不超过255个字符。 **默认取值：** 默认为空，表示维持原值。

        :return: The description of this UpdatePublicZoneInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdatePublicZoneInfo.

        **参数解释：** 域名的描述信息。 **约束限制：** 不涉及。 **取值范围：** 长度不超过255个字符。 **默认取值：** 默认为空，表示维持原值。

        :param description: The description of this UpdatePublicZoneInfo.
        :type description: str
        """
        self._description = description

    @property
    def email(self):
        r"""Gets the email of this UpdatePublicZoneInfo.

        **参数解释：** 管理该域名的管理员邮箱，用于生成该域名的SOA记录。   **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 默认为空，表示维持原值。

        :return: The email of this UpdatePublicZoneInfo.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        r"""Sets the email of this UpdatePublicZoneInfo.

        **参数解释：** 管理该域名的管理员邮箱，用于生成该域名的SOA记录。   **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 默认为空，表示维持原值。

        :param email: The email of this UpdatePublicZoneInfo.
        :type email: str
        """
        self._email = email

    @property
    def ttl(self):
        r"""Gets the ttl of this UpdatePublicZoneInfo.

        **参数解释：** 用于填写默认生成的SOA记录中有效缓存时间，以秒为单位。 **约束限制：** 不涉及。 **取值范围：** 1~2147483647。 **默认取值：** 默认为空，表示维持原值。

        :return: The ttl of this UpdatePublicZoneInfo.
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        r"""Sets the ttl of this UpdatePublicZoneInfo.

        **参数解释：** 用于填写默认生成的SOA记录中有效缓存时间，以秒为单位。 **约束限制：** 不涉及。 **取值范围：** 1~2147483647。 **默认取值：** 默认为空，表示维持原值。

        :param ttl: The ttl of this UpdatePublicZoneInfo.
        :type ttl: int
        """
        self._ttl = ttl

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
        if not isinstance(other, UpdatePublicZoneInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
