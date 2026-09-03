# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CloudTestCaseOperationInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'set_up_cases_info': 'list[CloudTestCaseInfo]',
        'tear_down_cases_info': 'list[CloudTestCaseInfo]',
        'test_cases_info': 'list[CloudTestCaseInfo]'
    }

    attribute_map = {
        'set_up_cases_info': 'setUpCasesInfo',
        'tear_down_cases_info': 'tearDownCasesInfo',
        'test_cases_info': 'testCasesInfo'
    }

    def __init__(self, set_up_cases_info=None, tear_down_cases_info=None, test_cases_info=None):
        r"""CloudTestCaseOperationInfo

        The model defined in huaweicloud sdk

        :param set_up_cases_info: 前置用例信息
        :type set_up_cases_info: list[:class:`huaweicloudsdkcloudtest.v1.CloudTestCaseInfo`]
        :param tear_down_cases_info: 后置用例信息
        :type tear_down_cases_info: list[:class:`huaweicloudsdkcloudtest.v1.CloudTestCaseInfo`]
        :param test_cases_info: 用例信息
        :type test_cases_info: list[:class:`huaweicloudsdkcloudtest.v1.CloudTestCaseInfo`]
        """
        
        

        self._set_up_cases_info = None
        self._tear_down_cases_info = None
        self._test_cases_info = None
        self.discriminator = None

        if set_up_cases_info is not None:
            self.set_up_cases_info = set_up_cases_info
        if tear_down_cases_info is not None:
            self.tear_down_cases_info = tear_down_cases_info
        if test_cases_info is not None:
            self.test_cases_info = test_cases_info

    @property
    def set_up_cases_info(self):
        r"""Gets the set_up_cases_info of this CloudTestCaseOperationInfo.

        前置用例信息

        :return: The set_up_cases_info of this CloudTestCaseOperationInfo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.CloudTestCaseInfo`]
        """
        return self._set_up_cases_info

    @set_up_cases_info.setter
    def set_up_cases_info(self, set_up_cases_info):
        r"""Sets the set_up_cases_info of this CloudTestCaseOperationInfo.

        前置用例信息

        :param set_up_cases_info: The set_up_cases_info of this CloudTestCaseOperationInfo.
        :type set_up_cases_info: list[:class:`huaweicloudsdkcloudtest.v1.CloudTestCaseInfo`]
        """
        self._set_up_cases_info = set_up_cases_info

    @property
    def tear_down_cases_info(self):
        r"""Gets the tear_down_cases_info of this CloudTestCaseOperationInfo.

        后置用例信息

        :return: The tear_down_cases_info of this CloudTestCaseOperationInfo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.CloudTestCaseInfo`]
        """
        return self._tear_down_cases_info

    @tear_down_cases_info.setter
    def tear_down_cases_info(self, tear_down_cases_info):
        r"""Sets the tear_down_cases_info of this CloudTestCaseOperationInfo.

        后置用例信息

        :param tear_down_cases_info: The tear_down_cases_info of this CloudTestCaseOperationInfo.
        :type tear_down_cases_info: list[:class:`huaweicloudsdkcloudtest.v1.CloudTestCaseInfo`]
        """
        self._tear_down_cases_info = tear_down_cases_info

    @property
    def test_cases_info(self):
        r"""Gets the test_cases_info of this CloudTestCaseOperationInfo.

        用例信息

        :return: The test_cases_info of this CloudTestCaseOperationInfo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.CloudTestCaseInfo`]
        """
        return self._test_cases_info

    @test_cases_info.setter
    def test_cases_info(self, test_cases_info):
        r"""Sets the test_cases_info of this CloudTestCaseOperationInfo.

        用例信息

        :param test_cases_info: The test_cases_info of this CloudTestCaseOperationInfo.
        :type test_cases_info: list[:class:`huaweicloudsdkcloudtest.v1.CloudTestCaseInfo`]
        """
        self._test_cases_info = test_cases_info

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
        if not isinstance(other, CloudTestCaseOperationInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
