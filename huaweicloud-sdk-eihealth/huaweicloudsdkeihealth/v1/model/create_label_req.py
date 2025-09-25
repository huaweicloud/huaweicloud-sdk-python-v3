# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateLabelReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'level': 'int'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'level': 'level'
    }

    def __init__(self, name=None, description=None, level=None):
        r"""CreateLabelReq

        The model defined in huaweicloud sdk

        :param name: 标签名称
        :type name: str
        :param description: 标签描述
        :type description: str
        :param level: **参数解释**:  标签级别，用于前端颜色展示。   **约束限制**:  不涉及   **取值范围**:  整数，取值范围[1-6]   **默认取值**:  1 
        :type level: int
        """
        
        

        self._name = None
        self._description = None
        self._level = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if level is not None:
            self.level = level

    @property
    def name(self):
        r"""Gets the name of this CreateLabelReq.

        标签名称

        :return: The name of this CreateLabelReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateLabelReq.

        标签名称

        :param name: The name of this CreateLabelReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateLabelReq.

        标签描述

        :return: The description of this CreateLabelReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateLabelReq.

        标签描述

        :param description: The description of this CreateLabelReq.
        :type description: str
        """
        self._description = description

    @property
    def level(self):
        r"""Gets the level of this CreateLabelReq.

        **参数解释**:  标签级别，用于前端颜色展示。   **约束限制**:  不涉及   **取值范围**:  整数，取值范围[1-6]   **默认取值**:  1 

        :return: The level of this CreateLabelReq.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this CreateLabelReq.

        **参数解释**:  标签级别，用于前端颜色展示。   **约束限制**:  不涉及   **取值范围**:  整数，取值范围[1-6]   **默认取值**:  1 

        :param level: The level of this CreateLabelReq.
        :type level: int
        """
        self._level = level

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
        if not isinstance(other, CreateLabelReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
