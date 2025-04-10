# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttributeInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rank_feature_pairs': 'list[RankFeaturePair]',
        'numerical_attrs': 'list[NumericalAttr]',
        'num_statistics_type': 'str'
    }

    attribute_map = {
        'rank_feature_pairs': 'rank_feature_pairs',
        'numerical_attrs': 'numerical_attrs',
        'num_statistics_type': 'num_statistics_type'
    }

    def __init__(self, rank_feature_pairs=None, numerical_attrs=None, num_statistics_type=None):
        r"""AttributeInfo

        The model defined in huaweicloud sdk

        :param rank_feature_pairs: 属性匹配对。
        :type rank_feature_pairs: list[:class:`huaweicloudsdkres.v1.RankFeaturePair`]
        :param numerical_attrs: 属性权重。
        :type numerical_attrs: list[:class:`huaweicloudsdkres.v1.NumericalAttr`]
        :param num_statistics_type: 统计方式： - ORDER，顺序 - ABS，绝对值
        :type num_statistics_type: str
        """
        
        

        self._rank_feature_pairs = None
        self._numerical_attrs = None
        self._num_statistics_type = None
        self.discriminator = None

        if rank_feature_pairs is not None:
            self.rank_feature_pairs = rank_feature_pairs
        if numerical_attrs is not None:
            self.numerical_attrs = numerical_attrs
        if num_statistics_type is not None:
            self.num_statistics_type = num_statistics_type

    @property
    def rank_feature_pairs(self):
        r"""Gets the rank_feature_pairs of this AttributeInfo.

        属性匹配对。

        :return: The rank_feature_pairs of this AttributeInfo.
        :rtype: list[:class:`huaweicloudsdkres.v1.RankFeaturePair`]
        """
        return self._rank_feature_pairs

    @rank_feature_pairs.setter
    def rank_feature_pairs(self, rank_feature_pairs):
        r"""Sets the rank_feature_pairs of this AttributeInfo.

        属性匹配对。

        :param rank_feature_pairs: The rank_feature_pairs of this AttributeInfo.
        :type rank_feature_pairs: list[:class:`huaweicloudsdkres.v1.RankFeaturePair`]
        """
        self._rank_feature_pairs = rank_feature_pairs

    @property
    def numerical_attrs(self):
        r"""Gets the numerical_attrs of this AttributeInfo.

        属性权重。

        :return: The numerical_attrs of this AttributeInfo.
        :rtype: list[:class:`huaweicloudsdkres.v1.NumericalAttr`]
        """
        return self._numerical_attrs

    @numerical_attrs.setter
    def numerical_attrs(self, numerical_attrs):
        r"""Sets the numerical_attrs of this AttributeInfo.

        属性权重。

        :param numerical_attrs: The numerical_attrs of this AttributeInfo.
        :type numerical_attrs: list[:class:`huaweicloudsdkres.v1.NumericalAttr`]
        """
        self._numerical_attrs = numerical_attrs

    @property
    def num_statistics_type(self):
        r"""Gets the num_statistics_type of this AttributeInfo.

        统计方式： - ORDER，顺序 - ABS，绝对值

        :return: The num_statistics_type of this AttributeInfo.
        :rtype: str
        """
        return self._num_statistics_type

    @num_statistics_type.setter
    def num_statistics_type(self, num_statistics_type):
        r"""Sets the num_statistics_type of this AttributeInfo.

        统计方式： - ORDER，顺序 - ABS，绝对值

        :param num_statistics_type: The num_statistics_type of this AttributeInfo.
        :type num_statistics_type: str
        """
        self._num_statistics_type = num_statistics_type

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
        if not isinstance(other, AttributeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
