# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KernelModuleStatisticsResponseInfo:

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
        'num': 'int'
    }

    attribute_map = {
        'name': 'name',
        'num': 'num'
    }

    def __init__(self, name=None, num=None):
        r"""KernelModuleStatisticsResponseInfo

        The model defined in huaweicloud sdk

        :param name: **参数解释**: 内核模块名称 **取值范围**: 字符长度0-256 
        :type name: str
        :param num: **参数解释** 内核模块统计信息总数 **取值范围** 最小值0，最大值300000 
        :type num: int
        """
        
        

        self._name = None
        self._num = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if num is not None:
            self.num = num

    @property
    def name(self):
        r"""Gets the name of this KernelModuleStatisticsResponseInfo.

        **参数解释**: 内核模块名称 **取值范围**: 字符长度0-256 

        :return: The name of this KernelModuleStatisticsResponseInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this KernelModuleStatisticsResponseInfo.

        **参数解释**: 内核模块名称 **取值范围**: 字符长度0-256 

        :param name: The name of this KernelModuleStatisticsResponseInfo.
        :type name: str
        """
        self._name = name

    @property
    def num(self):
        r"""Gets the num of this KernelModuleStatisticsResponseInfo.

        **参数解释** 内核模块统计信息总数 **取值范围** 最小值0，最大值300000 

        :return: The num of this KernelModuleStatisticsResponseInfo.
        :rtype: int
        """
        return self._num

    @num.setter
    def num(self, num):
        r"""Sets the num of this KernelModuleStatisticsResponseInfo.

        **参数解释** 内核模块统计信息总数 **取值范围** 最小值0，最大值300000 

        :param num: The num of this KernelModuleStatisticsResponseInfo.
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
        if not isinstance(other, KernelModuleStatisticsResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
