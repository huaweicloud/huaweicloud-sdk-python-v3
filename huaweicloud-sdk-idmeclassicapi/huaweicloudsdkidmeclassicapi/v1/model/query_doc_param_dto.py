# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryDocParamDto:

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
        'type': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'type': 'type'
    }

    def __init__(self, instance_id=None, type=None):
        r"""QueryDocParamDto

        The model defined in huaweicloud sdk

        :param instance_id: **参数解释**：  实例ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type instance_id: str
        :param type: **参数解释**：  文档类型。  **约束限制**：  不涉及。  **取值范围**：  - directory：目录。 - pageDocument：Page文档。 - boardDocument：Board文档。 - mindDocument：Mind文档。 - drawDocument：Draw文档。  **默认取值**：  不涉及。
        :type type: str
        """
        
        

        self._instance_id = None
        self._type = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if type is not None:
            self.type = type

    @property
    def instance_id(self):
        r"""Gets the instance_id of this QueryDocParamDto.

        **参数解释**：  实例ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The instance_id of this QueryDocParamDto.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this QueryDocParamDto.

        **参数解释**：  实例ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param instance_id: The instance_id of this QueryDocParamDto.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def type(self):
        r"""Gets the type of this QueryDocParamDto.

        **参数解释**：  文档类型。  **约束限制**：  不涉及。  **取值范围**：  - directory：目录。 - pageDocument：Page文档。 - boardDocument：Board文档。 - mindDocument：Mind文档。 - drawDocument：Draw文档。  **默认取值**：  不涉及。

        :return: The type of this QueryDocParamDto.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this QueryDocParamDto.

        **参数解释**：  文档类型。  **约束限制**：  不涉及。  **取值范围**：  - directory：目录。 - pageDocument：Page文档。 - boardDocument：Board文档。 - mindDocument：Mind文档。 - drawDocument：Draw文档。  **默认取值**：  不涉及。

        :param type: The type of this QueryDocParamDto.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, QueryDocParamDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
