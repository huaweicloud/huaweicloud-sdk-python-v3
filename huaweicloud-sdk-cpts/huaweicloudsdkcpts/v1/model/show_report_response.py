# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowReportResponse(SdkResponse):

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
        'extend': 'str',
        'result': 'ReportInfo'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message',
        'extend': 'extend',
        'result': 'result'
    }

    def __init__(self, code=None, message=None, extend=None, result=None):
        """ShowReportResponse

        The model defined in huaweicloud sdk

        :param code: code
        :type code: str
        :param message: message
        :type message: str
        :param extend: extend
        :type extend: str
        :param result: 
        :type result: :class:`huaweicloudsdkcpts.v1.ReportInfo`
        """
        
        super(ShowReportResponse, self).__init__()

        self._code = None
        self._message = None
        self._extend = None
        self._result = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if message is not None:
            self.message = message
        if extend is not None:
            self.extend = extend
        if result is not None:
            self.result = result

    @property
    def code(self):
        """Gets the code of this ShowReportResponse.

        code

        :return: The code of this ShowReportResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ShowReportResponse.

        code

        :param code: The code of this ShowReportResponse.
        :type code: str
        """
        self._code = code

    @property
    def message(self):
        """Gets the message of this ShowReportResponse.

        message

        :return: The message of this ShowReportResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ShowReportResponse.

        message

        :param message: The message of this ShowReportResponse.
        :type message: str
        """
        self._message = message

    @property
    def extend(self):
        """Gets the extend of this ShowReportResponse.

        extend

        :return: The extend of this ShowReportResponse.
        :rtype: str
        """
        return self._extend

    @extend.setter
    def extend(self, extend):
        """Sets the extend of this ShowReportResponse.

        extend

        :param extend: The extend of this ShowReportResponse.
        :type extend: str
        """
        self._extend = extend

    @property
    def result(self):
        """Gets the result of this ShowReportResponse.

        :return: The result of this ShowReportResponse.
        :rtype: :class:`huaweicloudsdkcpts.v1.ReportInfo`
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this ShowReportResponse.

        :param result: The result of this ShowReportResponse.
        :type result: :class:`huaweicloudsdkcpts.v1.ReportInfo`
        """
        self._result = result

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
        if not isinstance(other, ShowReportResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
