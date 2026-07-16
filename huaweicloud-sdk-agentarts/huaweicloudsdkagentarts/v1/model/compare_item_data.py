# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CompareItemData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_input': 'str',
        'user_output': 'str'
    }

    attribute_map = {
        'user_input': 'user_input',
        'user_output': 'user_output'
    }

    def __init__(self, user_input=None, user_output=None):
        r"""CompareItemData

        The model defined in huaweicloud sdk

        :param user_input: 用户输入的文本内容。
        :type user_input: str
        :param user_output: 系统或模型针对该输入给出的输出内容。
        :type user_output: str
        """
        
        

        self._user_input = None
        self._user_output = None
        self.discriminator = None

        if user_input is not None:
            self.user_input = user_input
        if user_output is not None:
            self.user_output = user_output

    @property
    def user_input(self):
        r"""Gets the user_input of this CompareItemData.

        用户输入的文本内容。

        :return: The user_input of this CompareItemData.
        :rtype: str
        """
        return self._user_input

    @user_input.setter
    def user_input(self, user_input):
        r"""Sets the user_input of this CompareItemData.

        用户输入的文本内容。

        :param user_input: The user_input of this CompareItemData.
        :type user_input: str
        """
        self._user_input = user_input

    @property
    def user_output(self):
        r"""Gets the user_output of this CompareItemData.

        系统或模型针对该输入给出的输出内容。

        :return: The user_output of this CompareItemData.
        :rtype: str
        """
        return self._user_output

    @user_output.setter
    def user_output(self, user_output):
        r"""Sets the user_output of this CompareItemData.

        系统或模型针对该输入给出的输出内容。

        :param user_output: The user_output of this CompareItemData.
        :type user_output: str
        """
        self._user_output = user_output

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
        if not isinstance(other, CompareItemData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
