# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRelatedCommitsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'repository_uuid': 'str',
        'type': 'int',
        'search': 'str',
        'page': 'int',
        'per_page': 'int'
    }

    attribute_map = {
        'repository_uuid': 'repository_uuid',
        'type': 'type',
        'search': 'search',
        'page': 'page',
        'per_page': 'per_page'
    }

    def __init__(self, repository_uuid=None, type=None, search=None, page=None, per_page=None):
        r"""ListRelatedCommitsRequest

        The model defined in huaweicloud sdk

        :param repository_uuid: 仓库长id
        :type repository_uuid: str
        :param type: 关联工作项类型
        :type type: int
        :param search: 查询关键字
        :type search: str
        :param page: 页码
        :type page: int
        :param per_page: 每页数量
        :type per_page: int
        """
        
        

        self._repository_uuid = None
        self._type = None
        self._search = None
        self._page = None
        self._per_page = None
        self.discriminator = None

        self.repository_uuid = repository_uuid
        if type is not None:
            self.type = type
        if search is not None:
            self.search = search
        if page is not None:
            self.page = page
        if per_page is not None:
            self.per_page = per_page

    @property
    def repository_uuid(self):
        r"""Gets the repository_uuid of this ListRelatedCommitsRequest.

        仓库长id

        :return: The repository_uuid of this ListRelatedCommitsRequest.
        :rtype: str
        """
        return self._repository_uuid

    @repository_uuid.setter
    def repository_uuid(self, repository_uuid):
        r"""Sets the repository_uuid of this ListRelatedCommitsRequest.

        仓库长id

        :param repository_uuid: The repository_uuid of this ListRelatedCommitsRequest.
        :type repository_uuid: str
        """
        self._repository_uuid = repository_uuid

    @property
    def type(self):
        r"""Gets the type of this ListRelatedCommitsRequest.

        关联工作项类型

        :return: The type of this ListRelatedCommitsRequest.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListRelatedCommitsRequest.

        关联工作项类型

        :param type: The type of this ListRelatedCommitsRequest.
        :type type: int
        """
        self._type = type

    @property
    def search(self):
        r"""Gets the search of this ListRelatedCommitsRequest.

        查询关键字

        :return: The search of this ListRelatedCommitsRequest.
        :rtype: str
        """
        return self._search

    @search.setter
    def search(self, search):
        r"""Sets the search of this ListRelatedCommitsRequest.

        查询关键字

        :param search: The search of this ListRelatedCommitsRequest.
        :type search: str
        """
        self._search = search

    @property
    def page(self):
        r"""Gets the page of this ListRelatedCommitsRequest.

        页码

        :return: The page of this ListRelatedCommitsRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this ListRelatedCommitsRequest.

        页码

        :param page: The page of this ListRelatedCommitsRequest.
        :type page: int
        """
        self._page = page

    @property
    def per_page(self):
        r"""Gets the per_page of this ListRelatedCommitsRequest.

        每页数量

        :return: The per_page of this ListRelatedCommitsRequest.
        :rtype: int
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        r"""Sets the per_page of this ListRelatedCommitsRequest.

        每页数量

        :param per_page: The per_page of this ListRelatedCommitsRequest.
        :type per_page: int
        """
        self._per_page = per_page

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
        if not isinstance(other, ListRelatedCommitsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
