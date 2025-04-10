# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BehaviorsConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'positive_behaviors': 'list[BehaviorWeights]',
        'negative_behaviors': 'list[BehaviorWeights]'
    }

    attribute_map = {
        'positive_behaviors': 'positive_behaviors',
        'negative_behaviors': 'negative_behaviors'
    }

    def __init__(self, positive_behaviors=None, negative_behaviors=None):
        r"""BehaviorsConfig

        The model defined in huaweicloud sdk

        :param positive_behaviors: 正向行为。
        :type positive_behaviors: list[:class:`huaweicloudsdkres.v1.BehaviorWeights`]
        :param negative_behaviors: 负向行为。
        :type negative_behaviors: list[:class:`huaweicloudsdkres.v1.BehaviorWeights`]
        """
        
        

        self._positive_behaviors = None
        self._negative_behaviors = None
        self.discriminator = None

        if positive_behaviors is not None:
            self.positive_behaviors = positive_behaviors
        if negative_behaviors is not None:
            self.negative_behaviors = negative_behaviors

    @property
    def positive_behaviors(self):
        r"""Gets the positive_behaviors of this BehaviorsConfig.

        正向行为。

        :return: The positive_behaviors of this BehaviorsConfig.
        :rtype: list[:class:`huaweicloudsdkres.v1.BehaviorWeights`]
        """
        return self._positive_behaviors

    @positive_behaviors.setter
    def positive_behaviors(self, positive_behaviors):
        r"""Sets the positive_behaviors of this BehaviorsConfig.

        正向行为。

        :param positive_behaviors: The positive_behaviors of this BehaviorsConfig.
        :type positive_behaviors: list[:class:`huaweicloudsdkres.v1.BehaviorWeights`]
        """
        self._positive_behaviors = positive_behaviors

    @property
    def negative_behaviors(self):
        r"""Gets the negative_behaviors of this BehaviorsConfig.

        负向行为。

        :return: The negative_behaviors of this BehaviorsConfig.
        :rtype: list[:class:`huaweicloudsdkres.v1.BehaviorWeights`]
        """
        return self._negative_behaviors

    @negative_behaviors.setter
    def negative_behaviors(self, negative_behaviors):
        r"""Sets the negative_behaviors of this BehaviorsConfig.

        负向行为。

        :param negative_behaviors: The negative_behaviors of this BehaviorsConfig.
        :type negative_behaviors: list[:class:`huaweicloudsdkres.v1.BehaviorWeights`]
        """
        self._negative_behaviors = negative_behaviors

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
        if not isinstance(other, BehaviorsConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
