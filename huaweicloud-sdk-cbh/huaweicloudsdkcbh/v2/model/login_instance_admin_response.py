# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LoginInstanceAdminResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'admin_url': 'str'
    }

    attribute_map = {
        'admin_url': 'admin_url'
    }

    def __init__(self, admin_url=None):
        """LoginInstanceAdminResponse

        The model defined in huaweicloud sdk

        :param admin_url: 云堡垒机登录admin链接。
        :type admin_url: str
        """
        
        super(LoginInstanceAdminResponse, self).__init__()

        self._admin_url = None
        self.discriminator = None

        if admin_url is not None:
            self.admin_url = admin_url

    @property
    def admin_url(self):
        """Gets the admin_url of this LoginInstanceAdminResponse.

        云堡垒机登录admin链接。

        :return: The admin_url of this LoginInstanceAdminResponse.
        :rtype: str
        """
        return self._admin_url

    @admin_url.setter
    def admin_url(self, admin_url):
        """Sets the admin_url of this LoginInstanceAdminResponse.

        云堡垒机登录admin链接。

        :param admin_url: The admin_url of this LoginInstanceAdminResponse.
        :type admin_url: str
        """
        self._admin_url = admin_url

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
        if not isinstance(other, LoginInstanceAdminResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
