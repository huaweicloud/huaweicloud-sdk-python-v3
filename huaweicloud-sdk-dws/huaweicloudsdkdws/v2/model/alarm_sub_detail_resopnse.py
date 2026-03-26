# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlarmSubDetailResopnse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'alarm_id': 'str',
        'alarm_name': 'str',
        'name_space': 'str',
        'alarm_level': 'str'
    }

    attribute_map = {
        'id': 'id',
        'alarm_id': 'alarm_id',
        'alarm_name': 'alarm_name',
        'name_space': 'name_space',
        'alarm_level': 'alarm_level'
    }

    def __init__(self, id=None, alarm_id=None, alarm_name=None, name_space=None, alarm_level=None):
        r"""AlarmSubDetailResopnse

        The model defined in huaweicloud sdk

        :param id: **参数解释**：  告警配置ID。  **取值范围**： 不涉及。
        :type id: str
        :param alarm_id: **参数解释**：  告警定义ID。  **取值范围**： 不涉及。
        :type alarm_id: str
        :param alarm_name: **参数解释**：  告警名称。  **取值范围**： 不涉及。
        :type alarm_name: str
        :param name_space: **参数解释**：  所属服务。  **取值范围**： 不涉及。
        :type name_space: str
        :param alarm_level: **参数解释**：  告警级别。  **取值范围**：  不涉及。
        :type alarm_level: str
        """
        
        

        self._id = None
        self._alarm_id = None
        self._alarm_name = None
        self._name_space = None
        self._alarm_level = None
        self.discriminator = None

        self.id = id
        self.alarm_id = alarm_id
        self.alarm_name = alarm_name
        self.name_space = name_space
        self.alarm_level = alarm_level

    @property
    def id(self):
        r"""Gets the id of this AlarmSubDetailResopnse.

        **参数解释**：  告警配置ID。  **取值范围**： 不涉及。

        :return: The id of this AlarmSubDetailResopnse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AlarmSubDetailResopnse.

        **参数解释**：  告警配置ID。  **取值范围**： 不涉及。

        :param id: The id of this AlarmSubDetailResopnse.
        :type id: str
        """
        self._id = id

    @property
    def alarm_id(self):
        r"""Gets the alarm_id of this AlarmSubDetailResopnse.

        **参数解释**：  告警定义ID。  **取值范围**： 不涉及。

        :return: The alarm_id of this AlarmSubDetailResopnse.
        :rtype: str
        """
        return self._alarm_id

    @alarm_id.setter
    def alarm_id(self, alarm_id):
        r"""Sets the alarm_id of this AlarmSubDetailResopnse.

        **参数解释**：  告警定义ID。  **取值范围**： 不涉及。

        :param alarm_id: The alarm_id of this AlarmSubDetailResopnse.
        :type alarm_id: str
        """
        self._alarm_id = alarm_id

    @property
    def alarm_name(self):
        r"""Gets the alarm_name of this AlarmSubDetailResopnse.

        **参数解释**：  告警名称。  **取值范围**： 不涉及。

        :return: The alarm_name of this AlarmSubDetailResopnse.
        :rtype: str
        """
        return self._alarm_name

    @alarm_name.setter
    def alarm_name(self, alarm_name):
        r"""Sets the alarm_name of this AlarmSubDetailResopnse.

        **参数解释**：  告警名称。  **取值范围**： 不涉及。

        :param alarm_name: The alarm_name of this AlarmSubDetailResopnse.
        :type alarm_name: str
        """
        self._alarm_name = alarm_name

    @property
    def name_space(self):
        r"""Gets the name_space of this AlarmSubDetailResopnse.

        **参数解释**：  所属服务。  **取值范围**： 不涉及。

        :return: The name_space of this AlarmSubDetailResopnse.
        :rtype: str
        """
        return self._name_space

    @name_space.setter
    def name_space(self, name_space):
        r"""Sets the name_space of this AlarmSubDetailResopnse.

        **参数解释**：  所属服务。  **取值范围**： 不涉及。

        :param name_space: The name_space of this AlarmSubDetailResopnse.
        :type name_space: str
        """
        self._name_space = name_space

    @property
    def alarm_level(self):
        r"""Gets the alarm_level of this AlarmSubDetailResopnse.

        **参数解释**：  告警级别。  **取值范围**：  不涉及。

        :return: The alarm_level of this AlarmSubDetailResopnse.
        :rtype: str
        """
        return self._alarm_level

    @alarm_level.setter
    def alarm_level(self, alarm_level):
        r"""Sets the alarm_level of this AlarmSubDetailResopnse.

        **参数解释**：  告警级别。  **取值范围**：  不涉及。

        :param alarm_level: The alarm_level of this AlarmSubDetailResopnse.
        :type alarm_level: str
        """
        self._alarm_level = alarm_level

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
        if not isinstance(other, AlarmSubDetailResopnse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
