# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateHostMassageReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'hosts': 'list[EnhancedConnectionsHost]'
    }

    attribute_map = {
        'hosts': 'hosts'
    }

    def __init__(self, hosts=None):
        """UpdateHostMassageReq

        The model defined in huaweicloud sdk

        :param hosts: 用户自定义主机信息，最大支持2万条记录。内容填空表示清除所有已配置的主机信息。
        :type hosts: list[:class:`huaweicloudsdkdli.v1.EnhancedConnectionsHost`]
        """
        
        

        self._hosts = None
        self.discriminator = None

        self.hosts = hosts

    @property
    def hosts(self):
        """Gets the hosts of this UpdateHostMassageReq.

        用户自定义主机信息，最大支持2万条记录。内容填空表示清除所有已配置的主机信息。

        :return: The hosts of this UpdateHostMassageReq.
        :rtype: list[:class:`huaweicloudsdkdli.v1.EnhancedConnectionsHost`]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this UpdateHostMassageReq.

        用户自定义主机信息，最大支持2万条记录。内容填空表示清除所有已配置的主机信息。

        :param hosts: The hosts of this UpdateHostMassageReq.
        :type hosts: list[:class:`huaweicloudsdkdli.v1.EnhancedConnectionsHost`]
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
        if not isinstance(other, UpdateHostMassageReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
