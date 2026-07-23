# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VersionModelVersionCheckOutDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'master_id': 'str',
        'work_copy_type': 'str',
        'custom_link_set': 'list[str]',
        'creator': 'str',
        'modifier': 'str'
    }

    attribute_map = {
        'master_id': 'masterId',
        'work_copy_type': 'workCopyType',
        'custom_link_set': 'customLinkSet',
        'creator': 'creator',
        'modifier': 'modifier'
    }

    def __init__(self, master_id=None, work_copy_type=None, custom_link_set=None, creator=None, modifier=None):
        r"""VersionModelVersionCheckOutDTO

        The model defined in huaweicloud sdk

        :param master_id: **参数解释：**  主对象ID，用于定位需要检出的M-V模型实例所属的主对象。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。
        :type master_id: str
        :param work_copy_type: **参数解释：**  关系的复制类型，控制检出后的工作副本是否继承原实例的关系实例。不同取值对应不同的关系继承策略，适用于不同的业务场景。  **约束限制：**  不涉及。  **取值范围：**  - BOTH：若存在关系实例引用此数据实例作为源端实例或目标端实例，检出后的数据实例将继承这些关系实例。 - SOURCE：若存在关系实例引用此数据实例作为源端实例，检出后的数据实例将继承这些关系实例。 - TARGET：若存在关系实例引用此数据实例作为目标端实例，检出后的数据实例将继承这些关系实例。 - NONE：检出后的数据实例将不继承任何关系实例。 - CUSTOM：若指定的关系实体集合对应的关系实例引用此数据实例作为源端实例或目标端实例，检出后的数据实例将继承这些关系实例。  **默认取值：**  不涉及。
        :type work_copy_type: str
        :param custom_link_set: **参数解释：**  关系实体名称集合，与workCopyType的值CUSTOM配合使用。 当需要仅继承部分特定关系实例时，在此指定关系实体的英文名称列表。  **约束限制：**  仅在workCopyType为CUSTOM时生效。  **取值范围：**  不涉及。  **默认取值：**  不涉及。
        :type custom_link_set: list[str]
        :param creator: **参数解释：**  创建者账号，记录本次生成的工作副本的创建者信息。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。
        :type creator: str
        :param modifier: **参数解释：**  更新者账号，记录本次检出操作的操作人信息。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。
        :type modifier: str
        """
        
        

        self._master_id = None
        self._work_copy_type = None
        self._custom_link_set = None
        self._creator = None
        self._modifier = None
        self.discriminator = None

        self.master_id = master_id
        if work_copy_type is not None:
            self.work_copy_type = work_copy_type
        if custom_link_set is not None:
            self.custom_link_set = custom_link_set
        if creator is not None:
            self.creator = creator
        if modifier is not None:
            self.modifier = modifier

    @property
    def master_id(self):
        r"""Gets the master_id of this VersionModelVersionCheckOutDTO.

        **参数解释：**  主对象ID，用于定位需要检出的M-V模型实例所属的主对象。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :return: The master_id of this VersionModelVersionCheckOutDTO.
        :rtype: str
        """
        return self._master_id

    @master_id.setter
    def master_id(self, master_id):
        r"""Sets the master_id of this VersionModelVersionCheckOutDTO.

        **参数解释：**  主对象ID，用于定位需要检出的M-V模型实例所属的主对象。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :param master_id: The master_id of this VersionModelVersionCheckOutDTO.
        :type master_id: str
        """
        self._master_id = master_id

    @property
    def work_copy_type(self):
        r"""Gets the work_copy_type of this VersionModelVersionCheckOutDTO.

        **参数解释：**  关系的复制类型，控制检出后的工作副本是否继承原实例的关系实例。不同取值对应不同的关系继承策略，适用于不同的业务场景。  **约束限制：**  不涉及。  **取值范围：**  - BOTH：若存在关系实例引用此数据实例作为源端实例或目标端实例，检出后的数据实例将继承这些关系实例。 - SOURCE：若存在关系实例引用此数据实例作为源端实例，检出后的数据实例将继承这些关系实例。 - TARGET：若存在关系实例引用此数据实例作为目标端实例，检出后的数据实例将继承这些关系实例。 - NONE：检出后的数据实例将不继承任何关系实例。 - CUSTOM：若指定的关系实体集合对应的关系实例引用此数据实例作为源端实例或目标端实例，检出后的数据实例将继承这些关系实例。  **默认取值：**  不涉及。

        :return: The work_copy_type of this VersionModelVersionCheckOutDTO.
        :rtype: str
        """
        return self._work_copy_type

    @work_copy_type.setter
    def work_copy_type(self, work_copy_type):
        r"""Sets the work_copy_type of this VersionModelVersionCheckOutDTO.

        **参数解释：**  关系的复制类型，控制检出后的工作副本是否继承原实例的关系实例。不同取值对应不同的关系继承策略，适用于不同的业务场景。  **约束限制：**  不涉及。  **取值范围：**  - BOTH：若存在关系实例引用此数据实例作为源端实例或目标端实例，检出后的数据实例将继承这些关系实例。 - SOURCE：若存在关系实例引用此数据实例作为源端实例，检出后的数据实例将继承这些关系实例。 - TARGET：若存在关系实例引用此数据实例作为目标端实例，检出后的数据实例将继承这些关系实例。 - NONE：检出后的数据实例将不继承任何关系实例。 - CUSTOM：若指定的关系实体集合对应的关系实例引用此数据实例作为源端实例或目标端实例，检出后的数据实例将继承这些关系实例。  **默认取值：**  不涉及。

        :param work_copy_type: The work_copy_type of this VersionModelVersionCheckOutDTO.
        :type work_copy_type: str
        """
        self._work_copy_type = work_copy_type

    @property
    def custom_link_set(self):
        r"""Gets the custom_link_set of this VersionModelVersionCheckOutDTO.

        **参数解释：**  关系实体名称集合，与workCopyType的值CUSTOM配合使用。 当需要仅继承部分特定关系实例时，在此指定关系实体的英文名称列表。  **约束限制：**  仅在workCopyType为CUSTOM时生效。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :return: The custom_link_set of this VersionModelVersionCheckOutDTO.
        :rtype: list[str]
        """
        return self._custom_link_set

    @custom_link_set.setter
    def custom_link_set(self, custom_link_set):
        r"""Sets the custom_link_set of this VersionModelVersionCheckOutDTO.

        **参数解释：**  关系实体名称集合，与workCopyType的值CUSTOM配合使用。 当需要仅继承部分特定关系实例时，在此指定关系实体的英文名称列表。  **约束限制：**  仅在workCopyType为CUSTOM时生效。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :param custom_link_set: The custom_link_set of this VersionModelVersionCheckOutDTO.
        :type custom_link_set: list[str]
        """
        self._custom_link_set = custom_link_set

    @property
    def creator(self):
        r"""Gets the creator of this VersionModelVersionCheckOutDTO.

        **参数解释：**  创建者账号，记录本次生成的工作副本的创建者信息。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :return: The creator of this VersionModelVersionCheckOutDTO.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this VersionModelVersionCheckOutDTO.

        **参数解释：**  创建者账号，记录本次生成的工作副本的创建者信息。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :param creator: The creator of this VersionModelVersionCheckOutDTO.
        :type creator: str
        """
        self._creator = creator

    @property
    def modifier(self):
        r"""Gets the modifier of this VersionModelVersionCheckOutDTO.

        **参数解释：**  更新者账号，记录本次检出操作的操作人信息。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :return: The modifier of this VersionModelVersionCheckOutDTO.
        :rtype: str
        """
        return self._modifier

    @modifier.setter
    def modifier(self, modifier):
        r"""Sets the modifier of this VersionModelVersionCheckOutDTO.

        **参数解释：**  更新者账号，记录本次检出操作的操作人信息。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :param modifier: The modifier of this VersionModelVersionCheckOutDTO.
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
        if not isinstance(other, VersionModelVersionCheckOutDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
