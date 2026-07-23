# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GenericLinkQueryDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'role': 'str',
        'object_id': 'str',
        'latest_only': 'bool',
        'is_need_total': 'bool'
    }

    attribute_map = {
        'role': 'role',
        'object_id': 'objectId',
        'latest_only': 'latestOnly',
        'is_need_total': 'isNeedTotal'
    }

    def __init__(self, role=None, object_id=None, latest_only=None, is_need_total=None):
        r"""GenericLinkQueryDTO

        The model defined in huaweicloud sdk

        :param role: **参数解释：**  查询角色，用于指定按哪种角色维度查询关系实例。  **约束限制：**  必须与objectId配合使用。  **取值范围：**  - TARGET：目标模型。 - SOURCE：源模型。 - TARGET_TYPE：目标模型对应的英文名称。 - SOURCE_TYPE：源模型对应的英文名称。  **默认取值：**  不涉及。
        :type role: str
        :param object_id: **参数解释：**  查询对象标识，与role参数配合使用。  **约束限制：**  - 当role为SOURCE或TARGET时，值为角色对应数据实例ID。 - 当role为SOURCE_TYPE或TARGET_TYPE时，值为角色对应的数据模型的英文名称。  **取值范围：**  - 当role为SOURCE或TARGET时，取值范围为：-9223372036854775808到9223372036854775807的整数。 - 当role为SOURCE_TYPE或TARGET_TYPE时，以大写字母开头，只能包含字母、数字、“_”，且长度为1-60个字符。  **默认取值：**  不涉及。
        :type object_id: str
        :param latest_only: **参数解释：**  是否仅返回关联的最新版本目标模型数据实例。此参数仅当源模型或目标模型为M-V模型实体时生效。  **约束限制：**  仅对M-V模型实体有效。  **取值范围：**  - true：仅返回关联的最新版本目标模型数据实例。 - false：返回关联的所有版本目标模型数据实例。  **默认取值：**  false。
        :type latest_only: bool
        :param is_need_total: **参数解释：**  是否需要查询总记录数。开启后响应中的pageInfo将包含准确的totalRows和totalPages，但可能影响查询性能。  **约束限制：**  不涉及。  **取值范围：**  - true：需要。 - false：不需要。  **默认取值：**  false。
        :type is_need_total: bool
        """
        
        

        self._role = None
        self._object_id = None
        self._latest_only = None
        self._is_need_total = None
        self.discriminator = None

        if role is not None:
            self.role = role
        if object_id is not None:
            self.object_id = object_id
        if latest_only is not None:
            self.latest_only = latest_only
        if is_need_total is not None:
            self.is_need_total = is_need_total

    @property
    def role(self):
        r"""Gets the role of this GenericLinkQueryDTO.

        **参数解释：**  查询角色，用于指定按哪种角色维度查询关系实例。  **约束限制：**  必须与objectId配合使用。  **取值范围：**  - TARGET：目标模型。 - SOURCE：源模型。 - TARGET_TYPE：目标模型对应的英文名称。 - SOURCE_TYPE：源模型对应的英文名称。  **默认取值：**  不涉及。

        :return: The role of this GenericLinkQueryDTO.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        r"""Sets the role of this GenericLinkQueryDTO.

        **参数解释：**  查询角色，用于指定按哪种角色维度查询关系实例。  **约束限制：**  必须与objectId配合使用。  **取值范围：**  - TARGET：目标模型。 - SOURCE：源模型。 - TARGET_TYPE：目标模型对应的英文名称。 - SOURCE_TYPE：源模型对应的英文名称。  **默认取值：**  不涉及。

        :param role: The role of this GenericLinkQueryDTO.
        :type role: str
        """
        self._role = role

    @property
    def object_id(self):
        r"""Gets the object_id of this GenericLinkQueryDTO.

        **参数解释：**  查询对象标识，与role参数配合使用。  **约束限制：**  - 当role为SOURCE或TARGET时，值为角色对应数据实例ID。 - 当role为SOURCE_TYPE或TARGET_TYPE时，值为角色对应的数据模型的英文名称。  **取值范围：**  - 当role为SOURCE或TARGET时，取值范围为：-9223372036854775808到9223372036854775807的整数。 - 当role为SOURCE_TYPE或TARGET_TYPE时，以大写字母开头，只能包含字母、数字、“_”，且长度为1-60个字符。  **默认取值：**  不涉及。

        :return: The object_id of this GenericLinkQueryDTO.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        r"""Sets the object_id of this GenericLinkQueryDTO.

        **参数解释：**  查询对象标识，与role参数配合使用。  **约束限制：**  - 当role为SOURCE或TARGET时，值为角色对应数据实例ID。 - 当role为SOURCE_TYPE或TARGET_TYPE时，值为角色对应的数据模型的英文名称。  **取值范围：**  - 当role为SOURCE或TARGET时，取值范围为：-9223372036854775808到9223372036854775807的整数。 - 当role为SOURCE_TYPE或TARGET_TYPE时，以大写字母开头，只能包含字母、数字、“_”，且长度为1-60个字符。  **默认取值：**  不涉及。

        :param object_id: The object_id of this GenericLinkQueryDTO.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def latest_only(self):
        r"""Gets the latest_only of this GenericLinkQueryDTO.

        **参数解释：**  是否仅返回关联的最新版本目标模型数据实例。此参数仅当源模型或目标模型为M-V模型实体时生效。  **约束限制：**  仅对M-V模型实体有效。  **取值范围：**  - true：仅返回关联的最新版本目标模型数据实例。 - false：返回关联的所有版本目标模型数据实例。  **默认取值：**  false。

        :return: The latest_only of this GenericLinkQueryDTO.
        :rtype: bool
        """
        return self._latest_only

    @latest_only.setter
    def latest_only(self, latest_only):
        r"""Sets the latest_only of this GenericLinkQueryDTO.

        **参数解释：**  是否仅返回关联的最新版本目标模型数据实例。此参数仅当源模型或目标模型为M-V模型实体时生效。  **约束限制：**  仅对M-V模型实体有效。  **取值范围：**  - true：仅返回关联的最新版本目标模型数据实例。 - false：返回关联的所有版本目标模型数据实例。  **默认取值：**  false。

        :param latest_only: The latest_only of this GenericLinkQueryDTO.
        :type latest_only: bool
        """
        self._latest_only = latest_only

    @property
    def is_need_total(self):
        r"""Gets the is_need_total of this GenericLinkQueryDTO.

        **参数解释：**  是否需要查询总记录数。开启后响应中的pageInfo将包含准确的totalRows和totalPages，但可能影响查询性能。  **约束限制：**  不涉及。  **取值范围：**  - true：需要。 - false：不需要。  **默认取值：**  false。

        :return: The is_need_total of this GenericLinkQueryDTO.
        :rtype: bool
        """
        return self._is_need_total

    @is_need_total.setter
    def is_need_total(self, is_need_total):
        r"""Sets the is_need_total of this GenericLinkQueryDTO.

        **参数解释：**  是否需要查询总记录数。开启后响应中的pageInfo将包含准确的totalRows和totalPages，但可能影响查询性能。  **约束限制：**  不涉及。  **取值范围：**  - true：需要。 - false：不需要。  **默认取值：**  false。

        :param is_need_total: The is_need_total of this GenericLinkQueryDTO.
        :type is_need_total: bool
        """
        self._is_need_total = is_need_total

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
        if not isinstance(other, GenericLinkQueryDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
