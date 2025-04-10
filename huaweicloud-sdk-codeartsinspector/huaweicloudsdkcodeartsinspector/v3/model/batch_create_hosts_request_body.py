# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateHostsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'hosts': 'list[HostItem]'
    }

    attribute_map = {
        'hosts': 'hosts'
    }

    def __init__(self, hosts=None):
        r"""BatchCreateHostsRequestBody

        The model defined in huaweicloud sdk

        :param hosts: 主机资产列表
        :type hosts: list[:class:`huaweicloudsdkcodeartsinspector.v3.HostItem`]
        """
        
        

        self._hosts = None
        self.discriminator = None

        self.hosts = hosts

    @property
    def hosts(self):
        r"""Gets the hosts of this BatchCreateHostsRequestBody.

        主机资产列表

        :return: The hosts of this BatchCreateHostsRequestBody.
        :rtype: list[:class:`huaweicloudsdkcodeartsinspector.v3.HostItem`]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        r"""Sets the hosts of this BatchCreateHostsRequestBody.

        主机资产列表

        :param hosts: The hosts of this BatchCreateHostsRequestBody.
        :type hosts: list[:class:`huaweicloudsdkcodeartsinspector.v3.HostItem`]
        """
        self._hosts = hosts

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
        if not isinstance(other, BatchCreateHostsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
