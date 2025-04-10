# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GenericLinkBatchQueryDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'latest_only': 'bool',
        'object_ids': 'list[str]',
        'role': 'str'
    }

    attribute_map = {
        'latest_only': 'latestOnly',
        'object_ids': 'objectIds',
        'role': 'role'
    }

    def __init__(self, latest_only=None, object_ids=None, role=None):
        r"""GenericLinkBatchQueryDTO

        The model defined in huaweicloud sdk

        :param latest_only: **参数解释：**  是否返回源模型数据实例关联的最新版本目标模型数据实例。此参数仅对源/目标模型为M-V模型实体有效。  **约束限制：**  不涉及。  **取值范围：**  - true：返回源模型数据实例关联的最新版本的目标模型数据实例。 - false：返回源模型数据实例关联的所有版本的目标模型数据实例。  **默认取值：**  false。 
        :type latest_only: bool
        :param object_ids: **参数解释：**  角色对应的数据实例ID列表。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type object_ids: list[str]
        :param role: **参数解释：**  角色。  **约束限制：**  不涉及。  **取值范围：**  - TARGET：目标模型。 - SOURCE：源模型。  **默认取值：**  不涉及。 
        :type role: str
        """
        
        

        self._latest_only = None
        self._object_ids = None
        self._role = None
        self.discriminator = None

        if latest_only is not None:
            self.latest_only = latest_only
        if object_ids is not None:
            self.object_ids = object_ids
        if role is not None:
            self.role = role

    @property
    def latest_only(self):
        r"""Gets the latest_only of this GenericLinkBatchQueryDTO.

        **参数解释：**  是否返回源模型数据实例关联的最新版本目标模型数据实例。此参数仅对源/目标模型为M-V模型实体有效。  **约束限制：**  不涉及。  **取值范围：**  - true：返回源模型数据实例关联的最新版本的目标模型数据实例。 - false：返回源模型数据实例关联的所有版本的目标模型数据实例。  **默认取值：**  false。 

        :return: The latest_only of this GenericLinkBatchQueryDTO.
        :rtype: bool
        """
        return self._latest_only

    @latest_only.setter
    def latest_only(self, latest_only):
        r"""Sets the latest_only of this GenericLinkBatchQueryDTO.

        **参数解释：**  是否返回源模型数据实例关联的最新版本目标模型数据实例。此参数仅对源/目标模型为M-V模型实体有效。  **约束限制：**  不涉及。  **取值范围：**  - true：返回源模型数据实例关联的最新版本的目标模型数据实例。 - false：返回源模型数据实例关联的所有版本的目标模型数据实例。  **默认取值：**  false。 

        :param latest_only: The latest_only of this GenericLinkBatchQueryDTO.
        :type latest_only: bool
        """
        self._latest_only = latest_only

    @property
    def object_ids(self):
        r"""Gets the object_ids of this GenericLinkBatchQueryDTO.

        **参数解释：**  角色对应的数据实例ID列表。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The object_ids of this GenericLinkBatchQueryDTO.
        :rtype: list[str]
        """
        return self._object_ids

    @object_ids.setter
    def object_ids(self, object_ids):
        r"""Sets the object_ids of this GenericLinkBatchQueryDTO.

        **参数解释：**  角色对应的数据实例ID列表。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param object_ids: The object_ids of this GenericLinkBatchQueryDTO.
        :type object_ids: list[str]
        """
        self._object_ids = object_ids

    @property
    def role(self):
        r"""Gets the role of this GenericLinkBatchQueryDTO.

        **参数解释：**  角色。  **约束限制：**  不涉及。  **取值范围：**  - TARGET：目标模型。 - SOURCE：源模型。  **默认取值：**  不涉及。 

        :return: The role of this GenericLinkBatchQueryDTO.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        r"""Sets the role of this GenericLinkBatchQueryDTO.

        **参数解释：**  角色。  **约束限制：**  不涉及。  **取值范围：**  - TARGET：目标模型。 - SOURCE：源模型。  **默认取值：**  不涉及。 

        :param role: The role of this GenericLinkBatchQueryDTO.
        :type role: str
        """
        self._role = role

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
        if not isinstance(other, GenericLinkBatchQueryDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
