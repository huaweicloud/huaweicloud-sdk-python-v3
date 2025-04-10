# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunGetFileTranslationResultResponse(SdkResponse):

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
        'url': 'str',
        'error_code': 'str',
        'error_msg': 'str'
    }

    attribute_map = {
        'status': 'status',
        'url': 'url',
        'error_code': 'error_code',
        'error_msg': 'error_msg'
    }

    def __init__(self, status=None, url=None, error_code=None, error_msg=None):
        r"""RunGetFileTranslationResultResponse

        The model defined in huaweicloud sdk

        :param status: 当前翻译状态。具体状态如下所示： WAITING 等待翻译。 FINISHED 翻译已经完成。 ERROR 翻译过程中发生错误。 调用失败时无此字段。
        :type status: str
        :param url: 临时url，用于获取翻译结果，有效期十分钟。过期后请再次调用接口获取新的url。调用失败时或翻译状态非FINISHED时无此字段。
        :type url: str
        :param error_code: 调用失败时的错误码，具体请参见错误码。调用成功时无此字段。
        :type error_code: str
        :param error_msg: 调用失败时的错误信息。调用成功时无此字段。
        :type error_msg: str
        """
        
        super(RunGetFileTranslationResultResponse, self).__init__()

        self._status = None
        self._url = None
        self._error_code = None
        self._error_msg = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if url is not None:
            self.url = url
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def status(self):
        r"""Gets the status of this RunGetFileTranslationResultResponse.

        当前翻译状态。具体状态如下所示： WAITING 等待翻译。 FINISHED 翻译已经完成。 ERROR 翻译过程中发生错误。 调用失败时无此字段。

        :return: The status of this RunGetFileTranslationResultResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this RunGetFileTranslationResultResponse.

        当前翻译状态。具体状态如下所示： WAITING 等待翻译。 FINISHED 翻译已经完成。 ERROR 翻译过程中发生错误。 调用失败时无此字段。

        :param status: The status of this RunGetFileTranslationResultResponse.
        :type status: str
        """
        self._status = status

    @property
    def url(self):
        r"""Gets the url of this RunGetFileTranslationResultResponse.

        临时url，用于获取翻译结果，有效期十分钟。过期后请再次调用接口获取新的url。调用失败时或翻译状态非FINISHED时无此字段。

        :return: The url of this RunGetFileTranslationResultResponse.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this RunGetFileTranslationResultResponse.

        临时url，用于获取翻译结果，有效期十分钟。过期后请再次调用接口获取新的url。调用失败时或翻译状态非FINISHED时无此字段。

        :param url: The url of this RunGetFileTranslationResultResponse.
        :type url: str
        """
        self._url = url

    @property
    def error_code(self):
        r"""Gets the error_code of this RunGetFileTranslationResultResponse.

        调用失败时的错误码，具体请参见错误码。调用成功时无此字段。

        :return: The error_code of this RunGetFileTranslationResultResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this RunGetFileTranslationResultResponse.

        调用失败时的错误码，具体请参见错误码。调用成功时无此字段。

        :param error_code: The error_code of this RunGetFileTranslationResultResponse.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        r"""Gets the error_msg of this RunGetFileTranslationResultResponse.

        调用失败时的错误信息。调用成功时无此字段。

        :return: The error_msg of this RunGetFileTranslationResultResponse.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this RunGetFileTranslationResultResponse.

        调用失败时的错误信息。调用成功时无此字段。

        :param error_msg: The error_msg of this RunGetFileTranslationResultResponse.
        :type error_msg: str
        """
        self._error_msg = error_msg

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
        if not isinstance(other, RunGetFileTranslationResultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
