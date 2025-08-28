# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstructionInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instruction_id': 'str',
        'name': 'str',
        'description': 'str',
        'instruction': 'str',
        'slot_list': 'list[InstructionSlotInfo]',
        'reply_words_list': 'list[InstructionReplyWordsInfo]',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'instruction_id': 'instruction_id',
        'name': 'name',
        'description': 'description',
        'instruction': 'instruction',
        'slot_list': 'slot_list',
        'reply_words_list': 'reply_words_list',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, instruction_id=None, name=None, description=None, instruction=None, slot_list=None, reply_words_list=None, create_time=None, update_time=None):
        r"""InstructionInfo

        The model defined in huaweicloud sdk

        :param instruction_id: 指令ID。
        :type instruction_id: str
        :param name: 指令名称。
        :type name: str
        :param description: 指令描述。
        :type description: str
        :param instruction: 操作指令。
        :type instruction: str
        :param slot_list: 槽位列表
        :type slot_list: list[:class:`huaweicloudsdkmetastudio.v1.InstructionSlotInfo`]
        :param reply_words_list: 指令回复话术列表
        :type reply_words_list: list[:class:`huaweicloudsdkmetastudio.v1.InstructionReplyWordsInfo`]
        :param create_time: 创建时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type create_time: str
        :param update_time: 更新时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type update_time: str
        """
        
        

        self._instruction_id = None
        self._name = None
        self._description = None
        self._instruction = None
        self._slot_list = None
        self._reply_words_list = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if instruction_id is not None:
            self.instruction_id = instruction_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if instruction is not None:
            self.instruction = instruction
        if slot_list is not None:
            self.slot_list = slot_list
        if reply_words_list is not None:
            self.reply_words_list = reply_words_list
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def instruction_id(self):
        r"""Gets the instruction_id of this InstructionInfo.

        指令ID。

        :return: The instruction_id of this InstructionInfo.
        :rtype: str
        """
        return self._instruction_id

    @instruction_id.setter
    def instruction_id(self, instruction_id):
        r"""Sets the instruction_id of this InstructionInfo.

        指令ID。

        :param instruction_id: The instruction_id of this InstructionInfo.
        :type instruction_id: str
        """
        self._instruction_id = instruction_id

    @property
    def name(self):
        r"""Gets the name of this InstructionInfo.

        指令名称。

        :return: The name of this InstructionInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this InstructionInfo.

        指令名称。

        :param name: The name of this InstructionInfo.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this InstructionInfo.

        指令描述。

        :return: The description of this InstructionInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this InstructionInfo.

        指令描述。

        :param description: The description of this InstructionInfo.
        :type description: str
        """
        self._description = description

    @property
    def instruction(self):
        r"""Gets the instruction of this InstructionInfo.

        操作指令。

        :return: The instruction of this InstructionInfo.
        :rtype: str
        """
        return self._instruction

    @instruction.setter
    def instruction(self, instruction):
        r"""Sets the instruction of this InstructionInfo.

        操作指令。

        :param instruction: The instruction of this InstructionInfo.
        :type instruction: str
        """
        self._instruction = instruction

    @property
    def slot_list(self):
        r"""Gets the slot_list of this InstructionInfo.

        槽位列表

        :return: The slot_list of this InstructionInfo.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.InstructionSlotInfo`]
        """
        return self._slot_list

    @slot_list.setter
    def slot_list(self, slot_list):
        r"""Sets the slot_list of this InstructionInfo.

        槽位列表

        :param slot_list: The slot_list of this InstructionInfo.
        :type slot_list: list[:class:`huaweicloudsdkmetastudio.v1.InstructionSlotInfo`]
        """
        self._slot_list = slot_list

    @property
    def reply_words_list(self):
        r"""Gets the reply_words_list of this InstructionInfo.

        指令回复话术列表

        :return: The reply_words_list of this InstructionInfo.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.InstructionReplyWordsInfo`]
        """
        return self._reply_words_list

    @reply_words_list.setter
    def reply_words_list(self, reply_words_list):
        r"""Sets the reply_words_list of this InstructionInfo.

        指令回复话术列表

        :param reply_words_list: The reply_words_list of this InstructionInfo.
        :type reply_words_list: list[:class:`huaweicloudsdkmetastudio.v1.InstructionReplyWordsInfo`]
        """
        self._reply_words_list = reply_words_list

    @property
    def create_time(self):
        r"""Gets the create_time of this InstructionInfo.

        创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The create_time of this InstructionInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this InstructionInfo.

        创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param create_time: The create_time of this InstructionInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this InstructionInfo.

        更新时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The update_time of this InstructionInfo.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this InstructionInfo.

        更新时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param update_time: The update_time of this InstructionInfo.
        :type update_time: str
        """
        self._update_time = update_time

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
        if not isinstance(other, InstructionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
