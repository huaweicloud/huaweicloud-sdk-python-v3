# coding: utf-8

import re
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
        """UpdatePublicZoneInfo

        The model defined in huaweicloud sdk

        :param description: 域名的描述信息。长度不超过255个字符。
        :type description: str
        :param email: 管理该zone的管理员邮箱。  如果为空，表示维持原值。  默认值为空。
        :type email: str
        :param ttl: 用于填写默认生成的SOA记录中有效缓存时间，以秒为单位。
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
        """Gets the description of this UpdatePublicZoneInfo.

        域名的描述信息。长度不超过255个字符。

        :return: The description of this UpdatePublicZoneInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdatePublicZoneInfo.

        域名的描述信息。长度不超过255个字符。

        :param description: The description of this UpdatePublicZoneInfo.
        :type description: str
        """
        self._description = description

    @property
    def email(self):
        """Gets the email of this UpdatePublicZoneInfo.

        管理该zone的管理员邮箱。  如果为空，表示维持原值。  默认值为空。

        :return: The email of this UpdatePublicZoneInfo.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UpdatePublicZoneInfo.

        管理该zone的管理员邮箱。  如果为空，表示维持原值。  默认值为空。

        :param email: The email of this UpdatePublicZoneInfo.
        :type email: str
        """
        self._email = email

    @property
    def ttl(self):
        """Gets the ttl of this UpdatePublicZoneInfo.

        用于填写默认生成的SOA记录中有效缓存时间，以秒为单位。

        :return: The ttl of this UpdatePublicZoneInfo.
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """Sets the ttl of this UpdatePublicZoneInfo.

        用于填写默认生成的SOA记录中有效缓存时间，以秒为单位。

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
