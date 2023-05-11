# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SampleParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'divide_type': 'str',
        'train_rate': 'float',
        'test_rate': 'float'
    }

    attribute_map = {
        'divide_type': 'divide_type',
        'train_rate': 'train_rate',
        'test_rate': 'test_rate'
    }

    def __init__(self, divide_type=None, train_rate=None, test_rate=None):
        """SampleParam

        The model defined in huaweicloud sdk

        :param divide_type: 训练集测试集划分方式： - TIME，时间比例 - RAMDOM，个数比例
        :type divide_type: str
        :param train_rate: 训练数据占比。
        :type train_rate: float
        :param test_rate: 测试数据占比。
        :type test_rate: float
        """
        
        

        self._divide_type = None
        self._train_rate = None
        self._test_rate = None
        self.discriminator = None

        self.divide_type = divide_type
        if train_rate is not None:
            self.train_rate = train_rate
        if test_rate is not None:
            self.test_rate = test_rate

    @property
    def divide_type(self):
        """Gets the divide_type of this SampleParam.

        训练集测试集划分方式： - TIME，时间比例 - RAMDOM，个数比例

        :return: The divide_type of this SampleParam.
        :rtype: str
        """
        return self._divide_type

    @divide_type.setter
    def divide_type(self, divide_type):
        """Sets the divide_type of this SampleParam.

        训练集测试集划分方式： - TIME，时间比例 - RAMDOM，个数比例

        :param divide_type: The divide_type of this SampleParam.
        :type divide_type: str
        """
        self._divide_type = divide_type

    @property
    def train_rate(self):
        """Gets the train_rate of this SampleParam.

        训练数据占比。

        :return: The train_rate of this SampleParam.
        :rtype: float
        """
        return self._train_rate

    @train_rate.setter
    def train_rate(self, train_rate):
        """Sets the train_rate of this SampleParam.

        训练数据占比。

        :param train_rate: The train_rate of this SampleParam.
        :type train_rate: float
        """
        self._train_rate = train_rate

    @property
    def test_rate(self):
        """Gets the test_rate of this SampleParam.

        测试数据占比。

        :return: The test_rate of this SampleParam.
        :rtype: float
        """
        return self._test_rate

    @test_rate.setter
    def test_rate(self, test_rate):
        """Sets the test_rate of this SampleParam.

        测试数据占比。

        :param test_rate: The test_rate of this SampleParam.
        :type test_rate: float
        """
        self._test_rate = test_rate

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
        if not isinstance(other, SampleParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
