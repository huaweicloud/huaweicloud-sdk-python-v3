# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AuthorizeDomainsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_name': 'str',
        'auth_mode': 'str'
    }

    attribute_map = {
        'domain_name': 'domain_name',
        'auth_mode': 'auth_mode'
    }

    def __init__(self, domain_name=None, auth_mode=None):
        """AuthorizeDomainsRequestBody

        The model defined in huaweicloud sdk

        :param domain_name: 域名
        :type domain_name: str
        :param auth_mode: 认证方式:   * file - 文件认证   * auto - 一键认证   * free - 免认证，选择此项默认已阅读并了解下述使用要求           使用须知：           1、您的账号已完成实名认证，且非受限账号。           2、您确认您已获得对扫描对象进行扫描的相关合法权利。           3、您确认您的扫描行为有合法合理目的，且符合适用的法律法规要求，不得利用本服务从事任何黑灰产等非法活动。           4、若您违反上述承诺，我们有权立即终止您对本服务的使用，并要求您对我们及相关第三方因此遭受的损失进行赔偿。 
        :type auth_mode: str
        """
        
        

        self._domain_name = None
        self._auth_mode = None
        self.discriminator = None

        self.domain_name = domain_name
        if auth_mode is not None:
            self.auth_mode = auth_mode

    @property
    def domain_name(self):
        """Gets the domain_name of this AuthorizeDomainsRequestBody.

        域名

        :return: The domain_name of this AuthorizeDomainsRequestBody.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this AuthorizeDomainsRequestBody.

        域名

        :param domain_name: The domain_name of this AuthorizeDomainsRequestBody.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def auth_mode(self):
        """Gets the auth_mode of this AuthorizeDomainsRequestBody.

        认证方式:   * file - 文件认证   * auto - 一键认证   * free - 免认证，选择此项默认已阅读并了解下述使用要求           使用须知：           1、您的账号已完成实名认证，且非受限账号。           2、您确认您已获得对扫描对象进行扫描的相关合法权利。           3、您确认您的扫描行为有合法合理目的，且符合适用的法律法规要求，不得利用本服务从事任何黑灰产等非法活动。           4、若您违反上述承诺，我们有权立即终止您对本服务的使用，并要求您对我们及相关第三方因此遭受的损失进行赔偿。 

        :return: The auth_mode of this AuthorizeDomainsRequestBody.
        :rtype: str
        """
        return self._auth_mode

    @auth_mode.setter
    def auth_mode(self, auth_mode):
        """Sets the auth_mode of this AuthorizeDomainsRequestBody.

        认证方式:   * file - 文件认证   * auto - 一键认证   * free - 免认证，选择此项默认已阅读并了解下述使用要求           使用须知：           1、您的账号已完成实名认证，且非受限账号。           2、您确认您已获得对扫描对象进行扫描的相关合法权利。           3、您确认您的扫描行为有合法合理目的，且符合适用的法律法规要求，不得利用本服务从事任何黑灰产等非法活动。           4、若您违反上述承诺，我们有权立即终止您对本服务的使用，并要求您对我们及相关第三方因此遭受的损失进行赔偿。 

        :param auth_mode: The auth_mode of this AuthorizeDomainsRequestBody.
        :type auth_mode: str
        """
        self._auth_mode = auth_mode

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
        if not isinstance(other, AuthorizeDomainsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
