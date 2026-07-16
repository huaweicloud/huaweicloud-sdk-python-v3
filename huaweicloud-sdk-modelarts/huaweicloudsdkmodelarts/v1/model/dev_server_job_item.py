# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DevServerJobItem:

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
        'spec': 'dict(str, str)'
    }

    attribute_map = {
        'type': 'type',
        'spec': 'spec'
    }

    def __init__(self, type=None, spec=None):
        r"""DevServerJobItem

        The model defined in huaweicloud sdk

        :param type: **参数解释**：细粒度任务类型。 **取值范围**：- COMMON   - DEVICE_LOG_COLLECT 等
        :type type: str
        :param spec: **参数解释**：任务所需参数。
        :type spec: dict(str, str)
        """
        
        

        self._type = None
        self._spec = None
        self.discriminator = None

        self.type = type
        if spec is not None:
            self.spec = spec

    @property
    def type(self):
        r"""Gets the type of this DevServerJobItem.

        **参数解释**：细粒度任务类型。 **取值范围**：- COMMON   - DEVICE_LOG_COLLECT 等

        :return: The type of this DevServerJobItem.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this DevServerJobItem.

        **参数解释**：细粒度任务类型。 **取值范围**：- COMMON   - DEVICE_LOG_COLLECT 等

        :param type: The type of this DevServerJobItem.
        :type type: str
        """
        self._type = type

    @property
    def spec(self):
        r"""Gets the spec of this DevServerJobItem.

        **参数解释**：任务所需参数。

        :return: The spec of this DevServerJobItem.
        :rtype: dict(str, str)
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        r"""Sets the spec of this DevServerJobItem.

        **参数解释**：任务所需参数。

        :param spec: The spec of this DevServerJobItem.
        :type spec: dict(str, str)
        """
        self._spec = spec

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
        if not isinstance(other, DevServerJobItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
