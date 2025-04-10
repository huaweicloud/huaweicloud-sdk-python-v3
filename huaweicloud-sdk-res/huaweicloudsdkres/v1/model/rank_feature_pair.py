# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RankFeaturePair:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'feature_name_a': 'str',
        'feature_name_b': 'str',
        'weight': 'float'
    }

    attribute_map = {
        'feature_name_a': 'feature_name_a',
        'feature_name_b': 'feature_name_b',
        'weight': 'weight'
    }

    def __init__(self, feature_name_a=None, feature_name_b=None, weight=None):
        r"""RankFeaturePair

        The model defined in huaweicloud sdk

        :param feature_name_a: 待推荐对象的属性。
        :type feature_name_a: str
        :param feature_name_b: 被推荐对象的属性。
        :type feature_name_b: str
        :param weight: 权重。
        :type weight: float
        """
        
        

        self._feature_name_a = None
        self._feature_name_b = None
        self._weight = None
        self.discriminator = None

        if feature_name_a is not None:
            self.feature_name_a = feature_name_a
        if feature_name_b is not None:
            self.feature_name_b = feature_name_b
        if weight is not None:
            self.weight = weight

    @property
    def feature_name_a(self):
        r"""Gets the feature_name_a of this RankFeaturePair.

        待推荐对象的属性。

        :return: The feature_name_a of this RankFeaturePair.
        :rtype: str
        """
        return self._feature_name_a

    @feature_name_a.setter
    def feature_name_a(self, feature_name_a):
        r"""Sets the feature_name_a of this RankFeaturePair.

        待推荐对象的属性。

        :param feature_name_a: The feature_name_a of this RankFeaturePair.
        :type feature_name_a: str
        """
        self._feature_name_a = feature_name_a

    @property
    def feature_name_b(self):
        r"""Gets the feature_name_b of this RankFeaturePair.

        被推荐对象的属性。

        :return: The feature_name_b of this RankFeaturePair.
        :rtype: str
        """
        return self._feature_name_b

    @feature_name_b.setter
    def feature_name_b(self, feature_name_b):
        r"""Sets the feature_name_b of this RankFeaturePair.

        被推荐对象的属性。

        :param feature_name_b: The feature_name_b of this RankFeaturePair.
        :type feature_name_b: str
        """
        self._feature_name_b = feature_name_b

    @property
    def weight(self):
        r"""Gets the weight of this RankFeaturePair.

        权重。

        :return: The weight of this RankFeaturePair.
        :rtype: float
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        r"""Sets the weight of this RankFeaturePair.

        权重。

        :param weight: The weight of this RankFeaturePair.
        :type weight: float
        """
        self._weight = weight

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
        if not isinstance(other, RankFeaturePair):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
