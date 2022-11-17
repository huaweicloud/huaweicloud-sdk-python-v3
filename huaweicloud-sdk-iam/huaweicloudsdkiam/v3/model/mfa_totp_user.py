# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MfaTotpUser:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'passcode': 'str'
    }

    attribute_map = {
        'id': 'id',
        'passcode': 'passcode'
    }

    def __init__(self, id=None, passcode=None):
        """MfaTotpUser

        The model defined in huaweicloud sdk

        :param id: 已开启虚拟MFA方式的登录保护的IAM用户ID。
        :type id: str
        :param passcode: 虚拟MFA验证码，在MFA应用程序中获取动态验证码，获取方法请参见：[如何获取虚拟MFA验证码](https://support.huaweicloud.com/iam_faq/iam_01_0001.html)。
        :type passcode: str
        """
        
        

        self._id = None
        self._passcode = None
        self.discriminator = None

        self.id = id
        self.passcode = passcode

    @property
    def id(self):
        """Gets the id of this MfaTotpUser.

        已开启虚拟MFA方式的登录保护的IAM用户ID。

        :return: The id of this MfaTotpUser.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MfaTotpUser.

        已开启虚拟MFA方式的登录保护的IAM用户ID。

        :param id: The id of this MfaTotpUser.
        :type id: str
        """
        self._id = id

    @property
    def passcode(self):
        """Gets the passcode of this MfaTotpUser.

        虚拟MFA验证码，在MFA应用程序中获取动态验证码，获取方法请参见：[如何获取虚拟MFA验证码](https://support.huaweicloud.com/iam_faq/iam_01_0001.html)。

        :return: The passcode of this MfaTotpUser.
        :rtype: str
        """
        return self._passcode

    @passcode.setter
    def passcode(self, passcode):
        """Sets the passcode of this MfaTotpUser.

        虚拟MFA验证码，在MFA应用程序中获取动态验证码，获取方法请参见：[如何获取虚拟MFA验证码](https://support.huaweicloud.com/iam_faq/iam_01_0001.html)。

        :param passcode: The passcode of this MfaTotpUser.
        :type passcode: str
        """
        self._passcode = passcode

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
        if not isinstance(other, MfaTotpUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
