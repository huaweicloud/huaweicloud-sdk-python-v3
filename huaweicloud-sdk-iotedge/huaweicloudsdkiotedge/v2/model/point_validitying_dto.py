# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PointValidityingDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'min': 'object',
        'max': 'object',
        'outlier_filtering': 'bool'
    }

    attribute_map = {
        'min': 'min',
        'max': 'max',
        'outlier_filtering': 'outlier_filtering'
    }

    def __init__(self, min=None, max=None, outlier_filtering=None):
        r"""PointValidityingDTO

        The model defined in huaweicloud sdk

        :param min: 点位上报值的最小值，小于该值则上报告警
        :type min: object
        :param max: 点位上报值的最大值，大于该值则上报告警
        :type max: object
        :param outlier_filtering: 异常值过滤
        :type outlier_filtering: bool
        """
        
        

        self._min = None
        self._max = None
        self._outlier_filtering = None
        self.discriminator = None

        self.min = min
        self.max = max
        if outlier_filtering is not None:
            self.outlier_filtering = outlier_filtering

    @property
    def min(self):
        r"""Gets the min of this PointValidityingDTO.

        点位上报值的最小值，小于该值则上报告警

        :return: The min of this PointValidityingDTO.
        :rtype: object
        """
        return self._min

    @min.setter
    def min(self, min):
        r"""Sets the min of this PointValidityingDTO.

        点位上报值的最小值，小于该值则上报告警

        :param min: The min of this PointValidityingDTO.
        :type min: object
        """
        self._min = min

    @property
    def max(self):
        r"""Gets the max of this PointValidityingDTO.

        点位上报值的最大值，大于该值则上报告警

        :return: The max of this PointValidityingDTO.
        :rtype: object
        """
        return self._max

    @max.setter
    def max(self, max):
        r"""Sets the max of this PointValidityingDTO.

        点位上报值的最大值，大于该值则上报告警

        :param max: The max of this PointValidityingDTO.
        :type max: object
        """
        self._max = max

    @property
    def outlier_filtering(self):
        r"""Gets the outlier_filtering of this PointValidityingDTO.

        异常值过滤

        :return: The outlier_filtering of this PointValidityingDTO.
        :rtype: bool
        """
        return self._outlier_filtering

    @outlier_filtering.setter
    def outlier_filtering(self, outlier_filtering):
        r"""Sets the outlier_filtering of this PointValidityingDTO.

        异常值过滤

        :param outlier_filtering: The outlier_filtering of this PointValidityingDTO.
        :type outlier_filtering: bool
        """
        self._outlier_filtering = outlier_filtering

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
        if not isinstance(other, PointValidityingDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
