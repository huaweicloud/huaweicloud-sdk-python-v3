# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModClusterProtectionEventRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_num': 'int',
        'opr': 'str',
        'data_list': 'list[str]'
    }

    attribute_map = {
        'total_num': 'total_num',
        'opr': 'opr',
        'data_list': 'data_list'
    }

    def __init__(self, total_num=None, opr=None, data_list=None):
        r"""ModClusterProtectionEventRequest

        The model defined in huaweicloud sdk

        :param total_num: 总数
        :type total_num: int
        :param opr: 操作类型，包含以下几种： - ignore：忽略 - handle：处理 - addWhiteImage：加白
        :type opr: str
        :param data_list: 事件ID列表
        :type data_list: list[str]
        """
        
        

        self._total_num = None
        self._opr = None
        self._data_list = None
        self.discriminator = None

        self.total_num = total_num
        self.opr = opr
        self.data_list = data_list

    @property
    def total_num(self):
        r"""Gets the total_num of this ModClusterProtectionEventRequest.

        总数

        :return: The total_num of this ModClusterProtectionEventRequest.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        r"""Sets the total_num of this ModClusterProtectionEventRequest.

        总数

        :param total_num: The total_num of this ModClusterProtectionEventRequest.
        :type total_num: int
        """
        self._total_num = total_num

    @property
    def opr(self):
        r"""Gets the opr of this ModClusterProtectionEventRequest.

        操作类型，包含以下几种： - ignore：忽略 - handle：处理 - addWhiteImage：加白

        :return: The opr of this ModClusterProtectionEventRequest.
        :rtype: str
        """
        return self._opr

    @opr.setter
    def opr(self, opr):
        r"""Sets the opr of this ModClusterProtectionEventRequest.

        操作类型，包含以下几种： - ignore：忽略 - handle：处理 - addWhiteImage：加白

        :param opr: The opr of this ModClusterProtectionEventRequest.
        :type opr: str
        """
        self._opr = opr

    @property
    def data_list(self):
        r"""Gets the data_list of this ModClusterProtectionEventRequest.

        事件ID列表

        :return: The data_list of this ModClusterProtectionEventRequest.
        :rtype: list[str]
        """
        return self._data_list

    @data_list.setter
    def data_list(self, data_list):
        r"""Sets the data_list of this ModClusterProtectionEventRequest.

        事件ID列表

        :param data_list: The data_list of this ModClusterProtectionEventRequest.
        :type data_list: list[str]
        """
        self._data_list = data_list

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
        if not isinstance(other, ModClusterProtectionEventRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
