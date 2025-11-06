# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateLoginProfileV5Response(SdkResponse):

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
        r"""CreateLoginProfileV5Response

        The model defined in huaweicloud sdk

        :param login_profile: 
        :type login_profile: :class:`huaweicloudsdkiam.v5.LoginProfile`
        """
        
        super().__init__()

        self._login_profile = None
        self.discriminator = None

        if login_profile is not None:
            self.login_profile = login_profile

    @property
    def login_profile(self):
        r"""Gets the login_profile of this CreateLoginProfileV5Response.

        :return: The login_profile of this CreateLoginProfileV5Response.
        :rtype: :class:`huaweicloudsdkiam.v5.LoginProfile`
        """
        return self._login_profile

    @login_profile.setter
    def login_profile(self, login_profile):
        r"""Sets the login_profile of this CreateLoginProfileV5Response.

        :param login_profile: The login_profile of this CreateLoginProfileV5Response.
        :type login_profile: :class:`huaweicloudsdkiam.v5.LoginProfile`
        """
        self._login_profile = login_profile

    def to_dict(self):
        import warnings
        warnings.warn("CreateLoginProfileV5Response.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateLoginProfileV5Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
