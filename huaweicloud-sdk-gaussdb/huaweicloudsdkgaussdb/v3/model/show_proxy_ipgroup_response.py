# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowProxyIpgroupResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable_ip_group': 'bool',
        'type': 'str',
        'ip_group': 'ProxyIpGroupDetail'
    }

    attribute_map = {
        'enable_ip_group': 'enable_ip_group',
        'type': 'type',
        'ip_group': 'ip_group'
    }

    def __init__(self, enable_ip_group=None, type=None, ip_group=None):
        """ShowProxyIpgroupResponse

        The model defined in huaweicloud sdk

        :param enable_ip_group: 允许访问控制或者不允许 true | false。
        :type enable_ip_group: bool
        :param type: 白名单或者黑名单 &#39;white&#39; | &#39;black&#39;
        :type type: str
        :param ip_group: 
        :type ip_group: :class:`huaweicloudsdkgaussdb.v3.ProxyIpGroupDetail`
        """
        
        super(ShowProxyIpgroupResponse, self).__init__()

        self._enable_ip_group = None
        self._type = None
        self._ip_group = None
        self.discriminator = None

        if enable_ip_group is not None:
            self.enable_ip_group = enable_ip_group
        if type is not None:
            self.type = type
        if ip_group is not None:
            self.ip_group = ip_group

    @property
    def enable_ip_group(self):
        """Gets the enable_ip_group of this ShowProxyIpgroupResponse.

        允许访问控制或者不允许 true | false。

        :return: The enable_ip_group of this ShowProxyIpgroupResponse.
        :rtype: bool
        """
        return self._enable_ip_group

    @enable_ip_group.setter
    def enable_ip_group(self, enable_ip_group):
        """Sets the enable_ip_group of this ShowProxyIpgroupResponse.

        允许访问控制或者不允许 true | false。

        :param enable_ip_group: The enable_ip_group of this ShowProxyIpgroupResponse.
        :type enable_ip_group: bool
        """
        self._enable_ip_group = enable_ip_group

    @property
    def type(self):
        """Gets the type of this ShowProxyIpgroupResponse.

        白名单或者黑名单 'white' | 'black'

        :return: The type of this ShowProxyIpgroupResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowProxyIpgroupResponse.

        白名单或者黑名单 'white' | 'black'

        :param type: The type of this ShowProxyIpgroupResponse.
        :type type: str
        """
        self._type = type

    @property
    def ip_group(self):
        """Gets the ip_group of this ShowProxyIpgroupResponse.

        :return: The ip_group of this ShowProxyIpgroupResponse.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ProxyIpGroupDetail`
        """
        return self._ip_group

    @ip_group.setter
    def ip_group(self, ip_group):
        """Sets the ip_group of this ShowProxyIpgroupResponse.

        :param ip_group: The ip_group of this ShowProxyIpgroupResponse.
        :type ip_group: :class:`huaweicloudsdkgaussdb.v3.ProxyIpGroupDetail`
        """
        self._ip_group = ip_group

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
        if not isinstance(other, ShowProxyIpgroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
