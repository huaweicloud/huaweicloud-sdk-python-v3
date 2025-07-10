# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListIssueFieldsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'category_id': 'str',
        'page': 'int',
        'size': 'int'
    }

    attribute_map = {
        'project_id': 'project_id',
        'category_id': 'category_id',
        'page': 'page',
        'size': 'size'
    }

    def __init__(self, project_id=None, category_id=None, page=None, size=None):
        r"""ListIssueFieldsRequest

        The model defined in huaweicloud sdk

        :param project_id: devcloud项目的32位id
        :type project_id: str
        :param category_id: 工作项类型5位id
        :type category_id: str
        :param page: 页码
        :type page: int
        :param size: 每页查询数据数量
        :type size: int
        """
        
        

        self._project_id = None
        self._category_id = None
        self._page = None
        self._size = None
        self.discriminator = None

        self.project_id = project_id
        self.category_id = category_id
        self.page = page
        self.size = size

    @property
    def project_id(self):
        r"""Gets the project_id of this ListIssueFieldsRequest.

        devcloud项目的32位id

        :return: The project_id of this ListIssueFieldsRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListIssueFieldsRequest.

        devcloud项目的32位id

        :param project_id: The project_id of this ListIssueFieldsRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def category_id(self):
        r"""Gets the category_id of this ListIssueFieldsRequest.

        工作项类型5位id

        :return: The category_id of this ListIssueFieldsRequest.
        :rtype: str
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        r"""Sets the category_id of this ListIssueFieldsRequest.

        工作项类型5位id

        :param category_id: The category_id of this ListIssueFieldsRequest.
        :type category_id: str
        """
        self._category_id = category_id

    @property
    def page(self):
        r"""Gets the page of this ListIssueFieldsRequest.

        页码

        :return: The page of this ListIssueFieldsRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this ListIssueFieldsRequest.

        页码

        :param page: The page of this ListIssueFieldsRequest.
        :type page: int
        """
        self._page = page

    @property
    def size(self):
        r"""Gets the size of this ListIssueFieldsRequest.

        每页查询数据数量

        :return: The size of this ListIssueFieldsRequest.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ListIssueFieldsRequest.

        每页查询数据数量

        :param size: The size of this ListIssueFieldsRequest.
        :type size: int
        """
        self._size = size

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
        if not isinstance(other, ListIssueFieldsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
