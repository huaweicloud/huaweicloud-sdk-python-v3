# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateRsuModel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'manufacturer_name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'manufacturer_name': 'manufacturer_name',
        'description': 'description'
    }

    def __init__(self, manufacturer_name=None, description=None):
        """UpdateRsuModel

        The model defined in huaweicloud sdk

        :param manufacturer_name: **参数说明**: RSU的厂商名称。  **取值范围**：长度不低于1不超过32，只允许中文、字母、数字、下划线（_）、问号（?）、反引号（&#39;）、井号（#）、左小括号（(）、右小括号（)）、点（.）、逗号（,）、与（&amp;）、百分号（%）、At（@）、感叹号（!）、连接符（-）的组合。
        :type manufacturer_name: str
        :param description: **参数说明**: RSU型号的描述信息。  **取值范围**：长度不低于1不超过128，只允许中文、字母、数字、下划线（_）、问号（?）、反引号（&#39;）、井号（#）、左小括号（(）、右小括号（)）、点（.）、逗号（,）、与（&amp;）、百分号（%）、At（@）、感叹号（!）、连接符（-）的组合。
        :type description: str
        """
        
        

        self._manufacturer_name = None
        self._description = None
        self.discriminator = None

        if manufacturer_name is not None:
            self.manufacturer_name = manufacturer_name
        if description is not None:
            self.description = description

    @property
    def manufacturer_name(self):
        """Gets the manufacturer_name of this UpdateRsuModel.

        **参数说明**: RSU的厂商名称。  **取值范围**：长度不低于1不超过32，只允许中文、字母、数字、下划线（_）、问号（?）、反引号（'）、井号（#）、左小括号（(）、右小括号（)）、点（.）、逗号（,）、与（&）、百分号（%）、At（@）、感叹号（!）、连接符（-）的组合。

        :return: The manufacturer_name of this UpdateRsuModel.
        :rtype: str
        """
        return self._manufacturer_name

    @manufacturer_name.setter
    def manufacturer_name(self, manufacturer_name):
        """Sets the manufacturer_name of this UpdateRsuModel.

        **参数说明**: RSU的厂商名称。  **取值范围**：长度不低于1不超过32，只允许中文、字母、数字、下划线（_）、问号（?）、反引号（'）、井号（#）、左小括号（(）、右小括号（)）、点（.）、逗号（,）、与（&）、百分号（%）、At（@）、感叹号（!）、连接符（-）的组合。

        :param manufacturer_name: The manufacturer_name of this UpdateRsuModel.
        :type manufacturer_name: str
        """
        self._manufacturer_name = manufacturer_name

    @property
    def description(self):
        """Gets the description of this UpdateRsuModel.

        **参数说明**: RSU型号的描述信息。  **取值范围**：长度不低于1不超过128，只允许中文、字母、数字、下划线（_）、问号（?）、反引号（'）、井号（#）、左小括号（(）、右小括号（)）、点（.）、逗号（,）、与（&）、百分号（%）、At（@）、感叹号（!）、连接符（-）的组合。

        :return: The description of this UpdateRsuModel.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateRsuModel.

        **参数说明**: RSU型号的描述信息。  **取值范围**：长度不低于1不超过128，只允许中文、字母、数字、下划线（_）、问号（?）、反引号（'）、井号（#）、左小括号（(）、右小括号（)）、点（.）、逗号（,）、与（&）、百分号（%）、At（@）、感叹号（!）、连接符（-）的组合。

        :param description: The description of this UpdateRsuModel.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, UpdateRsuModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
