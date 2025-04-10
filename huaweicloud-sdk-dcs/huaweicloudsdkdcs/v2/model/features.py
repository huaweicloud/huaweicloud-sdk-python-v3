# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Features:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'support_acl': 'bool',
        'support_transparent_client_ip': 'bool',
        'support_ssl': 'bool',
        'support_audit_log': 'bool'
    }

    attribute_map = {
        'support_acl': 'support_acl',
        'support_transparent_client_ip': 'support_transparent_client_ip',
        'support_ssl': 'support_ssl',
        'support_audit_log': 'support_audit_log'
    }

    def __init__(self, support_acl=None, support_transparent_client_ip=None, support_ssl=None, support_audit_log=None):
        r"""Features

        The model defined in huaweicloud sdk

        :param support_acl: 是否支持acl - true：是 - false：否 
        :type support_acl: bool
        :param support_transparent_client_ip: 实例是否支持客户端ip透传 - true：是 - false：否 
        :type support_transparent_client_ip: bool
        :param support_ssl: 是否支持SSL - true：是 - false：否 
        :type support_ssl: bool
        :param support_audit_log: 是否支持审计日志 - true: 是 - false: 否 
        :type support_audit_log: bool
        """
        
        

        self._support_acl = None
        self._support_transparent_client_ip = None
        self._support_ssl = None
        self._support_audit_log = None
        self.discriminator = None

        if support_acl is not None:
            self.support_acl = support_acl
        if support_transparent_client_ip is not None:
            self.support_transparent_client_ip = support_transparent_client_ip
        if support_ssl is not None:
            self.support_ssl = support_ssl
        if support_audit_log is not None:
            self.support_audit_log = support_audit_log

    @property
    def support_acl(self):
        r"""Gets the support_acl of this Features.

        是否支持acl - true：是 - false：否 

        :return: The support_acl of this Features.
        :rtype: bool
        """
        return self._support_acl

    @support_acl.setter
    def support_acl(self, support_acl):
        r"""Sets the support_acl of this Features.

        是否支持acl - true：是 - false：否 

        :param support_acl: The support_acl of this Features.
        :type support_acl: bool
        """
        self._support_acl = support_acl

    @property
    def support_transparent_client_ip(self):
        r"""Gets the support_transparent_client_ip of this Features.

        实例是否支持客户端ip透传 - true：是 - false：否 

        :return: The support_transparent_client_ip of this Features.
        :rtype: bool
        """
        return self._support_transparent_client_ip

    @support_transparent_client_ip.setter
    def support_transparent_client_ip(self, support_transparent_client_ip):
        r"""Sets the support_transparent_client_ip of this Features.

        实例是否支持客户端ip透传 - true：是 - false：否 

        :param support_transparent_client_ip: The support_transparent_client_ip of this Features.
        :type support_transparent_client_ip: bool
        """
        self._support_transparent_client_ip = support_transparent_client_ip

    @property
    def support_ssl(self):
        r"""Gets the support_ssl of this Features.

        是否支持SSL - true：是 - false：否 

        :return: The support_ssl of this Features.
        :rtype: bool
        """
        return self._support_ssl

    @support_ssl.setter
    def support_ssl(self, support_ssl):
        r"""Sets the support_ssl of this Features.

        是否支持SSL - true：是 - false：否 

        :param support_ssl: The support_ssl of this Features.
        :type support_ssl: bool
        """
        self._support_ssl = support_ssl

    @property
    def support_audit_log(self):
        r"""Gets the support_audit_log of this Features.

        是否支持审计日志 - true: 是 - false: 否 

        :return: The support_audit_log of this Features.
        :rtype: bool
        """
        return self._support_audit_log

    @support_audit_log.setter
    def support_audit_log(self, support_audit_log):
        r"""Sets the support_audit_log of this Features.

        是否支持审计日志 - true: 是 - false: 否 

        :param support_audit_log: The support_audit_log of this Features.
        :type support_audit_log: bool
        """
        self._support_audit_log = support_audit_log

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
        if not isinstance(other, Features):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
