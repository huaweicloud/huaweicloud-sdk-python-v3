# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SampleDataValue:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sample': 'QuerySample',
        'data_points': 'list[MetricDataPoints]'
    }

    attribute_map = {
        'sample': 'sample',
        'data_points': 'data_points'
    }

    def __init__(self, sample=None, data_points=None):
        """SampleDataValue

        The model defined in huaweicloud sdk

        :param sample: 
        :type sample: :class:`huaweicloudsdkaom.v2.QuerySample`
        :param data_points: 时序数据。
        :type data_points: list[:class:`huaweicloudsdkaom.v2.MetricDataPoints`]
        """
        
        

        self._sample = None
        self._data_points = None
        self.discriminator = None

        if sample is not None:
            self.sample = sample
        if data_points is not None:
            self.data_points = data_points

    @property
    def sample(self):
        """Gets the sample of this SampleDataValue.

        :return: The sample of this SampleDataValue.
        :rtype: :class:`huaweicloudsdkaom.v2.QuerySample`
        """
        return self._sample

    @sample.setter
    def sample(self, sample):
        """Sets the sample of this SampleDataValue.

        :param sample: The sample of this SampleDataValue.
        :type sample: :class:`huaweicloudsdkaom.v2.QuerySample`
        """
        self._sample = sample

    @property
    def data_points(self):
        """Gets the data_points of this SampleDataValue.

        时序数据。

        :return: The data_points of this SampleDataValue.
        :rtype: list[:class:`huaweicloudsdkaom.v2.MetricDataPoints`]
        """
        return self._data_points

    @data_points.setter
    def data_points(self, data_points):
        """Sets the data_points of this SampleDataValue.

        时序数据。

        :param data_points: The data_points of this SampleDataValue.
        :type data_points: list[:class:`huaweicloudsdkaom.v2.MetricDataPoints`]
        """
        self._data_points = data_points

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
        if not isinstance(other, SampleDataValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
