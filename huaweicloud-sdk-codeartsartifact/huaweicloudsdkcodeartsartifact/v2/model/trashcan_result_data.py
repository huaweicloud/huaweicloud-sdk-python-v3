# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TrashcanResultData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'success_num': 'int',
        'failed_num': 'int',
        'failed_messages': 'list[str]'
    }

    attribute_map = {
        'success_num': 'successNum',
        'failed_num': 'failedNum',
        'failed_messages': 'failedMessages'
    }

    def __init__(self, success_num=None, failed_num=None, failed_messages=None):
        r"""TrashcanResultData

        The model defined in huaweicloud sdk

        :param success_num: **参数解释**： 成功数目。 **取值范围**： 不涉及。 
        :type success_num: int
        :param failed_num: **参数解释**： 失败数目。 **取值范围**： 不涉及。 
        :type failed_num: int
        :param failed_messages: **参数解释**： 失败原因。 **取值范围**： 不涉及。 
        :type failed_messages: list[str]
        """
        
        

        self._success_num = None
        self._failed_num = None
        self._failed_messages = None
        self.discriminator = None

        if success_num is not None:
            self.success_num = success_num
        if failed_num is not None:
            self.failed_num = failed_num
        if failed_messages is not None:
            self.failed_messages = failed_messages

    @property
    def success_num(self):
        r"""Gets the success_num of this TrashcanResultData.

        **参数解释**： 成功数目。 **取值范围**： 不涉及。 

        :return: The success_num of this TrashcanResultData.
        :rtype: int
        """
        return self._success_num

    @success_num.setter
    def success_num(self, success_num):
        r"""Sets the success_num of this TrashcanResultData.

        **参数解释**： 成功数目。 **取值范围**： 不涉及。 

        :param success_num: The success_num of this TrashcanResultData.
        :type success_num: int
        """
        self._success_num = success_num

    @property
    def failed_num(self):
        r"""Gets the failed_num of this TrashcanResultData.

        **参数解释**： 失败数目。 **取值范围**： 不涉及。 

        :return: The failed_num of this TrashcanResultData.
        :rtype: int
        """
        return self._failed_num

    @failed_num.setter
    def failed_num(self, failed_num):
        r"""Sets the failed_num of this TrashcanResultData.

        **参数解释**： 失败数目。 **取值范围**： 不涉及。 

        :param failed_num: The failed_num of this TrashcanResultData.
        :type failed_num: int
        """
        self._failed_num = failed_num

    @property
    def failed_messages(self):
        r"""Gets the failed_messages of this TrashcanResultData.

        **参数解释**： 失败原因。 **取值范围**： 不涉及。 

        :return: The failed_messages of this TrashcanResultData.
        :rtype: list[str]
        """
        return self._failed_messages

    @failed_messages.setter
    def failed_messages(self, failed_messages):
        r"""Sets the failed_messages of this TrashcanResultData.

        **参数解释**： 失败原因。 **取值范围**： 不涉及。 

        :param failed_messages: The failed_messages of this TrashcanResultData.
        :type failed_messages: list[str]
        """
        self._failed_messages = failed_messages

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
        if not isinstance(other, TrashcanResultData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
