# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CommonTopResponseInfo:

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
        'host_num': 'int',
        'percentage': 'int'
    }

    attribute_map = {
        'name': 'name',
        'host_num': 'host_num',
        'percentage': 'percentage'
    }

    def __init__(self, name=None, host_num=None, percentage=None):
        r"""CommonTopResponseInfo

        The model defined in huaweicloud sdk

        :param name: **参数解释**: 名称 **取值范围**: 字符长度1-128位 
        :type name: str
        :param host_num: **参数解释**: 主机数量 **取值范围**: 取值0-2147483647位 
        :type host_num: int
        :param percentage: **参数解释**:  主机占用百分比  **取值范围**:  取值0-100位 
        :type percentage: int
        """
        
        

        self._name = None
        self._host_num = None
        self._percentage = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if host_num is not None:
            self.host_num = host_num
        if percentage is not None:
            self.percentage = percentage

    @property
    def name(self):
        r"""Gets the name of this CommonTopResponseInfo.

        **参数解释**: 名称 **取值范围**: 字符长度1-128位 

        :return: The name of this CommonTopResponseInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CommonTopResponseInfo.

        **参数解释**: 名称 **取值范围**: 字符长度1-128位 

        :param name: The name of this CommonTopResponseInfo.
        :type name: str
        """
        self._name = name

    @property
    def host_num(self):
        r"""Gets the host_num of this CommonTopResponseInfo.

        **参数解释**: 主机数量 **取值范围**: 取值0-2147483647位 

        :return: The host_num of this CommonTopResponseInfo.
        :rtype: int
        """
        return self._host_num

    @host_num.setter
    def host_num(self, host_num):
        r"""Sets the host_num of this CommonTopResponseInfo.

        **参数解释**: 主机数量 **取值范围**: 取值0-2147483647位 

        :param host_num: The host_num of this CommonTopResponseInfo.
        :type host_num: int
        """
        self._host_num = host_num

    @property
    def percentage(self):
        r"""Gets the percentage of this CommonTopResponseInfo.

        **参数解释**:  主机占用百分比  **取值范围**:  取值0-100位 

        :return: The percentage of this CommonTopResponseInfo.
        :rtype: int
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        r"""Sets the percentage of this CommonTopResponseInfo.

        **参数解释**:  主机占用百分比  **取值范围**:  取值0-100位 

        :param percentage: The percentage of this CommonTopResponseInfo.
        :type percentage: int
        """
        self._percentage = percentage

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
        if not isinstance(other, CommonTopResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
