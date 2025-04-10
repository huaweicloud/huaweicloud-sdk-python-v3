# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchListDcDsResponse(SdkResponse):

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
        'page_info': 'PageInfoDTO',
        'datasources': 'list[QueryDcDsBriefRespDTO]'
    }

    attribute_map = {
        'count': 'count',
        'page_info': 'page_info',
        'datasources': 'datasources'
    }

    def __init__(self, count=None, page_info=None, datasources=None):
        r"""BatchListDcDsResponse

        The model defined in huaweicloud sdk

        :param count: 总记录数
        :type count: int
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkiotedge.v2.PageInfoDTO`
        :param datasources: 每页记录数
        :type datasources: list[:class:`huaweicloudsdkiotedge.v2.QueryDcDsBriefRespDTO`]
        """
        
        super(BatchListDcDsResponse, self).__init__()

        self._count = None
        self._page_info = None
        self._datasources = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if page_info is not None:
            self.page_info = page_info
        if datasources is not None:
            self.datasources = datasources

    @property
    def count(self):
        r"""Gets the count of this BatchListDcDsResponse.

        总记录数

        :return: The count of this BatchListDcDsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this BatchListDcDsResponse.

        总记录数

        :param count: The count of this BatchListDcDsResponse.
        :type count: int
        """
        self._count = count

    @property
    def page_info(self):
        r"""Gets the page_info of this BatchListDcDsResponse.

        :return: The page_info of this BatchListDcDsResponse.
        :rtype: :class:`huaweicloudsdkiotedge.v2.PageInfoDTO`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this BatchListDcDsResponse.

        :param page_info: The page_info of this BatchListDcDsResponse.
        :type page_info: :class:`huaweicloudsdkiotedge.v2.PageInfoDTO`
        """
        self._page_info = page_info

    @property
    def datasources(self):
        r"""Gets the datasources of this BatchListDcDsResponse.

        每页记录数

        :return: The datasources of this BatchListDcDsResponse.
        :rtype: list[:class:`huaweicloudsdkiotedge.v2.QueryDcDsBriefRespDTO`]
        """
        return self._datasources

    @datasources.setter
    def datasources(self, datasources):
        r"""Sets the datasources of this BatchListDcDsResponse.

        每页记录数

        :param datasources: The datasources of this BatchListDcDsResponse.
        :type datasources: list[:class:`huaweicloudsdkiotedge.v2.QueryDcDsBriefRespDTO`]
        """
        self._datasources = datasources

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
        if not isinstance(other, BatchListDcDsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
