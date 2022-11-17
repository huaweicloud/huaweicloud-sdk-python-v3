# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFirewallUsingGetRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'service_type': 'int'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'service_type': 'service_type'
    }

    def __init__(self, offset=None, limit=None, service_type=None):
        """ListFirewallUsingGetRequest

        The model defined in huaweicloud sdk

        :param offset: 偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0
        :type offset: int
        :param limit: 每页显示个数
        :type limit: int
        :param service_type: 服务类型 0 南北向防火墙 1 东西向防火墙
        :type service_type: int
        """
        
        

        self._offset = None
        self._limit = None
        self._service_type = None
        self.discriminator = None

        self.offset = offset
        self.limit = limit
        self.service_type = service_type

    @property
    def offset(self):
        """Gets the offset of this ListFirewallUsingGetRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :return: The offset of this ListFirewallUsingGetRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListFirewallUsingGetRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :param offset: The offset of this ListFirewallUsingGetRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListFirewallUsingGetRequest.

        每页显示个数

        :return: The limit of this ListFirewallUsingGetRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListFirewallUsingGetRequest.

        每页显示个数

        :param limit: The limit of this ListFirewallUsingGetRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def service_type(self):
        """Gets the service_type of this ListFirewallUsingGetRequest.

        服务类型 0 南北向防火墙 1 东西向防火墙

        :return: The service_type of this ListFirewallUsingGetRequest.
        :rtype: int
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this ListFirewallUsingGetRequest.

        服务类型 0 南北向防火墙 1 东西向防火墙

        :param service_type: The service_type of this ListFirewallUsingGetRequest.
        :type service_type: int
        """
        self._service_type = service_type

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
        if not isinstance(other, ListFirewallUsingGetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
