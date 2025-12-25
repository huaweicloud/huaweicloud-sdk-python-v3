# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAnalysisScriptsResponse(SdkResponse):

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
        'records': 'list[AnalysisScript]'
    }

    attribute_map = {
        'count': 'count',
        'records': 'records'
    }

    def __init__(self, count=None, records=None):
        r"""ListAnalysisScriptsResponse

        The model defined in huaweicloud sdk

        :param count: 计数
        :type count: int
        :param records: 分析脚本
        :type records: list[:class:`huaweicloudsdksecmaster.v2.AnalysisScript`]
        """
        
        super().__init__()

        self._count = None
        self._records = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if records is not None:
            self.records = records

    @property
    def count(self):
        r"""Gets the count of this ListAnalysisScriptsResponse.

        计数

        :return: The count of this ListAnalysisScriptsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListAnalysisScriptsResponse.

        计数

        :param count: The count of this ListAnalysisScriptsResponse.
        :type count: int
        """
        self._count = count

    @property
    def records(self):
        r"""Gets the records of this ListAnalysisScriptsResponse.

        分析脚本

        :return: The records of this ListAnalysisScriptsResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v2.AnalysisScript`]
        """
        return self._records

    @records.setter
    def records(self, records):
        r"""Sets the records of this ListAnalysisScriptsResponse.

        分析脚本

        :param records: The records of this ListAnalysisScriptsResponse.
        :type records: list[:class:`huaweicloudsdksecmaster.v2.AnalysisScript`]
        """
        self._records = records

    def to_dict(self):
        import warnings
        warnings.warn("ListAnalysisScriptsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListAnalysisScriptsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
