# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AllowUserBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'manage_accesskey': 'bool',
        'manage_email': 'bool',
        'manage_mobile': 'bool',
        'manage_password': 'bool'
    }

    attribute_map = {
        'manage_accesskey': 'manage_accesskey',
        'manage_email': 'manage_email',
        'manage_mobile': 'manage_mobile',
        'manage_password': 'manage_password'
    }

    def __init__(self, manage_accesskey=None, manage_email=None, manage_mobile=None, manage_password=None):
        """AllowUserBody

        The model defined in huaweicloud sdk

        :param manage_accesskey: 是否允许子用户自行管理AK，取值范围true或false。
        :type manage_accesskey: bool
        :param manage_email: 是否允许子用户自己修改邮箱，取值范围true或false。
        :type manage_email: bool
        :param manage_mobile: 是否允许子用户自己修改电话，取值范围true或false。
        :type manage_mobile: bool
        :param manage_password: 是否允许子用户自己修改密码，取值范围true或false。
        :type manage_password: bool
        """
        
        

        self._manage_accesskey = None
        self._manage_email = None
        self._manage_mobile = None
        self._manage_password = None
        self.discriminator = None

        if manage_accesskey is not None:
            self.manage_accesskey = manage_accesskey
        if manage_email is not None:
            self.manage_email = manage_email
        if manage_mobile is not None:
            self.manage_mobile = manage_mobile
        if manage_password is not None:
            self.manage_password = manage_password

    @property
    def manage_accesskey(self):
        """Gets the manage_accesskey of this AllowUserBody.

        是否允许子用户自行管理AK，取值范围true或false。

        :return: The manage_accesskey of this AllowUserBody.
        :rtype: bool
        """
        return self._manage_accesskey

    @manage_accesskey.setter
    def manage_accesskey(self, manage_accesskey):
        """Sets the manage_accesskey of this AllowUserBody.

        是否允许子用户自行管理AK，取值范围true或false。

        :param manage_accesskey: The manage_accesskey of this AllowUserBody.
        :type manage_accesskey: bool
        """
        self._manage_accesskey = manage_accesskey

    @property
    def manage_email(self):
        """Gets the manage_email of this AllowUserBody.

        是否允许子用户自己修改邮箱，取值范围true或false。

        :return: The manage_email of this AllowUserBody.
        :rtype: bool
        """
        return self._manage_email

    @manage_email.setter
    def manage_email(self, manage_email):
        """Sets the manage_email of this AllowUserBody.

        是否允许子用户自己修改邮箱，取值范围true或false。

        :param manage_email: The manage_email of this AllowUserBody.
        :type manage_email: bool
        """
        self._manage_email = manage_email

    @property
    def manage_mobile(self):
        """Gets the manage_mobile of this AllowUserBody.

        是否允许子用户自己修改电话，取值范围true或false。

        :return: The manage_mobile of this AllowUserBody.
        :rtype: bool
        """
        return self._manage_mobile

    @manage_mobile.setter
    def manage_mobile(self, manage_mobile):
        """Sets the manage_mobile of this AllowUserBody.

        是否允许子用户自己修改电话，取值范围true或false。

        :param manage_mobile: The manage_mobile of this AllowUserBody.
        :type manage_mobile: bool
        """
        self._manage_mobile = manage_mobile

    @property
    def manage_password(self):
        """Gets the manage_password of this AllowUserBody.

        是否允许子用户自己修改密码，取值范围true或false。

        :return: The manage_password of this AllowUserBody.
        :rtype: bool
        """
        return self._manage_password

    @manage_password.setter
    def manage_password(self, manage_password):
        """Sets the manage_password of this AllowUserBody.

        是否允许子用户自己修改密码，取值范围true或false。

        :param manage_password: The manage_password of this AllowUserBody.
        :type manage_password: bool
        """
        self._manage_password = manage_password

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
        if not isinstance(other, AllowUserBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
