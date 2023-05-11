# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetadataInstall:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_data': 'str'
    }

    attribute_map = {
        'user_data': 'user_data'
    }

    def __init__(self, user_data=None):
        """MetadataInstall

        The model defined in huaweicloud sdk

        :param user_data: 重装裸金属服务器过程中注入Linux镜像root密码，用户自定义初始化密码。注：修改密码脚本需经Base64编码。建议密码复杂度如下：长度为8-26位。密码至少必须包含大写字母（A-Z）、小写字母（a-z）、数字（0-9）和特殊字符（!@$%^-_&#x3D;+[{}]:,./?）中的三种
        :type user_data: str
        """
        
        

        self._user_data = None
        self.discriminator = None

        if user_data is not None:
            self.user_data = user_data

    @property
    def user_data(self):
        """Gets the user_data of this MetadataInstall.

        重装裸金属服务器过程中注入Linux镜像root密码，用户自定义初始化密码。注：修改密码脚本需经Base64编码。建议密码复杂度如下：长度为8-26位。密码至少必须包含大写字母（A-Z）、小写字母（a-z）、数字（0-9）和特殊字符（!@$%^-_=+[{}]:,./?）中的三种

        :return: The user_data of this MetadataInstall.
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this MetadataInstall.

        重装裸金属服务器过程中注入Linux镜像root密码，用户自定义初始化密码。注：修改密码脚本需经Base64编码。建议密码复杂度如下：长度为8-26位。密码至少必须包含大写字母（A-Z）、小写字母（a-z）、数字（0-9）和特殊字符（!@$%^-_=+[{}]:,./?）中的三种

        :param user_data: The user_data of this MetadataInstall.
        :type user_data: str
        """
        self._user_data = user_data

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
        if not isinstance(other, MetadataInstall):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
