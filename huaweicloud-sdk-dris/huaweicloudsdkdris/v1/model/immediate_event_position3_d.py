# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImmediateEventPosition3D:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'lat': 'float',
        'lon': 'float',
        'ele': 'float'
    }

    attribute_map = {
        'lat': 'lat',
        'lon': 'lon',
        'ele': 'ele'
    }

    def __init__(self, lat=None, lon=None, ele=None):
        """ImmediateEventPosition3D

        The model defined in huaweicloud sdk

        :param lat: **参数说明**：定义纬度数值，北纬为正，南纬为负，单位°，精度小数点后7位。
        :type lat: float
        :param lon: **参数说明**：定义经度数值。东经为正，西经为负，单位°，精度小数点后7位。
        :type lon: float
        :param ele: **参数说明**：定义海拔高程，可选，单位为分米。
        :type ele: float
        """
        
        

        self._lat = None
        self._lon = None
        self._ele = None
        self.discriminator = None

        self.lat = lat
        self.lon = lon
        if ele is not None:
            self.ele = ele

    @property
    def lat(self):
        """Gets the lat of this ImmediateEventPosition3D.

        **参数说明**：定义纬度数值，北纬为正，南纬为负，单位°，精度小数点后7位。

        :return: The lat of this ImmediateEventPosition3D.
        :rtype: float
        """
        return self._lat

    @lat.setter
    def lat(self, lat):
        """Sets the lat of this ImmediateEventPosition3D.

        **参数说明**：定义纬度数值，北纬为正，南纬为负，单位°，精度小数点后7位。

        :param lat: The lat of this ImmediateEventPosition3D.
        :type lat: float
        """
        self._lat = lat

    @property
    def lon(self):
        """Gets the lon of this ImmediateEventPosition3D.

        **参数说明**：定义经度数值。东经为正，西经为负，单位°，精度小数点后7位。

        :return: The lon of this ImmediateEventPosition3D.
        :rtype: float
        """
        return self._lon

    @lon.setter
    def lon(self, lon):
        """Sets the lon of this ImmediateEventPosition3D.

        **参数说明**：定义经度数值。东经为正，西经为负，单位°，精度小数点后7位。

        :param lon: The lon of this ImmediateEventPosition3D.
        :type lon: float
        """
        self._lon = lon

    @property
    def ele(self):
        """Gets the ele of this ImmediateEventPosition3D.

        **参数说明**：定义海拔高程，可选，单位为分米。

        :return: The ele of this ImmediateEventPosition3D.
        :rtype: float
        """
        return self._ele

    @ele.setter
    def ele(self, ele):
        """Sets the ele of this ImmediateEventPosition3D.

        **参数说明**：定义海拔高程，可选，单位为分米。

        :param ele: The ele of this ImmediateEventPosition3D.
        :type ele: float
        """
        self._ele = ele

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
        if not isinstance(other, ImmediateEventPosition3D):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
