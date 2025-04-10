# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowLoginProfileV5Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'login_profile': 'LoginProfile'
    }

    attribute_map = {
        'login_profile': 'login_profile'
    }

    def __init__(self, login_profile=None):
        r"""ShowLoginProfileV5Response

        The model defined in huaweicloud sdk

        :param login_profile: 
        :type login_profile: :class:`huaweicloudsdkiam.v5.LoginProfile`
        """
        
        super(ShowLoginProfileV5Response, self).__init__()

        self._login_profile = None
        self.discriminator = None

        if login_profile is not None:
            self.login_profile = login_profile

    @property
    def login_profile(self):
        r"""Gets the login_profile of this ShowLoginProfileV5Response.

        :return: The login_profile of this ShowLoginProfileV5Response.
        :rtype: :class:`huaweicloudsdkiam.v5.LoginProfile`
        """
        return self._login_profile

    @login_profile.setter
    def login_profile(self, login_profile):
        r"""Sets the login_profile of this ShowLoginProfileV5Response.

        :param login_profile: The login_profile of this ShowLoginProfileV5Response.
        :type login_profile: :class:`huaweicloudsdkiam.v5.LoginProfile`
        """
        self._login_profile = login_profile

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
        if not isinstance(other, ShowLoginProfileV5Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
