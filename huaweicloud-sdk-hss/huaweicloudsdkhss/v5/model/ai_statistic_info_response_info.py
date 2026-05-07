# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AIStatisticInfoResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ai_component_name': 'str',
        'num': 'int'
    }

    attribute_map = {
        'ai_component_name': 'ai_component_name',
        'num': 'num'
    }

    def __init__(self, ai_component_name=None, num=None):
        r"""AIStatisticInfoResponseInfo

        The model defined in huaweicloud sdk

        :param ai_component_name: **参数解释**： AI组件对应类型的名称 **取值范围**： 字符长度1-256位 
        :type ai_component_name: str
        :param num: **参数解释**： AI组件所在的服务器数量 
        :type num: int
        """
        
        

        self._ai_component_name = None
        self._num = None
        self.discriminator = None

        if ai_component_name is not None:
            self.ai_component_name = ai_component_name
        if num is not None:
            self.num = num

    @property
    def ai_component_name(self):
        r"""Gets the ai_component_name of this AIStatisticInfoResponseInfo.

        **参数解释**： AI组件对应类型的名称 **取值范围**： 字符长度1-256位 

        :return: The ai_component_name of this AIStatisticInfoResponseInfo.
        :rtype: str
        """
        return self._ai_component_name

    @ai_component_name.setter
    def ai_component_name(self, ai_component_name):
        r"""Sets the ai_component_name of this AIStatisticInfoResponseInfo.

        **参数解释**： AI组件对应类型的名称 **取值范围**： 字符长度1-256位 

        :param ai_component_name: The ai_component_name of this AIStatisticInfoResponseInfo.
        :type ai_component_name: str
        """
        self._ai_component_name = ai_component_name

    @property
    def num(self):
        r"""Gets the num of this AIStatisticInfoResponseInfo.

        **参数解释**： AI组件所在的服务器数量 

        :return: The num of this AIStatisticInfoResponseInfo.
        :rtype: int
        """
        return self._num

    @num.setter
    def num(self, num):
        r"""Sets the num of this AIStatisticInfoResponseInfo.

        **参数解释**： AI组件所在的服务器数量 

        :param num: The num of this AIStatisticInfoResponseInfo.
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
        if not isinstance(other, AIStatisticInfoResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
