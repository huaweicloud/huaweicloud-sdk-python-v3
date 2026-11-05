# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SupabaseAppBasicConfig:

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
        'vpc_id': 'str',
        'subnet_id': 'str',
        'time_zone': 'str'
    }

    attribute_map = {
        'region': 'region',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'time_zone': 'time_zone'
    }

    def __init__(self, region=None, vpc_id=None, subnet_id=None, time_zone=None):
        r"""SupabaseAppBasicConfig

        The model defined in huaweicloud sdk

        :param region: 区域ID。
        :type region: str
        :param vpc_id: 虚拟私有云ID。
        :type vpc_id: str
        :param subnet_id: 子网网络ID。
        :type subnet_id: str
        :param time_zone: UTC时区（可选）。
        :type time_zone: str
        """
        
        

        self._region = None
        self._vpc_id = None
        self._subnet_id = None
        self._time_zone = None
        self.discriminator = None

        self.region = region
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        if time_zone is not None:
            self.time_zone = time_zone

    @property
    def region(self):
        r"""Gets the region of this SupabaseAppBasicConfig.

        区域ID。

        :return: The region of this SupabaseAppBasicConfig.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this SupabaseAppBasicConfig.

        区域ID。

        :param region: The region of this SupabaseAppBasicConfig.
        :type region: str
        """
        self._region = region

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this SupabaseAppBasicConfig.

        虚拟私有云ID。

        :return: The vpc_id of this SupabaseAppBasicConfig.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this SupabaseAppBasicConfig.

        虚拟私有云ID。

        :param vpc_id: The vpc_id of this SupabaseAppBasicConfig.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this SupabaseAppBasicConfig.

        子网网络ID。

        :return: The subnet_id of this SupabaseAppBasicConfig.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this SupabaseAppBasicConfig.

        子网网络ID。

        :param subnet_id: The subnet_id of this SupabaseAppBasicConfig.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def time_zone(self):
        r"""Gets the time_zone of this SupabaseAppBasicConfig.

        UTC时区（可选）。

        :return: The time_zone of this SupabaseAppBasicConfig.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        r"""Sets the time_zone of this SupabaseAppBasicConfig.

        UTC时区（可选）。

        :param time_zone: The time_zone of this SupabaseAppBasicConfig.
        :type time_zone: str
        """
        self._time_zone = time_zone

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SupabaseAppBasicConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
