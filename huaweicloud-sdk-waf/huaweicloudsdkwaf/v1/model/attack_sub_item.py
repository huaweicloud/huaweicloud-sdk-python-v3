# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttackSubItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'num': 'int'
    }

    attribute_map = {
        'key': 'key',
        'num': 'num'
    }

    def __init__(self, key=None, num=None):
        r"""AttackSubItem

        The model defined in huaweicloud sdk

        :param key: 子类型标识： 合规检测子类型：politics_matched, violent_matched, illegal_matched, hatespeech_matched, privatesensitive_matched, religion_matched, other_matched 注入检测子类型：goal_hijacking_matched, prompt_leaking_matched, role_play_instruction_matched, unsafe_instruction_topic_matched, inquiry_with_unsafe_opinion_matched, reverse_exposure_matched, multi_step_instruction_matched, context_task_matched, opposition_response_matched, virtual_conversation_matched, do_anything_now_matched, code_injection_matched 
        :type key: str
        :param num: 该子类型命中次数
        :type num: int
        """
        
        

        self._key = None
        self._num = None
        self.discriminator = None

        self.key = key
        self.num = num

    @property
    def key(self):
        r"""Gets the key of this AttackSubItem.

        子类型标识： 合规检测子类型：politics_matched, violent_matched, illegal_matched, hatespeech_matched, privatesensitive_matched, religion_matched, other_matched 注入检测子类型：goal_hijacking_matched, prompt_leaking_matched, role_play_instruction_matched, unsafe_instruction_topic_matched, inquiry_with_unsafe_opinion_matched, reverse_exposure_matched, multi_step_instruction_matched, context_task_matched, opposition_response_matched, virtual_conversation_matched, do_anything_now_matched, code_injection_matched 

        :return: The key of this AttackSubItem.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this AttackSubItem.

        子类型标识： 合规检测子类型：politics_matched, violent_matched, illegal_matched, hatespeech_matched, privatesensitive_matched, religion_matched, other_matched 注入检测子类型：goal_hijacking_matched, prompt_leaking_matched, role_play_instruction_matched, unsafe_instruction_topic_matched, inquiry_with_unsafe_opinion_matched, reverse_exposure_matched, multi_step_instruction_matched, context_task_matched, opposition_response_matched, virtual_conversation_matched, do_anything_now_matched, code_injection_matched 

        :param key: The key of this AttackSubItem.
        :type key: str
        """
        self._key = key

    @property
    def num(self):
        r"""Gets the num of this AttackSubItem.

        该子类型命中次数

        :return: The num of this AttackSubItem.
        :rtype: int
        """
        return self._num

    @num.setter
    def num(self, num):
        r"""Sets the num of this AttackSubItem.

        该子类型命中次数

        :param num: The num of this AttackSubItem.
        :type num: int
        """
        self._num = num

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
        if not isinstance(other, AttackSubItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
