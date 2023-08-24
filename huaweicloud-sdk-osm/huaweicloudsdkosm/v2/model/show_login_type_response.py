# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowLoginTypeResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'login_type': 'str'
    }

    attribute_map = {
        'login_type': 'login_type'
    }

    def __init__(self, login_type=None):
        """ShowLoginTypeResponse

        The model defined in huaweicloud sdk

        :param login_type: 登录类型
        :type login_type: str
        """
        
        super(ShowLoginTypeResponse, self).__init__()

        self._login_type = None
        self.discriminator = None

        if login_type is not None:
            self.login_type = login_type

    @property
    def login_type(self):
        """Gets the login_type of this ShowLoginTypeResponse.

        登录类型

        :return: The login_type of this ShowLoginTypeResponse.
        :rtype: str
        """
        return self._login_type

    @login_type.setter
    def login_type(self, login_type):
        """Sets the login_type of this ShowLoginTypeResponse.

        登录类型

        :param login_type: The login_type of this ShowLoginTypeResponse.
        :type login_type: str
        """
        self._login_type = login_type

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
        if not isinstance(other, ShowLoginTypeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
