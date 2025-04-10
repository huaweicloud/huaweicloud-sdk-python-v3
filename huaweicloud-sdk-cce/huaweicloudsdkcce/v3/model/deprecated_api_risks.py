# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeprecatedAPIRisks:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'url': 'str',
        'user_agent': 'str'
    }

    attribute_map = {
        'url': 'url',
        'user_agent': 'userAgent'
    }

    def __init__(self, url=None, user_agent=None):
        r"""DeprecatedAPIRisks

        The model defined in huaweicloud sdk

        :param url: 请求路径，如/apis/policy/v1beta1/podsecuritypolicies
        :type url: str
        :param user_agent: 客户端信息
        :type user_agent: str
        """
        
        

        self._url = None
        self._user_agent = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if user_agent is not None:
            self.user_agent = user_agent

    @property
    def url(self):
        r"""Gets the url of this DeprecatedAPIRisks.

        请求路径，如/apis/policy/v1beta1/podsecuritypolicies

        :return: The url of this DeprecatedAPIRisks.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this DeprecatedAPIRisks.

        请求路径，如/apis/policy/v1beta1/podsecuritypolicies

        :param url: The url of this DeprecatedAPIRisks.
        :type url: str
        """
        self._url = url

    @property
    def user_agent(self):
        r"""Gets the user_agent of this DeprecatedAPIRisks.

        客户端信息

        :return: The user_agent of this DeprecatedAPIRisks.
        :rtype: str
        """
        return self._user_agent

    @user_agent.setter
    def user_agent(self, user_agent):
        r"""Sets the user_agent of this DeprecatedAPIRisks.

        客户端信息

        :param user_agent: The user_agent of this DeprecatedAPIRisks.
        :type user_agent: str
        """
        self._user_agent = user_agent

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
        if not isinstance(other, DeprecatedAPIRisks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
