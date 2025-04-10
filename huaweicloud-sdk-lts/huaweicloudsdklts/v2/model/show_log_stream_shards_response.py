# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowLogStreamShardsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'error_code': 'str',
        'is_query_complete': 'bool',
        'result': 'str'
    }

    attribute_map = {
        'error_code': 'errorCode',
        'is_query_complete': 'isQueryComplete',
        'result': 'result'
    }

    def __init__(self, error_code=None, is_query_complete=None, result=None):
        r"""ShowLogStreamShardsResponse

        The model defined in huaweicloud sdk

        :param error_code: 错误码
        :type error_code: str
        :param is_query_complete: 是否完全查询
        :type is_query_complete: bool
        :param result: 查询结果
        :type result: str
        """
        
        super(ShowLogStreamShardsResponse, self).__init__()

        self._error_code = None
        self._is_query_complete = None
        self._result = None
        self.discriminator = None

        if error_code is not None:
            self.error_code = error_code
        if is_query_complete is not None:
            self.is_query_complete = is_query_complete
        if result is not None:
            self.result = result

    @property
    def error_code(self):
        r"""Gets the error_code of this ShowLogStreamShardsResponse.

        错误码

        :return: The error_code of this ShowLogStreamShardsResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this ShowLogStreamShardsResponse.

        错误码

        :param error_code: The error_code of this ShowLogStreamShardsResponse.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def is_query_complete(self):
        r"""Gets the is_query_complete of this ShowLogStreamShardsResponse.

        是否完全查询

        :return: The is_query_complete of this ShowLogStreamShardsResponse.
        :rtype: bool
        """
        return self._is_query_complete

    @is_query_complete.setter
    def is_query_complete(self, is_query_complete):
        r"""Sets the is_query_complete of this ShowLogStreamShardsResponse.

        是否完全查询

        :param is_query_complete: The is_query_complete of this ShowLogStreamShardsResponse.
        :type is_query_complete: bool
        """
        self._is_query_complete = is_query_complete

    @property
    def result(self):
        r"""Gets the result of this ShowLogStreamShardsResponse.

        查询结果

        :return: The result of this ShowLogStreamShardsResponse.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this ShowLogStreamShardsResponse.

        查询结果

        :param result: The result of this ShowLogStreamShardsResponse.
        :type result: str
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
        if not isinstance(other, ShowLogStreamShardsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
