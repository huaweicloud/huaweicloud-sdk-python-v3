# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GenericLinkTypeDTO:

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
        'source_id': 'str',
        'target_type': 'str'
    }

    attribute_map = {
        'latest_only': 'latestOnly',
        'source_id': 'sourceId',
        'target_type': 'targetType'
    }

    def __init__(self, latest_only=None, source_id=None, target_type=None):
        r"""GenericLinkTypeDTO

        The model defined in huaweicloud sdk

        :param latest_only: **参数解释：**  是否返回源模型数据实例关联的最新版本目标模型数据实例。此参数仅对源/目标模型为M-V模型实体有效。  **约束限制：**  不涉及。  **取值范围：**  - true：返回源模型数据实例关联的最新版本的目标模型数据实例。 - false：返回源模型数据实例关联的所有版本的目标模型数据实例。默认为false。  **默认取值：**  false。 
        :type latest_only: bool
        :param source_id: **参数解释：**  源模型数据实例的ID。  **约束限制：**  不涉及。  **取值范围：**  -9223372036854775808到9223372036854775807的整数。  **默认取值：**  不涉及。 
        :type source_id: str
        :param target_type: **参数解释：**  目标模型的英文名称。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type target_type: str
        """
        
        

        self._latest_only = None
        self._source_id = None
        self._target_type = None
        self.discriminator = None

        if latest_only is not None:
            self.latest_only = latest_only
        if source_id is not None:
            self.source_id = source_id
        if target_type is not None:
            self.target_type = target_type

    @property
    def latest_only(self):
        r"""Gets the latest_only of this GenericLinkTypeDTO.

        **参数解释：**  是否返回源模型数据实例关联的最新版本目标模型数据实例。此参数仅对源/目标模型为M-V模型实体有效。  **约束限制：**  不涉及。  **取值范围：**  - true：返回源模型数据实例关联的最新版本的目标模型数据实例。 - false：返回源模型数据实例关联的所有版本的目标模型数据实例。默认为false。  **默认取值：**  false。 

        :return: The latest_only of this GenericLinkTypeDTO.
        :rtype: bool
        """
        return self._latest_only

    @latest_only.setter
    def latest_only(self, latest_only):
        r"""Sets the latest_only of this GenericLinkTypeDTO.

        **参数解释：**  是否返回源模型数据实例关联的最新版本目标模型数据实例。此参数仅对源/目标模型为M-V模型实体有效。  **约束限制：**  不涉及。  **取值范围：**  - true：返回源模型数据实例关联的最新版本的目标模型数据实例。 - false：返回源模型数据实例关联的所有版本的目标模型数据实例。默认为false。  **默认取值：**  false。 

        :param latest_only: The latest_only of this GenericLinkTypeDTO.
        :type latest_only: bool
        """
        self._latest_only = latest_only

    @property
    def source_id(self):
        r"""Gets the source_id of this GenericLinkTypeDTO.

        **参数解释：**  源模型数据实例的ID。  **约束限制：**  不涉及。  **取值范围：**  -9223372036854775808到9223372036854775807的整数。  **默认取值：**  不涉及。 

        :return: The source_id of this GenericLinkTypeDTO.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        r"""Sets the source_id of this GenericLinkTypeDTO.

        **参数解释：**  源模型数据实例的ID。  **约束限制：**  不涉及。  **取值范围：**  -9223372036854775808到9223372036854775807的整数。  **默认取值：**  不涉及。 

        :param source_id: The source_id of this GenericLinkTypeDTO.
        :type source_id: str
        """
        self._source_id = source_id

    @property
    def target_type(self):
        r"""Gets the target_type of this GenericLinkTypeDTO.

        **参数解释：**  目标模型的英文名称。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The target_type of this GenericLinkTypeDTO.
        :rtype: str
        """
        return self._target_type

    @target_type.setter
    def target_type(self, target_type):
        r"""Sets the target_type of this GenericLinkTypeDTO.

        **参数解释：**  目标模型的英文名称。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param target_type: The target_type of this GenericLinkTypeDTO.
        :type target_type: str
        """
        self._target_type = target_type

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
        if not isinstance(other, GenericLinkTypeDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
