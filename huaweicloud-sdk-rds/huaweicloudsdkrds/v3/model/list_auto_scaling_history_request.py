# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAutoScalingHistoryRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'x_language': 'str',
        'strategy_type': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'x_language': 'X-Language',
        'strategy_type': 'strategy_type',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, instance_id=None, x_language=None, strategy_type=None, offset=None, limit=None):
        r"""ListAutoScalingHistoryRequest

        The model defined in huaweicloud sdk

        :param instance_id: **参数解释**：  实例ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type instance_id: str
        :param x_language: **参数解释**：  请求语言类型。  **约束限制**：  不涉及。  **取值范围**：  - en-us - zh-cn  **默认取值**：  en-us。
        :type x_language: str
        :param strategy_type: **参数解释**：  查询的变配策略类型。  **约束限制**：  不涉及。  **取值范围**：  - FLAVOR_SCALING：规格变配 - READ_ONLY_SCALING：只读变配  **默认取值**：  FLAVOR_SCALING。
        :type strategy_type: str
        :param offset: **参数解释**：  索引位置，偏移量。  **约束限制**：  不涉及。  **取值范围**：  不涉及  **默认取值**：  0
        :type offset: int
        :param limit: **参数解释**：  查询记录数。  **约束限制**：  不涉及。  **取值范围**：  1-100  **默认取值**：  10
        :type limit: int
        """
        
        

        self._instance_id = None
        self._x_language = None
        self._strategy_type = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.instance_id = instance_id
        if x_language is not None:
            self.x_language = x_language
        if strategy_type is not None:
            self.strategy_type = strategy_type
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListAutoScalingHistoryRequest.

        **参数解释**：  实例ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The instance_id of this ListAutoScalingHistoryRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListAutoScalingHistoryRequest.

        **参数解释**：  实例ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param instance_id: The instance_id of this ListAutoScalingHistoryRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def x_language(self):
        r"""Gets the x_language of this ListAutoScalingHistoryRequest.

        **参数解释**：  请求语言类型。  **约束限制**：  不涉及。  **取值范围**：  - en-us - zh-cn  **默认取值**：  en-us。

        :return: The x_language of this ListAutoScalingHistoryRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListAutoScalingHistoryRequest.

        **参数解释**：  请求语言类型。  **约束限制**：  不涉及。  **取值范围**：  - en-us - zh-cn  **默认取值**：  en-us。

        :param x_language: The x_language of this ListAutoScalingHistoryRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def strategy_type(self):
        r"""Gets the strategy_type of this ListAutoScalingHistoryRequest.

        **参数解释**：  查询的变配策略类型。  **约束限制**：  不涉及。  **取值范围**：  - FLAVOR_SCALING：规格变配 - READ_ONLY_SCALING：只读变配  **默认取值**：  FLAVOR_SCALING。

        :return: The strategy_type of this ListAutoScalingHistoryRequest.
        :rtype: str
        """
        return self._strategy_type

    @strategy_type.setter
    def strategy_type(self, strategy_type):
        r"""Sets the strategy_type of this ListAutoScalingHistoryRequest.

        **参数解释**：  查询的变配策略类型。  **约束限制**：  不涉及。  **取值范围**：  - FLAVOR_SCALING：规格变配 - READ_ONLY_SCALING：只读变配  **默认取值**：  FLAVOR_SCALING。

        :param strategy_type: The strategy_type of this ListAutoScalingHistoryRequest.
        :type strategy_type: str
        """
        self._strategy_type = strategy_type

    @property
    def offset(self):
        r"""Gets the offset of this ListAutoScalingHistoryRequest.

        **参数解释**：  索引位置，偏移量。  **约束限制**：  不涉及。  **取值范围**：  不涉及  **默认取值**：  0

        :return: The offset of this ListAutoScalingHistoryRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAutoScalingHistoryRequest.

        **参数解释**：  索引位置，偏移量。  **约束限制**：  不涉及。  **取值范围**：  不涉及  **默认取值**：  0

        :param offset: The offset of this ListAutoScalingHistoryRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListAutoScalingHistoryRequest.

        **参数解释**：  查询记录数。  **约束限制**：  不涉及。  **取值范围**：  1-100  **默认取值**：  10

        :return: The limit of this ListAutoScalingHistoryRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAutoScalingHistoryRequest.

        **参数解释**：  查询记录数。  **约束限制**：  不涉及。  **取值范围**：  1-100  **默认取值**：  10

        :param limit: The limit of this ListAutoScalingHistoryRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListAutoScalingHistoryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
