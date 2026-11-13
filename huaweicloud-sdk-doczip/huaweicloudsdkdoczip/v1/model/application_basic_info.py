# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApplicationBasicInfo:

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
        'icon_url': 'str',
        'description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'icon_url': 'icon_url',
        'description': 'description'
    }

    def __init__(self, name=None, icon_url=None, description=None):
        r"""ApplicationBasicInfo

        The model defined in huaweicloud sdk

        :param name: **参数解释**： 应用名称。 **约束限制**： 不涉及。 **取值范围**： [1-200]个字符。 **默认取值**： 不涉及。
        :type name: str
        :param icon_url: **参数解释**： 应用图标URL，当前仅支持预置应用图标，取值为0~9的数字，分别标识第1到第10张预置图标。 **约束限制**： 0~9的数字。 **取值范围**： [1-200]的字符串。 **默认取值**： 不涉及。
        :type icon_url: str
        :param description: **参数解释**： 应用描述。 **约束限制**： 不涉及。 **取值范围**： [1-200]个字符。 **默认取值**： 不涉及。
        :type description: str
        """
        
        

        self._name = None
        self._icon_url = None
        self._description = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if icon_url is not None:
            self.icon_url = icon_url
        if description is not None:
            self.description = description

    @property
    def name(self):
        r"""Gets the name of this ApplicationBasicInfo.

        **参数解释**： 应用名称。 **约束限制**： 不涉及。 **取值范围**： [1-200]个字符。 **默认取值**： 不涉及。

        :return: The name of this ApplicationBasicInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ApplicationBasicInfo.

        **参数解释**： 应用名称。 **约束限制**： 不涉及。 **取值范围**： [1-200]个字符。 **默认取值**： 不涉及。

        :param name: The name of this ApplicationBasicInfo.
        :type name: str
        """
        self._name = name

    @property
    def icon_url(self):
        r"""Gets the icon_url of this ApplicationBasicInfo.

        **参数解释**： 应用图标URL，当前仅支持预置应用图标，取值为0~9的数字，分别标识第1到第10张预置图标。 **约束限制**： 0~9的数字。 **取值范围**： [1-200]的字符串。 **默认取值**： 不涉及。

        :return: The icon_url of this ApplicationBasicInfo.
        :rtype: str
        """
        return self._icon_url

    @icon_url.setter
    def icon_url(self, icon_url):
        r"""Sets the icon_url of this ApplicationBasicInfo.

        **参数解释**： 应用图标URL，当前仅支持预置应用图标，取值为0~9的数字，分别标识第1到第10张预置图标。 **约束限制**： 0~9的数字。 **取值范围**： [1-200]的字符串。 **默认取值**： 不涉及。

        :param icon_url: The icon_url of this ApplicationBasicInfo.
        :type icon_url: str
        """
        self._icon_url = icon_url

    @property
    def description(self):
        r"""Gets the description of this ApplicationBasicInfo.

        **参数解释**： 应用描述。 **约束限制**： 不涉及。 **取值范围**： [1-200]个字符。 **默认取值**： 不涉及。

        :return: The description of this ApplicationBasicInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ApplicationBasicInfo.

        **参数解释**： 应用描述。 **约束限制**： 不涉及。 **取值范围**： [1-200]个字符。 **默认取值**： 不涉及。

        :param description: The description of this ApplicationBasicInfo.
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
        if not isinstance(other, ApplicationBasicInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
