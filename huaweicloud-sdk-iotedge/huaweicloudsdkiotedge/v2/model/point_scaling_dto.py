# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PointScalingDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ratio': 'float',
        'base': 'float',
        'accuracy': 'int'
    }

    attribute_map = {
        'ratio': 'ratio',
        'base': 'base',
        'accuracy': 'accuracy'
    }

    def __init__(self, ratio=None, base=None, accuracy=None):
        r"""PointScalingDTO

        The model defined in huaweicloud sdk

        :param ratio: 缩放的倍率
        :type ratio: float
        :param base: 基准值
        :type base: float
        :param accuracy: 缩放后结果的精度，精确到小数点后几位,-1表示全部保留，0表示只保留整数位
        :type accuracy: int
        """
        
        

        self._ratio = None
        self._base = None
        self._accuracy = None
        self.discriminator = None

        self.ratio = ratio
        self.base = base
        if accuracy is not None:
            self.accuracy = accuracy

    @property
    def ratio(self):
        r"""Gets the ratio of this PointScalingDTO.

        缩放的倍率

        :return: The ratio of this PointScalingDTO.
        :rtype: float
        """
        return self._ratio

    @ratio.setter
    def ratio(self, ratio):
        r"""Sets the ratio of this PointScalingDTO.

        缩放的倍率

        :param ratio: The ratio of this PointScalingDTO.
        :type ratio: float
        """
        self._ratio = ratio

    @property
    def base(self):
        r"""Gets the base of this PointScalingDTO.

        基准值

        :return: The base of this PointScalingDTO.
        :rtype: float
        """
        return self._base

    @base.setter
    def base(self, base):
        r"""Sets the base of this PointScalingDTO.

        基准值

        :param base: The base of this PointScalingDTO.
        :type base: float
        """
        self._base = base

    @property
    def accuracy(self):
        r"""Gets the accuracy of this PointScalingDTO.

        缩放后结果的精度，精确到小数点后几位,-1表示全部保留，0表示只保留整数位

        :return: The accuracy of this PointScalingDTO.
        :rtype: int
        """
        return self._accuracy

    @accuracy.setter
    def accuracy(self, accuracy):
        r"""Sets the accuracy of this PointScalingDTO.

        缩放后结果的精度，精确到小数点后几位,-1表示全部保留，0表示只保留整数位

        :param accuracy: The accuracy of this PointScalingDTO.
        :type accuracy: int
        """
        self._accuracy = accuracy

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
        if not isinstance(other, PointScalingDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
