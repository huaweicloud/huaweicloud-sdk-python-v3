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
        'status': 'str',
        'result': 'ResultValueCustomReportListVo',
        'error': 'ApiError',
        'request_id': 'str'
    }

    attribute_map = {
        'status': 'status',
        'result': 'result',
        'error': 'error',
        'request_id': 'request_id'
    }

    def __init__(self, status=None, result=None, error=None, request_id=None):
        """ShowReportResponse

        The model defined in huaweicloud sdk

        :param status: success|error
        :type status: str
        :param result: 
        :type result: :class:`huaweicloudsdkcloudtest.v1.ResultValueCustomReportListVo`
        :param error: 
        :type error: :class:`huaweicloudsdkcloudtest.v1.ApiError`
        :param request_id: 由接口调用方传入，建议使用UUID保证请求的唯一性。
        :type request_id: str
        """
        
        super(ShowReportResponse, self).__init__()

        self._status = None
        self._result = None
        self._error = None
        self._request_id = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if result is not None:
            self.result = result
        if error is not None:
            self.error = error
        if request_id is not None:
            self.request_id = request_id

    @property
    def status(self):
        """Gets the status of this ShowReportResponse.

        success|error

        :return: The status of this ShowReportResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowReportResponse.

        success|error

        :param status: The status of this ShowReportResponse.
        :type status: str
        """
        self._status = status

    @property
    def result(self):
        """Gets the result of this ShowReportResponse.

        :return: The result of this ShowReportResponse.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ResultValueCustomReportListVo`
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this ShowReportResponse.

        :param result: The result of this ShowReportResponse.
        :type result: :class:`huaweicloudsdkcloudtest.v1.ResultValueCustomReportListVo`
        """
        self._result = result

    @property
    def error(self):
        """Gets the error of this ShowReportResponse.

        :return: The error of this ShowReportResponse.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.ApiError`
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this ShowReportResponse.

        :param error: The error of this ShowReportResponse.
        :type error: :class:`huaweicloudsdkcloudtest.v1.ApiError`
        """
        self._error = error

    @property
    def request_id(self):
        """Gets the request_id of this ShowReportResponse.

        由接口调用方传入，建议使用UUID保证请求的唯一性。

        :return: The request_id of this ShowReportResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ShowReportResponse.

        由接口调用方传入，建议使用UUID保证请求的唯一性。

        :param request_id: The request_id of this ShowReportResponse.
        :type request_id: str
        """
        self._request_id = request_id

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
