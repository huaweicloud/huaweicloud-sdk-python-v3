# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ADDomainInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_admin_account_name': 'str',
        'domain_admin_pwd': 'str'
    }

    attribute_map = {
        'domain_admin_account_name': 'domain_admin_account_name',
        'domain_admin_pwd': 'domain_admin_pwd'
    }

    def __init__(self, domain_admin_account_name=None, domain_admin_pwd=None):
        r"""ADDomainInfo

        The model defined in huaweicloud sdk

        :param domain_admin_account_name: 域管理员账号名
        :type domain_admin_account_name: str
        :param domain_admin_pwd: 域管理员密码
        :type domain_admin_pwd: str
        """
        
        

        self._domain_admin_account_name = None
        self._domain_admin_pwd = None
        self.discriminator = None

        self.domain_admin_account_name = domain_admin_account_name
        self.domain_admin_pwd = domain_admin_pwd

    @property
    def domain_admin_account_name(self):
        r"""Gets the domain_admin_account_name of this ADDomainInfo.

        域管理员账号名

        :return: The domain_admin_account_name of this ADDomainInfo.
        :rtype: str
        """
        return self._domain_admin_account_name

    @domain_admin_account_name.setter
    def domain_admin_account_name(self, domain_admin_account_name):
        r"""Sets the domain_admin_account_name of this ADDomainInfo.

        域管理员账号名

        :param domain_admin_account_name: The domain_admin_account_name of this ADDomainInfo.
        :type domain_admin_account_name: str
        """
        self._domain_admin_account_name = domain_admin_account_name

    @property
    def domain_admin_pwd(self):
        r"""Gets the domain_admin_pwd of this ADDomainInfo.

        域管理员密码

        :return: The domain_admin_pwd of this ADDomainInfo.
        :rtype: str
        """
        return self._domain_admin_pwd

    @domain_admin_pwd.setter
    def domain_admin_pwd(self, domain_admin_pwd):
        r"""Sets the domain_admin_pwd of this ADDomainInfo.

        域管理员密码

        :param domain_admin_pwd: The domain_admin_pwd of this ADDomainInfo.
        :type domain_admin_pwd: str
        """
        self._domain_admin_pwd = domain_admin_pwd

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
        if not isinstance(other, ADDomainInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
