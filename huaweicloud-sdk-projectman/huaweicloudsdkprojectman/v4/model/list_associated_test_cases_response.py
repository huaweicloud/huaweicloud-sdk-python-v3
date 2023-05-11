# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAssociatedTestCasesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'test_cases': 'list[AssociatedTestCase]',
        'total': 'int'
    }

    attribute_map = {
        'test_cases': 'test_cases',
        'total': 'total'
    }

    def __init__(self, test_cases=None, total=None):
        """ListAssociatedTestCasesResponse

        The model defined in huaweicloud sdk

        :param test_cases: 关联的测试用例列表
        :type test_cases: list[:class:`huaweicloudsdkprojectman.v4.AssociatedTestCase`]
        :param total: 总数
        :type total: int
        """
        
        super(ListAssociatedTestCasesResponse, self).__init__()

        self._test_cases = None
        self._total = None
        self.discriminator = None

        if test_cases is not None:
            self.test_cases = test_cases
        if total is not None:
            self.total = total

    @property
    def test_cases(self):
        """Gets the test_cases of this ListAssociatedTestCasesResponse.

        关联的测试用例列表

        :return: The test_cases of this ListAssociatedTestCasesResponse.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.AssociatedTestCase`]
        """
        return self._test_cases

    @test_cases.setter
    def test_cases(self, test_cases):
        """Sets the test_cases of this ListAssociatedTestCasesResponse.

        关联的测试用例列表

        :param test_cases: The test_cases of this ListAssociatedTestCasesResponse.
        :type test_cases: list[:class:`huaweicloudsdkprojectman.v4.AssociatedTestCase`]
        """
        self._test_cases = test_cases

    @property
    def total(self):
        """Gets the total of this ListAssociatedTestCasesResponse.

        总数

        :return: The total of this ListAssociatedTestCasesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListAssociatedTestCasesResponse.

        总数

        :param total: The total of this ListAssociatedTestCasesResponse.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, ListAssociatedTestCasesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
