# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSubnetBandwidthReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bandwidth_name': 'str',
        'bandwidth_size': 'int',
        'enterprise_project_id': 'str',
        'charge_mode': 'str'
    }

    attribute_map = {
        'bandwidth_name': 'bandwidth_name',
        'bandwidth_size': 'bandwidth_size',
        'enterprise_project_id': 'enterprise_project_id',
        'charge_mode': 'charge_mode'
    }

    def __init__(self, bandwidth_name=None, bandwidth_size=None, enterprise_project_id=None, charge_mode=None):
        r"""UpdateSubnetBandwidthReq

        The model defined in huaweicloud sdk

        :param bandwidth_name: 云办公带宽名称。
        :type bandwidth_name: str
        :param bandwidth_size: 云办公带宽大小。
        :type bandwidth_size: int
        :param enterprise_project_id: 企业项目ID，默认\&quot;0。\&quot;
        :type enterprise_project_id: str
        :param charge_mode: 计费模式 - wks_bandwidth：按带宽计费。 - free: 不计费，不支持包周期订购。 - wks_traffic：按流量计费
        :type charge_mode: str
        """
        
        

        self._bandwidth_name = None
        self._bandwidth_size = None
        self._enterprise_project_id = None
        self._charge_mode = None
        self.discriminator = None

        if bandwidth_name is not None:
            self.bandwidth_name = bandwidth_name
        if bandwidth_size is not None:
            self.bandwidth_size = bandwidth_size
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if charge_mode is not None:
            self.charge_mode = charge_mode

    @property
    def bandwidth_name(self):
        r"""Gets the bandwidth_name of this UpdateSubnetBandwidthReq.

        云办公带宽名称。

        :return: The bandwidth_name of this UpdateSubnetBandwidthReq.
        :rtype: str
        """
        return self._bandwidth_name

    @bandwidth_name.setter
    def bandwidth_name(self, bandwidth_name):
        r"""Sets the bandwidth_name of this UpdateSubnetBandwidthReq.

        云办公带宽名称。

        :param bandwidth_name: The bandwidth_name of this UpdateSubnetBandwidthReq.
        :type bandwidth_name: str
        """
        self._bandwidth_name = bandwidth_name

    @property
    def bandwidth_size(self):
        r"""Gets the bandwidth_size of this UpdateSubnetBandwidthReq.

        云办公带宽大小。

        :return: The bandwidth_size of this UpdateSubnetBandwidthReq.
        :rtype: int
        """
        return self._bandwidth_size

    @bandwidth_size.setter
    def bandwidth_size(self, bandwidth_size):
        r"""Sets the bandwidth_size of this UpdateSubnetBandwidthReq.

        云办公带宽大小。

        :param bandwidth_size: The bandwidth_size of this UpdateSubnetBandwidthReq.
        :type bandwidth_size: int
        """
        self._bandwidth_size = bandwidth_size

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this UpdateSubnetBandwidthReq.

        企业项目ID，默认\"0。\"

        :return: The enterprise_project_id of this UpdateSubnetBandwidthReq.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this UpdateSubnetBandwidthReq.

        企业项目ID，默认\"0。\"

        :param enterprise_project_id: The enterprise_project_id of this UpdateSubnetBandwidthReq.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def charge_mode(self):
        r"""Gets the charge_mode of this UpdateSubnetBandwidthReq.

        计费模式 - wks_bandwidth：按带宽计费。 - free: 不计费，不支持包周期订购。 - wks_traffic：按流量计费

        :return: The charge_mode of this UpdateSubnetBandwidthReq.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        r"""Sets the charge_mode of this UpdateSubnetBandwidthReq.

        计费模式 - wks_bandwidth：按带宽计费。 - free: 不计费，不支持包周期订购。 - wks_traffic：按流量计费

        :param charge_mode: The charge_mode of this UpdateSubnetBandwidthReq.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

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
        if not isinstance(other, UpdateSubnetBandwidthReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
