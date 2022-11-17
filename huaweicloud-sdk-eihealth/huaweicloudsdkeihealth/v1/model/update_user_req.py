# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateUserReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'mobile': 'str',
        'areacode': 'str',
        'email': 'str',
        'ticket': 'str'
    }

    attribute_map = {
        'mobile': 'mobile',
        'areacode': 'areacode',
        'email': 'email',
        'ticket': 'ticket'
    }

    def __init__(self, mobile=None, areacode=None, email=None, ticket=None):
        """UpdateUserReq

        The model defined in huaweicloud sdk

        :param mobile: 用户手机号，纯数字，长度小于等于32位。必须与国家码同时存在。
        :type mobile: str
        :param areacode: 国家码。中国大陆为“0086”
        :type areacode: str
        :param email: 用户邮箱，需符合邮箱格式
        :type email: str
        :param ticket: 预验证凭证
        :type ticket: str
        """
        
        

        self._mobile = None
        self._areacode = None
        self._email = None
        self._ticket = None
        self.discriminator = None

        if mobile is not None:
            self.mobile = mobile
        if areacode is not None:
            self.areacode = areacode
        if email is not None:
            self.email = email
        if ticket is not None:
            self.ticket = ticket

    @property
    def mobile(self):
        """Gets the mobile of this UpdateUserReq.

        用户手机号，纯数字，长度小于等于32位。必须与国家码同时存在。

        :return: The mobile of this UpdateUserReq.
        :rtype: str
        """
        return self._mobile

    @mobile.setter
    def mobile(self, mobile):
        """Sets the mobile of this UpdateUserReq.

        用户手机号，纯数字，长度小于等于32位。必须与国家码同时存在。

        :param mobile: The mobile of this UpdateUserReq.
        :type mobile: str
        """
        self._mobile = mobile

    @property
    def areacode(self):
        """Gets the areacode of this UpdateUserReq.

        国家码。中国大陆为“0086”

        :return: The areacode of this UpdateUserReq.
        :rtype: str
        """
        return self._areacode

    @areacode.setter
    def areacode(self, areacode):
        """Sets the areacode of this UpdateUserReq.

        国家码。中国大陆为“0086”

        :param areacode: The areacode of this UpdateUserReq.
        :type areacode: str
        """
        self._areacode = areacode

    @property
    def email(self):
        """Gets the email of this UpdateUserReq.

        用户邮箱，需符合邮箱格式

        :return: The email of this UpdateUserReq.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UpdateUserReq.

        用户邮箱，需符合邮箱格式

        :param email: The email of this UpdateUserReq.
        :type email: str
        """
        self._email = email

    @property
    def ticket(self):
        """Gets the ticket of this UpdateUserReq.

        预验证凭证

        :return: The ticket of this UpdateUserReq.
        :rtype: str
        """
        return self._ticket

    @ticket.setter
    def ticket(self, ticket):
        """Sets the ticket of this UpdateUserReq.

        预验证凭证

        :param ticket: The ticket of this UpdateUserReq.
        :type ticket: str
        """
        self._ticket = ticket

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
        if not isinstance(other, UpdateUserReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
