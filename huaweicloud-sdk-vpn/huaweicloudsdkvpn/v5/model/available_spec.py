# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AvailableSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flavor': 'str',
        'attachment_type': 'str',
        'ip_version': 'str'
    }

    attribute_map = {
        'flavor': 'flavor',
        'attachment_type': 'attachment_type',
        'ip_version': 'ip_version'
    }

    def __init__(self, flavor=None, attachment_type=None, ip_version=None):
        r"""AvailableSpec

        The model defined in huaweicloud sdk

        :param flavor: VPN网关规格
        :type flavor: str
        :param attachment_type: 关联模式
        :type attachment_type: str
        :param ip_version: 网关的IP协议版本
        :type ip_version: str
        """
        
        

        self._flavor = None
        self._attachment_type = None
        self._ip_version = None
        self.discriminator = None

        if flavor is not None:
            self.flavor = flavor
        if attachment_type is not None:
            self.attachment_type = attachment_type
        if ip_version is not None:
            self.ip_version = ip_version

    @property
    def flavor(self):
        r"""Gets the flavor of this AvailableSpec.

        VPN网关规格

        :return: The flavor of this AvailableSpec.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this AvailableSpec.

        VPN网关规格

        :param flavor: The flavor of this AvailableSpec.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def attachment_type(self):
        r"""Gets the attachment_type of this AvailableSpec.

        关联模式

        :return: The attachment_type of this AvailableSpec.
        :rtype: str
        """
        return self._attachment_type

    @attachment_type.setter
    def attachment_type(self, attachment_type):
        r"""Sets the attachment_type of this AvailableSpec.

        关联模式

        :param attachment_type: The attachment_type of this AvailableSpec.
        :type attachment_type: str
        """
        self._attachment_type = attachment_type

    @property
    def ip_version(self):
        r"""Gets the ip_version of this AvailableSpec.

        网关的IP协议版本

        :return: The ip_version of this AvailableSpec.
        :rtype: str
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        r"""Sets the ip_version of this AvailableSpec.

        网关的IP协议版本

        :param ip_version: The ip_version of this AvailableSpec.
        :type ip_version: str
        """
        self._ip_version = ip_version

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
        if not isinstance(other, AvailableSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
