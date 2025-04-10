# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoverRateVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'testing': 'int',
        'finished': 'int',
        'not_tested': 'int',
        'total_number': 'int',
        'cover_rate': 'str'
    }

    attribute_map = {
        'testing': 'testing',
        'finished': 'finished',
        'not_tested': 'not_tested',
        'total_number': 'total_number',
        'cover_rate': 'cover_rate'
    }

    def __init__(self, testing=None, finished=None, not_tested=None, total_number=None, cover_rate=None):
        r"""CoverRateVo

        The model defined in huaweicloud sdk

        :param testing: 统计测试中的需求
        :type testing: int
        :param finished: 统计已完成的需求
        :type finished: int
        :param not_tested: 统计未测试的需求
        :type not_tested: int
        :param total_number: 计算需求总数
        :type total_number: int
        :param cover_rate: 需求覆盖率
        :type cover_rate: str
        """
        
        

        self._testing = None
        self._finished = None
        self._not_tested = None
        self._total_number = None
        self._cover_rate = None
        self.discriminator = None

        if testing is not None:
            self.testing = testing
        if finished is not None:
            self.finished = finished
        if not_tested is not None:
            self.not_tested = not_tested
        if total_number is not None:
            self.total_number = total_number
        if cover_rate is not None:
            self.cover_rate = cover_rate

    @property
    def testing(self):
        r"""Gets the testing of this CoverRateVo.

        统计测试中的需求

        :return: The testing of this CoverRateVo.
        :rtype: int
        """
        return self._testing

    @testing.setter
    def testing(self, testing):
        r"""Sets the testing of this CoverRateVo.

        统计测试中的需求

        :param testing: The testing of this CoverRateVo.
        :type testing: int
        """
        self._testing = testing

    @property
    def finished(self):
        r"""Gets the finished of this CoverRateVo.

        统计已完成的需求

        :return: The finished of this CoverRateVo.
        :rtype: int
        """
        return self._finished

    @finished.setter
    def finished(self, finished):
        r"""Sets the finished of this CoverRateVo.

        统计已完成的需求

        :param finished: The finished of this CoverRateVo.
        :type finished: int
        """
        self._finished = finished

    @property
    def not_tested(self):
        r"""Gets the not_tested of this CoverRateVo.

        统计未测试的需求

        :return: The not_tested of this CoverRateVo.
        :rtype: int
        """
        return self._not_tested

    @not_tested.setter
    def not_tested(self, not_tested):
        r"""Sets the not_tested of this CoverRateVo.

        统计未测试的需求

        :param not_tested: The not_tested of this CoverRateVo.
        :type not_tested: int
        """
        self._not_tested = not_tested

    @property
    def total_number(self):
        r"""Gets the total_number of this CoverRateVo.

        计算需求总数

        :return: The total_number of this CoverRateVo.
        :rtype: int
        """
        return self._total_number

    @total_number.setter
    def total_number(self, total_number):
        r"""Sets the total_number of this CoverRateVo.

        计算需求总数

        :param total_number: The total_number of this CoverRateVo.
        :type total_number: int
        """
        self._total_number = total_number

    @property
    def cover_rate(self):
        r"""Gets the cover_rate of this CoverRateVo.

        需求覆盖率

        :return: The cover_rate of this CoverRateVo.
        :rtype: str
        """
        return self._cover_rate

    @cover_rate.setter
    def cover_rate(self, cover_rate):
        r"""Sets the cover_rate of this CoverRateVo.

        需求覆盖率

        :param cover_rate: The cover_rate of this CoverRateVo.
        :type cover_rate: str
        """
        self._cover_rate = cover_rate

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
        if not isinstance(other, CoverRateVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
