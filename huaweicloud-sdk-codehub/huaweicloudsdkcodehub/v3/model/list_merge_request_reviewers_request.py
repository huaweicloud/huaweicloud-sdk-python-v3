# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMergeRequestReviewersRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'repository_id': 'str',
        'merge_request_iid': 'int',
        'page': 'int',
        'per_page': 'int'
    }

    attribute_map = {
        'repository_id': 'repository_id',
        'merge_request_iid': 'merge_request_iid',
        'page': 'page',
        'per_page': 'per_page'
    }

    def __init__(self, repository_id=None, merge_request_iid=None, page=None, per_page=None):
        r"""ListMergeRequestReviewersRequest

        The model defined in huaweicloud sdk

        :param repository_id: 仓库的主键id
        :type repository_id: str
        :param merge_request_iid: 合并请求的短id
        :type merge_request_iid: int
        :param page: 页码
        :type page: int
        :param per_page: 每页条数
        :type per_page: int
        """
        
        

        self._repository_id = None
        self._merge_request_iid = None
        self._page = None
        self._per_page = None
        self.discriminator = None

        self.repository_id = repository_id
        self.merge_request_iid = merge_request_iid
        if page is not None:
            self.page = page
        if per_page is not None:
            self.per_page = per_page

    @property
    def repository_id(self):
        r"""Gets the repository_id of this ListMergeRequestReviewersRequest.

        仓库的主键id

        :return: The repository_id of this ListMergeRequestReviewersRequest.
        :rtype: str
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this ListMergeRequestReviewersRequest.

        仓库的主键id

        :param repository_id: The repository_id of this ListMergeRequestReviewersRequest.
        :type repository_id: str
        """
        self._repository_id = repository_id

    @property
    def merge_request_iid(self):
        r"""Gets the merge_request_iid of this ListMergeRequestReviewersRequest.

        合并请求的短id

        :return: The merge_request_iid of this ListMergeRequestReviewersRequest.
        :rtype: int
        """
        return self._merge_request_iid

    @merge_request_iid.setter
    def merge_request_iid(self, merge_request_iid):
        r"""Sets the merge_request_iid of this ListMergeRequestReviewersRequest.

        合并请求的短id

        :param merge_request_iid: The merge_request_iid of this ListMergeRequestReviewersRequest.
        :type merge_request_iid: int
        """
        self._merge_request_iid = merge_request_iid

    @property
    def page(self):
        r"""Gets the page of this ListMergeRequestReviewersRequest.

        页码

        :return: The page of this ListMergeRequestReviewersRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this ListMergeRequestReviewersRequest.

        页码

        :param page: The page of this ListMergeRequestReviewersRequest.
        :type page: int
        """
        self._page = page

    @property
    def per_page(self):
        r"""Gets the per_page of this ListMergeRequestReviewersRequest.

        每页条数

        :return: The per_page of this ListMergeRequestReviewersRequest.
        :rtype: int
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        r"""Sets the per_page of this ListMergeRequestReviewersRequest.

        每页条数

        :param per_page: The per_page of this ListMergeRequestReviewersRequest.
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
        if not isinstance(other, ListMergeRequestReviewersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
