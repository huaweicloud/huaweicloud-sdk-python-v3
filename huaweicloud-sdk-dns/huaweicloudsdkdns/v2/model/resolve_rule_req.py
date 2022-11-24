# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResolveRuleReq:

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
        'region': 'str',
        'ipaddresses': 'list[IpInfo]',
        'routers': 'list[Router]'
    }

    attribute_map = {
        'name': 'name',
        'domain_name': 'domain_name',
        'endpoint_id': 'endpoint_id',
        'region': 'region',
        'ipaddresses': 'ipaddresses',
        'routers': 'routers'
    }

    def __init__(self, name=None, domain_name=None, endpoint_id=None, region=None, ipaddresses=None, routers=None):
        """ResolveRuleReq

        The model defined in huaweicloud sdk

        :param name: 规则名称。 取值范围：1-64个字符，支持数字、字母、中文、_（下划线）、-（中划线）、.（点）。
        :type name: str
        :param domain_name: 域名。
        :type domain_name: str
        :param endpoint_id: 当前规则所属的endpoint_id。
        :type endpoint_id: str
        :param region: 当前规则所在的region。
        :type region: str
        :param ipaddresses: 规则关联的目标ip地址。
        :type ipaddresses: list[:class:`huaweicloudsdkdns.v2.IpInfo`]
        :param routers: 规则关联的目标ip地址。
        :type routers: list[:class:`huaweicloudsdkdns.v2.Router`]
        """
        
        

        self._name = None
        self._domain_name = None
        self._endpoint_id = None
        self._region = None
        self._ipaddresses = None
        self._routers = None
        self.discriminator = None

        self.name = name
        self.domain_name = domain_name
        self.endpoint_id = endpoint_id
        self.region = region
        self.ipaddresses = ipaddresses
        self.routers = routers

    @property
    def name(self):
        """Gets the name of this ResolveRuleReq.

        规则名称。 取值范围：1-64个字符，支持数字、字母、中文、_（下划线）、-（中划线）、.（点）。

        :return: The name of this ResolveRuleReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ResolveRuleReq.

        规则名称。 取值范围：1-64个字符，支持数字、字母、中文、_（下划线）、-（中划线）、.（点）。

        :param name: The name of this ResolveRuleReq.
        :type name: str
        """
        self._name = name

    @property
    def domain_name(self):
        """Gets the domain_name of this ResolveRuleReq.

        域名。

        :return: The domain_name of this ResolveRuleReq.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this ResolveRuleReq.

        域名。

        :param domain_name: The domain_name of this ResolveRuleReq.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def endpoint_id(self):
        """Gets the endpoint_id of this ResolveRuleReq.

        当前规则所属的endpoint_id。

        :return: The endpoint_id of this ResolveRuleReq.
        :rtype: str
        """
        return self._endpoint_id

    @endpoint_id.setter
    def endpoint_id(self, endpoint_id):
        """Sets the endpoint_id of this ResolveRuleReq.

        当前规则所属的endpoint_id。

        :param endpoint_id: The endpoint_id of this ResolveRuleReq.
        :type endpoint_id: str
        """
        self._endpoint_id = endpoint_id

    @property
    def region(self):
        """Gets the region of this ResolveRuleReq.

        当前规则所在的region。

        :return: The region of this ResolveRuleReq.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ResolveRuleReq.

        当前规则所在的region。

        :param region: The region of this ResolveRuleReq.
        :type region: str
        """
        self._region = region

    @property
    def ipaddresses(self):
        """Gets the ipaddresses of this ResolveRuleReq.

        规则关联的目标ip地址。

        :return: The ipaddresses of this ResolveRuleReq.
        :rtype: list[:class:`huaweicloudsdkdns.v2.IpInfo`]
        """
        return self._ipaddresses

    @ipaddresses.setter
    def ipaddresses(self, ipaddresses):
        """Sets the ipaddresses of this ResolveRuleReq.

        规则关联的目标ip地址。

        :param ipaddresses: The ipaddresses of this ResolveRuleReq.
        :type ipaddresses: list[:class:`huaweicloudsdkdns.v2.IpInfo`]
        """
        self._ipaddresses = ipaddresses

    @property
    def routers(self):
        """Gets the routers of this ResolveRuleReq.

        规则关联的目标ip地址。

        :return: The routers of this ResolveRuleReq.
        :rtype: list[:class:`huaweicloudsdkdns.v2.Router`]
        """
        return self._routers

    @routers.setter
    def routers(self, routers):
        """Sets the routers of this ResolveRuleReq.

        规则关联的目标ip地址。

        :param routers: The routers of this ResolveRuleReq.
        :type routers: list[:class:`huaweicloudsdkdns.v2.Router`]
        """
        self._routers = routers

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
        if not isinstance(other, ResolveRuleReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
