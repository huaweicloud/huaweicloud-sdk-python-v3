# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListContentCompareOverviewResponse(SdkResponse):

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
        'content_compare_result_infos': 'list[NodeContentCompareOverviewResult]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'content_compare_result_infos': 'content_compare_result_infos'
    }

    def __init__(self, total_count=None, content_compare_result_infos=None):
        """ListContentCompareOverviewResponse

        The model defined in huaweicloud sdk

        :param total_count: 对比数量
        :type total_count: int
        :param content_compare_result_infos: 信息列表
        :type content_compare_result_infos: list[:class:`huaweicloudsdkdrs.v3.NodeContentCompareOverviewResult`]
        """
        
        super(ListContentCompareOverviewResponse, self).__init__()

        self._total_count = None
        self._content_compare_result_infos = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if content_compare_result_infos is not None:
            self.content_compare_result_infos = content_compare_result_infos

    @property
    def total_count(self):
        """Gets the total_count of this ListContentCompareOverviewResponse.

        对比数量

        :return: The total_count of this ListContentCompareOverviewResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListContentCompareOverviewResponse.

        对比数量

        :param total_count: The total_count of this ListContentCompareOverviewResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def content_compare_result_infos(self):
        """Gets the content_compare_result_infos of this ListContentCompareOverviewResponse.

        信息列表

        :return: The content_compare_result_infos of this ListContentCompareOverviewResponse.
        :rtype: list[:class:`huaweicloudsdkdrs.v3.NodeContentCompareOverviewResult`]
        """
        return self._content_compare_result_infos

    @content_compare_result_infos.setter
    def content_compare_result_infos(self, content_compare_result_infos):
        """Sets the content_compare_result_infos of this ListContentCompareOverviewResponse.

        信息列表

        :param content_compare_result_infos: The content_compare_result_infos of this ListContentCompareOverviewResponse.
        :type content_compare_result_infos: list[:class:`huaweicloudsdkdrs.v3.NodeContentCompareOverviewResult`]
        """
        self._content_compare_result_infos = content_compare_result_infos

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
        if not isinstance(other, ListContentCompareOverviewResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
