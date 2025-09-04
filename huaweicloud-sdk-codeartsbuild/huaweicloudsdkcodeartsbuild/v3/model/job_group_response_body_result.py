# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobGroupResponseBodyResult:

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
        'parent_id': 'str',
        'group_id': 'str',
        'domain_id': 'str',
        'ordinal': 'str',
        'create_user': 'str',
        'update_user': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'path_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'project_id': 'project_id',
        'parent_id': 'parent_id',
        'group_id': 'group_id',
        'domain_id': 'domain_id',
        'ordinal': 'ordinal',
        'create_user': 'create_user',
        'update_user': 'update_user',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'path_id': 'path_id'
    }

    def __init__(self, id=None, name=None, project_id=None, parent_id=None, group_id=None, domain_id=None, ordinal=None, create_user=None, update_user=None, create_time=None, update_time=None, path_id=None):
        r"""JobGroupResponseBodyResult

        The model defined in huaweicloud sdk

        :param id: 主键id
        :type id: str
        :param name: 分组名称
        :type name: str
        :param project_id: CodeArts项目ID。构建任务所在项目的ID。
        :type project_id: str
        :param parent_id: 父分组id
        :type parent_id: str
        :param group_id: 任务分组id
        :type group_id: str
        :param domain_id: 租户id
        :type domain_id: str
        :param ordinal: 分组的index
        :type ordinal: str
        :param create_user: 创建者
        :type create_user: str
        :param update_user: 修改者
        :type update_user: str
        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 修改时间
        :type update_time: str
        :param path_id: 分组地址id
        :type path_id: str
        """
        
        

        self._id = None
        self._name = None
        self._project_id = None
        self._parent_id = None
        self._group_id = None
        self._domain_id = None
        self._ordinal = None
        self._create_user = None
        self._update_user = None
        self._create_time = None
        self._update_time = None
        self._path_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if project_id is not None:
            self.project_id = project_id
        if parent_id is not None:
            self.parent_id = parent_id
        if group_id is not None:
            self.group_id = group_id
        if domain_id is not None:
            self.domain_id = domain_id
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
        if path_id is not None:
            self.path_id = path_id

    @property
    def id(self):
        r"""Gets the id of this JobGroupResponseBodyResult.

        主键id

        :return: The id of this JobGroupResponseBodyResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this JobGroupResponseBodyResult.

        主键id

        :param id: The id of this JobGroupResponseBodyResult.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this JobGroupResponseBodyResult.

        分组名称

        :return: The name of this JobGroupResponseBodyResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this JobGroupResponseBodyResult.

        分组名称

        :param name: The name of this JobGroupResponseBodyResult.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        r"""Gets the project_id of this JobGroupResponseBodyResult.

        CodeArts项目ID。构建任务所在项目的ID。

        :return: The project_id of this JobGroupResponseBodyResult.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this JobGroupResponseBodyResult.

        CodeArts项目ID。构建任务所在项目的ID。

        :param project_id: The project_id of this JobGroupResponseBodyResult.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def parent_id(self):
        r"""Gets the parent_id of this JobGroupResponseBodyResult.

        父分组id

        :return: The parent_id of this JobGroupResponseBodyResult.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this JobGroupResponseBodyResult.

        父分组id

        :param parent_id: The parent_id of this JobGroupResponseBodyResult.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def group_id(self):
        r"""Gets the group_id of this JobGroupResponseBodyResult.

        任务分组id

        :return: The group_id of this JobGroupResponseBodyResult.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this JobGroupResponseBodyResult.

        任务分组id

        :param group_id: The group_id of this JobGroupResponseBodyResult.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this JobGroupResponseBodyResult.

        租户id

        :return: The domain_id of this JobGroupResponseBodyResult.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this JobGroupResponseBodyResult.

        租户id

        :param domain_id: The domain_id of this JobGroupResponseBodyResult.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def ordinal(self):
        r"""Gets the ordinal of this JobGroupResponseBodyResult.

        分组的index

        :return: The ordinal of this JobGroupResponseBodyResult.
        :rtype: str
        """
        return self._ordinal

    @ordinal.setter
    def ordinal(self, ordinal):
        r"""Sets the ordinal of this JobGroupResponseBodyResult.

        分组的index

        :param ordinal: The ordinal of this JobGroupResponseBodyResult.
        :type ordinal: str
        """
        self._ordinal = ordinal

    @property
    def create_user(self):
        r"""Gets the create_user of this JobGroupResponseBodyResult.

        创建者

        :return: The create_user of this JobGroupResponseBodyResult.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        r"""Sets the create_user of this JobGroupResponseBodyResult.

        创建者

        :param create_user: The create_user of this JobGroupResponseBodyResult.
        :type create_user: str
        """
        self._create_user = create_user

    @property
    def update_user(self):
        r"""Gets the update_user of this JobGroupResponseBodyResult.

        修改者

        :return: The update_user of this JobGroupResponseBodyResult.
        :rtype: str
        """
        return self._update_user

    @update_user.setter
    def update_user(self, update_user):
        r"""Sets the update_user of this JobGroupResponseBodyResult.

        修改者

        :param update_user: The update_user of this JobGroupResponseBodyResult.
        :type update_user: str
        """
        self._update_user = update_user

    @property
    def create_time(self):
        r"""Gets the create_time of this JobGroupResponseBodyResult.

        创建时间

        :return: The create_time of this JobGroupResponseBodyResult.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this JobGroupResponseBodyResult.

        创建时间

        :param create_time: The create_time of this JobGroupResponseBodyResult.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this JobGroupResponseBodyResult.

        修改时间

        :return: The update_time of this JobGroupResponseBodyResult.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this JobGroupResponseBodyResult.

        修改时间

        :param update_time: The update_time of this JobGroupResponseBodyResult.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def path_id(self):
        r"""Gets the path_id of this JobGroupResponseBodyResult.

        分组地址id

        :return: The path_id of this JobGroupResponseBodyResult.
        :rtype: str
        """
        return self._path_id

    @path_id.setter
    def path_id(self, path_id):
        r"""Sets the path_id of this JobGroupResponseBodyResult.

        分组地址id

        :param path_id: The path_id of this JobGroupResponseBodyResult.
        :type path_id: str
        """
        self._path_id = path_id

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
        if not isinstance(other, JobGroupResponseBodyResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
