# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GenericLinkTypeModifierDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_id': 'str',
        'target_type': 'str',
        'latest_only': 'bool',
        'modifier': 'str'
    }

    attribute_map = {
        'source_id': 'sourceId',
        'target_type': 'targetType',
        'latest_only': 'latestOnly',
        'modifier': 'modifier'
    }

    def __init__(self, source_id=None, target_type=None, latest_only=None, modifier=None):
        r"""GenericLinkTypeModifierDTO

        The model defined in huaweicloud sdk

        :param source_id: **参数解释：**  源模型数据实例的ID，用于指定删除哪个源实例与目标模型的关联关系。  **约束限制：**  如不传入，将删除该源模型下所有实例与目标模型的关联关系，请谨慎使用。  **取值范围：**  -9223372036854775808到9223372036854775807的整数。  **默认取值：**  不涉及。
        :type source_id: str
        :param target_type: **参数解释：**  目标模型的英文名称，用于指定删除源实例与哪个目标模型的关联关系。  **约束限制：**  如不传入，将删除源实例与所有目标模型的关联关系，请谨慎使用。  **取值范围：**  不涉及。  **默认取值：**  不涉及。
        :type target_type: str
        :param latest_only: **参数解释：**  是否仅删除源实例关联的最新版本目标模型数据实例的关系。此参数仅当源模型或目标模型为M-V（Master-View）模型实体时生效。  **约束限制：**  仅对M-V模型实体有效。  **取值范围：**  - true：仅删除源实例关联的最新版本目标模型数据实例的关系。 - false：删除源实例关联的所有版本目标模型数据实例的关系。  **默认取值：**  false。
        :type latest_only: bool
        :param modifier: **参数解释：**  更新者账号，用于记录删除操作执行者信息。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。
        :type modifier: str
        """
        
        

        self._source_id = None
        self._target_type = None
        self._latest_only = None
        self._modifier = None
        self.discriminator = None

        if source_id is not None:
            self.source_id = source_id
        if target_type is not None:
            self.target_type = target_type
        if latest_only is not None:
            self.latest_only = latest_only
        if modifier is not None:
            self.modifier = modifier

    @property
    def source_id(self):
        r"""Gets the source_id of this GenericLinkTypeModifierDTO.

        **参数解释：**  源模型数据实例的ID，用于指定删除哪个源实例与目标模型的关联关系。  **约束限制：**  如不传入，将删除该源模型下所有实例与目标模型的关联关系，请谨慎使用。  **取值范围：**  -9223372036854775808到9223372036854775807的整数。  **默认取值：**  不涉及。

        :return: The source_id of this GenericLinkTypeModifierDTO.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        r"""Sets the source_id of this GenericLinkTypeModifierDTO.

        **参数解释：**  源模型数据实例的ID，用于指定删除哪个源实例与目标模型的关联关系。  **约束限制：**  如不传入，将删除该源模型下所有实例与目标模型的关联关系，请谨慎使用。  **取值范围：**  -9223372036854775808到9223372036854775807的整数。  **默认取值：**  不涉及。

        :param source_id: The source_id of this GenericLinkTypeModifierDTO.
        :type source_id: str
        """
        self._source_id = source_id

    @property
    def target_type(self):
        r"""Gets the target_type of this GenericLinkTypeModifierDTO.

        **参数解释：**  目标模型的英文名称，用于指定删除源实例与哪个目标模型的关联关系。  **约束限制：**  如不传入，将删除源实例与所有目标模型的关联关系，请谨慎使用。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :return: The target_type of this GenericLinkTypeModifierDTO.
        :rtype: str
        """
        return self._target_type

    @target_type.setter
    def target_type(self, target_type):
        r"""Sets the target_type of this GenericLinkTypeModifierDTO.

        **参数解释：**  目标模型的英文名称，用于指定删除源实例与哪个目标模型的关联关系。  **约束限制：**  如不传入，将删除源实例与所有目标模型的关联关系，请谨慎使用。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :param target_type: The target_type of this GenericLinkTypeModifierDTO.
        :type target_type: str
        """
        self._target_type = target_type

    @property
    def latest_only(self):
        r"""Gets the latest_only of this GenericLinkTypeModifierDTO.

        **参数解释：**  是否仅删除源实例关联的最新版本目标模型数据实例的关系。此参数仅当源模型或目标模型为M-V（Master-View）模型实体时生效。  **约束限制：**  仅对M-V模型实体有效。  **取值范围：**  - true：仅删除源实例关联的最新版本目标模型数据实例的关系。 - false：删除源实例关联的所有版本目标模型数据实例的关系。  **默认取值：**  false。

        :return: The latest_only of this GenericLinkTypeModifierDTO.
        :rtype: bool
        """
        return self._latest_only

    @latest_only.setter
    def latest_only(self, latest_only):
        r"""Sets the latest_only of this GenericLinkTypeModifierDTO.

        **参数解释：**  是否仅删除源实例关联的最新版本目标模型数据实例的关系。此参数仅当源模型或目标模型为M-V（Master-View）模型实体时生效。  **约束限制：**  仅对M-V模型实体有效。  **取值范围：**  - true：仅删除源实例关联的最新版本目标模型数据实例的关系。 - false：删除源实例关联的所有版本目标模型数据实例的关系。  **默认取值：**  false。

        :param latest_only: The latest_only of this GenericLinkTypeModifierDTO.
        :type latest_only: bool
        """
        self._latest_only = latest_only

    @property
    def modifier(self):
        r"""Gets the modifier of this GenericLinkTypeModifierDTO.

        **参数解释：**  更新者账号，用于记录删除操作执行者信息。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :return: The modifier of this GenericLinkTypeModifierDTO.
        :rtype: str
        """
        return self._modifier

    @modifier.setter
    def modifier(self, modifier):
        r"""Sets the modifier of this GenericLinkTypeModifierDTO.

        **参数解释：**  更新者账号，用于记录删除操作执行者信息。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :param modifier: The modifier of this GenericLinkTypeModifierDTO.
        :type modifier: str
        """
        self._modifier = modifier

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
        if not isinstance(other, GenericLinkTypeModifierDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
