# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AdDomainInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_type': 'str',
        'domain_admin_account': 'str',
        'domain_password': 'str'
    }

    attribute_map = {
        'domain_type': 'domain_type',
        'domain_admin_account': 'domain_admin_account',
        'domain_password': 'domain_password'
    }

    def __init__(self, domain_type=None, domain_admin_account=None, domain_password=None):
        """AdDomainInfo

        The model defined in huaweicloud sdk

        :param domain_type: 域类型。 - LITE_AS：LiteAS。 - LOCAL_AD：本地AD。 说明：域类型为“LOCAL_AD”时，请确保所选VPC网络与“LOCAL_AD”所属网络可连通。
        :type domain_type: str
        :param domain_admin_account: 域管理员帐号。
        :type domain_admin_account: str
        :param domain_password: 域管理员账号密码。
        :type domain_password: str
        """
        
        

        self._domain_type = None
        self._domain_admin_account = None
        self._domain_password = None
        self.discriminator = None

        self.domain_type = domain_type
        self.domain_admin_account = domain_admin_account
        self.domain_password = domain_password

    @property
    def domain_type(self):
        """Gets the domain_type of this AdDomainInfo.

        域类型。 - LITE_AS：LiteAS。 - LOCAL_AD：本地AD。 说明：域类型为“LOCAL_AD”时，请确保所选VPC网络与“LOCAL_AD”所属网络可连通。

        :return: The domain_type of this AdDomainInfo.
        :rtype: str
        """
        return self._domain_type

    @domain_type.setter
    def domain_type(self, domain_type):
        """Sets the domain_type of this AdDomainInfo.

        域类型。 - LITE_AS：LiteAS。 - LOCAL_AD：本地AD。 说明：域类型为“LOCAL_AD”时，请确保所选VPC网络与“LOCAL_AD”所属网络可连通。

        :param domain_type: The domain_type of this AdDomainInfo.
        :type domain_type: str
        """
        self._domain_type = domain_type

    @property
    def domain_admin_account(self):
        """Gets the domain_admin_account of this AdDomainInfo.

        域管理员帐号。

        :return: The domain_admin_account of this AdDomainInfo.
        :rtype: str
        """
        return self._domain_admin_account

    @domain_admin_account.setter
    def domain_admin_account(self, domain_admin_account):
        """Sets the domain_admin_account of this AdDomainInfo.

        域管理员帐号。

        :param domain_admin_account: The domain_admin_account of this AdDomainInfo.
        :type domain_admin_account: str
        """
        self._domain_admin_account = domain_admin_account

    @property
    def domain_password(self):
        """Gets the domain_password of this AdDomainInfo.

        域管理员账号密码。

        :return: The domain_password of this AdDomainInfo.
        :rtype: str
        """
        return self._domain_password

    @domain_password.setter
    def domain_password(self, domain_password):
        """Sets the domain_password of this AdDomainInfo.

        域管理员账号密码。

        :param domain_password: The domain_password of this AdDomainInfo.
        :type domain_password: str
        """
        self._domain_password = domain_password

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
        if not isinstance(other, AdDomainInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
