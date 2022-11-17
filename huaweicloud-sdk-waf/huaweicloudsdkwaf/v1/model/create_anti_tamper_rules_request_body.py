# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAntiTamperRulesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'hostname': 'str',
        'url': 'str',
        'description': 'str'
    }

    attribute_map = {
        'hostname': 'hostname',
        'url': 'url',
        'description': 'description'
    }

    def __init__(self, hostname=None, url=None, description=None):
        """CreateAntiTamperRulesRequestBody

        The model defined in huaweicloud sdk

        :param hostname: 防护网站，查询云模式防护域名列表（ListHost）接口获取防护域名，响应体中的的hostname字段
        :type hostname: str
        :param url: 防篡改规则防护的url，需要填写标准的url格式，例如/admin/xxx或者/admin/*,以\&quot;*\&quot;号结尾代表路径前缀
        :type url: str
        :param description: 规则描述
        :type description: str
        """
        
        

        self._hostname = None
        self._url = None
        self._description = None
        self.discriminator = None

        self.hostname = hostname
        self.url = url
        if description is not None:
            self.description = description

    @property
    def hostname(self):
        """Gets the hostname of this CreateAntiTamperRulesRequestBody.

        防护网站，查询云模式防护域名列表（ListHost）接口获取防护域名，响应体中的的hostname字段

        :return: The hostname of this CreateAntiTamperRulesRequestBody.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this CreateAntiTamperRulesRequestBody.

        防护网站，查询云模式防护域名列表（ListHost）接口获取防护域名，响应体中的的hostname字段

        :param hostname: The hostname of this CreateAntiTamperRulesRequestBody.
        :type hostname: str
        """
        self._hostname = hostname

    @property
    def url(self):
        """Gets the url of this CreateAntiTamperRulesRequestBody.

        防篡改规则防护的url，需要填写标准的url格式，例如/admin/xxx或者/admin/*,以\"*\"号结尾代表路径前缀

        :return: The url of this CreateAntiTamperRulesRequestBody.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this CreateAntiTamperRulesRequestBody.

        防篡改规则防护的url，需要填写标准的url格式，例如/admin/xxx或者/admin/*,以\"*\"号结尾代表路径前缀

        :param url: The url of this CreateAntiTamperRulesRequestBody.
        :type url: str
        """
        self._url = url

    @property
    def description(self):
        """Gets the description of this CreateAntiTamperRulesRequestBody.

        规则描述

        :return: The description of this CreateAntiTamperRulesRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateAntiTamperRulesRequestBody.

        规则描述

        :param description: The description of this CreateAntiTamperRulesRequestBody.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, CreateAntiTamperRulesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
