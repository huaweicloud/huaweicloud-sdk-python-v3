# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportCollectorParserResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'fail': 'int',
        'result': 'list[ImportParserVo]',
        'success': 'int'
    }

    attribute_map = {
        'fail': 'fail',
        'result': 'result',
        'success': 'success'
    }

    def __init__(self, fail=None, result=None, success=None):
        r"""ImportCollectorParserResponse

        The model defined in huaweicloud sdk

        :param fail: 失败的数量
        :type fail: int
        :param result: 解析器数组
        :type result: list[:class:`huaweicloudsdksecmaster.v1.ImportParserVo`]
        :param success: 成功的数量
        :type success: int
        """
        
        super().__init__()

        self._fail = None
        self._result = None
        self._success = None
        self.discriminator = None

        if fail is not None:
            self.fail = fail
        if result is not None:
            self.result = result
        if success is not None:
            self.success = success

    @property
    def fail(self):
        r"""Gets the fail of this ImportCollectorParserResponse.

        失败的数量

        :return: The fail of this ImportCollectorParserResponse.
        :rtype: int
        """
        return self._fail

    @fail.setter
    def fail(self, fail):
        r"""Sets the fail of this ImportCollectorParserResponse.

        失败的数量

        :param fail: The fail of this ImportCollectorParserResponse.
        :type fail: int
        """
        self._fail = fail

    @property
    def result(self):
        r"""Gets the result of this ImportCollectorParserResponse.

        解析器数组

        :return: The result of this ImportCollectorParserResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.ImportParserVo`]
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this ImportCollectorParserResponse.

        解析器数组

        :param result: The result of this ImportCollectorParserResponse.
        :type result: list[:class:`huaweicloudsdksecmaster.v1.ImportParserVo`]
        """
        self._result = result

    @property
    def success(self):
        r"""Gets the success of this ImportCollectorParserResponse.

        成功的数量

        :return: The success of this ImportCollectorParserResponse.
        :rtype: int
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this ImportCollectorParserResponse.

        成功的数量

        :param success: The success of this ImportCollectorParserResponse.
        :type success: int
        """
        self._success = success

    def to_dict(self):
        import warnings
        warnings.warn("ImportCollectorParserResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ImportCollectorParserResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
