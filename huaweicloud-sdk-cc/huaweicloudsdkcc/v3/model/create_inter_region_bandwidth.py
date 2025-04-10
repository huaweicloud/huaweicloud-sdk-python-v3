# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateInterRegionBandwidth:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cloud_connection_id': 'str',
        'bandwidth_package_id': 'str',
        'bandwidth': 'int',
        'inter_region_ids': 'list[str]'
    }

    attribute_map = {
        'cloud_connection_id': 'cloud_connection_id',
        'bandwidth_package_id': 'bandwidth_package_id',
        'bandwidth': 'bandwidth',
        'inter_region_ids': 'inter_region_ids'
    }

    def __init__(self, cloud_connection_id=None, bandwidth_package_id=None, bandwidth=None, inter_region_ids=None):
        r"""CreateInterRegionBandwidth

        The model defined in huaweicloud sdk

        :param cloud_connection_id: 云连接实例ID。
        :type cloud_connection_id: str
        :param bandwidth_package_id: 带宽包实例ID。
        :type bandwidth_package_id: str
        :param bandwidth: 域间带宽值。
        :type bandwidth: int
        :param inter_region_ids: 域间RegionID。
        :type inter_region_ids: list[str]
        """
        
        

        self._cloud_connection_id = None
        self._bandwidth_package_id = None
        self._bandwidth = None
        self._inter_region_ids = None
        self.discriminator = None

        self.cloud_connection_id = cloud_connection_id
        self.bandwidth_package_id = bandwidth_package_id
        self.bandwidth = bandwidth
        self.inter_region_ids = inter_region_ids

    @property
    def cloud_connection_id(self):
        r"""Gets the cloud_connection_id of this CreateInterRegionBandwidth.

        云连接实例ID。

        :return: The cloud_connection_id of this CreateInterRegionBandwidth.
        :rtype: str
        """
        return self._cloud_connection_id

    @cloud_connection_id.setter
    def cloud_connection_id(self, cloud_connection_id):
        r"""Sets the cloud_connection_id of this CreateInterRegionBandwidth.

        云连接实例ID。

        :param cloud_connection_id: The cloud_connection_id of this CreateInterRegionBandwidth.
        :type cloud_connection_id: str
        """
        self._cloud_connection_id = cloud_connection_id

    @property
    def bandwidth_package_id(self):
        r"""Gets the bandwidth_package_id of this CreateInterRegionBandwidth.

        带宽包实例ID。

        :return: The bandwidth_package_id of this CreateInterRegionBandwidth.
        :rtype: str
        """
        return self._bandwidth_package_id

    @bandwidth_package_id.setter
    def bandwidth_package_id(self, bandwidth_package_id):
        r"""Sets the bandwidth_package_id of this CreateInterRegionBandwidth.

        带宽包实例ID。

        :param bandwidth_package_id: The bandwidth_package_id of this CreateInterRegionBandwidth.
        :type bandwidth_package_id: str
        """
        self._bandwidth_package_id = bandwidth_package_id

    @property
    def bandwidth(self):
        r"""Gets the bandwidth of this CreateInterRegionBandwidth.

        域间带宽值。

        :return: The bandwidth of this CreateInterRegionBandwidth.
        :rtype: int
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        r"""Sets the bandwidth of this CreateInterRegionBandwidth.

        域间带宽值。

        :param bandwidth: The bandwidth of this CreateInterRegionBandwidth.
        :type bandwidth: int
        """
        self._bandwidth = bandwidth

    @property
    def inter_region_ids(self):
        r"""Gets the inter_region_ids of this CreateInterRegionBandwidth.

        域间RegionID。

        :return: The inter_region_ids of this CreateInterRegionBandwidth.
        :rtype: list[str]
        """
        return self._inter_region_ids

    @inter_region_ids.setter
    def inter_region_ids(self, inter_region_ids):
        r"""Sets the inter_region_ids of this CreateInterRegionBandwidth.

        域间RegionID。

        :param inter_region_ids: The inter_region_ids of this CreateInterRegionBandwidth.
        :type inter_region_ids: list[str]
        """
        self._inter_region_ids = inter_region_ids

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
        if not isinstance(other, CreateInterRegionBandwidth):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
