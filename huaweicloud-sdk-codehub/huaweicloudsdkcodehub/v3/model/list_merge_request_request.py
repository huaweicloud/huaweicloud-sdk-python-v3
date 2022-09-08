# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMergeRequestRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'repository_id': 'int',
        'state': 'str',
        'page': 'str',
        'per_page': 'str',
        'search': 'str'
    }

    attribute_map = {
        'repository_id': 'repository_id',
        'state': 'state',
        'page': 'page',
        'per_page': 'per_page',
        'search': 'search'
    }

    def __init__(self, repository_id=None, state=None, page=None, per_page=None, search=None):
        """ListMergeRequestRequest

        The model defined in huaweicloud sdk

        :param repository_id: 仓库短id
        :type repository_id: int
        :param state: 匹配条件
        :type state: str
        :param page: 分页页数
        :type page: str
        :param per_page: 每页数据数
        :type per_page: str
        :param search: 匹配条件
        :type search: str
        """
        
        

        self._repository_id = None
        self._state = None
        self._page = None
        self._per_page = None
        self._search = None
        self.discriminator = None

        self.repository_id = repository_id
        if state is not None:
            self.state = state
        if page is not None:
            self.page = page
        if per_page is not None:
            self.per_page = per_page
        if search is not None:
            self.search = search

    @property
    def repository_id(self):
        """Gets the repository_id of this ListMergeRequestRequest.

        仓库短id

        :return: The repository_id of this ListMergeRequestRequest.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        """Sets the repository_id of this ListMergeRequestRequest.

        仓库短id

        :param repository_id: The repository_id of this ListMergeRequestRequest.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def state(self):
        """Gets the state of this ListMergeRequestRequest.

        匹配条件

        :return: The state of this ListMergeRequestRequest.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ListMergeRequestRequest.

        匹配条件

        :param state: The state of this ListMergeRequestRequest.
        :type state: str
        """
        self._state = state

    @property
    def page(self):
        """Gets the page of this ListMergeRequestRequest.

        分页页数

        :return: The page of this ListMergeRequestRequest.
        :rtype: str
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ListMergeRequestRequest.

        分页页数

        :param page: The page of this ListMergeRequestRequest.
        :type page: str
        """
        self._page = page

    @property
    def per_page(self):
        """Gets the per_page of this ListMergeRequestRequest.

        每页数据数

        :return: The per_page of this ListMergeRequestRequest.
        :rtype: str
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        """Sets the per_page of this ListMergeRequestRequest.

        每页数据数

        :param per_page: The per_page of this ListMergeRequestRequest.
        :type per_page: str
        """
        self._per_page = per_page

    @property
    def search(self):
        """Gets the search of this ListMergeRequestRequest.

        匹配条件

        :return: The search of this ListMergeRequestRequest.
        :rtype: str
        """
        return self._search

    @search.setter
    def search(self, search):
        """Sets the search of this ListMergeRequestRequest.

        匹配条件

        :param search: The search of this ListMergeRequestRequest.
        :type search: str
        """
        self._search = search

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
        if not isinstance(other, ListMergeRequestRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
