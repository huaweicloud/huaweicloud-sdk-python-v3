# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProtectInfoCoverAreaInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'protect_host_num': 'int',
        'un_protect_host_num': 'int',
        'protect_rate': 'float',
        'beat_rate': 'float'
    }

    attribute_map = {
        'protect_host_num': 'protect_host_num',
        'un_protect_host_num': 'un_protect_host_num',
        'protect_rate': 'protect_rate',
        'beat_rate': 'beat_rate'
    }

    def __init__(self, protect_host_num=None, un_protect_host_num=None, protect_rate=None, beat_rate=None):
        r"""ProtectInfoCoverAreaInfo

        The model defined in huaweicloud sdk

        :param protect_host_num: **参数解释**: 防护主机数量 **取值范围**: 最小值0，最大值2147483647 
        :type protect_host_num: int
        :param un_protect_host_num: **参数解释**: 未防护主机数量 **取值范围**: 最小值0，最大值2147483647 
        :type un_protect_host_num: int
        :param protect_rate: **参数解释**: 防护率 **取值范围**: 最小值0，最大值1 
        :type protect_rate: float
        :param beat_rate: **参数解释**: 击败用户率 **取值范围**: 最小值0，最大值1 
        :type beat_rate: float
        """
        
        

        self._protect_host_num = None
        self._un_protect_host_num = None
        self._protect_rate = None
        self._beat_rate = None
        self.discriminator = None

        if protect_host_num is not None:
            self.protect_host_num = protect_host_num
        if un_protect_host_num is not None:
            self.un_protect_host_num = un_protect_host_num
        if protect_rate is not None:
            self.protect_rate = protect_rate
        if beat_rate is not None:
            self.beat_rate = beat_rate

    @property
    def protect_host_num(self):
        r"""Gets the protect_host_num of this ProtectInfoCoverAreaInfo.

        **参数解释**: 防护主机数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The protect_host_num of this ProtectInfoCoverAreaInfo.
        :rtype: int
        """
        return self._protect_host_num

    @protect_host_num.setter
    def protect_host_num(self, protect_host_num):
        r"""Sets the protect_host_num of this ProtectInfoCoverAreaInfo.

        **参数解释**: 防护主机数量 **取值范围**: 最小值0，最大值2147483647 

        :param protect_host_num: The protect_host_num of this ProtectInfoCoverAreaInfo.
        :type protect_host_num: int
        """
        self._protect_host_num = protect_host_num

    @property
    def un_protect_host_num(self):
        r"""Gets the un_protect_host_num of this ProtectInfoCoverAreaInfo.

        **参数解释**: 未防护主机数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The un_protect_host_num of this ProtectInfoCoverAreaInfo.
        :rtype: int
        """
        return self._un_protect_host_num

    @un_protect_host_num.setter
    def un_protect_host_num(self, un_protect_host_num):
        r"""Sets the un_protect_host_num of this ProtectInfoCoverAreaInfo.

        **参数解释**: 未防护主机数量 **取值范围**: 最小值0，最大值2147483647 

        :param un_protect_host_num: The un_protect_host_num of this ProtectInfoCoverAreaInfo.
        :type un_protect_host_num: int
        """
        self._un_protect_host_num = un_protect_host_num

    @property
    def protect_rate(self):
        r"""Gets the protect_rate of this ProtectInfoCoverAreaInfo.

        **参数解释**: 防护率 **取值范围**: 最小值0，最大值1 

        :return: The protect_rate of this ProtectInfoCoverAreaInfo.
        :rtype: float
        """
        return self._protect_rate

    @protect_rate.setter
    def protect_rate(self, protect_rate):
        r"""Sets the protect_rate of this ProtectInfoCoverAreaInfo.

        **参数解释**: 防护率 **取值范围**: 最小值0，最大值1 

        :param protect_rate: The protect_rate of this ProtectInfoCoverAreaInfo.
        :type protect_rate: float
        """
        self._protect_rate = protect_rate

    @property
    def beat_rate(self):
        r"""Gets the beat_rate of this ProtectInfoCoverAreaInfo.

        **参数解释**: 击败用户率 **取值范围**: 最小值0，最大值1 

        :return: The beat_rate of this ProtectInfoCoverAreaInfo.
        :rtype: float
        """
        return self._beat_rate

    @beat_rate.setter
    def beat_rate(self, beat_rate):
        r"""Sets the beat_rate of this ProtectInfoCoverAreaInfo.

        **参数解释**: 击败用户率 **取值范围**: 最小值0，最大值1 

        :param beat_rate: The beat_rate of this ProtectInfoCoverAreaInfo.
        :type beat_rate: float
        """
        self._beat_rate = beat_rate

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
        if not isinstance(other, ProtectInfoCoverAreaInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
