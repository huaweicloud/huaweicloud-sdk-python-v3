# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DetailTestTypeCasePassRateVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'test_type': 'int',
        'case_pass_rate': 'str'
    }

    attribute_map = {
        'test_type': 'test_type',
        'case_pass_rate': 'case_pass_rate'
    }

    def __init__(self, test_type=None, case_pass_rate=None):
        r"""DetailTestTypeCasePassRateVo

        The model defined in huaweicloud sdk

        :param test_type: 测试类型
        :type test_type: int
        :param case_pass_rate: 用例通过率
        :type case_pass_rate: str
        """
        
        

        self._test_type = None
        self._case_pass_rate = None
        self.discriminator = None

        if test_type is not None:
            self.test_type = test_type
        if case_pass_rate is not None:
            self.case_pass_rate = case_pass_rate

    @property
    def test_type(self):
        r"""Gets the test_type of this DetailTestTypeCasePassRateVo.

        测试类型

        :return: The test_type of this DetailTestTypeCasePassRateVo.
        :rtype: int
        """
        return self._test_type

    @test_type.setter
    def test_type(self, test_type):
        r"""Sets the test_type of this DetailTestTypeCasePassRateVo.

        测试类型

        :param test_type: The test_type of this DetailTestTypeCasePassRateVo.
        :type test_type: int
        """
        self._test_type = test_type

    @property
    def case_pass_rate(self):
        r"""Gets the case_pass_rate of this DetailTestTypeCasePassRateVo.

        用例通过率

        :return: The case_pass_rate of this DetailTestTypeCasePassRateVo.
        :rtype: str
        """
        return self._case_pass_rate

    @case_pass_rate.setter
    def case_pass_rate(self, case_pass_rate):
        r"""Sets the case_pass_rate of this DetailTestTypeCasePassRateVo.

        用例通过率

        :param case_pass_rate: The case_pass_rate of this DetailTestTypeCasePassRateVo.
        :type case_pass_rate: str
        """
        self._case_pass_rate = case_pass_rate

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
        if not isinstance(other, DetailTestTypeCasePassRateVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
