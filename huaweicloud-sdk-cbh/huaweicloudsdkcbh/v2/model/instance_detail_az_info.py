# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceDetailAzInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region': 'str',
        'zone': 'str',
        'availability_zone_display': 'str',
        'slave_zone': 'str',
        'slave_zone_display': 'str'
    }

    attribute_map = {
        'region': 'region',
        'zone': 'zone',
        'availability_zone_display': 'availability_zone_display',
        'slave_zone': 'slave_zone',
        'slave_zone_display': 'slave_zone_display'
    }

    def __init__(self, region=None, zone=None, availability_zone_display=None, slave_zone=None, slave_zone_display=None):
        r"""InstanceDetailAzInfo

        The model defined in huaweicloud sdk

        :param region: 云堡垒机实例所在可用区ID。
        :type region: str
        :param zone: 云堡垒机实例所在可用分区ID。(实例为主备模式时作为主机实例所在可用分区)
        :type zone: str
        :param availability_zone_display: 云堡垒机实例所在可用分区中文名称。(实例为主备模式时作为主机实例所在可用分区中文名称)
        :type availability_zone_display: str
        :param slave_zone: 云堡垒机备机实例所在可用区。
        :type slave_zone: str
        :param slave_zone_display: 云堡垒机备机实例所在可用区中文名称。
        :type slave_zone_display: str
        """
        
        

        self._region = None
        self._zone = None
        self._availability_zone_display = None
        self._slave_zone = None
        self._slave_zone_display = None
        self.discriminator = None

        self.region = region
        self.zone = zone
        self.availability_zone_display = availability_zone_display
        if slave_zone is not None:
            self.slave_zone = slave_zone
        if slave_zone_display is not None:
            self.slave_zone_display = slave_zone_display

    @property
    def region(self):
        r"""Gets the region of this InstanceDetailAzInfo.

        云堡垒机实例所在可用区ID。

        :return: The region of this InstanceDetailAzInfo.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this InstanceDetailAzInfo.

        云堡垒机实例所在可用区ID。

        :param region: The region of this InstanceDetailAzInfo.
        :type region: str
        """
        self._region = region

    @property
    def zone(self):
        r"""Gets the zone of this InstanceDetailAzInfo.

        云堡垒机实例所在可用分区ID。(实例为主备模式时作为主机实例所在可用分区)

        :return: The zone of this InstanceDetailAzInfo.
        :rtype: str
        """
        return self._zone

    @zone.setter
    def zone(self, zone):
        r"""Sets the zone of this InstanceDetailAzInfo.

        云堡垒机实例所在可用分区ID。(实例为主备模式时作为主机实例所在可用分区)

        :param zone: The zone of this InstanceDetailAzInfo.
        :type zone: str
        """
        self._zone = zone

    @property
    def availability_zone_display(self):
        r"""Gets the availability_zone_display of this InstanceDetailAzInfo.

        云堡垒机实例所在可用分区中文名称。(实例为主备模式时作为主机实例所在可用分区中文名称)

        :return: The availability_zone_display of this InstanceDetailAzInfo.
        :rtype: str
        """
        return self._availability_zone_display

    @availability_zone_display.setter
    def availability_zone_display(self, availability_zone_display):
        r"""Sets the availability_zone_display of this InstanceDetailAzInfo.

        云堡垒机实例所在可用分区中文名称。(实例为主备模式时作为主机实例所在可用分区中文名称)

        :param availability_zone_display: The availability_zone_display of this InstanceDetailAzInfo.
        :type availability_zone_display: str
        """
        self._availability_zone_display = availability_zone_display

    @property
    def slave_zone(self):
        r"""Gets the slave_zone of this InstanceDetailAzInfo.

        云堡垒机备机实例所在可用区。

        :return: The slave_zone of this InstanceDetailAzInfo.
        :rtype: str
        """
        return self._slave_zone

    @slave_zone.setter
    def slave_zone(self, slave_zone):
        r"""Sets the slave_zone of this InstanceDetailAzInfo.

        云堡垒机备机实例所在可用区。

        :param slave_zone: The slave_zone of this InstanceDetailAzInfo.
        :type slave_zone: str
        """
        self._slave_zone = slave_zone

    @property
    def slave_zone_display(self):
        r"""Gets the slave_zone_display of this InstanceDetailAzInfo.

        云堡垒机备机实例所在可用区中文名称。

        :return: The slave_zone_display of this InstanceDetailAzInfo.
        :rtype: str
        """
        return self._slave_zone_display

    @slave_zone_display.setter
    def slave_zone_display(self, slave_zone_display):
        r"""Sets the slave_zone_display of this InstanceDetailAzInfo.

        云堡垒机备机实例所在可用区中文名称。

        :param slave_zone_display: The slave_zone_display of this InstanceDetailAzInfo.
        :type slave_zone_display: str
        """
        self._slave_zone_display = slave_zone_display

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
        if not isinstance(other, InstanceDetailAzInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
