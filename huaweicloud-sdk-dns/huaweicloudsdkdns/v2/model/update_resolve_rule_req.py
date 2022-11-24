# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateResolveRuleReq:

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
        'ipaddresses': 'IpInfo',
        'routers': 'list[Router]'
    }

    attribute_map = {
        'name': 'name',
        'ipaddresses': 'ipaddresses',
        'routers': 'routers'
    }

    def __init__(self, name=None, ipaddresses=None, routers=None):
        """UpdateResolveRuleReq

        The model defined in huaweicloud sdk

        :param name: 规则名称。 取值范围：1-64个字符，支持数字、字母、中文、_（下划线）、-（中划线）、.（点）。
        :type name: str
        :param ipaddresses: 
        :type ipaddresses: :class:`huaweicloudsdkdns.v2.IpInfo`
        :param routers: 规则关联的目标ip地址。
        :type routers: list[:class:`huaweicloudsdkdns.v2.Router`]
        """
        
        

        self._name = None
        self._ipaddresses = None
        self._routers = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if ipaddresses is not None:
            self.ipaddresses = ipaddresses
        if routers is not None:
            self.routers = routers

    @property
    def name(self):
        """Gets the name of this UpdateResolveRuleReq.

        规则名称。 取值范围：1-64个字符，支持数字、字母、中文、_（下划线）、-（中划线）、.（点）。

        :return: The name of this UpdateResolveRuleReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateResolveRuleReq.

        规则名称。 取值范围：1-64个字符，支持数字、字母、中文、_（下划线）、-（中划线）、.（点）。

        :param name: The name of this UpdateResolveRuleReq.
        :type name: str
        """
        self._name = name

    @property
    def ipaddresses(self):
        """Gets the ipaddresses of this UpdateResolveRuleReq.

        :return: The ipaddresses of this UpdateResolveRuleReq.
        :rtype: :class:`huaweicloudsdkdns.v2.IpInfo`
        """
        return self._ipaddresses

    @ipaddresses.setter
    def ipaddresses(self, ipaddresses):
        """Sets the ipaddresses of this UpdateResolveRuleReq.

        :param ipaddresses: The ipaddresses of this UpdateResolveRuleReq.
        :type ipaddresses: :class:`huaweicloudsdkdns.v2.IpInfo`
        """
        self._ipaddresses = ipaddresses

    @property
    def routers(self):
        """Gets the routers of this UpdateResolveRuleReq.

        规则关联的目标ip地址。

        :return: The routers of this UpdateResolveRuleReq.
        :rtype: list[:class:`huaweicloudsdkdns.v2.Router`]
        """
        return self._routers

    @routers.setter
    def routers(self, routers):
        """Sets the routers of this UpdateResolveRuleReq.

        规则关联的目标ip地址。

        :param routers: The routers of this UpdateResolveRuleReq.
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
        if not isinstance(other, UpdateResolveRuleReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
