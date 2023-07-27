# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Region:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region_id': 'str',
        'area': 'str',
        'supported_endpoint_types': 'list[str]'
    }

    attribute_map = {
        'region_id': 'region_id',
        'area': 'area',
        'supported_endpoint_types': 'supported_endpoint_types'
    }

    def __init__(self, region_id=None, area=None, supported_endpoint_types=None):
        """Region

        The model defined in huaweicloud sdk

        :param region_id: 区域ID。
        :type region_id: str
        :param area: 区域所属地区，取值： - OUTOFCM： 中国大陆以外 - CM：中国大陆
        :type area: str
        :param supported_endpoint_types: 区域支持的终端节点类型。取值： EIP：弹性公网IP
        :type supported_endpoint_types: list[str]
        """
        
        

        self._region_id = None
        self._area = None
        self._supported_endpoint_types = None
        self.discriminator = None

        if region_id is not None:
            self.region_id = region_id
        if area is not None:
            self.area = area
        if supported_endpoint_types is not None:
            self.supported_endpoint_types = supported_endpoint_types

    @property
    def region_id(self):
        """Gets the region_id of this Region.

        区域ID。

        :return: The region_id of this Region.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this Region.

        区域ID。

        :param region_id: The region_id of this Region.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def area(self):
        """Gets the area of this Region.

        区域所属地区，取值： - OUTOFCM： 中国大陆以外 - CM：中国大陆

        :return: The area of this Region.
        :rtype: str
        """
        return self._area

    @area.setter
    def area(self, area):
        """Sets the area of this Region.

        区域所属地区，取值： - OUTOFCM： 中国大陆以外 - CM：中国大陆

        :param area: The area of this Region.
        :type area: str
        """
        self._area = area

    @property
    def supported_endpoint_types(self):
        """Gets the supported_endpoint_types of this Region.

        区域支持的终端节点类型。取值： EIP：弹性公网IP

        :return: The supported_endpoint_types of this Region.
        :rtype: list[str]
        """
        return self._supported_endpoint_types

    @supported_endpoint_types.setter
    def supported_endpoint_types(self, supported_endpoint_types):
        """Sets the supported_endpoint_types of this Region.

        区域支持的终端节点类型。取值： EIP：弹性公网IP

        :param supported_endpoint_types: The supported_endpoint_types of this Region.
        :type supported_endpoint_types: list[str]
        """
        self._supported_endpoint_types = supported_endpoint_types

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
        if not isinstance(other, Region):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
