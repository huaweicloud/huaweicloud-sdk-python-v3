# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCaseResponse(SdkResponse):

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
        'test_case': 'CaseInfoDetail'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message',
        'test_case': 'test_case'
    }

    def __init__(self, code=None, message=None, test_case=None):
        r"""ShowCaseResponse

        The model defined in huaweicloud sdk

        :param code: 响应码
        :type code: str
        :param message: 响应消息
        :type message: str
        :param test_case: 
        :type test_case: :class:`huaweicloudsdkcpts.v1.CaseInfoDetail`
        """
        
        super(ShowCaseResponse, self).__init__()

        self._code = None
        self._message = None
        self._test_case = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if message is not None:
            self.message = message
        if test_case is not None:
            self.test_case = test_case

    @property
    def code(self):
        r"""Gets the code of this ShowCaseResponse.

        响应码

        :return: The code of this ShowCaseResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this ShowCaseResponse.

        响应码

        :param code: The code of this ShowCaseResponse.
        :type code: str
        """
        self._code = code

    @property
    def message(self):
        r"""Gets the message of this ShowCaseResponse.

        响应消息

        :return: The message of this ShowCaseResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ShowCaseResponse.

        响应消息

        :param message: The message of this ShowCaseResponse.
        :type message: str
        """
        self._message = message

    @property
    def test_case(self):
        r"""Gets the test_case of this ShowCaseResponse.

        :return: The test_case of this ShowCaseResponse.
        :rtype: :class:`huaweicloudsdkcpts.v1.CaseInfoDetail`
        """
        return self._test_case

    @test_case.setter
    def test_case(self, test_case):
        r"""Sets the test_case of this ShowCaseResponse.

        :param test_case: The test_case of this ShowCaseResponse.
        :type test_case: :class:`huaweicloudsdkcpts.v1.CaseInfoDetail`
        """
        self._test_case = test_case

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
        if not isinstance(other, ShowCaseResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
