# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMeasureUnitsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'measure_units': 'list[MeasureUnitRest]'
    }

    attribute_map = {
        'measure_units': 'measure_units'
    }

    def __init__(self, measure_units=None):
        """ListMeasureUnitsResponse

        The model defined in huaweicloud sdk

        :param measure_units: 度量单位信息，具体参见表2。
        :type measure_units: list[:class:`huaweicloudsdkbssintl.v2.MeasureUnitRest`]
        """
        
        super(ListMeasureUnitsResponse, self).__init__()

        self._measure_units = None
        self.discriminator = None

        if measure_units is not None:
            self.measure_units = measure_units

    @property
    def measure_units(self):
        """Gets the measure_units of this ListMeasureUnitsResponse.

        度量单位信息，具体参见表2。

        :return: The measure_units of this ListMeasureUnitsResponse.
        :rtype: list[:class:`huaweicloudsdkbssintl.v2.MeasureUnitRest`]
        """
        return self._measure_units

    @measure_units.setter
    def measure_units(self, measure_units):
        """Sets the measure_units of this ListMeasureUnitsResponse.

        度量单位信息，具体参见表2。

        :param measure_units: The measure_units of this ListMeasureUnitsResponse.
        :type measure_units: list[:class:`huaweicloudsdkbssintl.v2.MeasureUnitRest`]
        """
        self._measure_units = measure_units

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
        if not isinstance(other, ListMeasureUnitsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
