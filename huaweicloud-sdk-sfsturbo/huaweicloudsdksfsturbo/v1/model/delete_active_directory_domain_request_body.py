# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteActiveDirectoryDomainRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service_account': 'str',
        'password': 'str'
    }

    attribute_map = {
        'service_account': 'service_account',
        'password': 'password'
    }

    def __init__(self, service_account=None, password=None):
        r"""DeleteActiveDirectoryDomainRequestBody

        The model defined in huaweicloud sdk

        :param service_account: 服务账号，在创建域服务器时指定，一般默认为administrator
        :type service_account: str
        :param password: 账号对应密码
        :type password: str
        """
        
        

        self._service_account = None
        self._password = None
        self.discriminator = None

        self.service_account = service_account
        self.password = password

    @property
    def service_account(self):
        r"""Gets the service_account of this DeleteActiveDirectoryDomainRequestBody.

        服务账号，在创建域服务器时指定，一般默认为administrator

        :return: The service_account of this DeleteActiveDirectoryDomainRequestBody.
        :rtype: str
        """
        return self._service_account

    @service_account.setter
    def service_account(self, service_account):
        r"""Sets the service_account of this DeleteActiveDirectoryDomainRequestBody.

        服务账号，在创建域服务器时指定，一般默认为administrator

        :param service_account: The service_account of this DeleteActiveDirectoryDomainRequestBody.
        :type service_account: str
        """
        self._service_account = service_account

    @property
    def password(self):
        r"""Gets the password of this DeleteActiveDirectoryDomainRequestBody.

        账号对应密码

        :return: The password of this DeleteActiveDirectoryDomainRequestBody.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        r"""Sets the password of this DeleteActiveDirectoryDomainRequestBody.

        账号对应密码

        :param password: The password of this DeleteActiveDirectoryDomainRequestBody.
        :type password: str
        """
        self._password = password

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
        if not isinstance(other, DeleteActiveDirectoryDomainRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
