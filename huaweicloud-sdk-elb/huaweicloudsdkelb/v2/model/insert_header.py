# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InsertHeader:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_forwarded_elb_ip': 'bool',
        'x_forwarded_host': 'bool'
    }

    attribute_map = {
        'x_forwarded_elb_ip': 'X-Forwarded-ELB-IP',
        'x_forwarded_host': 'X-Forwarded-Host'
    }

    def __init__(self, x_forwarded_elb_ip=None, x_forwarded_host=None):
        """InsertHeader

        The model defined in huaweicloud sdk

        :param x_forwarded_elb_ip: 负载均衡器弹性公网IP透传开关。
        :type x_forwarded_elb_ip: bool
        :param x_forwarded_host: X-Forwarded-Host设为true可以将客户请求头的第一个X-Forwarded-Host设置为请求头的Host带到后端云服务器。
        :type x_forwarded_host: bool
        """
        
        

        self._x_forwarded_elb_ip = None
        self._x_forwarded_host = None
        self.discriminator = None

        if x_forwarded_elb_ip is not None:
            self.x_forwarded_elb_ip = x_forwarded_elb_ip
        if x_forwarded_host is not None:
            self.x_forwarded_host = x_forwarded_host

    @property
    def x_forwarded_elb_ip(self):
        """Gets the x_forwarded_elb_ip of this InsertHeader.

        负载均衡器弹性公网IP透传开关。

        :return: The x_forwarded_elb_ip of this InsertHeader.
        :rtype: bool
        """
        return self._x_forwarded_elb_ip

    @x_forwarded_elb_ip.setter
    def x_forwarded_elb_ip(self, x_forwarded_elb_ip):
        """Sets the x_forwarded_elb_ip of this InsertHeader.

        负载均衡器弹性公网IP透传开关。

        :param x_forwarded_elb_ip: The x_forwarded_elb_ip of this InsertHeader.
        :type x_forwarded_elb_ip: bool
        """
        self._x_forwarded_elb_ip = x_forwarded_elb_ip

    @property
    def x_forwarded_host(self):
        """Gets the x_forwarded_host of this InsertHeader.

        X-Forwarded-Host设为true可以将客户请求头的第一个X-Forwarded-Host设置为请求头的Host带到后端云服务器。

        :return: The x_forwarded_host of this InsertHeader.
        :rtype: bool
        """
        return self._x_forwarded_host

    @x_forwarded_host.setter
    def x_forwarded_host(self, x_forwarded_host):
        """Sets the x_forwarded_host of this InsertHeader.

        X-Forwarded-Host设为true可以将客户请求头的第一个X-Forwarded-Host设置为请求头的Host带到后端云服务器。

        :param x_forwarded_host: The x_forwarded_host of this InsertHeader.
        :type x_forwarded_host: bool
        """
        self._x_forwarded_host = x_forwarded_host

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
        if not isinstance(other, InsertHeader):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
