# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSearchHistogramsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'histograms': 'list[Histogram]',
        'total_count': 'int'
    }

    attribute_map = {
        'histograms': 'histograms',
        'total_count': 'total_count'
    }

    def __init__(self, histograms=None, total_count=None):
        r"""ListSearchHistogramsResponse

        The model defined in huaweicloud sdk

        :param histograms: 直方图
        :type histograms: list[:class:`huaweicloudsdksecmaster.v1.Histogram`]
        :param total_count: 数据总条数
        :type total_count: int
        """
        
        super().__init__()

        self._histograms = None
        self._total_count = None
        self.discriminator = None

        if histograms is not None:
            self.histograms = histograms
        if total_count is not None:
            self.total_count = total_count

    @property
    def histograms(self):
        r"""Gets the histograms of this ListSearchHistogramsResponse.

        直方图

        :return: The histograms of this ListSearchHistogramsResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.Histogram`]
        """
        return self._histograms

    @histograms.setter
    def histograms(self, histograms):
        r"""Sets the histograms of this ListSearchHistogramsResponse.

        直方图

        :param histograms: The histograms of this ListSearchHistogramsResponse.
        :type histograms: list[:class:`huaweicloudsdksecmaster.v1.Histogram`]
        """
        self._histograms = histograms

    @property
    def total_count(self):
        r"""Gets the total_count of this ListSearchHistogramsResponse.

        数据总条数

        :return: The total_count of this ListSearchHistogramsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListSearchHistogramsResponse.

        数据总条数

        :param total_count: The total_count of this ListSearchHistogramsResponse.
        :type total_count: int
        """
        self._total_count = total_count

    def to_dict(self):
        import warnings
        warnings.warn("ListSearchHistogramsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListSearchHistogramsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
