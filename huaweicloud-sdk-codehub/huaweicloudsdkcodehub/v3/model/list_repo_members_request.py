# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRepoMembersRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'page_index': 'int',
        'page_size': 'int',
        'repository_uuid': 'str',
        'subject': 'str'
    }

    attribute_map = {
        'page_index': 'page_index',
        'page_size': 'page_size',
        'repository_uuid': 'repository_uuid',
        'subject': 'subject'
    }

    def __init__(self, page_index=None, page_size=None, repository_uuid=None, subject=None):
        """ListRepoMembersRequest

        The model defined in huaweicloud sdk

        :param page_index: 第几页
        :type page_index: int
        :param page_size: 每页显示size
        :type page_size: int
        :param repository_uuid: 仓库uuid(由CreateRepository接口返回)
        :type repository_uuid: str
        :param subject: 搜索关键字
        :type subject: str
        """
        
        

        self._page_index = None
        self._page_size = None
        self._repository_uuid = None
        self._subject = None
        self.discriminator = None

        if page_index is not None:
            self.page_index = page_index
        if page_size is not None:
            self.page_size = page_size
        self.repository_uuid = repository_uuid
        if subject is not None:
            self.subject = subject

    @property
    def page_index(self):
        """Gets the page_index of this ListRepoMembersRequest.

        第几页

        :return: The page_index of this ListRepoMembersRequest.
        :rtype: int
        """
        return self._page_index

    @page_index.setter
    def page_index(self, page_index):
        """Sets the page_index of this ListRepoMembersRequest.

        第几页

        :param page_index: The page_index of this ListRepoMembersRequest.
        :type page_index: int
        """
        self._page_index = page_index

    @property
    def page_size(self):
        """Gets the page_size of this ListRepoMembersRequest.

        每页显示size

        :return: The page_size of this ListRepoMembersRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ListRepoMembersRequest.

        每页显示size

        :param page_size: The page_size of this ListRepoMembersRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def repository_uuid(self):
        """Gets the repository_uuid of this ListRepoMembersRequest.

        仓库uuid(由CreateRepository接口返回)

        :return: The repository_uuid of this ListRepoMembersRequest.
        :rtype: str
        """
        return self._repository_uuid

    @repository_uuid.setter
    def repository_uuid(self, repository_uuid):
        """Sets the repository_uuid of this ListRepoMembersRequest.

        仓库uuid(由CreateRepository接口返回)

        :param repository_uuid: The repository_uuid of this ListRepoMembersRequest.
        :type repository_uuid: str
        """
        self._repository_uuid = repository_uuid

    @property
    def subject(self):
        """Gets the subject of this ListRepoMembersRequest.

        搜索关键字

        :return: The subject of this ListRepoMembersRequest.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this ListRepoMembersRequest.

        搜索关键字

        :param subject: The subject of this ListRepoMembersRequest.
        :type subject: str
        """
        self._subject = subject

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
        if not isinstance(other, ListRepoMembersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
