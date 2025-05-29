# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFactoryFullTextResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'search_details': 'list[SearchDetailV2]',
        'total_hits': 'int'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'search_details': 'search_details',
        'total_hits': 'total_hits'
    }

    def __init__(self, limit=None, offset=None, search_details=None, total_hits=None):
        r"""ShowFactoryFullTextResponse

        The model defined in huaweicloud sdk

        :param limit: 分页大小限制。 取值范围[1,100]。
        :type limit: int
        :param offset: 当前所在分页。
        :type offset: int
        :param search_details: 查询成功，返回搜索结果。
        :type search_details: list[:class:`huaweicloudsdkdataartsstudio.v1.SearchDetailV2`]
        :param total_hits: 成功命中数量。
        :type total_hits: int
        """
        
        super(ShowFactoryFullTextResponse, self).__init__()

        self._limit = None
        self._offset = None
        self._search_details = None
        self._total_hits = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if search_details is not None:
            self.search_details = search_details
        if total_hits is not None:
            self.total_hits = total_hits

    @property
    def limit(self):
        r"""Gets the limit of this ShowFactoryFullTextResponse.

        分页大小限制。 取值范围[1,100]。

        :return: The limit of this ShowFactoryFullTextResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowFactoryFullTextResponse.

        分页大小限制。 取值范围[1,100]。

        :param limit: The limit of this ShowFactoryFullTextResponse.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ShowFactoryFullTextResponse.

        当前所在分页。

        :return: The offset of this ShowFactoryFullTextResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowFactoryFullTextResponse.

        当前所在分页。

        :param offset: The offset of this ShowFactoryFullTextResponse.
        :type offset: int
        """
        self._offset = offset

    @property
    def search_details(self):
        r"""Gets the search_details of this ShowFactoryFullTextResponse.

        查询成功，返回搜索结果。

        :return: The search_details of this ShowFactoryFullTextResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.SearchDetailV2`]
        """
        return self._search_details

    @search_details.setter
    def search_details(self, search_details):
        r"""Sets the search_details of this ShowFactoryFullTextResponse.

        查询成功，返回搜索结果。

        :param search_details: The search_details of this ShowFactoryFullTextResponse.
        :type search_details: list[:class:`huaweicloudsdkdataartsstudio.v1.SearchDetailV2`]
        """
        self._search_details = search_details

    @property
    def total_hits(self):
        r"""Gets the total_hits of this ShowFactoryFullTextResponse.

        成功命中数量。

        :return: The total_hits of this ShowFactoryFullTextResponse.
        :rtype: int
        """
        return self._total_hits

    @total_hits.setter
    def total_hits(self, total_hits):
        r"""Sets the total_hits of this ShowFactoryFullTextResponse.

        成功命中数量。

        :param total_hits: The total_hits of this ShowFactoryFullTextResponse.
        :type total_hits: int
        """
        self._total_hits = total_hits

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
        if not isinstance(other, ShowFactoryFullTextResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
