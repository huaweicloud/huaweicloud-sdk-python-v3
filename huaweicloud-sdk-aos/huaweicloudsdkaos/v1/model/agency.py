# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Agency:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'provider_name': 'str',
        'agency_name': 'str'
    }

    attribute_map = {
        'provider_name': 'provider_name',
        'agency_name': 'agency_name'
    }

    def __init__(self, provider_name=None, agency_name=None):
        """Agency

        The model defined in huaweicloud sdk

        :param provider_name: 用户使用的provider的名字。如果用户给与的provider_name含有重复的值，则返回400
        :type provider_name: str
        :param agency_name: 对应provider所使用的IAM委托名称，资源编排服务会使用此委托的权限去访问、创建对应provider的资源
        :type agency_name: str
        """
        
        

        self._provider_name = None
        self._agency_name = None
        self.discriminator = None

        self.provider_name = provider_name
        self.agency_name = agency_name

    @property
    def provider_name(self):
        """Gets the provider_name of this Agency.

        用户使用的provider的名字。如果用户给与的provider_name含有重复的值，则返回400

        :return: The provider_name of this Agency.
        :rtype: str
        """
        return self._provider_name

    @provider_name.setter
    def provider_name(self, provider_name):
        """Sets the provider_name of this Agency.

        用户使用的provider的名字。如果用户给与的provider_name含有重复的值，则返回400

        :param provider_name: The provider_name of this Agency.
        :type provider_name: str
        """
        self._provider_name = provider_name

    @property
    def agency_name(self):
        """Gets the agency_name of this Agency.

        对应provider所使用的IAM委托名称，资源编排服务会使用此委托的权限去访问、创建对应provider的资源

        :return: The agency_name of this Agency.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        """Sets the agency_name of this Agency.

        对应provider所使用的IAM委托名称，资源编排服务会使用此委托的权限去访问、创建对应provider的资源

        :param agency_name: The agency_name of this Agency.
        :type agency_name: str
        """
        self._agency_name = agency_name

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
        if not isinstance(other, Agency):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
