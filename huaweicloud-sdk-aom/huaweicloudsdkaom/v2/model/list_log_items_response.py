# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLogItemsResponse(SdkResponse):

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
        'error_message': 'str',
        'result': 'str'
    }

    attribute_map = {
        'error_code': 'errorCode',
        'error_message': 'errorMessage',
        'result': 'result'
    }

    def __init__(self, error_code=None, error_message=None, result=None):
        r"""ListLogItemsResponse

        The model defined in huaweicloud sdk

        :param error_code: 响应码,SVCSTG_AMS_2000000代表正常返回。
        :type error_code: str
        :param error_message: 响应信息描述。
        :type error_message: str
        :param result: 查询结果元数据信息，包括返回总数及结果。
        :type result: str
        """
        
        super(ListLogItemsResponse, self).__init__()

        self._error_code = None
        self._error_message = None
        self._result = None
        self.discriminator = None

        if error_code is not None:
            self.error_code = error_code
        if error_message is not None:
            self.error_message = error_message
        if result is not None:
            self.result = result

    @property
    def error_code(self):
        r"""Gets the error_code of this ListLogItemsResponse.

        响应码,SVCSTG_AMS_2000000代表正常返回。

        :return: The error_code of this ListLogItemsResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this ListLogItemsResponse.

        响应码,SVCSTG_AMS_2000000代表正常返回。

        :param error_code: The error_code of this ListLogItemsResponse.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_message(self):
        r"""Gets the error_message of this ListLogItemsResponse.

        响应信息描述。

        :return: The error_message of this ListLogItemsResponse.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        r"""Sets the error_message of this ListLogItemsResponse.

        响应信息描述。

        :param error_message: The error_message of this ListLogItemsResponse.
        :type error_message: str
        """
        self._error_message = error_message

    @property
    def result(self):
        r"""Gets the result of this ListLogItemsResponse.

        查询结果元数据信息，包括返回总数及结果。

        :return: The result of this ListLogItemsResponse.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this ListLogItemsResponse.

        查询结果元数据信息，包括返回总数及结果。

        :param result: The result of this ListLogItemsResponse.
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
        if not isinstance(other, ListLogItemsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
