# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTaskCasesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code': 'str',
        'message': 'str',
        'test_cases': 'list[TestCaseBriefInfo]'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message',
        'test_cases': 'test_cases'
    }

    def __init__(self, code=None, message=None, test_cases=None):
        """ListTaskCasesResponse

        The model defined in huaweicloud sdk

        :param code: 响应码
        :type code: str
        :param message: 响应消息
        :type message: str
        :param test_cases: 用例列表
        :type test_cases: list[:class:`huaweicloudsdkcpts.v1.TestCaseBriefInfo`]
        """
        
        super(ListTaskCasesResponse, self).__init__()

        self._code = None
        self._message = None
        self._test_cases = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if message is not None:
            self.message = message
        if test_cases is not None:
            self.test_cases = test_cases

    @property
    def code(self):
        """Gets the code of this ListTaskCasesResponse.

        响应码

        :return: The code of this ListTaskCasesResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ListTaskCasesResponse.

        响应码

        :param code: The code of this ListTaskCasesResponse.
        :type code: str
        """
        self._code = code

    @property
    def message(self):
        """Gets the message of this ListTaskCasesResponse.

        响应消息

        :return: The message of this ListTaskCasesResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ListTaskCasesResponse.

        响应消息

        :param message: The message of this ListTaskCasesResponse.
        :type message: str
        """
        self._message = message

    @property
    def test_cases(self):
        """Gets the test_cases of this ListTaskCasesResponse.

        用例列表

        :return: The test_cases of this ListTaskCasesResponse.
        :rtype: list[:class:`huaweicloudsdkcpts.v1.TestCaseBriefInfo`]
        """
        return self._test_cases

    @test_cases.setter
    def test_cases(self, test_cases):
        """Sets the test_cases of this ListTaskCasesResponse.

        用例列表

        :param test_cases: The test_cases of this ListTaskCasesResponse.
        :type test_cases: list[:class:`huaweicloudsdkcpts.v1.TestCaseBriefInfo`]
        """
        self._test_cases = test_cases

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
        if not isinstance(other, ListTaskCasesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
