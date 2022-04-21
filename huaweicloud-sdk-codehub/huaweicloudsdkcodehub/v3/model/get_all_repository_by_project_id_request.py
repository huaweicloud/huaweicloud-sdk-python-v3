# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetAllRepositoryByProjectIdRequest:

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
        'project_uuid': 'str',
        'search': 'str'
    }

    attribute_map = {
        'page_index': 'page_index',
        'page_size': 'page_size',
        'project_uuid': 'project_uuid',
        'search': 'search'
    }

    def __init__(self, page_index=None, page_size=None, project_uuid=None, search=None):
        """GetAllRepositoryByProjectIdRequest

        The model defined in huaweicloud sdk

        :param page_index: 分页索引，从1开始计数
        :type page_index: int
        :param page_size: 每页条目数
        :type page_size: int
        :param project_uuid: 项目的uuid
        :type project_uuid: str
        :param search: 搜索关键字
        :type search: str
        """
        
        

        self._page_index = None
        self._page_size = None
        self._project_uuid = None
        self._search = None
        self.discriminator = None

        if page_index is not None:
            self.page_index = page_index
        if page_size is not None:
            self.page_size = page_size
        self.project_uuid = project_uuid
        if search is not None:
            self.search = search

    @property
    def page_index(self):
        """Gets the page_index of this GetAllRepositoryByProjectIdRequest.

        分页索引，从1开始计数

        :return: The page_index of this GetAllRepositoryByProjectIdRequest.
        :rtype: int
        """
        return self._page_index

    @page_index.setter
    def page_index(self, page_index):
        """Sets the page_index of this GetAllRepositoryByProjectIdRequest.

        分页索引，从1开始计数

        :param page_index: The page_index of this GetAllRepositoryByProjectIdRequest.
        :type page_index: int
        """
        self._page_index = page_index

    @property
    def page_size(self):
        """Gets the page_size of this GetAllRepositoryByProjectIdRequest.

        每页条目数

        :return: The page_size of this GetAllRepositoryByProjectIdRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this GetAllRepositoryByProjectIdRequest.

        每页条目数

        :param page_size: The page_size of this GetAllRepositoryByProjectIdRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def project_uuid(self):
        """Gets the project_uuid of this GetAllRepositoryByProjectIdRequest.

        项目的uuid

        :return: The project_uuid of this GetAllRepositoryByProjectIdRequest.
        :rtype: str
        """
        return self._project_uuid

    @project_uuid.setter
    def project_uuid(self, project_uuid):
        """Sets the project_uuid of this GetAllRepositoryByProjectIdRequest.

        项目的uuid

        :param project_uuid: The project_uuid of this GetAllRepositoryByProjectIdRequest.
        :type project_uuid: str
        """
        self._project_uuid = project_uuid

    @property
    def search(self):
        """Gets the search of this GetAllRepositoryByProjectIdRequest.

        搜索关键字

        :return: The search of this GetAllRepositoryByProjectIdRequest.
        :rtype: str
        """
        return self._search

    @search.setter
    def search(self, search):
        """Sets the search of this GetAllRepositoryByProjectIdRequest.

        搜索关键字

        :param search: The search of this GetAllRepositoryByProjectIdRequest.
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
        if not isinstance(other, GetAllRepositoryByProjectIdRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
