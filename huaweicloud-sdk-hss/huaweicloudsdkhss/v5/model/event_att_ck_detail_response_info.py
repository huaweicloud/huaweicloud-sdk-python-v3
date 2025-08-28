# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventAttCkDetailResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'att_ck': 'str',
        'num': 'int'
    }

    attribute_map = {
        'att_ck': 'att_ck',
        'num': 'num'
    }

    def __init__(self, att_ck=None, num=None):
        r"""EventAttCkDetailResponseInfo

        The model defined in huaweicloud sdk

        :param att_ck: **参数解释**： 攻击阶段名称，根据页面语言环境，返回中文或英文 **取值范围**： 字符长度1-64位 
        :type att_ck: str
        :param num: **参数解释**: 数量 **取值范围**: 最小值0，最大值2147483647 
        :type num: int
        """
        
        

        self._att_ck = None
        self._num = None
        self.discriminator = None

        if att_ck is not None:
            self.att_ck = att_ck
        if num is not None:
            self.num = num

    @property
    def att_ck(self):
        r"""Gets the att_ck of this EventAttCkDetailResponseInfo.

        **参数解释**： 攻击阶段名称，根据页面语言环境，返回中文或英文 **取值范围**： 字符长度1-64位 

        :return: The att_ck of this EventAttCkDetailResponseInfo.
        :rtype: str
        """
        return self._att_ck

    @att_ck.setter
    def att_ck(self, att_ck):
        r"""Sets the att_ck of this EventAttCkDetailResponseInfo.

        **参数解释**： 攻击阶段名称，根据页面语言环境，返回中文或英文 **取值范围**： 字符长度1-64位 

        :param att_ck: The att_ck of this EventAttCkDetailResponseInfo.
        :type att_ck: str
        """
        self._att_ck = att_ck

    @property
    def num(self):
        r"""Gets the num of this EventAttCkDetailResponseInfo.

        **参数解释**: 数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The num of this EventAttCkDetailResponseInfo.
        :rtype: int
        """
        return self._num

    @num.setter
    def num(self, num):
        r"""Sets the num of this EventAttCkDetailResponseInfo.

        **参数解释**: 数量 **取值范围**: 最小值0，最大值2147483647 

        :param num: The num of this EventAttCkDetailResponseInfo.
        :type num: int
        """
        self._num = num

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
        if not isinstance(other, EventAttCkDetailResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
