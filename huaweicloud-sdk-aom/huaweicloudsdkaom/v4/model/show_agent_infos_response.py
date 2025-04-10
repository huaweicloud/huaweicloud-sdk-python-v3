# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAgentInfosResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'page': 'int',
        'page_size': 'int',
        'total_count': 'int',
        'data_list': 'list[AgentInfoResult]'
    }

    attribute_map = {
        'page': 'page',
        'page_size': 'page_size',
        'total_count': 'total_count',
        'data_list': 'data_list'
    }

    def __init__(self, page=None, page_size=None, total_count=None, data_list=None):
        r"""ShowAgentInfosResponse

        The model defined in huaweicloud sdk

        :param page: 页码，默认1
        :type page: int
        :param page_size: 每页数量，默认20
        :type page_size: int
        :param total_count: 总数量
        :type total_count: int
        :param data_list: 主机列表信息。
        :type data_list: list[:class:`huaweicloudsdkaom.v4.AgentInfoResult`]
        """
        
        super(ShowAgentInfosResponse, self).__init__()

        self._page = None
        self._page_size = None
        self._total_count = None
        self._data_list = None
        self.discriminator = None

        if page is not None:
            self.page = page
        if page_size is not None:
            self.page_size = page_size
        if total_count is not None:
            self.total_count = total_count
        if data_list is not None:
            self.data_list = data_list

    @property
    def page(self):
        r"""Gets the page of this ShowAgentInfosResponse.

        页码，默认1

        :return: The page of this ShowAgentInfosResponse.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this ShowAgentInfosResponse.

        页码，默认1

        :param page: The page of this ShowAgentInfosResponse.
        :type page: int
        """
        self._page = page

    @property
    def page_size(self):
        r"""Gets the page_size of this ShowAgentInfosResponse.

        每页数量，默认20

        :return: The page_size of this ShowAgentInfosResponse.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ShowAgentInfosResponse.

        每页数量，默认20

        :param page_size: The page_size of this ShowAgentInfosResponse.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def total_count(self):
        r"""Gets the total_count of this ShowAgentInfosResponse.

        总数量

        :return: The total_count of this ShowAgentInfosResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ShowAgentInfosResponse.

        总数量

        :param total_count: The total_count of this ShowAgentInfosResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def data_list(self):
        r"""Gets the data_list of this ShowAgentInfosResponse.

        主机列表信息。

        :return: The data_list of this ShowAgentInfosResponse.
        :rtype: list[:class:`huaweicloudsdkaom.v4.AgentInfoResult`]
        """
        return self._data_list

    @data_list.setter
    def data_list(self, data_list):
        r"""Sets the data_list of this ShowAgentInfosResponse.

        主机列表信息。

        :param data_list: The data_list of this ShowAgentInfosResponse.
        :type data_list: list[:class:`huaweicloudsdkaom.v4.AgentInfoResult`]
        """
        self._data_list = data_list

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
        if not isinstance(other, ShowAgentInfosResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
