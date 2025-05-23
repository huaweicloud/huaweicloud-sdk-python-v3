# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHostsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'page_size': 'str',
        'current_page': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'page_size': 'pageSize',
        'current_page': 'currentPage'
    }

    def __init__(self, cluster_id=None, page_size=None, current_page=None):
        r"""ListHostsRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 集群ID。获取方法，请参见[获取集群ID](https://support.huaweicloud.com/api-mrs/mrs_02_9001.html)。
        :type cluster_id: str
        :param page_size: 分页查询每页返回的最大集群数量。 取值范围：[1～2147483646] 默认值为10。
        :type page_size: str
        :param current_page: 当前查询页码。默认值为1。
        :type current_page: str
        """
        
        

        self._cluster_id = None
        self._page_size = None
        self._current_page = None
        self.discriminator = None

        self.cluster_id = cluster_id
        if page_size is not None:
            self.page_size = page_size
        if current_page is not None:
            self.current_page = current_page

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ListHostsRequest.

        集群ID。获取方法，请参见[获取集群ID](https://support.huaweicloud.com/api-mrs/mrs_02_9001.html)。

        :return: The cluster_id of this ListHostsRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ListHostsRequest.

        集群ID。获取方法，请参见[获取集群ID](https://support.huaweicloud.com/api-mrs/mrs_02_9001.html)。

        :param cluster_id: The cluster_id of this ListHostsRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def page_size(self):
        r"""Gets the page_size of this ListHostsRequest.

        分页查询每页返回的最大集群数量。 取值范围：[1～2147483646] 默认值为10。

        :return: The page_size of this ListHostsRequest.
        :rtype: str
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ListHostsRequest.

        分页查询每页返回的最大集群数量。 取值范围：[1～2147483646] 默认值为10。

        :param page_size: The page_size of this ListHostsRequest.
        :type page_size: str
        """
        self._page_size = page_size

    @property
    def current_page(self):
        r"""Gets the current_page of this ListHostsRequest.

        当前查询页码。默认值为1。

        :return: The current_page of this ListHostsRequest.
        :rtype: str
        """
        return self._current_page

    @current_page.setter
    def current_page(self, current_page):
        r"""Sets the current_page of this ListHostsRequest.

        当前查询页码。默认值为1。

        :param current_page: The current_page of this ListHostsRequest.
        :type current_page: str
        """
        self._current_page = current_page

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
        if not isinstance(other, ListHostsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
