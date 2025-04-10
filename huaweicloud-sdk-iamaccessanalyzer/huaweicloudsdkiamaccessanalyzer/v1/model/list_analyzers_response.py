# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAnalyzersResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'analyzers': 'list[AnalyzerSummary]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'analyzers': 'analyzers',
        'page_info': 'page_info'
    }

    def __init__(self, analyzers=None, page_info=None):
        r"""ListAnalyzersResponse

        The model defined in huaweicloud sdk

        :param analyzers: 分析器列表信息。
        :type analyzers: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.AnalyzerSummary`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkiamaccessanalyzer.v1.PageInfo`
        """
        
        super(ListAnalyzersResponse, self).__init__()

        self._analyzers = None
        self._page_info = None
        self.discriminator = None

        if analyzers is not None:
            self.analyzers = analyzers
        if page_info is not None:
            self.page_info = page_info

    @property
    def analyzers(self):
        r"""Gets the analyzers of this ListAnalyzersResponse.

        分析器列表信息。

        :return: The analyzers of this ListAnalyzersResponse.
        :rtype: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.AnalyzerSummary`]
        """
        return self._analyzers

    @analyzers.setter
    def analyzers(self, analyzers):
        r"""Sets the analyzers of this ListAnalyzersResponse.

        分析器列表信息。

        :param analyzers: The analyzers of this ListAnalyzersResponse.
        :type analyzers: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.AnalyzerSummary`]
        """
        self._analyzers = analyzers

    @property
    def page_info(self):
        r"""Gets the page_info of this ListAnalyzersResponse.

        :return: The page_info of this ListAnalyzersResponse.
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListAnalyzersResponse.

        :param page_info: The page_info of this ListAnalyzersResponse.
        :type page_info: :class:`huaweicloudsdkiamaccessanalyzer.v1.PageInfo`
        """
        self._page_info = page_info

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
        if not isinstance(other, ListAnalyzersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
