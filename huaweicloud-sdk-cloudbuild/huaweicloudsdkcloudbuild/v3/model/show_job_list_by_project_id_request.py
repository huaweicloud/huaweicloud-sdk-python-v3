# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJobListByProjectIdRequest:

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
        'page_index': 'int',
        'page_size': 'int'
    }

    attribute_map = {
        'project_id': 'project_id',
        'page_index': 'page_index',
        'page_size': 'page_size'
    }

    def __init__(self, project_id=None, page_index=None, page_size=None):
        """ShowJobListByProjectIdRequest

        The model defined in huaweicloud sdk

        :param project_id: DevCloud项目ID，32位数字、小写字母组合。[查询项目列表](https://support.huaweicloud.com/api-projectman/ListProjectsV4.html)
        :type project_id: str
        :param page_index: 分页页码， 表示从此页开始查询， page_index大于等于0
        :type page_index: int
        :param page_size: 每页显示的条目数量，page_size小于等于100
        :type page_size: int
        """
        
        

        self._project_id = None
        self._page_index = None
        self._page_size = None
        self.discriminator = None

        self.project_id = project_id
        self.page_index = page_index
        self.page_size = page_size

    @property
    def project_id(self):
        """Gets the project_id of this ShowJobListByProjectIdRequest.

        DevCloud项目ID，32位数字、小写字母组合。[查询项目列表](https://support.huaweicloud.com/api-projectman/ListProjectsV4.html)

        :return: The project_id of this ShowJobListByProjectIdRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ShowJobListByProjectIdRequest.

        DevCloud项目ID，32位数字、小写字母组合。[查询项目列表](https://support.huaweicloud.com/api-projectman/ListProjectsV4.html)

        :param project_id: The project_id of this ShowJobListByProjectIdRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def page_index(self):
        """Gets the page_index of this ShowJobListByProjectIdRequest.

        分页页码， 表示从此页开始查询， page_index大于等于0

        :return: The page_index of this ShowJobListByProjectIdRequest.
        :rtype: int
        """
        return self._page_index

    @page_index.setter
    def page_index(self, page_index):
        """Sets the page_index of this ShowJobListByProjectIdRequest.

        分页页码， 表示从此页开始查询， page_index大于等于0

        :param page_index: The page_index of this ShowJobListByProjectIdRequest.
        :type page_index: int
        """
        self._page_index = page_index

    @property
    def page_size(self):
        """Gets the page_size of this ShowJobListByProjectIdRequest.

        每页显示的条目数量，page_size小于等于100

        :return: The page_size of this ShowJobListByProjectIdRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ShowJobListByProjectIdRequest.

        每页显示的条目数量，page_size小于等于100

        :param page_size: The page_size of this ShowJobListByProjectIdRequest.
        :type page_size: int
        """
        self._page_size = page_size

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
        if not isinstance(other, ShowJobListByProjectIdRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
