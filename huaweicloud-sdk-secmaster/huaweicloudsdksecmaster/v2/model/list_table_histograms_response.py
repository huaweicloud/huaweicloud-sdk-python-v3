# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTableHistogramsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'histograms': 'list[SearchQueryResultHistogram]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'histograms': 'histograms'
    }

    def __init__(self, total_count=None, histograms=None):
        r"""ListTableHistogramsResponse

        The model defined in huaweicloud sdk

        :param total_count: 总数
        :type total_count: int
        :param histograms: 直方图
        :type histograms: list[:class:`huaweicloudsdksecmaster.v2.SearchQueryResultHistogram`]
        """
        
        super().__init__()

        self._total_count = None
        self._histograms = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if histograms is not None:
            self.histograms = histograms

    @property
    def total_count(self):
        r"""Gets the total_count of this ListTableHistogramsResponse.

        总数

        :return: The total_count of this ListTableHistogramsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListTableHistogramsResponse.

        总数

        :param total_count: The total_count of this ListTableHistogramsResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def histograms(self):
        r"""Gets the histograms of this ListTableHistogramsResponse.

        直方图

        :return: The histograms of this ListTableHistogramsResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v2.SearchQueryResultHistogram`]
        """
        return self._histograms

    @histograms.setter
    def histograms(self, histograms):
        r"""Sets the histograms of this ListTableHistogramsResponse.

        直方图

        :param histograms: The histograms of this ListTableHistogramsResponse.
        :type histograms: list[:class:`huaweicloudsdksecmaster.v2.SearchQueryResultHistogram`]
        """
        self._histograms = histograms

    def to_dict(self):
        import warnings
        warnings.warn("ListTableHistogramsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListTableHistogramsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
