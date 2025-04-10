# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateInstanceCrossVpcIpRespResults:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'advertised_ip': 'str',
        'success': 'bool',
        'ip': 'str'
    }

    attribute_map = {
        'advertised_ip': 'advertised_ip',
        'success': 'success',
        'ip': 'ip'
    }

    def __init__(self, advertised_ip=None, success=None, ip=None):
        r"""UpdateInstanceCrossVpcIpRespResults

        The model defined in huaweicloud sdk

        :param advertised_ip: advertised.listeners IP/域名。
        :type advertised_ip: str
        :param success: 修改broker跨VPC访问的状态。
        :type success: bool
        :param ip: listeners IP。
        :type ip: str
        """
        
        

        self._advertised_ip = None
        self._success = None
        self._ip = None
        self.discriminator = None

        if advertised_ip is not None:
            self.advertised_ip = advertised_ip
        if success is not None:
            self.success = success
        if ip is not None:
            self.ip = ip

    @property
    def advertised_ip(self):
        r"""Gets the advertised_ip of this UpdateInstanceCrossVpcIpRespResults.

        advertised.listeners IP/域名。

        :return: The advertised_ip of this UpdateInstanceCrossVpcIpRespResults.
        :rtype: str
        """
        return self._advertised_ip

    @advertised_ip.setter
    def advertised_ip(self, advertised_ip):
        r"""Sets the advertised_ip of this UpdateInstanceCrossVpcIpRespResults.

        advertised.listeners IP/域名。

        :param advertised_ip: The advertised_ip of this UpdateInstanceCrossVpcIpRespResults.
        :type advertised_ip: str
        """
        self._advertised_ip = advertised_ip

    @property
    def success(self):
        r"""Gets the success of this UpdateInstanceCrossVpcIpRespResults.

        修改broker跨VPC访问的状态。

        :return: The success of this UpdateInstanceCrossVpcIpRespResults.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this UpdateInstanceCrossVpcIpRespResults.

        修改broker跨VPC访问的状态。

        :param success: The success of this UpdateInstanceCrossVpcIpRespResults.
        :type success: bool
        """
        self._success = success

    @property
    def ip(self):
        r"""Gets the ip of this UpdateInstanceCrossVpcIpRespResults.

        listeners IP。

        :return: The ip of this UpdateInstanceCrossVpcIpRespResults.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this UpdateInstanceCrossVpcIpRespResults.

        listeners IP。

        :param ip: The ip of this UpdateInstanceCrossVpcIpRespResults.
        :type ip: str
        """
        self._ip = ip

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
        if not isinstance(other, UpdateInstanceCrossVpcIpRespResults):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
