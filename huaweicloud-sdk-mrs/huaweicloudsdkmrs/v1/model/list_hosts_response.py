# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHostsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'hosts': 'list[HostModel]',
        'total': 'int'
    }

    attribute_map = {
        'hosts': 'hosts',
        'total': 'total'
    }

    def __init__(self, hosts=None, total=None):
        r"""ListHostsResponse

        The model defined in huaweicloud sdk

        :param hosts: 主机参数。
        :type hosts: list[:class:`huaweicloudsdkmrs.v1.HostModel`]
        :param total: 主机列表总数。
        :type total: int
        """
        
        super(ListHostsResponse, self).__init__()

        self._hosts = None
        self._total = None
        self.discriminator = None

        if hosts is not None:
            self.hosts = hosts
        if total is not None:
            self.total = total

    @property
    def hosts(self):
        r"""Gets the hosts of this ListHostsResponse.

        主机参数。

        :return: The hosts of this ListHostsResponse.
        :rtype: list[:class:`huaweicloudsdkmrs.v1.HostModel`]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        r"""Sets the hosts of this ListHostsResponse.

        主机参数。

        :param hosts: The hosts of this ListHostsResponse.
        :type hosts: list[:class:`huaweicloudsdkmrs.v1.HostModel`]
        """
        self._hosts = hosts

    @property
    def total(self):
        r"""Gets the total of this ListHostsResponse.

        主机列表总数。

        :return: The total of this ListHostsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListHostsResponse.

        主机列表总数。

        :param total: The total of this ListHostsResponse.
        :type total: int
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
        if not isinstance(other, ListHostsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
