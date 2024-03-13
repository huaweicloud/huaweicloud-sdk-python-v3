# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IDERepoSearchDO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'artifact_name': 'str',
        'artifact_type': 'str',
        'page_no': 'int',
        'page_size': 'int',
        'project_id': 'str',
        'in_project': 'str'
    }

    attribute_map = {
        'artifact_name': 'artifact_name',
        'artifact_type': 'artifact_type',
        'page_no': 'page_no',
        'page_size': 'page_size',
        'project_id': 'project_id',
        'in_project': 'in_project'
    }

    def __init__(self, artifact_name=None, artifact_type=None, page_no=None, page_size=None, project_id=None, in_project=None):
        """IDERepoSearchDO

        The model defined in huaweicloud sdk

        :param artifact_name: 搜索制品名称
        :type artifact_name: str
        :param artifact_type: 制品类型
        :type artifact_type: str
        :param page_no: 页码
        :type page_no: int
        :param page_size: 每页条数
        :type page_size: int
        :param project_id: 项目id
        :type project_id: str
        :param in_project: 是否在项目中
        :type in_project: str
        """
        
        

        self._artifact_name = None
        self._artifact_type = None
        self._page_no = None
        self._page_size = None
        self._project_id = None
        self._in_project = None
        self.discriminator = None

        self.artifact_name = artifact_name
        if artifact_type is not None:
            self.artifact_type = artifact_type
        if page_no is not None:
            self.page_no = page_no
        if page_size is not None:
            self.page_size = page_size
        if project_id is not None:
            self.project_id = project_id
        if in_project is not None:
            self.in_project = in_project

    @property
    def artifact_name(self):
        """Gets the artifact_name of this IDERepoSearchDO.

        搜索制品名称

        :return: The artifact_name of this IDERepoSearchDO.
        :rtype: str
        """
        return self._artifact_name

    @artifact_name.setter
    def artifact_name(self, artifact_name):
        """Sets the artifact_name of this IDERepoSearchDO.

        搜索制品名称

        :param artifact_name: The artifact_name of this IDERepoSearchDO.
        :type artifact_name: str
        """
        self._artifact_name = artifact_name

    @property
    def artifact_type(self):
        """Gets the artifact_type of this IDERepoSearchDO.

        制品类型

        :return: The artifact_type of this IDERepoSearchDO.
        :rtype: str
        """
        return self._artifact_type

    @artifact_type.setter
    def artifact_type(self, artifact_type):
        """Sets the artifact_type of this IDERepoSearchDO.

        制品类型

        :param artifact_type: The artifact_type of this IDERepoSearchDO.
        :type artifact_type: str
        """
        self._artifact_type = artifact_type

    @property
    def page_no(self):
        """Gets the page_no of this IDERepoSearchDO.

        页码

        :return: The page_no of this IDERepoSearchDO.
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        """Sets the page_no of this IDERepoSearchDO.

        页码

        :param page_no: The page_no of this IDERepoSearchDO.
        :type page_no: int
        """
        self._page_no = page_no

    @property
    def page_size(self):
        """Gets the page_size of this IDERepoSearchDO.

        每页条数

        :return: The page_size of this IDERepoSearchDO.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this IDERepoSearchDO.

        每页条数

        :param page_size: The page_size of this IDERepoSearchDO.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def project_id(self):
        """Gets the project_id of this IDERepoSearchDO.

        项目id

        :return: The project_id of this IDERepoSearchDO.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this IDERepoSearchDO.

        项目id

        :param project_id: The project_id of this IDERepoSearchDO.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def in_project(self):
        """Gets the in_project of this IDERepoSearchDO.

        是否在项目中

        :return: The in_project of this IDERepoSearchDO.
        :rtype: str
        """
        return self._in_project

    @in_project.setter
    def in_project(self, in_project):
        """Sets the in_project of this IDERepoSearchDO.

        是否在项目中

        :param in_project: The in_project of this IDERepoSearchDO.
        :type in_project: str
        """
        self._in_project = in_project

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
        if not isinstance(other, IDERepoSearchDO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
