# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubStage:

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
        'en_message': 'str',
        'zh_message': 'str',
        'create_time': 'str'
    }

    attribute_map = {
        'name': 'name',
        'en_message': 'en_message',
        'zh_message': 'zh_message',
        'create_time': 'create_time'
    }

    def __init__(self, name=None, en_message=None, zh_message=None, create_time=None):
        r"""SubStage

        The model defined in huaweicloud sdk

        :param name: **参数解释**：子阶段名称。  **取值范围**：不涉及。
        :type name: str
        :param en_message: **参数解释**：子阶段英文描述信息。  **取值范围**：不涉及。
        :type en_message: str
        :param zh_message: **参数解释**：子阶段中文描述信息。  **取值范围**：不涉及。
        :type zh_message: str
        :param create_time: **参数解释**：子阶段开始时间。  **取值范围**：不涉及。
        :type create_time: str
        """
        
        

        self._name = None
        self._en_message = None
        self._zh_message = None
        self._create_time = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if en_message is not None:
            self.en_message = en_message
        if zh_message is not None:
            self.zh_message = zh_message
        if create_time is not None:
            self.create_time = create_time

    @property
    def name(self):
        r"""Gets the name of this SubStage.

        **参数解释**：子阶段名称。  **取值范围**：不涉及。

        :return: The name of this SubStage.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this SubStage.

        **参数解释**：子阶段名称。  **取值范围**：不涉及。

        :param name: The name of this SubStage.
        :type name: str
        """
        self._name = name

    @property
    def en_message(self):
        r"""Gets the en_message of this SubStage.

        **参数解释**：子阶段英文描述信息。  **取值范围**：不涉及。

        :return: The en_message of this SubStage.
        :rtype: str
        """
        return self._en_message

    @en_message.setter
    def en_message(self, en_message):
        r"""Sets the en_message of this SubStage.

        **参数解释**：子阶段英文描述信息。  **取值范围**：不涉及。

        :param en_message: The en_message of this SubStage.
        :type en_message: str
        """
        self._en_message = en_message

    @property
    def zh_message(self):
        r"""Gets the zh_message of this SubStage.

        **参数解释**：子阶段中文描述信息。  **取值范围**：不涉及。

        :return: The zh_message of this SubStage.
        :rtype: str
        """
        return self._zh_message

    @zh_message.setter
    def zh_message(self, zh_message):
        r"""Sets the zh_message of this SubStage.

        **参数解释**：子阶段中文描述信息。  **取值范围**：不涉及。

        :param zh_message: The zh_message of this SubStage.
        :type zh_message: str
        """
        self._zh_message = zh_message

    @property
    def create_time(self):
        r"""Gets the create_time of this SubStage.

        **参数解释**：子阶段开始时间。  **取值范围**：不涉及。

        :return: The create_time of this SubStage.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this SubStage.

        **参数解释**：子阶段开始时间。  **取值范围**：不涉及。

        :param create_time: The create_time of this SubStage.
        :type create_time: str
        """
        self._create_time = create_time

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
        if not isinstance(other, SubStage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
