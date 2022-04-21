# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DomainNameEntity:

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
        'is_readonly': 'bool'
    }

    attribute_map = {
        'domain_name': 'domain_name',
        'is_readonly': 'is_readonly'
    }

    def __init__(self, domain_name=None, is_readonly=None):
        """DomainNameEntity

        The model defined in huaweicloud sdk

        :param domain_name: 实例历史域名。
        :type domain_name: str
        :param is_readonly: 是否只读域名 - true：是 - false：否 
        :type is_readonly: bool
        """
        
        

        self._domain_name = None
        self._is_readonly = None
        self.discriminator = None

        if domain_name is not None:
            self.domain_name = domain_name
        if is_readonly is not None:
            self.is_readonly = is_readonly

    @property
    def domain_name(self):
        """Gets the domain_name of this DomainNameEntity.

        实例历史域名。

        :return: The domain_name of this DomainNameEntity.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this DomainNameEntity.

        实例历史域名。

        :param domain_name: The domain_name of this DomainNameEntity.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def is_readonly(self):
        """Gets the is_readonly of this DomainNameEntity.

        是否只读域名 - true：是 - false：否 

        :return: The is_readonly of this DomainNameEntity.
        :rtype: bool
        """
        return self._is_readonly

    @is_readonly.setter
    def is_readonly(self, is_readonly):
        """Sets the is_readonly of this DomainNameEntity.

        是否只读域名 - true：是 - false：否 

        :param is_readonly: The is_readonly of this DomainNameEntity.
        :type is_readonly: bool
        """
        self._is_readonly = is_readonly

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
        if not isinstance(other, DomainNameEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
