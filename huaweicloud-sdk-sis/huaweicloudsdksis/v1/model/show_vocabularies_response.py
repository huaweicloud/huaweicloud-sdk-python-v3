# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowVocabulariesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'result': 'list[VocabInfo]'
    }

    attribute_map = {
        'count': 'count',
        'result': 'result'
    }

    def __init__(self, count=None, result=None):
        r"""ShowVocabulariesResponse

        The model defined in huaweicloud sdk

        :param count: 热词表数。
        :type count: int
        :param result: 调用成功返回热词表列表，调用失败时无此字段。
        :type result: list[:class:`huaweicloudsdksis.v1.VocabInfo`]
        """
        
        super().__init__()

        self._count = None
        self._result = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if result is not None:
            self.result = result

    @property
    def count(self):
        r"""Gets the count of this ShowVocabulariesResponse.

        热词表数。

        :return: The count of this ShowVocabulariesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ShowVocabulariesResponse.

        热词表数。

        :param count: The count of this ShowVocabulariesResponse.
        :type count: int
        """
        self._count = count

    @property
    def result(self):
        r"""Gets the result of this ShowVocabulariesResponse.

        调用成功返回热词表列表，调用失败时无此字段。

        :return: The result of this ShowVocabulariesResponse.
        :rtype: list[:class:`huaweicloudsdksis.v1.VocabInfo`]
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this ShowVocabulariesResponse.

        调用成功返回热词表列表，调用失败时无此字段。

        :param result: The result of this ShowVocabulariesResponse.
        :type result: list[:class:`huaweicloudsdksis.v1.VocabInfo`]
        """
        self._result = result

    def to_dict(self):
        import warnings
        warnings.warn("ShowVocabulariesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowVocabulariesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
