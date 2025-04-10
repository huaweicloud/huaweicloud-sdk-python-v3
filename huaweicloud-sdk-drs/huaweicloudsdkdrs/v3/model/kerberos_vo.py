# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KerberosVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'krb5_conf_file': 'str',
        'key_tab_file': 'str',
        'domain_name': 'str',
        'user_principal': 'str'
    }

    attribute_map = {
        'krb5_conf_file': 'krb5_conf_file',
        'key_tab_file': 'key_tab_file',
        'domain_name': 'domain_name',
        'user_principal': 'user_principal'
    }

    def __init__(self, krb5_conf_file=None, key_tab_file=None, domain_name=None, user_principal=None):
        r"""KerberosVO

        The model defined in huaweicloud sdk

        :param krb5_conf_file: krb5配置文件
        :type krb5_conf_file: str
        :param key_tab_file: key文件
        :type key_tab_file: str
        :param domain_name: 域名
        :type domain_name: str
        :param user_principal: Kerberos用户对象
        :type user_principal: str
        """
        
        

        self._krb5_conf_file = None
        self._key_tab_file = None
        self._domain_name = None
        self._user_principal = None
        self.discriminator = None

        if krb5_conf_file is not None:
            self.krb5_conf_file = krb5_conf_file
        if key_tab_file is not None:
            self.key_tab_file = key_tab_file
        if domain_name is not None:
            self.domain_name = domain_name
        if user_principal is not None:
            self.user_principal = user_principal

    @property
    def krb5_conf_file(self):
        r"""Gets the krb5_conf_file of this KerberosVO.

        krb5配置文件

        :return: The krb5_conf_file of this KerberosVO.
        :rtype: str
        """
        return self._krb5_conf_file

    @krb5_conf_file.setter
    def krb5_conf_file(self, krb5_conf_file):
        r"""Sets the krb5_conf_file of this KerberosVO.

        krb5配置文件

        :param krb5_conf_file: The krb5_conf_file of this KerberosVO.
        :type krb5_conf_file: str
        """
        self._krb5_conf_file = krb5_conf_file

    @property
    def key_tab_file(self):
        r"""Gets the key_tab_file of this KerberosVO.

        key文件

        :return: The key_tab_file of this KerberosVO.
        :rtype: str
        """
        return self._key_tab_file

    @key_tab_file.setter
    def key_tab_file(self, key_tab_file):
        r"""Sets the key_tab_file of this KerberosVO.

        key文件

        :param key_tab_file: The key_tab_file of this KerberosVO.
        :type key_tab_file: str
        """
        self._key_tab_file = key_tab_file

    @property
    def domain_name(self):
        r"""Gets the domain_name of this KerberosVO.

        域名

        :return: The domain_name of this KerberosVO.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this KerberosVO.

        域名

        :param domain_name: The domain_name of this KerberosVO.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def user_principal(self):
        r"""Gets the user_principal of this KerberosVO.

        Kerberos用户对象

        :return: The user_principal of this KerberosVO.
        :rtype: str
        """
        return self._user_principal

    @user_principal.setter
    def user_principal(self, user_principal):
        r"""Sets the user_principal of this KerberosVO.

        Kerberos用户对象

        :param user_principal: The user_principal of this KerberosVO.
        :type user_principal: str
        """
        self._user_principal = user_principal

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
        if not isinstance(other, KerberosVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
