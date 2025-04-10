# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowGroupResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'creator_id': 'int',
        'project_id': 'str',
        'created_at': 'datetime',
        'description': 'str',
        'full_name': 'str',
        'ancestor_ids': 'list[int]',
        'ancestor_names': 'list[str]',
        'id': 'int',
        'members_count': 'int',
        'name': 'str',
        'repository_count': 'int',
        'star_count': 'int',
        'starred': 'bool',
        'subgroup_count': 'int',
        'visibility': 'str',
        'sum': 'GroupSumDto'
    }

    attribute_map = {
        'creator_id': 'creator_id',
        'project_id': 'project_id',
        'created_at': 'created_at',
        'description': 'description',
        'full_name': 'full_name',
        'ancestor_ids': 'ancestor_ids',
        'ancestor_names': 'ancestor_names',
        'id': 'id',
        'members_count': 'members_count',
        'name': 'name',
        'repository_count': 'repository_count',
        'star_count': 'star_count',
        'starred': 'starred',
        'subgroup_count': 'subgroup_count',
        'visibility': 'visibility',
        'sum': 'sum'
    }

    def __init__(self, creator_id=None, project_id=None, created_at=None, description=None, full_name=None, ancestor_ids=None, ancestor_names=None, id=None, members_count=None, name=None, repository_count=None, star_count=None, starred=None, subgroup_count=None, visibility=None, sum=None):
        r"""ShowGroupResponse

        The model defined in huaweicloud sdk

        :param creator_id: 创建者id
        :type creator_id: int
        :param project_id: 项目id
        :type project_id: str
        :param created_at: 创建时间
        :type created_at: datetime
        :param description: 描述
        :type description: str
        :param full_name: 代码组全名
        :type full_name: str
        :param ancestor_ids: 代码组层级路径id
        :type ancestor_ids: list[int]
        :param ancestor_names: 代码组层级路径名称
        :type ancestor_names: list[str]
        :param id: 代码组id
        :type id: int
        :param members_count: 代码组成员计数
        :type members_count: int
        :param name: 代码组名
        :type name: str
        :param repository_count: 仓库计数
        :type repository_count: int
        :param star_count: 关注计数
        :type star_count: int
        :param starred: 是否关注
        :type starred: bool
        :param subgroup_count: 子组计数
        :type subgroup_count: int
        :param visibility: 可见性, private public
        :type visibility: str
        :param sum: 
        :type sum: :class:`huaweicloudsdkcodehub.v4.GroupSumDto`
        """
        
        super(ShowGroupResponse, self).__init__()

        self._creator_id = None
        self._project_id = None
        self._created_at = None
        self._description = None
        self._full_name = None
        self._ancestor_ids = None
        self._ancestor_names = None
        self._id = None
        self._members_count = None
        self._name = None
        self._repository_count = None
        self._star_count = None
        self._starred = None
        self._subgroup_count = None
        self._visibility = None
        self._sum = None
        self.discriminator = None

        if creator_id is not None:
            self.creator_id = creator_id
        if project_id is not None:
            self.project_id = project_id
        if created_at is not None:
            self.created_at = created_at
        if description is not None:
            self.description = description
        if full_name is not None:
            self.full_name = full_name
        if ancestor_ids is not None:
            self.ancestor_ids = ancestor_ids
        if ancestor_names is not None:
            self.ancestor_names = ancestor_names
        if id is not None:
            self.id = id
        if members_count is not None:
            self.members_count = members_count
        if name is not None:
            self.name = name
        if repository_count is not None:
            self.repository_count = repository_count
        if star_count is not None:
            self.star_count = star_count
        if starred is not None:
            self.starred = starred
        if subgroup_count is not None:
            self.subgroup_count = subgroup_count
        if visibility is not None:
            self.visibility = visibility
        if sum is not None:
            self.sum = sum

    @property
    def creator_id(self):
        r"""Gets the creator_id of this ShowGroupResponse.

        创建者id

        :return: The creator_id of this ShowGroupResponse.
        :rtype: int
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        r"""Sets the creator_id of this ShowGroupResponse.

        创建者id

        :param creator_id: The creator_id of this ShowGroupResponse.
        :type creator_id: int
        """
        self._creator_id = creator_id

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowGroupResponse.

        项目id

        :return: The project_id of this ShowGroupResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowGroupResponse.

        项目id

        :param project_id: The project_id of this ShowGroupResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def created_at(self):
        r"""Gets the created_at of this ShowGroupResponse.

        创建时间

        :return: The created_at of this ShowGroupResponse.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ShowGroupResponse.

        创建时间

        :param created_at: The created_at of this ShowGroupResponse.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def description(self):
        r"""Gets the description of this ShowGroupResponse.

        描述

        :return: The description of this ShowGroupResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowGroupResponse.

        描述

        :param description: The description of this ShowGroupResponse.
        :type description: str
        """
        self._description = description

    @property
    def full_name(self):
        r"""Gets the full_name of this ShowGroupResponse.

        代码组全名

        :return: The full_name of this ShowGroupResponse.
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        r"""Sets the full_name of this ShowGroupResponse.

        代码组全名

        :param full_name: The full_name of this ShowGroupResponse.
        :type full_name: str
        """
        self._full_name = full_name

    @property
    def ancestor_ids(self):
        r"""Gets the ancestor_ids of this ShowGroupResponse.

        代码组层级路径id

        :return: The ancestor_ids of this ShowGroupResponse.
        :rtype: list[int]
        """
        return self._ancestor_ids

    @ancestor_ids.setter
    def ancestor_ids(self, ancestor_ids):
        r"""Sets the ancestor_ids of this ShowGroupResponse.

        代码组层级路径id

        :param ancestor_ids: The ancestor_ids of this ShowGroupResponse.
        :type ancestor_ids: list[int]
        """
        self._ancestor_ids = ancestor_ids

    @property
    def ancestor_names(self):
        r"""Gets the ancestor_names of this ShowGroupResponse.

        代码组层级路径名称

        :return: The ancestor_names of this ShowGroupResponse.
        :rtype: list[str]
        """
        return self._ancestor_names

    @ancestor_names.setter
    def ancestor_names(self, ancestor_names):
        r"""Sets the ancestor_names of this ShowGroupResponse.

        代码组层级路径名称

        :param ancestor_names: The ancestor_names of this ShowGroupResponse.
        :type ancestor_names: list[str]
        """
        self._ancestor_names = ancestor_names

    @property
    def id(self):
        r"""Gets the id of this ShowGroupResponse.

        代码组id

        :return: The id of this ShowGroupResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowGroupResponse.

        代码组id

        :param id: The id of this ShowGroupResponse.
        :type id: int
        """
        self._id = id

    @property
    def members_count(self):
        r"""Gets the members_count of this ShowGroupResponse.

        代码组成员计数

        :return: The members_count of this ShowGroupResponse.
        :rtype: int
        """
        return self._members_count

    @members_count.setter
    def members_count(self, members_count):
        r"""Sets the members_count of this ShowGroupResponse.

        代码组成员计数

        :param members_count: The members_count of this ShowGroupResponse.
        :type members_count: int
        """
        self._members_count = members_count

    @property
    def name(self):
        r"""Gets the name of this ShowGroupResponse.

        代码组名

        :return: The name of this ShowGroupResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowGroupResponse.

        代码组名

        :param name: The name of this ShowGroupResponse.
        :type name: str
        """
        self._name = name

    @property
    def repository_count(self):
        r"""Gets the repository_count of this ShowGroupResponse.

        仓库计数

        :return: The repository_count of this ShowGroupResponse.
        :rtype: int
        """
        return self._repository_count

    @repository_count.setter
    def repository_count(self, repository_count):
        r"""Sets the repository_count of this ShowGroupResponse.

        仓库计数

        :param repository_count: The repository_count of this ShowGroupResponse.
        :type repository_count: int
        """
        self._repository_count = repository_count

    @property
    def star_count(self):
        r"""Gets the star_count of this ShowGroupResponse.

        关注计数

        :return: The star_count of this ShowGroupResponse.
        :rtype: int
        """
        return self._star_count

    @star_count.setter
    def star_count(self, star_count):
        r"""Sets the star_count of this ShowGroupResponse.

        关注计数

        :param star_count: The star_count of this ShowGroupResponse.
        :type star_count: int
        """
        self._star_count = star_count

    @property
    def starred(self):
        r"""Gets the starred of this ShowGroupResponse.

        是否关注

        :return: The starred of this ShowGroupResponse.
        :rtype: bool
        """
        return self._starred

    @starred.setter
    def starred(self, starred):
        r"""Sets the starred of this ShowGroupResponse.

        是否关注

        :param starred: The starred of this ShowGroupResponse.
        :type starred: bool
        """
        self._starred = starred

    @property
    def subgroup_count(self):
        r"""Gets the subgroup_count of this ShowGroupResponse.

        子组计数

        :return: The subgroup_count of this ShowGroupResponse.
        :rtype: int
        """
        return self._subgroup_count

    @subgroup_count.setter
    def subgroup_count(self, subgroup_count):
        r"""Sets the subgroup_count of this ShowGroupResponse.

        子组计数

        :param subgroup_count: The subgroup_count of this ShowGroupResponse.
        :type subgroup_count: int
        """
        self._subgroup_count = subgroup_count

    @property
    def visibility(self):
        r"""Gets the visibility of this ShowGroupResponse.

        可见性, private public

        :return: The visibility of this ShowGroupResponse.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        r"""Sets the visibility of this ShowGroupResponse.

        可见性, private public

        :param visibility: The visibility of this ShowGroupResponse.
        :type visibility: str
        """
        self._visibility = visibility

    @property
    def sum(self):
        r"""Gets the sum of this ShowGroupResponse.

        :return: The sum of this ShowGroupResponse.
        :rtype: :class:`huaweicloudsdkcodehub.v4.GroupSumDto`
        """
        return self._sum

    @sum.setter
    def sum(self, sum):
        r"""Sets the sum of this ShowGroupResponse.

        :param sum: The sum of this ShowGroupResponse.
        :type sum: :class:`huaweicloudsdkcodehub.v4.GroupSumDto`
        """
        self._sum = sum

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
        if not isinstance(other, ShowGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
