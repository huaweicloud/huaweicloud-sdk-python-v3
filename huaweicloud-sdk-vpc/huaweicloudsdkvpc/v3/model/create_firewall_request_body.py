# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateFirewallRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'firewall': 'CreateFirewallOption',
        'dry_run': 'bool'
    }

    attribute_map = {
        'firewall': 'firewall',
        'dry_run': 'dry_run'
    }

    def __init__(self, firewall=None, dry_run=None):
        """CreateFirewallRequestBody

        The model defined in huaweicloud sdk

        :param firewall: 
        :type firewall: :class:`huaweicloudsdkvpc.v3.CreateFirewallOption`
        :param dry_run: 功能说明：是否只预检此次请求 取值范围： -true：发送检查请求，不会创建ACL。检查项包括是否填写了必需参数、请求格式、业务限制。如果检查不通过，则返回对应错误。如果检查通过，则返回响应码202。 -false（默认值）：发送正常请求，并直接创建ACL。
        :type dry_run: bool
        """
        
        

        self._firewall = None
        self._dry_run = None
        self.discriminator = None

        self.firewall = firewall
        if dry_run is not None:
            self.dry_run = dry_run

    @property
    def firewall(self):
        """Gets the firewall of this CreateFirewallRequestBody.

        :return: The firewall of this CreateFirewallRequestBody.
        :rtype: :class:`huaweicloudsdkvpc.v3.CreateFirewallOption`
        """
        return self._firewall

    @firewall.setter
    def firewall(self, firewall):
        """Sets the firewall of this CreateFirewallRequestBody.

        :param firewall: The firewall of this CreateFirewallRequestBody.
        :type firewall: :class:`huaweicloudsdkvpc.v3.CreateFirewallOption`
        """
        self._firewall = firewall

    @property
    def dry_run(self):
        """Gets the dry_run of this CreateFirewallRequestBody.

        功能说明：是否只预检此次请求 取值范围： -true：发送检查请求，不会创建ACL。检查项包括是否填写了必需参数、请求格式、业务限制。如果检查不通过，则返回对应错误。如果检查通过，则返回响应码202。 -false（默认值）：发送正常请求，并直接创建ACL。

        :return: The dry_run of this CreateFirewallRequestBody.
        :rtype: bool
        """
        return self._dry_run

    @dry_run.setter
    def dry_run(self, dry_run):
        """Sets the dry_run of this CreateFirewallRequestBody.

        功能说明：是否只预检此次请求 取值范围： -true：发送检查请求，不会创建ACL。检查项包括是否填写了必需参数、请求格式、业务限制。如果检查不通过，则返回对应错误。如果检查通过，则返回响应码202。 -false（默认值）：发送正常请求，并直接创建ACL。

        :param dry_run: The dry_run of this CreateFirewallRequestBody.
        :type dry_run: bool
        """
        self._dry_run = dry_run

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
        if not isinstance(other, CreateFirewallRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
