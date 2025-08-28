# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateInstructionReq:

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
        'instruction': 'str',
        'slot_list': 'list[InstructionSlotInfo]',
        'reply_words_list': 'list[InstructionReplyWordsInfo]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'instruction': 'instruction',
        'slot_list': 'slot_list',
        'reply_words_list': 'reply_words_list'
    }

    def __init__(self, name=None, description=None, instruction=None, slot_list=None, reply_words_list=None):
        r"""UpdateInstructionReq

        The model defined in huaweicloud sdk

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
        """
        
        

        self._name = None
        self._description = None
        self._instruction = None
        self._slot_list = None
        self._reply_words_list = None
        self.discriminator = None

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

    @property
    def name(self):
        r"""Gets the name of this UpdateInstructionReq.

        指令名称。

        :return: The name of this UpdateInstructionReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateInstructionReq.

        指令名称。

        :param name: The name of this UpdateInstructionReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this UpdateInstructionReq.

        指令描述。

        :return: The description of this UpdateInstructionReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateInstructionReq.

        指令描述。

        :param description: The description of this UpdateInstructionReq.
        :type description: str
        """
        self._description = description

    @property
    def instruction(self):
        r"""Gets the instruction of this UpdateInstructionReq.

        操作指令。

        :return: The instruction of this UpdateInstructionReq.
        :rtype: str
        """
        return self._instruction

    @instruction.setter
    def instruction(self, instruction):
        r"""Sets the instruction of this UpdateInstructionReq.

        操作指令。

        :param instruction: The instruction of this UpdateInstructionReq.
        :type instruction: str
        """
        self._instruction = instruction

    @property
    def slot_list(self):
        r"""Gets the slot_list of this UpdateInstructionReq.

        槽位列表

        :return: The slot_list of this UpdateInstructionReq.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.InstructionSlotInfo`]
        """
        return self._slot_list

    @slot_list.setter
    def slot_list(self, slot_list):
        r"""Sets the slot_list of this UpdateInstructionReq.

        槽位列表

        :param slot_list: The slot_list of this UpdateInstructionReq.
        :type slot_list: list[:class:`huaweicloudsdkmetastudio.v1.InstructionSlotInfo`]
        """
        self._slot_list = slot_list

    @property
    def reply_words_list(self):
        r"""Gets the reply_words_list of this UpdateInstructionReq.

        指令回复话术列表

        :return: The reply_words_list of this UpdateInstructionReq.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.InstructionReplyWordsInfo`]
        """
        return self._reply_words_list

    @reply_words_list.setter
    def reply_words_list(self, reply_words_list):
        r"""Sets the reply_words_list of this UpdateInstructionReq.

        指令回复话术列表

        :param reply_words_list: The reply_words_list of this UpdateInstructionReq.
        :type reply_words_list: list[:class:`huaweicloudsdkmetastudio.v1.InstructionReplyWordsInfo`]
        """
        self._reply_words_list = reply_words_list

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
        if not isinstance(other, UpdateInstructionReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
