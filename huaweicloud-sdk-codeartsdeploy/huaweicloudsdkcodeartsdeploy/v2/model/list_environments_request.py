# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEnvironmentsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'application_id': 'str',
        'project_id': 'str',
        'page_index': 'int',
        'page_size': 'int',
        'name': 'str',
        'sort_key': 'str',
        'sort_dir': 'str'
    }

    attribute_map = {
        'application_id': 'application_id',
        'project_id': 'project_id',
        'page_index': 'page_index',
        'page_size': 'page_size',
        'name': 'name',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir'
    }

    def __init__(self, application_id=None, project_id=None, page_index=None, page_size=None, name=None, sort_key=None, sort_dir=None):
        r"""ListEnvironmentsRequest

        The model defined in huaweicloud sdk

        :param application_id: 应用id
        :type application_id: str
        :param project_id: 项目id
        :type project_id: str
        :param page_index: 分页页码， 表示从此页开始查询， page大于等于1
        :type page_index: int
        :param page_size: 每页显示的条目数量，size小于等于100
        :type page_size: int
        :param name: 要查询的环境名称
        :type name: str
        :param sort_key: 排序字段，支持按照环境名称|用户名称|创建时间|用户昵称排序
        :type sort_key: str
        :param sort_dir: 排序顺序，DESC降序，ASC升序
        :type sort_dir: str
        """
        
        

        self._application_id = None
        self._project_id = None
        self._page_index = None
        self._page_size = None
        self._name = None
        self._sort_key = None
        self._sort_dir = None
        self.discriminator = None

        self.application_id = application_id
        self.project_id = project_id
        if page_index is not None:
            self.page_index = page_index
        if page_size is not None:
            self.page_size = page_size
        if name is not None:
            self.name = name
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir

    @property
    def application_id(self):
        r"""Gets the application_id of this ListEnvironmentsRequest.

        应用id

        :return: The application_id of this ListEnvironmentsRequest.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        r"""Sets the application_id of this ListEnvironmentsRequest.

        应用id

        :param application_id: The application_id of this ListEnvironmentsRequest.
        :type application_id: str
        """
        self._application_id = application_id

    @property
    def project_id(self):
        r"""Gets the project_id of this ListEnvironmentsRequest.

        项目id

        :return: The project_id of this ListEnvironmentsRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListEnvironmentsRequest.

        项目id

        :param project_id: The project_id of this ListEnvironmentsRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def page_index(self):
        r"""Gets the page_index of this ListEnvironmentsRequest.

        分页页码， 表示从此页开始查询， page大于等于1

        :return: The page_index of this ListEnvironmentsRequest.
        :rtype: int
        """
        return self._page_index

    @page_index.setter
    def page_index(self, page_index):
        r"""Sets the page_index of this ListEnvironmentsRequest.

        分页页码， 表示从此页开始查询， page大于等于1

        :param page_index: The page_index of this ListEnvironmentsRequest.
        :type page_index: int
        """
        self._page_index = page_index

    @property
    def page_size(self):
        r"""Gets the page_size of this ListEnvironmentsRequest.

        每页显示的条目数量，size小于等于100

        :return: The page_size of this ListEnvironmentsRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ListEnvironmentsRequest.

        每页显示的条目数量，size小于等于100

        :param page_size: The page_size of this ListEnvironmentsRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def name(self):
        r"""Gets the name of this ListEnvironmentsRequest.

        要查询的环境名称

        :return: The name of this ListEnvironmentsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListEnvironmentsRequest.

        要查询的环境名称

        :param name: The name of this ListEnvironmentsRequest.
        :type name: str
        """
        self._name = name

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListEnvironmentsRequest.

        排序字段，支持按照环境名称|用户名称|创建时间|用户昵称排序

        :return: The sort_key of this ListEnvironmentsRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListEnvironmentsRequest.

        排序字段，支持按照环境名称|用户名称|创建时间|用户昵称排序

        :param sort_key: The sort_key of this ListEnvironmentsRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListEnvironmentsRequest.

        排序顺序，DESC降序，ASC升序

        :return: The sort_dir of this ListEnvironmentsRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListEnvironmentsRequest.

        排序顺序，DESC降序，ASC升序

        :param sort_dir: The sort_dir of this ListEnvironmentsRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

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
        if not isinstance(other, ListEnvironmentsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
