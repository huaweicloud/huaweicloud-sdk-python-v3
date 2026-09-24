# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MysqlAutoScalingRecord:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'instance_id': 'str',
        'scaling_type': 'str',
        'original_value': 'str',
        'target_value': 'str',
        'result': 'str',
        'created_at': 'int'
    }

    attribute_map = {
        'id': 'id',
        'instance_id': 'instance_id',
        'scaling_type': 'scaling_type',
        'original_value': 'original_value',
        'target_value': 'target_value',
        'result': 'result',
        'created_at': 'created_at'
    }

    def __init__(self, id=None, instance_id=None, scaling_type=None, original_value=None, target_value=None, result=None, created_at=None):
        r"""MysqlAutoScalingRecord

        The model defined in huaweicloud sdk

        :param id: **参数解释**：  记录ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type id: str
        :param instance_id: **参数解释**：  实例ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type instance_id: str
        :param scaling_type: **参数解释**：  变配类型。  **约束限制**：  不涉及。  **取值范围**：  - ENLARGE_FLAVOR：升配 - REDUCE_FLAVOR：降配 - COUNT_UP：只读升配 - COUNT_DOWN：只读降配  **默认取值**：  不涉及。
        :type scaling_type: str
        :param original_value: **参数解释**：  原规格。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type original_value: str
        :param target_value: **参数解释**：  目标规格。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type target_value: str
        :param result: **参数解释**：  变更结果。  **约束限制**：  不涉及。  **取值范围**：  - SUCCESSFUL：成功 - FAILED：失败  **默认取值**：  不涉及。
        :type result: str
        :param created_at: **参数解释**：  开始时间。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type created_at: int
        """
        
        

        self._id = None
        self._instance_id = None
        self._scaling_type = None
        self._original_value = None
        self._target_value = None
        self._result = None
        self._created_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if instance_id is not None:
            self.instance_id = instance_id
        if scaling_type is not None:
            self.scaling_type = scaling_type
        if original_value is not None:
            self.original_value = original_value
        if target_value is not None:
            self.target_value = target_value
        if result is not None:
            self.result = result
        if created_at is not None:
            self.created_at = created_at

    @property
    def id(self):
        r"""Gets the id of this MysqlAutoScalingRecord.

        **参数解释**：  记录ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The id of this MysqlAutoScalingRecord.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this MysqlAutoScalingRecord.

        **参数解释**：  记录ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param id: The id of this MysqlAutoScalingRecord.
        :type id: str
        """
        self._id = id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this MysqlAutoScalingRecord.

        **参数解释**：  实例ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The instance_id of this MysqlAutoScalingRecord.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this MysqlAutoScalingRecord.

        **参数解释**：  实例ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param instance_id: The instance_id of this MysqlAutoScalingRecord.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def scaling_type(self):
        r"""Gets the scaling_type of this MysqlAutoScalingRecord.

        **参数解释**：  变配类型。  **约束限制**：  不涉及。  **取值范围**：  - ENLARGE_FLAVOR：升配 - REDUCE_FLAVOR：降配 - COUNT_UP：只读升配 - COUNT_DOWN：只读降配  **默认取值**：  不涉及。

        :return: The scaling_type of this MysqlAutoScalingRecord.
        :rtype: str
        """
        return self._scaling_type

    @scaling_type.setter
    def scaling_type(self, scaling_type):
        r"""Sets the scaling_type of this MysqlAutoScalingRecord.

        **参数解释**：  变配类型。  **约束限制**：  不涉及。  **取值范围**：  - ENLARGE_FLAVOR：升配 - REDUCE_FLAVOR：降配 - COUNT_UP：只读升配 - COUNT_DOWN：只读降配  **默认取值**：  不涉及。

        :param scaling_type: The scaling_type of this MysqlAutoScalingRecord.
        :type scaling_type: str
        """
        self._scaling_type = scaling_type

    @property
    def original_value(self):
        r"""Gets the original_value of this MysqlAutoScalingRecord.

        **参数解释**：  原规格。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The original_value of this MysqlAutoScalingRecord.
        :rtype: str
        """
        return self._original_value

    @original_value.setter
    def original_value(self, original_value):
        r"""Sets the original_value of this MysqlAutoScalingRecord.

        **参数解释**：  原规格。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param original_value: The original_value of this MysqlAutoScalingRecord.
        :type original_value: str
        """
        self._original_value = original_value

    @property
    def target_value(self):
        r"""Gets the target_value of this MysqlAutoScalingRecord.

        **参数解释**：  目标规格。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The target_value of this MysqlAutoScalingRecord.
        :rtype: str
        """
        return self._target_value

    @target_value.setter
    def target_value(self, target_value):
        r"""Sets the target_value of this MysqlAutoScalingRecord.

        **参数解释**：  目标规格。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param target_value: The target_value of this MysqlAutoScalingRecord.
        :type target_value: str
        """
        self._target_value = target_value

    @property
    def result(self):
        r"""Gets the result of this MysqlAutoScalingRecord.

        **参数解释**：  变更结果。  **约束限制**：  不涉及。  **取值范围**：  - SUCCESSFUL：成功 - FAILED：失败  **默认取值**：  不涉及。

        :return: The result of this MysqlAutoScalingRecord.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this MysqlAutoScalingRecord.

        **参数解释**：  变更结果。  **约束限制**：  不涉及。  **取值范围**：  - SUCCESSFUL：成功 - FAILED：失败  **默认取值**：  不涉及。

        :param result: The result of this MysqlAutoScalingRecord.
        :type result: str
        """
        self._result = result

    @property
    def created_at(self):
        r"""Gets the created_at of this MysqlAutoScalingRecord.

        **参数解释**：  开始时间。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The created_at of this MysqlAutoScalingRecord.
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this MysqlAutoScalingRecord.

        **参数解释**：  开始时间。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param created_at: The created_at of this MysqlAutoScalingRecord.
        :type created_at: int
        """
        self._created_at = created_at

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
        if not isinstance(other, MysqlAutoScalingRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
