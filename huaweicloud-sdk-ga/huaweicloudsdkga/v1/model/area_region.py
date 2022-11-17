# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AreaRegion:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'area': 'str',
        'regions': 'list[str]'
    }

    attribute_map = {
        'area': 'area',
        'regions': 'regions'
    }

    def __init__(self, area=None, regions=None):
        """AreaRegion

        The model defined in huaweicloud sdk

        :param area: 区域所属地区，取值： - OUTOFCM： 中国大陆以外 - CM：中国大陆
        :type area: str
        :param regions: 区域ID列表。
        :type regions: list[str]
        """
        
        

        self._area = None
        self._regions = None
        self.discriminator = None

        if area is not None:
            self.area = area
        if regions is not None:
            self.regions = regions

    @property
    def area(self):
        """Gets the area of this AreaRegion.

        区域所属地区，取值： - OUTOFCM： 中国大陆以外 - CM：中国大陆

        :return: The area of this AreaRegion.
        :rtype: str
        """
        return self._area

    @area.setter
    def area(self, area):
        """Sets the area of this AreaRegion.

        区域所属地区，取值： - OUTOFCM： 中国大陆以外 - CM：中国大陆

        :param area: The area of this AreaRegion.
        :type area: str
        """
        self._area = area

    @property
    def regions(self):
        """Gets the regions of this AreaRegion.

        区域ID列表。

        :return: The regions of this AreaRegion.
        :rtype: list[str]
        """
        return self._regions

    @regions.setter
    def regions(self, regions):
        """Sets the regions of this AreaRegion.

        区域ID列表。

        :param regions: The regions of this AreaRegion.
        :type regions: list[str]
        """
        self._regions = regions

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
        if not isinstance(other, AreaRegion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
