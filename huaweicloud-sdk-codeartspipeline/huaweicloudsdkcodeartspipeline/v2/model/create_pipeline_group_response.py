# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePipelineGroupResponse(SdkResponse):

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
        r"""CreatePipelineGroupResponse

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
        
        super(CreatePipelineGroupResponse, self).__init__()

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
        if creator is not None:
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
        r"""Gets the id of this CreatePipelineGroupResponse.

        分组ID

        :return: The id of this CreatePipelineGroupResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreatePipelineGroupResponse.

        分组ID

        :param id: The id of this CreatePipelineGroupResponse.
        :type id: str
        """
        self._id = id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this CreatePipelineGroupResponse.

        租户ID

        :return: The domain_id of this CreatePipelineGroupResponse.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this CreatePipelineGroupResponse.

        租户ID

        :param domain_id: The domain_id of this CreatePipelineGroupResponse.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def project_id(self):
        r"""Gets the project_id of this CreatePipelineGroupResponse.

        项目ID

        :return: The project_id of this CreatePipelineGroupResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this CreatePipelineGroupResponse.

        项目ID

        :param project_id: The project_id of this CreatePipelineGroupResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def name(self):
        r"""Gets the name of this CreatePipelineGroupResponse.

        分组名

        :return: The name of this CreatePipelineGroupResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreatePipelineGroupResponse.

        分组名

        :param name: The name of this CreatePipelineGroupResponse.
        :type name: str
        """
        self._name = name

    @property
    def parent_id(self):
        r"""Gets the parent_id of this CreatePipelineGroupResponse.

        父分组ID

        :return: The parent_id of this CreatePipelineGroupResponse.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this CreatePipelineGroupResponse.

        父分组ID

        :param parent_id: The parent_id of this CreatePipelineGroupResponse.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def path_id(self):
        r"""Gets the path_id of this CreatePipelineGroupResponse.

        分组路径ID

        :return: The path_id of this CreatePipelineGroupResponse.
        :rtype: str
        """
        return self._path_id

    @path_id.setter
    def path_id(self, path_id):
        r"""Sets the path_id of this CreatePipelineGroupResponse.

        分组路径ID

        :param path_id: The path_id of this CreatePipelineGroupResponse.
        :type path_id: str
        """
        self._path_id = path_id

    @property
    def ordinal(self):
        r"""Gets the ordinal of this CreatePipelineGroupResponse.

        序号

        :return: The ordinal of this CreatePipelineGroupResponse.
        :rtype: int
        """
        return self._ordinal

    @ordinal.setter
    def ordinal(self, ordinal):
        r"""Sets the ordinal of this CreatePipelineGroupResponse.

        序号

        :param ordinal: The ordinal of this CreatePipelineGroupResponse.
        :type ordinal: int
        """
        self._ordinal = ordinal

    @property
    def creator(self):
        r"""Gets the creator of this CreatePipelineGroupResponse.

        创建用户ID

        :return: The creator of this CreatePipelineGroupResponse.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this CreatePipelineGroupResponse.

        创建用户ID

        :param creator: The creator of this CreatePipelineGroupResponse.
        :type creator: str
        """
        self._creator = creator

    @property
    def updater(self):
        r"""Gets the updater of this CreatePipelineGroupResponse.

        更新用户ID

        :return: The updater of this CreatePipelineGroupResponse.
        :rtype: str
        """
        return self._updater

    @updater.setter
    def updater(self, updater):
        r"""Sets the updater of this CreatePipelineGroupResponse.

        更新用户ID

        :param updater: The updater of this CreatePipelineGroupResponse.
        :type updater: str
        """
        self._updater = updater

    @property
    def create_time(self):
        r"""Gets the create_time of this CreatePipelineGroupResponse.

        创建时间

        :return: The create_time of this CreatePipelineGroupResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this CreatePipelineGroupResponse.

        创建时间

        :param create_time: The create_time of this CreatePipelineGroupResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this CreatePipelineGroupResponse.

        更新时间

        :return: The update_time of this CreatePipelineGroupResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this CreatePipelineGroupResponse.

        更新时间

        :param update_time: The update_time of this CreatePipelineGroupResponse.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def children(self):
        r"""Gets the children of this CreatePipelineGroupResponse.

        子分组列表

        :return: The children of this CreatePipelineGroupResponse.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.PipelineGroupVo`]
        """
        return self._children

    @children.setter
    def children(self, children):
        r"""Sets the children of this CreatePipelineGroupResponse.

        子分组列表

        :param children: The children of this CreatePipelineGroupResponse.
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
        if not isinstance(other, CreatePipelineGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
