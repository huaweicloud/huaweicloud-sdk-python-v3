# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppGroupsEntity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'project_id': 'str',
        'path': 'str',
        'parent_id': 'str',
        'ordinal': 'int',
        'create_user_id': 'str',
        'last_update_user_id': 'str',
        'count': 'int',
        'children': 'list[AppGroupsEntity]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'project_id': 'project_id',
        'path': 'path',
        'parent_id': 'parent_id',
        'ordinal': 'ordinal',
        'create_user_id': 'create_user_id',
        'last_update_user_id': 'last_update_user_id',
        'count': 'count',
        'children': 'children'
    }

    def __init__(self, id=None, name=None, project_id=None, path=None, parent_id=None, ordinal=None, create_user_id=None, last_update_user_id=None, count=None, children=None):
        r"""AppGroupsEntity

        The model defined in huaweicloud sdk

        :param id: 分组id
        :type id: str
        :param name: 分组名称
        :type name: str
        :param project_id: 项目id
        :type project_id: str
        :param path: 分组路径
        :type path: str
        :param parent_id: 父分组id，首层为null
        :type parent_id: str
        :param ordinal: 分组排序字段
        :type ordinal: int
        :param create_user_id: 分组创建者用户id
        :type create_user_id: str
        :param last_update_user_id: 最近一次更新该分组用户id
        :type last_update_user_id: str
        :param count: 该分组应用总数
        :type count: int
        :param children: 子分组列表
        :type children: list[:class:`huaweicloudsdkcodeartsdeploy.v2.AppGroupsEntity`]
        """
        
        

        self._id = None
        self._name = None
        self._project_id = None
        self._path = None
        self._parent_id = None
        self._ordinal = None
        self._create_user_id = None
        self._last_update_user_id = None
        self._count = None
        self._children = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if project_id is not None:
            self.project_id = project_id
        if path is not None:
            self.path = path
        if parent_id is not None:
            self.parent_id = parent_id
        if ordinal is not None:
            self.ordinal = ordinal
        if create_user_id is not None:
            self.create_user_id = create_user_id
        if last_update_user_id is not None:
            self.last_update_user_id = last_update_user_id
        if count is not None:
            self.count = count
        if children is not None:
            self.children = children

    @property
    def id(self):
        r"""Gets the id of this AppGroupsEntity.

        分组id

        :return: The id of this AppGroupsEntity.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AppGroupsEntity.

        分组id

        :param id: The id of this AppGroupsEntity.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this AppGroupsEntity.

        分组名称

        :return: The name of this AppGroupsEntity.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AppGroupsEntity.

        分组名称

        :param name: The name of this AppGroupsEntity.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        r"""Gets the project_id of this AppGroupsEntity.

        项目id

        :return: The project_id of this AppGroupsEntity.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this AppGroupsEntity.

        项目id

        :param project_id: The project_id of this AppGroupsEntity.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def path(self):
        r"""Gets the path of this AppGroupsEntity.

        分组路径

        :return: The path of this AppGroupsEntity.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this AppGroupsEntity.

        分组路径

        :param path: The path of this AppGroupsEntity.
        :type path: str
        """
        self._path = path

    @property
    def parent_id(self):
        r"""Gets the parent_id of this AppGroupsEntity.

        父分组id，首层为null

        :return: The parent_id of this AppGroupsEntity.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this AppGroupsEntity.

        父分组id，首层为null

        :param parent_id: The parent_id of this AppGroupsEntity.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def ordinal(self):
        r"""Gets the ordinal of this AppGroupsEntity.

        分组排序字段

        :return: The ordinal of this AppGroupsEntity.
        :rtype: int
        """
        return self._ordinal

    @ordinal.setter
    def ordinal(self, ordinal):
        r"""Sets the ordinal of this AppGroupsEntity.

        分组排序字段

        :param ordinal: The ordinal of this AppGroupsEntity.
        :type ordinal: int
        """
        self._ordinal = ordinal

    @property
    def create_user_id(self):
        r"""Gets the create_user_id of this AppGroupsEntity.

        分组创建者用户id

        :return: The create_user_id of this AppGroupsEntity.
        :rtype: str
        """
        return self._create_user_id

    @create_user_id.setter
    def create_user_id(self, create_user_id):
        r"""Sets the create_user_id of this AppGroupsEntity.

        分组创建者用户id

        :param create_user_id: The create_user_id of this AppGroupsEntity.
        :type create_user_id: str
        """
        self._create_user_id = create_user_id

    @property
    def last_update_user_id(self):
        r"""Gets the last_update_user_id of this AppGroupsEntity.

        最近一次更新该分组用户id

        :return: The last_update_user_id of this AppGroupsEntity.
        :rtype: str
        """
        return self._last_update_user_id

    @last_update_user_id.setter
    def last_update_user_id(self, last_update_user_id):
        r"""Sets the last_update_user_id of this AppGroupsEntity.

        最近一次更新该分组用户id

        :param last_update_user_id: The last_update_user_id of this AppGroupsEntity.
        :type last_update_user_id: str
        """
        self._last_update_user_id = last_update_user_id

    @property
    def count(self):
        r"""Gets the count of this AppGroupsEntity.

        该分组应用总数

        :return: The count of this AppGroupsEntity.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this AppGroupsEntity.

        该分组应用总数

        :param count: The count of this AppGroupsEntity.
        :type count: int
        """
        self._count = count

    @property
    def children(self):
        r"""Gets the children of this AppGroupsEntity.

        子分组列表

        :return: The children of this AppGroupsEntity.
        :rtype: list[:class:`huaweicloudsdkcodeartsdeploy.v2.AppGroupsEntity`]
        """
        return self._children

    @children.setter
    def children(self, children):
        r"""Sets the children of this AppGroupsEntity.

        子分组列表

        :param children: The children of this AppGroupsEntity.
        :type children: list[:class:`huaweicloudsdkcodeartsdeploy.v2.AppGroupsEntity`]
        """
        self._children = children

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
        if not isinstance(other, AppGroupsEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
