# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Toleration:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'operator': 'str',
        'value': 'str',
        'effect': 'str',
        'toleration_seconds': 'int'
    }

    attribute_map = {
        'key': 'key',
        'operator': 'operator',
        'value': 'value',
        'effect': 'effect',
        'toleration_seconds': 'tolerationSeconds'
    }

    def __init__(self, key=None, operator=None, value=None, effect=None, toleration_seconds=None):
        r"""Toleration

        The model defined in huaweicloud sdk

        :param key: 表示要容忍的污点键名
        :type key: str
        :param operator: 定义Key与Value之间的关系，可选值为Exists或Equal，默认为Equal
        :type operator: str
        :param value: 表示要匹配的污点值，当Operator为Exists时，Value应为空
        :type value: str
        :param effect: 指定要匹配的污点效果，可选值为 NoSchedule、PreferNoSchedule或NoExecute，如果为空，表示匹配所有效果
        :type effect: str
        :param toleration_seconds: 仅对NoExecute效果有效，表示Pod能容忍污点的时间
        :type toleration_seconds: int
        """
        
        

        self._key = None
        self._operator = None
        self._value = None
        self._effect = None
        self._toleration_seconds = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if operator is not None:
            self.operator = operator
        if value is not None:
            self.value = value
        if effect is not None:
            self.effect = effect
        if toleration_seconds is not None:
            self.toleration_seconds = toleration_seconds

    @property
    def key(self):
        r"""Gets the key of this Toleration.

        表示要容忍的污点键名

        :return: The key of this Toleration.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this Toleration.

        表示要容忍的污点键名

        :param key: The key of this Toleration.
        :type key: str
        """
        self._key = key

    @property
    def operator(self):
        r"""Gets the operator of this Toleration.

        定义Key与Value之间的关系，可选值为Exists或Equal，默认为Equal

        :return: The operator of this Toleration.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        r"""Sets the operator of this Toleration.

        定义Key与Value之间的关系，可选值为Exists或Equal，默认为Equal

        :param operator: The operator of this Toleration.
        :type operator: str
        """
        self._operator = operator

    @property
    def value(self):
        r"""Gets the value of this Toleration.

        表示要匹配的污点值，当Operator为Exists时，Value应为空

        :return: The value of this Toleration.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this Toleration.

        表示要匹配的污点值，当Operator为Exists时，Value应为空

        :param value: The value of this Toleration.
        :type value: str
        """
        self._value = value

    @property
    def effect(self):
        r"""Gets the effect of this Toleration.

        指定要匹配的污点效果，可选值为 NoSchedule、PreferNoSchedule或NoExecute，如果为空，表示匹配所有效果

        :return: The effect of this Toleration.
        :rtype: str
        """
        return self._effect

    @effect.setter
    def effect(self, effect):
        r"""Sets the effect of this Toleration.

        指定要匹配的污点效果，可选值为 NoSchedule、PreferNoSchedule或NoExecute，如果为空，表示匹配所有效果

        :param effect: The effect of this Toleration.
        :type effect: str
        """
        self._effect = effect

    @property
    def toleration_seconds(self):
        r"""Gets the toleration_seconds of this Toleration.

        仅对NoExecute效果有效，表示Pod能容忍污点的时间

        :return: The toleration_seconds of this Toleration.
        :rtype: int
        """
        return self._toleration_seconds

    @toleration_seconds.setter
    def toleration_seconds(self, toleration_seconds):
        r"""Sets the toleration_seconds of this Toleration.

        仅对NoExecute效果有效，表示Pod能容忍污点的时间

        :param toleration_seconds: The toleration_seconds of this Toleration.
        :type toleration_seconds: int
        """
        self._toleration_seconds = toleration_seconds

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
        if not isinstance(other, Toleration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
