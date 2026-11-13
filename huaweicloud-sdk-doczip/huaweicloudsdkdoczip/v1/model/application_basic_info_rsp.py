# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApplicationBasicInfoRsp:

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
        'icon': 'str',
        'description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'icon': 'icon',
        'description': 'description'
    }

    def __init__(self, name=None, icon=None, description=None):
        r"""ApplicationBasicInfoRsp

        The model defined in huaweicloud sdk

        :param name: **参数解释**： 应用名称。 **约束限制**： 不涉及。 **取值范围**： [1-200]个字符。 **默认取值**： 不涉及。
        :type name: str
        :param icon: **参数解释**： 应用图标URL，当前仅支持预置应用图标，取值为0~9的数字，分别标识第1到第10张预置图标。 **约束限制**： 0~9的数字。 **取值范围**： [1-200]个字符。 **默认取值**： 不涉及。
        :type icon: str
        :param description: **参数解释**： 应用描述。 **约束限制**： 不涉及。 **取值范围**： [1-200]个字符。 **默认取值**： 不涉及。
        :type description: str
        """
        
        

        self._name = None
        self._icon = None
        self._description = None
        self.discriminator = None

        self.name = name
        if icon is not None:
            self.icon = icon
        if description is not None:
            self.description = description

    @property
    def name(self):
        r"""Gets the name of this ApplicationBasicInfoRsp.

        **参数解释**： 应用名称。 **约束限制**： 不涉及。 **取值范围**： [1-200]个字符。 **默认取值**： 不涉及。

        :return: The name of this ApplicationBasicInfoRsp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ApplicationBasicInfoRsp.

        **参数解释**： 应用名称。 **约束限制**： 不涉及。 **取值范围**： [1-200]个字符。 **默认取值**： 不涉及。

        :param name: The name of this ApplicationBasicInfoRsp.
        :type name: str
        """
        self._name = name

    @property
    def icon(self):
        r"""Gets the icon of this ApplicationBasicInfoRsp.

        **参数解释**： 应用图标URL，当前仅支持预置应用图标，取值为0~9的数字，分别标识第1到第10张预置图标。 **约束限制**： 0~9的数字。 **取值范围**： [1-200]个字符。 **默认取值**： 不涉及。

        :return: The icon of this ApplicationBasicInfoRsp.
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        r"""Sets the icon of this ApplicationBasicInfoRsp.

        **参数解释**： 应用图标URL，当前仅支持预置应用图标，取值为0~9的数字，分别标识第1到第10张预置图标。 **约束限制**： 0~9的数字。 **取值范围**： [1-200]个字符。 **默认取值**： 不涉及。

        :param icon: The icon of this ApplicationBasicInfoRsp.
        :type icon: str
        """
        self._icon = icon

    @property
    def description(self):
        r"""Gets the description of this ApplicationBasicInfoRsp.

        **参数解释**： 应用描述。 **约束限制**： 不涉及。 **取值范围**： [1-200]个字符。 **默认取值**： 不涉及。

        :return: The description of this ApplicationBasicInfoRsp.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ApplicationBasicInfoRsp.

        **参数解释**： 应用描述。 **约束限制**： 不涉及。 **取值范围**： [1-200]个字符。 **默认取值**： 不涉及。

        :param description: The description of this ApplicationBasicInfoRsp.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, ApplicationBasicInfoRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
