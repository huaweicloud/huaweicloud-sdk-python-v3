# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateResolverRuleRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'domain_name': 'str',
        'endpoint_id': 'str',
        'ipaddresses': 'list[IpInfo]'
    }

    attribute_map = {
        'name': 'name',
        'domain_name': 'domain_name',
        'endpoint_id': 'endpoint_id',
        'ipaddresses': 'ipaddresses'
    }

    def __init__(self, name=None, domain_name=None, endpoint_id=None, ipaddresses=None):
        r"""CreateResolverRuleRequestBody

        The model defined in huaweicloud sdk

        :param name: 规则名称。 取值范围：1-64个字符，支持数字、字母、中文、_（下划线）、-（中划线）、.（点）。
        :type name: str
        :param domain_name: 域名。
        :type domain_name: str
        :param endpoint_id: 当前规则所属的终端节点ID。
        :type endpoint_id: str
        :param ipaddresses: 规则的目标IP地址。
        :type ipaddresses: list[:class:`huaweicloudsdkdns.v2.IpInfo`]
        """
        
        

        self._name = None
        self._domain_name = None
        self._endpoint_id = None
        self._ipaddresses = None
        self.discriminator = None

        self.name = name
        self.domain_name = domain_name
        self.endpoint_id = endpoint_id
        self.ipaddresses = ipaddresses

    @property
    def name(self):
        r"""Gets the name of this CreateResolverRuleRequestBody.

        规则名称。 取值范围：1-64个字符，支持数字、字母、中文、_（下划线）、-（中划线）、.（点）。

        :return: The name of this CreateResolverRuleRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateResolverRuleRequestBody.

        规则名称。 取值范围：1-64个字符，支持数字、字母、中文、_（下划线）、-（中划线）、.（点）。

        :param name: The name of this CreateResolverRuleRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def domain_name(self):
        r"""Gets the domain_name of this CreateResolverRuleRequestBody.

        域名。

        :return: The domain_name of this CreateResolverRuleRequestBody.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this CreateResolverRuleRequestBody.

        域名。

        :param domain_name: The domain_name of this CreateResolverRuleRequestBody.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def endpoint_id(self):
        r"""Gets the endpoint_id of this CreateResolverRuleRequestBody.

        当前规则所属的终端节点ID。

        :return: The endpoint_id of this CreateResolverRuleRequestBody.
        :rtype: str
        """
        return self._endpoint_id

    @endpoint_id.setter
    def endpoint_id(self, endpoint_id):
        r"""Sets the endpoint_id of this CreateResolverRuleRequestBody.

        当前规则所属的终端节点ID。

        :param endpoint_id: The endpoint_id of this CreateResolverRuleRequestBody.
        :type endpoint_id: str
        """
        self._endpoint_id = endpoint_id

    @property
    def ipaddresses(self):
        r"""Gets the ipaddresses of this CreateResolverRuleRequestBody.

        规则的目标IP地址。

        :return: The ipaddresses of this CreateResolverRuleRequestBody.
        :rtype: list[:class:`huaweicloudsdkdns.v2.IpInfo`]
        """
        return self._ipaddresses

    @ipaddresses.setter
    def ipaddresses(self, ipaddresses):
        r"""Sets the ipaddresses of this CreateResolverRuleRequestBody.

        规则的目标IP地址。

        :param ipaddresses: The ipaddresses of this CreateResolverRuleRequestBody.
        :type ipaddresses: list[:class:`huaweicloudsdkdns.v2.IpInfo`]
        """
        self._ipaddresses = ipaddresses

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
        if not isinstance(other, CreateResolverRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
