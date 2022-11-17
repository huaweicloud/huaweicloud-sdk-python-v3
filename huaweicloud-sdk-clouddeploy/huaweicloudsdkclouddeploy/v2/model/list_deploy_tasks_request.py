# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDeployTasksRequest:

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
        'page': 'int',
        'size': 'int'
    }

    attribute_map = {
        'project_id': 'project_id',
        'page': 'page',
        'size': 'size'
    }

    def __init__(self, project_id=None, page=None, size=None):
        """ListDeployTasksRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目ID
        :type project_id: str
        :param page: 分页页码， 表示从此页开始查询， page大于等于1
        :type page: int
        :param size: 每页显示的条目数量，size小于等于100
        :type size: int
        """
        
        

        self._project_id = None
        self._page = None
        self._size = None
        self.discriminator = None

        self.project_id = project_id
        self.page = page
        self.size = size

    @property
    def project_id(self):
        """Gets the project_id of this ListDeployTasksRequest.

        项目ID

        :return: The project_id of this ListDeployTasksRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ListDeployTasksRequest.

        项目ID

        :param project_id: The project_id of this ListDeployTasksRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def page(self):
        """Gets the page of this ListDeployTasksRequest.

        分页页码， 表示从此页开始查询， page大于等于1

        :return: The page of this ListDeployTasksRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ListDeployTasksRequest.

        分页页码， 表示从此页开始查询， page大于等于1

        :param page: The page of this ListDeployTasksRequest.
        :type page: int
        """
        self._page = page

    @property
    def size(self):
        """Gets the size of this ListDeployTasksRequest.

        每页显示的条目数量，size小于等于100

        :return: The size of this ListDeployTasksRequest.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ListDeployTasksRequest.

        每页显示的条目数量，size小于等于100

        :param size: The size of this ListDeployTasksRequest.
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
        if not isinstance(other, ListDeployTasksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
