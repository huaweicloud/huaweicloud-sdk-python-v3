# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeTypeElasticVolumeSpecs:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'step': 'int',
        'min_size': 'int',
        'max_size': 'int'
    }

    attribute_map = {
        'type': 'type',
        'step': 'step',
        'min_size': 'min_size',
        'max_size': 'max_size'
    }

    def __init__(self, type=None, step=None, min_size=None, max_size=None):
        r"""NodeTypeElasticVolumeSpecs

        The model defined in huaweicloud sdk

        :param type: **参数解释**： 云盘存储类型。 **取值范围**： 不涉及。
        :type type: str
        :param step: **参数解释**： 云盘容量调整步长。 **取值范围**： 不涉及。
        :type step: int
        :param min_size: **参数解释**： 云盘支持的最小容量。 **取值范围**： 不涉及。
        :type min_size: int
        :param max_size: **参数解释**： 云盘支持的最大容量。 **取值范围**： 不涉及。
        :type max_size: int
        """
        
        

        self._type = None
        self._step = None
        self._min_size = None
        self._max_size = None
        self.discriminator = None

        self.type = type
        self.step = step
        self.min_size = min_size
        self.max_size = max_size

    @property
    def type(self):
        r"""Gets the type of this NodeTypeElasticVolumeSpecs.

        **参数解释**： 云盘存储类型。 **取值范围**： 不涉及。

        :return: The type of this NodeTypeElasticVolumeSpecs.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this NodeTypeElasticVolumeSpecs.

        **参数解释**： 云盘存储类型。 **取值范围**： 不涉及。

        :param type: The type of this NodeTypeElasticVolumeSpecs.
        :type type: str
        """
        self._type = type

    @property
    def step(self):
        r"""Gets the step of this NodeTypeElasticVolumeSpecs.

        **参数解释**： 云盘容量调整步长。 **取值范围**： 不涉及。

        :return: The step of this NodeTypeElasticVolumeSpecs.
        :rtype: int
        """
        return self._step

    @step.setter
    def step(self, step):
        r"""Sets the step of this NodeTypeElasticVolumeSpecs.

        **参数解释**： 云盘容量调整步长。 **取值范围**： 不涉及。

        :param step: The step of this NodeTypeElasticVolumeSpecs.
        :type step: int
        """
        self._step = step

    @property
    def min_size(self):
        r"""Gets the min_size of this NodeTypeElasticVolumeSpecs.

        **参数解释**： 云盘支持的最小容量。 **取值范围**： 不涉及。

        :return: The min_size of this NodeTypeElasticVolumeSpecs.
        :rtype: int
        """
        return self._min_size

    @min_size.setter
    def min_size(self, min_size):
        r"""Sets the min_size of this NodeTypeElasticVolumeSpecs.

        **参数解释**： 云盘支持的最小容量。 **取值范围**： 不涉及。

        :param min_size: The min_size of this NodeTypeElasticVolumeSpecs.
        :type min_size: int
        """
        self._min_size = min_size

    @property
    def max_size(self):
        r"""Gets the max_size of this NodeTypeElasticVolumeSpecs.

        **参数解释**： 云盘支持的最大容量。 **取值范围**： 不涉及。

        :return: The max_size of this NodeTypeElasticVolumeSpecs.
        :rtype: int
        """
        return self._max_size

    @max_size.setter
    def max_size(self, max_size):
        r"""Sets the max_size of this NodeTypeElasticVolumeSpecs.

        **参数解释**： 云盘支持的最大容量。 **取值范围**： 不涉及。

        :param max_size: The max_size of this NodeTypeElasticVolumeSpecs.
        :type max_size: int
        """
        self._max_size = max_size

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
        if not isinstance(other, NodeTypeElasticVolumeSpecs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
