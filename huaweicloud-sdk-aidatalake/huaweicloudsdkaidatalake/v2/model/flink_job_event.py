# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlinkJobEvent:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'event_id': 'str',
        'create_time': 'int',
        'event_name': 'str',
        'event_message': 'str'
    }

    attribute_map = {
        'event_id': 'event_id',
        'create_time': 'create_time',
        'event_name': 'event_name',
        'event_message': 'event_message'
    }

    def __init__(self, event_id=None, create_time=None, event_name=None, event_message=None):
        r"""FlinkJobEvent

        The model defined in huaweicloud sdk

        :param event_id: **参数解释**：运行事件ID。 **取值范围**：UUIDv7格式，固定36位，由英文小写字母、数字及中划线组成。 
        :type event_id: str
        :param create_time: **参数解释**：事件创建时间戳。 **取值范围**：0~4102416000000，13位毫秒时间戳。 
        :type create_time: int
        :param event_name: **参数解释**：运行事件名称。 **取值范围**：1~128个字符。 
        :type event_name: str
        :param event_message: **参数解释**：运行事件信息。 **取值范围**：0~1024个字符。 
        :type event_message: str
        """
        
        

        self._event_id = None
        self._create_time = None
        self._event_name = None
        self._event_message = None
        self.discriminator = None

        self.event_id = event_id
        self.create_time = create_time
        self.event_name = event_name
        self.event_message = event_message

    @property
    def event_id(self):
        r"""Gets the event_id of this FlinkJobEvent.

        **参数解释**：运行事件ID。 **取值范围**：UUIDv7格式，固定36位，由英文小写字母、数字及中划线组成。 

        :return: The event_id of this FlinkJobEvent.
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        r"""Sets the event_id of this FlinkJobEvent.

        **参数解释**：运行事件ID。 **取值范围**：UUIDv7格式，固定36位，由英文小写字母、数字及中划线组成。 

        :param event_id: The event_id of this FlinkJobEvent.
        :type event_id: str
        """
        self._event_id = event_id

    @property
    def create_time(self):
        r"""Gets the create_time of this FlinkJobEvent.

        **参数解释**：事件创建时间戳。 **取值范围**：0~4102416000000，13位毫秒时间戳。 

        :return: The create_time of this FlinkJobEvent.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this FlinkJobEvent.

        **参数解释**：事件创建时间戳。 **取值范围**：0~4102416000000，13位毫秒时间戳。 

        :param create_time: The create_time of this FlinkJobEvent.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def event_name(self):
        r"""Gets the event_name of this FlinkJobEvent.

        **参数解释**：运行事件名称。 **取值范围**：1~128个字符。 

        :return: The event_name of this FlinkJobEvent.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        r"""Sets the event_name of this FlinkJobEvent.

        **参数解释**：运行事件名称。 **取值范围**：1~128个字符。 

        :param event_name: The event_name of this FlinkJobEvent.
        :type event_name: str
        """
        self._event_name = event_name

    @property
    def event_message(self):
        r"""Gets the event_message of this FlinkJobEvent.

        **参数解释**：运行事件信息。 **取值范围**：0~1024个字符。 

        :return: The event_message of this FlinkJobEvent.
        :rtype: str
        """
        return self._event_message

    @event_message.setter
    def event_message(self, event_message):
        r"""Sets the event_message of this FlinkJobEvent.

        **参数解释**：运行事件信息。 **取值范围**：0~1024个字符。 

        :param event_message: The event_message of this FlinkJobEvent.
        :type event_message: str
        """
        self._event_message = event_message

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
        if not isinstance(other, FlinkJobEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
