# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SignInOptionsDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'origin': 'str',
        'application_url': 'str'
    }

    attribute_map = {
        'origin': 'origin',
        'application_url': 'application_url'
    }

    def __init__(self, origin=None, application_url=None):
        r"""SignInOptionsDto

        The model defined in huaweicloud sdk

        :param origin: IAM身份中心跳转应用程序的方式
        :type origin: str
        :param application_url: 接受应用程序身份验证请求的Url
        :type application_url: str
        """
        
        

        self._origin = None
        self._application_url = None
        self.discriminator = None

        self.origin = origin
        if application_url is not None:
            self.application_url = application_url

    @property
    def origin(self):
        r"""Gets the origin of this SignInOptionsDto.

        IAM身份中心跳转应用程序的方式

        :return: The origin of this SignInOptionsDto.
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        r"""Sets the origin of this SignInOptionsDto.

        IAM身份中心跳转应用程序的方式

        :param origin: The origin of this SignInOptionsDto.
        :type origin: str
        """
        self._origin = origin

    @property
    def application_url(self):
        r"""Gets the application_url of this SignInOptionsDto.

        接受应用程序身份验证请求的Url

        :return: The application_url of this SignInOptionsDto.
        :rtype: str
        """
        return self._application_url

    @application_url.setter
    def application_url(self, application_url):
        r"""Sets the application_url of this SignInOptionsDto.

        接受应用程序身份验证请求的Url

        :param application_url: The application_url of this SignInOptionsDto.
        :type application_url: str
        """
        self._application_url = application_url

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
        if not isinstance(other, SignInOptionsDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
