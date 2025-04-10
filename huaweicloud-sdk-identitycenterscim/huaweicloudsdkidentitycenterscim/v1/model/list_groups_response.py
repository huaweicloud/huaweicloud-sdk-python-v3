# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGroupsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_results': 'int',
        'items_per_page': 'int',
        'start_index': 'str',
        'schemas': 'list[str]',
        'resources': 'list[GetGroupResp]'
    }

    attribute_map = {
        'total_results': 'totalResults',
        'items_per_page': 'itemsPerPage',
        'start_index': 'startIndex',
        'schemas': 'schemas',
        'resources': 'Resources'
    }

    def __init__(self, total_results=None, items_per_page=None, start_index=None, schemas=None, resources=None):
        r"""ListGroupsResponse

        The model defined in huaweicloud sdk

        :param total_results: 总结果数
        :type total_results: int
        :param items_per_page: 每页的元素个数
        :type items_per_page: int
        :param start_index: 起始索引
        :type start_index: str
        :param schemas: 概要
        :type schemas: list[str]
        :param resources: 包含用户组信息的列表
        :type resources: list[:class:`huaweicloudsdkidentitycenterscim.v1.GetGroupResp`]
        """
        
        super(ListGroupsResponse, self).__init__()

        self._total_results = None
        self._items_per_page = None
        self._start_index = None
        self._schemas = None
        self._resources = None
        self.discriminator = None

        if total_results is not None:
            self.total_results = total_results
        if items_per_page is not None:
            self.items_per_page = items_per_page
        if start_index is not None:
            self.start_index = start_index
        if schemas is not None:
            self.schemas = schemas
        if resources is not None:
            self.resources = resources

    @property
    def total_results(self):
        r"""Gets the total_results of this ListGroupsResponse.

        总结果数

        :return: The total_results of this ListGroupsResponse.
        :rtype: int
        """
        return self._total_results

    @total_results.setter
    def total_results(self, total_results):
        r"""Sets the total_results of this ListGroupsResponse.

        总结果数

        :param total_results: The total_results of this ListGroupsResponse.
        :type total_results: int
        """
        self._total_results = total_results

    @property
    def items_per_page(self):
        r"""Gets the items_per_page of this ListGroupsResponse.

        每页的元素个数

        :return: The items_per_page of this ListGroupsResponse.
        :rtype: int
        """
        return self._items_per_page

    @items_per_page.setter
    def items_per_page(self, items_per_page):
        r"""Sets the items_per_page of this ListGroupsResponse.

        每页的元素个数

        :param items_per_page: The items_per_page of this ListGroupsResponse.
        :type items_per_page: int
        """
        self._items_per_page = items_per_page

    @property
    def start_index(self):
        r"""Gets the start_index of this ListGroupsResponse.

        起始索引

        :return: The start_index of this ListGroupsResponse.
        :rtype: str
        """
        return self._start_index

    @start_index.setter
    def start_index(self, start_index):
        r"""Sets the start_index of this ListGroupsResponse.

        起始索引

        :param start_index: The start_index of this ListGroupsResponse.
        :type start_index: str
        """
        self._start_index = start_index

    @property
    def schemas(self):
        r"""Gets the schemas of this ListGroupsResponse.

        概要

        :return: The schemas of this ListGroupsResponse.
        :rtype: list[str]
        """
        return self._schemas

    @schemas.setter
    def schemas(self, schemas):
        r"""Sets the schemas of this ListGroupsResponse.

        概要

        :param schemas: The schemas of this ListGroupsResponse.
        :type schemas: list[str]
        """
        self._schemas = schemas

    @property
    def resources(self):
        r"""Gets the resources of this ListGroupsResponse.

        包含用户组信息的列表

        :return: The resources of this ListGroupsResponse.
        :rtype: list[:class:`huaweicloudsdkidentitycenterscim.v1.GetGroupResp`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this ListGroupsResponse.

        包含用户组信息的列表

        :param resources: The resources of this ListGroupsResponse.
        :type resources: list[:class:`huaweicloudsdkidentitycenterscim.v1.GetGroupResp`]
        """
        self._resources = resources

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
        if not isinstance(other, ListGroupsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
