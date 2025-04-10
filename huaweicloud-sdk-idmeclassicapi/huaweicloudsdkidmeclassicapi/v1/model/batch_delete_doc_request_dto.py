# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteDocRequestDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ids': 'list[str]',
        'model_name': 'str',
        'is_check': 'bool'
    }

    attribute_map = {
        'ids': 'ids',
        'model_name': 'model_name',
        'is_check': 'is_check'
    }

    def __init__(self, ids=None, model_name=None, is_check=None):
        r"""BatchDeleteDocRequestDto

        The model defined in huaweicloud sdk

        :param ids: **参数解释**：  文档ID列表。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type ids: list[str]
        :param model_name: **参数解释**：  模型名称。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type model_name: str
        :param is_check: **参数解释**：  是否检查文档删除权限。  **约束限制**：  不涉及。  **取值范围**：  - true：检查。 - false：不检查。  **默认取值**：  true。
        :type is_check: bool
        """
        
        

        self._ids = None
        self._model_name = None
        self._is_check = None
        self.discriminator = None

        if ids is not None:
            self.ids = ids
        if model_name is not None:
            self.model_name = model_name
        if is_check is not None:
            self.is_check = is_check

    @property
    def ids(self):
        r"""Gets the ids of this BatchDeleteDocRequestDto.

        **参数解释**：  文档ID列表。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The ids of this BatchDeleteDocRequestDto.
        :rtype: list[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        r"""Sets the ids of this BatchDeleteDocRequestDto.

        **参数解释**：  文档ID列表。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param ids: The ids of this BatchDeleteDocRequestDto.
        :type ids: list[str]
        """
        self._ids = ids

    @property
    def model_name(self):
        r"""Gets the model_name of this BatchDeleteDocRequestDto.

        **参数解释**：  模型名称。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The model_name of this BatchDeleteDocRequestDto.
        :rtype: str
        """
        return self._model_name

    @model_name.setter
    def model_name(self, model_name):
        r"""Sets the model_name of this BatchDeleteDocRequestDto.

        **参数解释**：  模型名称。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param model_name: The model_name of this BatchDeleteDocRequestDto.
        :type model_name: str
        """
        self._model_name = model_name

    @property
    def is_check(self):
        r"""Gets the is_check of this BatchDeleteDocRequestDto.

        **参数解释**：  是否检查文档删除权限。  **约束限制**：  不涉及。  **取值范围**：  - true：检查。 - false：不检查。  **默认取值**：  true。

        :return: The is_check of this BatchDeleteDocRequestDto.
        :rtype: bool
        """
        return self._is_check

    @is_check.setter
    def is_check(self, is_check):
        r"""Sets the is_check of this BatchDeleteDocRequestDto.

        **参数解释**：  是否检查文档删除权限。  **约束限制**：  不涉及。  **取值范围**：  - true：检查。 - false：不检查。  **默认取值**：  true。

        :param is_check: The is_check of this BatchDeleteDocRequestDto.
        :type is_check: bool
        """
        self._is_check = is_check

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
        if not isinstance(other, BatchDeleteDocRequestDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
