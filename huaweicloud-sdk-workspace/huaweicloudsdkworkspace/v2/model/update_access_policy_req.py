# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAccessPolicyReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'operation_type': 'str',
        'ip_white_list': 'list[IpInfo]'
    }

    attribute_map = {
        'operation_type': 'operation_type',
        'ip_white_list': 'ip_white_list'
    }

    def __init__(self, operation_type=None, ip_white_list=None):
        """UpdateAccessPolicyReq

        The model defined in huaweicloud sdk

        :param operation_type: 操作类别。 * ADD_IP： 添加IP * DELETE_IP： 删除IP
        :type operation_type: str
        :param ip_white_list: 策略的ip列表。
        :type ip_white_list: list[:class:`huaweicloudsdkworkspace.v2.IpInfo`]
        """
        
        

        self._operation_type = None
        self._ip_white_list = None
        self.discriminator = None

        if operation_type is not None:
            self.operation_type = operation_type
        if ip_white_list is not None:
            self.ip_white_list = ip_white_list

    @property
    def operation_type(self):
        """Gets the operation_type of this UpdateAccessPolicyReq.

        操作类别。 * ADD_IP： 添加IP * DELETE_IP： 删除IP

        :return: The operation_type of this UpdateAccessPolicyReq.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """Sets the operation_type of this UpdateAccessPolicyReq.

        操作类别。 * ADD_IP： 添加IP * DELETE_IP： 删除IP

        :param operation_type: The operation_type of this UpdateAccessPolicyReq.
        :type operation_type: str
        """
        self._operation_type = operation_type

    @property
    def ip_white_list(self):
        """Gets the ip_white_list of this UpdateAccessPolicyReq.

        策略的ip列表。

        :return: The ip_white_list of this UpdateAccessPolicyReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.IpInfo`]
        """
        return self._ip_white_list

    @ip_white_list.setter
    def ip_white_list(self, ip_white_list):
        """Sets the ip_white_list of this UpdateAccessPolicyReq.

        策略的ip列表。

        :param ip_white_list: The ip_white_list of this UpdateAccessPolicyReq.
        :type ip_white_list: list[:class:`huaweicloudsdkworkspace.v2.IpInfo`]
        """
        self._ip_white_list = ip_white_list

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
        if not isinstance(other, UpdateAccessPolicyReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
