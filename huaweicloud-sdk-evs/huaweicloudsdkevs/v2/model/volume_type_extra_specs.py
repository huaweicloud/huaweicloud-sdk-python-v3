# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VolumeTypeExtraSpecs:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'reske_yavailability_zones': 'str',
        'availability_zone': 'str',
        'os_vendor_extendedsold_out_availability_zones': 'str',
        'volume_backend_name': 'str',
        'h_wavailability_zone': 'str'
    }

    attribute_map = {
        'reske_yavailability_zones': 'RESKEY:availability_zones',
        'availability_zone': 'availability-zone',
        'os_vendor_extendedsold_out_availability_zones': 'os-vendor-extended:sold_out_availability_zones',
        'volume_backend_name': 'volume_backend_name',
        'h_wavailability_zone': 'HW:availability_zone'
    }

    def __init__(self, reske_yavailability_zones=None, availability_zone=None, os_vendor_extendedsold_out_availability_zones=None, volume_backend_name=None, h_wavailability_zone=None):
        """VolumeTypeExtraSpecs

        The model defined in huaweicloud sdk

        :param reske_yavailability_zones: 支持当前云硬盘类型的可用区列表，列表的元素以逗号分隔。
        :type reske_yavailability_zones: str
        :param availability_zone: 预留属性。
        :type availability_zone: str
        :param os_vendor_extendedsold_out_availability_zones: 当前云硬盘类型已售罄的可用区列表，列表的元素以逗号分隔。
        :type os_vendor_extendedsold_out_availability_zones: str
        :param volume_backend_name: 预留属性。
        :type volume_backend_name: str
        :param h_wavailability_zone: 预留属性。
        :type h_wavailability_zone: str
        """
        
        

        self._reske_yavailability_zones = None
        self._availability_zone = None
        self._os_vendor_extendedsold_out_availability_zones = None
        self._volume_backend_name = None
        self._h_wavailability_zone = None
        self.discriminator = None

        if reske_yavailability_zones is not None:
            self.reske_yavailability_zones = reske_yavailability_zones
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if os_vendor_extendedsold_out_availability_zones is not None:
            self.os_vendor_extendedsold_out_availability_zones = os_vendor_extendedsold_out_availability_zones
        if volume_backend_name is not None:
            self.volume_backend_name = volume_backend_name
        if h_wavailability_zone is not None:
            self.h_wavailability_zone = h_wavailability_zone

    @property
    def reske_yavailability_zones(self):
        """Gets the reske_yavailability_zones of this VolumeTypeExtraSpecs.

        支持当前云硬盘类型的可用区列表，列表的元素以逗号分隔。

        :return: The reske_yavailability_zones of this VolumeTypeExtraSpecs.
        :rtype: str
        """
        return self._reske_yavailability_zones

    @reske_yavailability_zones.setter
    def reske_yavailability_zones(self, reske_yavailability_zones):
        """Sets the reske_yavailability_zones of this VolumeTypeExtraSpecs.

        支持当前云硬盘类型的可用区列表，列表的元素以逗号分隔。

        :param reske_yavailability_zones: The reske_yavailability_zones of this VolumeTypeExtraSpecs.
        :type reske_yavailability_zones: str
        """
        self._reske_yavailability_zones = reske_yavailability_zones

    @property
    def availability_zone(self):
        """Gets the availability_zone of this VolumeTypeExtraSpecs.

        预留属性。

        :return: The availability_zone of this VolumeTypeExtraSpecs.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this VolumeTypeExtraSpecs.

        预留属性。

        :param availability_zone: The availability_zone of this VolumeTypeExtraSpecs.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def os_vendor_extendedsold_out_availability_zones(self):
        """Gets the os_vendor_extendedsold_out_availability_zones of this VolumeTypeExtraSpecs.

        当前云硬盘类型已售罄的可用区列表，列表的元素以逗号分隔。

        :return: The os_vendor_extendedsold_out_availability_zones of this VolumeTypeExtraSpecs.
        :rtype: str
        """
        return self._os_vendor_extendedsold_out_availability_zones

    @os_vendor_extendedsold_out_availability_zones.setter
    def os_vendor_extendedsold_out_availability_zones(self, os_vendor_extendedsold_out_availability_zones):
        """Sets the os_vendor_extendedsold_out_availability_zones of this VolumeTypeExtraSpecs.

        当前云硬盘类型已售罄的可用区列表，列表的元素以逗号分隔。

        :param os_vendor_extendedsold_out_availability_zones: The os_vendor_extendedsold_out_availability_zones of this VolumeTypeExtraSpecs.
        :type os_vendor_extendedsold_out_availability_zones: str
        """
        self._os_vendor_extendedsold_out_availability_zones = os_vendor_extendedsold_out_availability_zones

    @property
    def volume_backend_name(self):
        """Gets the volume_backend_name of this VolumeTypeExtraSpecs.

        预留属性。

        :return: The volume_backend_name of this VolumeTypeExtraSpecs.
        :rtype: str
        """
        return self._volume_backend_name

    @volume_backend_name.setter
    def volume_backend_name(self, volume_backend_name):
        """Sets the volume_backend_name of this VolumeTypeExtraSpecs.

        预留属性。

        :param volume_backend_name: The volume_backend_name of this VolumeTypeExtraSpecs.
        :type volume_backend_name: str
        """
        self._volume_backend_name = volume_backend_name

    @property
    def h_wavailability_zone(self):
        """Gets the h_wavailability_zone of this VolumeTypeExtraSpecs.

        预留属性。

        :return: The h_wavailability_zone of this VolumeTypeExtraSpecs.
        :rtype: str
        """
        return self._h_wavailability_zone

    @h_wavailability_zone.setter
    def h_wavailability_zone(self, h_wavailability_zone):
        """Sets the h_wavailability_zone of this VolumeTypeExtraSpecs.

        预留属性。

        :param h_wavailability_zone: The h_wavailability_zone of this VolumeTypeExtraSpecs.
        :type h_wavailability_zone: str
        """
        self._h_wavailability_zone = h_wavailability_zone

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
        if not isinstance(other, VolumeTypeExtraSpecs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
