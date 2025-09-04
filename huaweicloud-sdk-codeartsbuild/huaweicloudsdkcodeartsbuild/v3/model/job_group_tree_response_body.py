# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobGroupTreeResponseBody:

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
        'domain_id': 'str',
        'project_id': 'str',
        'name': 'str',
        'parent_id': 'str',
        'path_id': 'str',
        'ordinal': 'int',
        'create_user': 'str',
        'update_user': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'children': 'list[JobGroupTreeResponseBody]'
    }

    attribute_map = {
        'id': 'id',
        'domain_id': 'domain_id',
        'project_id': 'project_id',
        'name': 'name',
        'parent_id': 'parent_id',
        'path_id': 'path_id',
        'ordinal': 'ordinal',
        'create_user': 'create_user',
        'update_user': 'update_user',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'children': 'children'
    }

    def __init__(self, id=None, domain_id=None, project_id=None, name=None, parent_id=None, path_id=None, ordinal=None, create_user=None, update_user=None, create_time=None, update_time=None, children=None):
        r"""JobGroupTreeResponseBody

        The model defined in huaweicloud sdk

        :param id: 分组编号
        :type id: str
        :param domain_id: 租户ID
        :type domain_id: str
        :param project_id: CodeArts项目ID。构建任务所在项目的ID。
        :type project_id: str
        :param name: 分组名称
        :type name: str
        :param parent_id: 父分组编号
        :type parent_id: str
        :param path_id: 分组路径
        :type path_id: str
        :param ordinal: 序数
        :type ordinal: int
        :param create_user: 创建用户
        :type create_user: str
        :param update_user: 更新用户
        :type update_user: str
        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 更新时间
        :type update_time: str
        :param children: 子分组
        :type children: list[:class:`huaweicloudsdkcodeartsbuild.v3.JobGroupTreeResponseBody`]
        """
        
        

        self._id = None
        self._domain_id = None
        self._project_id = None
        self._name = None
        self._parent_id = None
        self._path_id = None
        self._ordinal = None
        self._create_user = None
        self._update_user = None
        self._create_time = None
        self._update_time = None
        self._children = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if domain_id is not None:
            self.domain_id = domain_id
        if project_id is not None:
            self.project_id = project_id
        if name is not None:
            self.name = name
        if parent_id is not None:
            self.parent_id = parent_id
        if path_id is not None:
            self.path_id = path_id
        if ordinal is not None:
            self.ordinal = ordinal
        if create_user is not None:
            self.create_user = create_user
        if update_user is not None:
            self.update_user = update_user
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if children is not None:
            self.children = children

    @property
    def id(self):
        r"""Gets the id of this JobGroupTreeResponseBody.

        分组编号

        :return: The id of this JobGroupTreeResponseBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this JobGroupTreeResponseBody.

        分组编号

        :param id: The id of this JobGroupTreeResponseBody.
        :type id: str
        """
        self._id = id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this JobGroupTreeResponseBody.

        租户ID

        :return: The domain_id of this JobGroupTreeResponseBody.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this JobGroupTreeResponseBody.

        租户ID

        :param domain_id: The domain_id of this JobGroupTreeResponseBody.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def project_id(self):
        r"""Gets the project_id of this JobGroupTreeResponseBody.

        CodeArts项目ID。构建任务所在项目的ID。

        :return: The project_id of this JobGroupTreeResponseBody.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this JobGroupTreeResponseBody.

        CodeArts项目ID。构建任务所在项目的ID。

        :param project_id: The project_id of this JobGroupTreeResponseBody.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def name(self):
        r"""Gets the name of this JobGroupTreeResponseBody.

        分组名称

        :return: The name of this JobGroupTreeResponseBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this JobGroupTreeResponseBody.

        分组名称

        :param name: The name of this JobGroupTreeResponseBody.
        :type name: str
        """
        self._name = name

    @property
    def parent_id(self):
        r"""Gets the parent_id of this JobGroupTreeResponseBody.

        父分组编号

        :return: The parent_id of this JobGroupTreeResponseBody.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this JobGroupTreeResponseBody.

        父分组编号

        :param parent_id: The parent_id of this JobGroupTreeResponseBody.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def path_id(self):
        r"""Gets the path_id of this JobGroupTreeResponseBody.

        分组路径

        :return: The path_id of this JobGroupTreeResponseBody.
        :rtype: str
        """
        return self._path_id

    @path_id.setter
    def path_id(self, path_id):
        r"""Sets the path_id of this JobGroupTreeResponseBody.

        分组路径

        :param path_id: The path_id of this JobGroupTreeResponseBody.
        :type path_id: str
        """
        self._path_id = path_id

    @property
    def ordinal(self):
        r"""Gets the ordinal of this JobGroupTreeResponseBody.

        序数

        :return: The ordinal of this JobGroupTreeResponseBody.
        :rtype: int
        """
        return self._ordinal

    @ordinal.setter
    def ordinal(self, ordinal):
        r"""Sets the ordinal of this JobGroupTreeResponseBody.

        序数

        :param ordinal: The ordinal of this JobGroupTreeResponseBody.
        :type ordinal: int
        """
        self._ordinal = ordinal

    @property
    def create_user(self):
        r"""Gets the create_user of this JobGroupTreeResponseBody.

        创建用户

        :return: The create_user of this JobGroupTreeResponseBody.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        r"""Sets the create_user of this JobGroupTreeResponseBody.

        创建用户

        :param create_user: The create_user of this JobGroupTreeResponseBody.
        :type create_user: str
        """
        self._create_user = create_user

    @property
    def update_user(self):
        r"""Gets the update_user of this JobGroupTreeResponseBody.

        更新用户

        :return: The update_user of this JobGroupTreeResponseBody.
        :rtype: str
        """
        return self._update_user

    @update_user.setter
    def update_user(self, update_user):
        r"""Sets the update_user of this JobGroupTreeResponseBody.

        更新用户

        :param update_user: The update_user of this JobGroupTreeResponseBody.
        :type update_user: str
        """
        self._update_user = update_user

    @property
    def create_time(self):
        r"""Gets the create_time of this JobGroupTreeResponseBody.

        创建时间

        :return: The create_time of this JobGroupTreeResponseBody.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this JobGroupTreeResponseBody.

        创建时间

        :param create_time: The create_time of this JobGroupTreeResponseBody.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this JobGroupTreeResponseBody.

        更新时间

        :return: The update_time of this JobGroupTreeResponseBody.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this JobGroupTreeResponseBody.

        更新时间

        :param update_time: The update_time of this JobGroupTreeResponseBody.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def children(self):
        r"""Gets the children of this JobGroupTreeResponseBody.

        子分组

        :return: The children of this JobGroupTreeResponseBody.
        :rtype: list[:class:`huaweicloudsdkcodeartsbuild.v3.JobGroupTreeResponseBody`]
        """
        return self._children

    @children.setter
    def children(self, children):
        r"""Sets the children of this JobGroupTreeResponseBody.

        子分组

        :param children: The children of this JobGroupTreeResponseBody.
        :type children: list[:class:`huaweicloudsdkcodeartsbuild.v3.JobGroupTreeResponseBody`]
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
        if not isinstance(other, JobGroupTreeResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
