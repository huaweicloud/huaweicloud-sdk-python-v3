# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDedicatedHostsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'dedicated_hosts': 'list[RespDedicatedHost]',
        'total': 'int'
    }

    attribute_map = {
        'dedicated_hosts': 'dedicated_hosts',
        'total': 'total'
    }

    def __init__(self, dedicated_hosts=None, total=None):
        """ListDedicatedHostsResponse - a model defined in huaweicloud sdk"""
        
        super(ListDedicatedHostsResponse, self).__init__()

        self._dedicated_hosts = None
        self._total = None
        self.discriminator = None

        if dedicated_hosts is not None:
            self.dedicated_hosts = dedicated_hosts
        if total is not None:
            self.total = total

    @property
    def dedicated_hosts(self):
        """Gets the dedicated_hosts of this ListDedicatedHostsResponse.

        满足查询条件的专属主机。

        :return: The dedicated_hosts of this ListDedicatedHostsResponse.
        :rtype: list[RespDedicatedHost]
        """
        return self._dedicated_hosts

    @dedicated_hosts.setter
    def dedicated_hosts(self, dedicated_hosts):
        """Sets the dedicated_hosts of this ListDedicatedHostsResponse.

        满足查询条件的专属主机。

        :param dedicated_hosts: The dedicated_hosts of this ListDedicatedHostsResponse.
        :type: list[RespDedicatedHost]
        """
        self._dedicated_hosts = dedicated_hosts

    @property
    def total(self):
        """Gets the total of this ListDedicatedHostsResponse.

        满足查询条件的专属主机数量。

        :return: The total of this ListDedicatedHostsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListDedicatedHostsResponse.

        满足查询条件的专属主机数量。

        :param total: The total of this ListDedicatedHostsResponse.
        :type: int
        """
        self._total = total

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
        if not isinstance(other, ListDedicatedHostsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other