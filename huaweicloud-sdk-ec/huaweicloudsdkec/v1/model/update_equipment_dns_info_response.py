# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateEquipmentDnsInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'master_dns': 'str',
        'slave_dns': 'str'
    }

    attribute_map = {
        'master_dns': 'master_dns',
        'slave_dns': 'slave_dns'
    }

    def __init__(self, master_dns=None, slave_dns=None):
        r"""UpdateEquipmentDnsInfoResponse

        The model defined in huaweicloud sdk

        :param master_dns: 主DNS
        :type master_dns: str
        :param slave_dns: 备DNS
        :type slave_dns: str
        """
        
        super(UpdateEquipmentDnsInfoResponse, self).__init__()

        self._master_dns = None
        self._slave_dns = None
        self.discriminator = None

        if master_dns is not None:
            self.master_dns = master_dns
        if slave_dns is not None:
            self.slave_dns = slave_dns

    @property
    def master_dns(self):
        r"""Gets the master_dns of this UpdateEquipmentDnsInfoResponse.

        主DNS

        :return: The master_dns of this UpdateEquipmentDnsInfoResponse.
        :rtype: str
        """
        return self._master_dns

    @master_dns.setter
    def master_dns(self, master_dns):
        r"""Sets the master_dns of this UpdateEquipmentDnsInfoResponse.

        主DNS

        :param master_dns: The master_dns of this UpdateEquipmentDnsInfoResponse.
        :type master_dns: str
        """
        self._master_dns = master_dns

    @property
    def slave_dns(self):
        r"""Gets the slave_dns of this UpdateEquipmentDnsInfoResponse.

        备DNS

        :return: The slave_dns of this UpdateEquipmentDnsInfoResponse.
        :rtype: str
        """
        return self._slave_dns

    @slave_dns.setter
    def slave_dns(self, slave_dns):
        r"""Sets the slave_dns of this UpdateEquipmentDnsInfoResponse.

        备DNS

        :param slave_dns: The slave_dns of this UpdateEquipmentDnsInfoResponse.
        :type slave_dns: str
        """
        self._slave_dns = slave_dns

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
        if not isinstance(other, UpdateEquipmentDnsInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
