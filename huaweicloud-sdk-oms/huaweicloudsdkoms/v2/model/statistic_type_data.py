# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StatisticTypeData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data_type': 'str',
        'data': 'list[StatisticData]'
    }

    attribute_map = {
        'data_type': 'data_type',
        'data': 'data'
    }

    def __init__(self, data_type=None, data=None):
        r"""StatisticTypeData

        The model defined in huaweicloud sdk

        :param data_type: 统计数据类型： REQUEST：请求对象数 SUCCESS：成功对象数 FAILURE：失败对象数 SKIP：跳过对象数 SIZE：对象容量(Byte)
        :type data_type: str
        :param data: 查询的同步任务统计结果集
        :type data: list[:class:`huaweicloudsdkoms.v2.StatisticData`]
        """
        
        

        self._data_type = None
        self._data = None
        self.discriminator = None

        if data_type is not None:
            self.data_type = data_type
        if data is not None:
            self.data = data

    @property
    def data_type(self):
        r"""Gets the data_type of this StatisticTypeData.

        统计数据类型： REQUEST：请求对象数 SUCCESS：成功对象数 FAILURE：失败对象数 SKIP：跳过对象数 SIZE：对象容量(Byte)

        :return: The data_type of this StatisticTypeData.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        r"""Sets the data_type of this StatisticTypeData.

        统计数据类型： REQUEST：请求对象数 SUCCESS：成功对象数 FAILURE：失败对象数 SKIP：跳过对象数 SIZE：对象容量(Byte)

        :param data_type: The data_type of this StatisticTypeData.
        :type data_type: str
        """
        self._data_type = data_type

    @property
    def data(self):
        r"""Gets the data of this StatisticTypeData.

        查询的同步任务统计结果集

        :return: The data of this StatisticTypeData.
        :rtype: list[:class:`huaweicloudsdkoms.v2.StatisticData`]
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this StatisticTypeData.

        查询的同步任务统计结果集

        :param data: The data of this StatisticTypeData.
        :type data: list[:class:`huaweicloudsdkoms.v2.StatisticData`]
        """
        self._data = data

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
        if not isinstance(other, StatisticTypeData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
