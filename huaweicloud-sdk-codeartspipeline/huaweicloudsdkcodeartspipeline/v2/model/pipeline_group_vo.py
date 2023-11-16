# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PipelineGroupVo:

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
        'creator': 'str',
        'updater': 'str',
        'create_time': 'int',
        'update_time': 'int',
        'children': 'list[PipelineGroupVo]'
    }

    attribute_map = {
        'id': 'id',
        'domain_id': 'domain_id',
        'project_id': 'project_id',
        'name': 'name',
        'parent_id': 'parent_id',
        'path_id': 'path_id',
        'ordinal': 'ordinal',
        'creator': 'creator',
        'updater': 'updater',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'children': 'children'
    }

    def __init__(self, id=None, domain_id=None, project_id=None, name=None, parent_id=None, path_id=None, ordinal=None, creator=None, updater=None, create_time=None, update_time=None, children=None):
        """PipelineGroupVo

        The model defined in huaweicloud sdk

        :param id: 分组ID
        :type id: str
        :param domain_id: 租户ID
        :type domain_id: str
        :param project_id: 项目ID
        :type project_id: str
        :param name: 分组名
        :type name: str
        :param parent_id: 父分组ID
        :type parent_id: str
        :param path_id: 分组路径ID
        :type path_id: str
        :param ordinal: 序号
        :type ordinal: int
        :param creator: 创建用户ID
        :type creator: str
        :param updater: 更新用户ID
        :type updater: str
        :param create_time: 创建时间
        :type create_time: int
        :param update_time: 更新时间
        :type update_time: int
        :param children: 子分组列表
        :type children: list[:class:`huaweicloudsdkcodeartspipeline.v2.PipelineGroupVo`]
        """
        
        

        self._id = None
        self._domain_id = None
        self._project_id = None
        self._name = None
        self._parent_id = None
        self._path_id = None
        self._ordinal = None
        self._creator = None
        self._updater = None
        self._create_time = None
        self._update_time = None
        self._children = None
        self.discriminator = None

        self.id = id
        self.domain_id = domain_id
        self.project_id = project_id
        self.name = name
        if parent_id is not None:
            self.parent_id = parent_id
        self.path_id = path_id
        if ordinal is not None:
            self.ordinal = ordinal
        self.creator = creator
        if updater is not None:
            self.updater = updater
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if children is not None:
            self.children = children

    @property
    def id(self):
        """Gets the id of this PipelineGroupVo.

        分组ID

        :return: The id of this PipelineGroupVo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PipelineGroupVo.

        分组ID

        :param id: The id of this PipelineGroupVo.
        :type id: str
        """
        self._id = id

    @property
    def domain_id(self):
        """Gets the domain_id of this PipelineGroupVo.

        租户ID

        :return: The domain_id of this PipelineGroupVo.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this PipelineGroupVo.

        租户ID

        :param domain_id: The domain_id of this PipelineGroupVo.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def project_id(self):
        """Gets the project_id of this PipelineGroupVo.

        项目ID

        :return: The project_id of this PipelineGroupVo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this PipelineGroupVo.

        项目ID

        :param project_id: The project_id of this PipelineGroupVo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def name(self):
        """Gets the name of this PipelineGroupVo.

        分组名

        :return: The name of this PipelineGroupVo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PipelineGroupVo.

        分组名

        :param name: The name of this PipelineGroupVo.
        :type name: str
        """
        self._name = name

    @property
    def parent_id(self):
        """Gets the parent_id of this PipelineGroupVo.

        父分组ID

        :return: The parent_id of this PipelineGroupVo.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this PipelineGroupVo.

        父分组ID

        :param parent_id: The parent_id of this PipelineGroupVo.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def path_id(self):
        """Gets the path_id of this PipelineGroupVo.

        分组路径ID

        :return: The path_id of this PipelineGroupVo.
        :rtype: str
        """
        return self._path_id

    @path_id.setter
    def path_id(self, path_id):
        """Sets the path_id of this PipelineGroupVo.

        分组路径ID

        :param path_id: The path_id of this PipelineGroupVo.
        :type path_id: str
        """
        self._path_id = path_id

    @property
    def ordinal(self):
        """Gets the ordinal of this PipelineGroupVo.

        序号

        :return: The ordinal of this PipelineGroupVo.
        :rtype: int
        """
        return self._ordinal

    @ordinal.setter
    def ordinal(self, ordinal):
        """Sets the ordinal of this PipelineGroupVo.

        序号

        :param ordinal: The ordinal of this PipelineGroupVo.
        :type ordinal: int
        """
        self._ordinal = ordinal

    @property
    def creator(self):
        """Gets the creator of this PipelineGroupVo.

        创建用户ID

        :return: The creator of this PipelineGroupVo.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this PipelineGroupVo.

        创建用户ID

        :param creator: The creator of this PipelineGroupVo.
        :type creator: str
        """
        self._creator = creator

    @property
    def updater(self):
        """Gets the updater of this PipelineGroupVo.

        更新用户ID

        :return: The updater of this PipelineGroupVo.
        :rtype: str
        """
        return self._updater

    @updater.setter
    def updater(self, updater):
        """Sets the updater of this PipelineGroupVo.

        更新用户ID

        :param updater: The updater of this PipelineGroupVo.
        :type updater: str
        """
        self._updater = updater

    @property
    def create_time(self):
        """Gets the create_time of this PipelineGroupVo.

        创建时间

        :return: The create_time of this PipelineGroupVo.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this PipelineGroupVo.

        创建时间

        :param create_time: The create_time of this PipelineGroupVo.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this PipelineGroupVo.

        更新时间

        :return: The update_time of this PipelineGroupVo.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this PipelineGroupVo.

        更新时间

        :param update_time: The update_time of this PipelineGroupVo.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def children(self):
        """Gets the children of this PipelineGroupVo.

        子分组列表

        :return: The children of this PipelineGroupVo.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.PipelineGroupVo`]
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this PipelineGroupVo.

        子分组列表

        :param children: The children of this PipelineGroupVo.
        :type children: list[:class:`huaweicloudsdkcodeartspipeline.v2.PipelineGroupVo`]
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
        if not isinstance(other, PipelineGroupVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
