# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SnapshotsVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'title': 'str',
        'issue_id': 'str',
        'snapshot2workitem': 'object',
        'created_by': 'UserVO',
        'modified_by': 'UserVO',
        'category': 'str',
        'description': 'str',
        'path': 'str',
        'region': 'str',
        'id': 'str',
        'tenant_id': 'str',
        'created_date': 'str',
        'modified_date': 'str',
        'domain_id': 'str',
        'type': 'str',
        'snap_base_info_id': 'str',
        'issue_category': 'str',
        'parent_id': 'str',
        'root_id': 'str',
        'parent_full_path': 'str',
        'parent_path': 'str',
        'full_path': 'str',
        'version_number': 'int',
        'deletable': 'bool',
        'category_name': 'str'
    }

    attribute_map = {
        'title': 'title',
        'issue_id': 'issue_id',
        'snapshot2workitem': 'snapshot2workitem',
        'created_by': 'created_by',
        'modified_by': 'modified_by',
        'category': 'category',
        'description': 'description',
        'path': 'path',
        'region': 'region',
        'id': 'id',
        'tenant_id': 'tenant_id',
        'created_date': 'created_date',
        'modified_date': 'modified_date',
        'domain_id': 'domain_id',
        'type': 'type',
        'snap_base_info_id': 'snap_base_info_id',
        'issue_category': 'issue_category',
        'parent_id': 'parent_id',
        'root_id': 'root_id',
        'parent_full_path': 'parent_full_path',
        'parent_path': 'parent_path',
        'full_path': 'full_path',
        'version_number': 'version_number',
        'deletable': 'deletable',
        'category_name': 'category_name'
    }

    def __init__(self, title=None, issue_id=None, snapshot2workitem=None, created_by=None, modified_by=None, category=None, description=None, path=None, region=None, id=None, tenant_id=None, created_date=None, modified_date=None, domain_id=None, type=None, snap_base_info_id=None, issue_category=None, parent_id=None, root_id=None, parent_full_path=None, parent_path=None, full_path=None, version_number=None, deletable=None, category_name=None):
        r"""SnapshotsVO

        The model defined in huaweicloud sdk

        :param title: 快照标题。
        :type title: str
        :param issue_id: 工作项ID。
        :type issue_id: str
        :param snapshot2workitem: 快照记录工作项。键为工作项类型编码（如 Bug、IR），值为 IssueVO 对象或工作项ID字符串。
        :type snapshot2workitem: object
        :param created_by: 
        :type created_by: :class:`huaweicloudsdkprojectman.v4.UserVO`
        :param modified_by: 
        :type modified_by: :class:`huaweicloudsdkprojectman.v4.UserVO`
        :param category: 工作项类型。
        :type category: str
        :param description: 描述信息。
        :type description: str
        :param path: 工作项父子挂载路径。
        :type path: str
        :param region: 区域。
        :type region: str
        :param id: 快照ID。
        :type id: str
        :param tenant_id: 租户ID。
        :type tenant_id: str
        :param created_date: 快照创建时间，unix时间戳，单位：毫秒。
        :type created_date: str
        :param modified_date: 快照最后修改时间，unix时间戳，单位：毫秒。
        :type modified_date: str
        :param domain_id: 项目空间ID。
        :type domain_id: str
        :param type: 快照类型。
        :type type: str
        :param snap_base_info_id: 快照基础信息ID。
        :type snap_base_info_id: str
        :param issue_category: 工作项类型编码。
        :type issue_category: str
        :param parent_id: 父工作项ID。
        :type parent_id: str
        :param root_id: 根工作项ID。
        :type root_id: str
        :param parent_full_path: 父工作项完整路径。
        :type parent_full_path: str
        :param parent_path: 父工作项路径。
        :type parent_path: str
        :param full_path: 工作项完整路径。
        :type full_path: str
        :param version_number: 快照版本号。
        :type version_number: int
        :param deletable: 是否可删除。
        :type deletable: bool
        :param category_name: 工作项类型名称。
        :type category_name: str
        """
        
        

        self._title = None
        self._issue_id = None
        self._snapshot2workitem = None
        self._created_by = None
        self._modified_by = None
        self._category = None
        self._description = None
        self._path = None
        self._region = None
        self._id = None
        self._tenant_id = None
        self._created_date = None
        self._modified_date = None
        self._domain_id = None
        self._type = None
        self._snap_base_info_id = None
        self._issue_category = None
        self._parent_id = None
        self._root_id = None
        self._parent_full_path = None
        self._parent_path = None
        self._full_path = None
        self._version_number = None
        self._deletable = None
        self._category_name = None
        self.discriminator = None

        if title is not None:
            self.title = title
        if issue_id is not None:
            self.issue_id = issue_id
        if snapshot2workitem is not None:
            self.snapshot2workitem = snapshot2workitem
        if created_by is not None:
            self.created_by = created_by
        if modified_by is not None:
            self.modified_by = modified_by
        if category is not None:
            self.category = category
        if description is not None:
            self.description = description
        if path is not None:
            self.path = path
        if region is not None:
            self.region = region
        if id is not None:
            self.id = id
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if created_date is not None:
            self.created_date = created_date
        if modified_date is not None:
            self.modified_date = modified_date
        if domain_id is not None:
            self.domain_id = domain_id
        if type is not None:
            self.type = type
        if snap_base_info_id is not None:
            self.snap_base_info_id = snap_base_info_id
        if issue_category is not None:
            self.issue_category = issue_category
        if parent_id is not None:
            self.parent_id = parent_id
        if root_id is not None:
            self.root_id = root_id
        if parent_full_path is not None:
            self.parent_full_path = parent_full_path
        if parent_path is not None:
            self.parent_path = parent_path
        if full_path is not None:
            self.full_path = full_path
        if version_number is not None:
            self.version_number = version_number
        if deletable is not None:
            self.deletable = deletable
        if category_name is not None:
            self.category_name = category_name

    @property
    def title(self):
        r"""Gets the title of this SnapshotsVO.

        快照标题。

        :return: The title of this SnapshotsVO.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this SnapshotsVO.

        快照标题。

        :param title: The title of this SnapshotsVO.
        :type title: str
        """
        self._title = title

    @property
    def issue_id(self):
        r"""Gets the issue_id of this SnapshotsVO.

        工作项ID。

        :return: The issue_id of this SnapshotsVO.
        :rtype: str
        """
        return self._issue_id

    @issue_id.setter
    def issue_id(self, issue_id):
        r"""Sets the issue_id of this SnapshotsVO.

        工作项ID。

        :param issue_id: The issue_id of this SnapshotsVO.
        :type issue_id: str
        """
        self._issue_id = issue_id

    @property
    def snapshot2workitem(self):
        r"""Gets the snapshot2workitem of this SnapshotsVO.

        快照记录工作项。键为工作项类型编码（如 Bug、IR），值为 IssueVO 对象或工作项ID字符串。

        :return: The snapshot2workitem of this SnapshotsVO.
        :rtype: object
        """
        return self._snapshot2workitem

    @snapshot2workitem.setter
    def snapshot2workitem(self, snapshot2workitem):
        r"""Sets the snapshot2workitem of this SnapshotsVO.

        快照记录工作项。键为工作项类型编码（如 Bug、IR），值为 IssueVO 对象或工作项ID字符串。

        :param snapshot2workitem: The snapshot2workitem of this SnapshotsVO.
        :type snapshot2workitem: object
        """
        self._snapshot2workitem = snapshot2workitem

    @property
    def created_by(self):
        r"""Gets the created_by of this SnapshotsVO.

        :return: The created_by of this SnapshotsVO.
        :rtype: :class:`huaweicloudsdkprojectman.v4.UserVO`
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        r"""Sets the created_by of this SnapshotsVO.

        :param created_by: The created_by of this SnapshotsVO.
        :type created_by: :class:`huaweicloudsdkprojectman.v4.UserVO`
        """
        self._created_by = created_by

    @property
    def modified_by(self):
        r"""Gets the modified_by of this SnapshotsVO.

        :return: The modified_by of this SnapshotsVO.
        :rtype: :class:`huaweicloudsdkprojectman.v4.UserVO`
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        r"""Sets the modified_by of this SnapshotsVO.

        :param modified_by: The modified_by of this SnapshotsVO.
        :type modified_by: :class:`huaweicloudsdkprojectman.v4.UserVO`
        """
        self._modified_by = modified_by

    @property
    def category(self):
        r"""Gets the category of this SnapshotsVO.

        工作项类型。

        :return: The category of this SnapshotsVO.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this SnapshotsVO.

        工作项类型。

        :param category: The category of this SnapshotsVO.
        :type category: str
        """
        self._category = category

    @property
    def description(self):
        r"""Gets the description of this SnapshotsVO.

        描述信息。

        :return: The description of this SnapshotsVO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this SnapshotsVO.

        描述信息。

        :param description: The description of this SnapshotsVO.
        :type description: str
        """
        self._description = description

    @property
    def path(self):
        r"""Gets the path of this SnapshotsVO.

        工作项父子挂载路径。

        :return: The path of this SnapshotsVO.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this SnapshotsVO.

        工作项父子挂载路径。

        :param path: The path of this SnapshotsVO.
        :type path: str
        """
        self._path = path

    @property
    def region(self):
        r"""Gets the region of this SnapshotsVO.

        区域。

        :return: The region of this SnapshotsVO.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this SnapshotsVO.

        区域。

        :param region: The region of this SnapshotsVO.
        :type region: str
        """
        self._region = region

    @property
    def id(self):
        r"""Gets the id of this SnapshotsVO.

        快照ID。

        :return: The id of this SnapshotsVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SnapshotsVO.

        快照ID。

        :param id: The id of this SnapshotsVO.
        :type id: str
        """
        self._id = id

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this SnapshotsVO.

        租户ID。

        :return: The tenant_id of this SnapshotsVO.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this SnapshotsVO.

        租户ID。

        :param tenant_id: The tenant_id of this SnapshotsVO.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def created_date(self):
        r"""Gets the created_date of this SnapshotsVO.

        快照创建时间，unix时间戳，单位：毫秒。

        :return: The created_date of this SnapshotsVO.
        :rtype: str
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        r"""Sets the created_date of this SnapshotsVO.

        快照创建时间，unix时间戳，单位：毫秒。

        :param created_date: The created_date of this SnapshotsVO.
        :type created_date: str
        """
        self._created_date = created_date

    @property
    def modified_date(self):
        r"""Gets the modified_date of this SnapshotsVO.

        快照最后修改时间，unix时间戳，单位：毫秒。

        :return: The modified_date of this SnapshotsVO.
        :rtype: str
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        r"""Sets the modified_date of this SnapshotsVO.

        快照最后修改时间，unix时间戳，单位：毫秒。

        :param modified_date: The modified_date of this SnapshotsVO.
        :type modified_date: str
        """
        self._modified_date = modified_date

    @property
    def domain_id(self):
        r"""Gets the domain_id of this SnapshotsVO.

        项目空间ID。

        :return: The domain_id of this SnapshotsVO.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this SnapshotsVO.

        项目空间ID。

        :param domain_id: The domain_id of this SnapshotsVO.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def type(self):
        r"""Gets the type of this SnapshotsVO.

        快照类型。

        :return: The type of this SnapshotsVO.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this SnapshotsVO.

        快照类型。

        :param type: The type of this SnapshotsVO.
        :type type: str
        """
        self._type = type

    @property
    def snap_base_info_id(self):
        r"""Gets the snap_base_info_id of this SnapshotsVO.

        快照基础信息ID。

        :return: The snap_base_info_id of this SnapshotsVO.
        :rtype: str
        """
        return self._snap_base_info_id

    @snap_base_info_id.setter
    def snap_base_info_id(self, snap_base_info_id):
        r"""Sets the snap_base_info_id of this SnapshotsVO.

        快照基础信息ID。

        :param snap_base_info_id: The snap_base_info_id of this SnapshotsVO.
        :type snap_base_info_id: str
        """
        self._snap_base_info_id = snap_base_info_id

    @property
    def issue_category(self):
        r"""Gets the issue_category of this SnapshotsVO.

        工作项类型编码。

        :return: The issue_category of this SnapshotsVO.
        :rtype: str
        """
        return self._issue_category

    @issue_category.setter
    def issue_category(self, issue_category):
        r"""Sets the issue_category of this SnapshotsVO.

        工作项类型编码。

        :param issue_category: The issue_category of this SnapshotsVO.
        :type issue_category: str
        """
        self._issue_category = issue_category

    @property
    def parent_id(self):
        r"""Gets the parent_id of this SnapshotsVO.

        父工作项ID。

        :return: The parent_id of this SnapshotsVO.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this SnapshotsVO.

        父工作项ID。

        :param parent_id: The parent_id of this SnapshotsVO.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def root_id(self):
        r"""Gets the root_id of this SnapshotsVO.

        根工作项ID。

        :return: The root_id of this SnapshotsVO.
        :rtype: str
        """
        return self._root_id

    @root_id.setter
    def root_id(self, root_id):
        r"""Sets the root_id of this SnapshotsVO.

        根工作项ID。

        :param root_id: The root_id of this SnapshotsVO.
        :type root_id: str
        """
        self._root_id = root_id

    @property
    def parent_full_path(self):
        r"""Gets the parent_full_path of this SnapshotsVO.

        父工作项完整路径。

        :return: The parent_full_path of this SnapshotsVO.
        :rtype: str
        """
        return self._parent_full_path

    @parent_full_path.setter
    def parent_full_path(self, parent_full_path):
        r"""Sets the parent_full_path of this SnapshotsVO.

        父工作项完整路径。

        :param parent_full_path: The parent_full_path of this SnapshotsVO.
        :type parent_full_path: str
        """
        self._parent_full_path = parent_full_path

    @property
    def parent_path(self):
        r"""Gets the parent_path of this SnapshotsVO.

        父工作项路径。

        :return: The parent_path of this SnapshotsVO.
        :rtype: str
        """
        return self._parent_path

    @parent_path.setter
    def parent_path(self, parent_path):
        r"""Sets the parent_path of this SnapshotsVO.

        父工作项路径。

        :param parent_path: The parent_path of this SnapshotsVO.
        :type parent_path: str
        """
        self._parent_path = parent_path

    @property
    def full_path(self):
        r"""Gets the full_path of this SnapshotsVO.

        工作项完整路径。

        :return: The full_path of this SnapshotsVO.
        :rtype: str
        """
        return self._full_path

    @full_path.setter
    def full_path(self, full_path):
        r"""Sets the full_path of this SnapshotsVO.

        工作项完整路径。

        :param full_path: The full_path of this SnapshotsVO.
        :type full_path: str
        """
        self._full_path = full_path

    @property
    def version_number(self):
        r"""Gets the version_number of this SnapshotsVO.

        快照版本号。

        :return: The version_number of this SnapshotsVO.
        :rtype: int
        """
        return self._version_number

    @version_number.setter
    def version_number(self, version_number):
        r"""Sets the version_number of this SnapshotsVO.

        快照版本号。

        :param version_number: The version_number of this SnapshotsVO.
        :type version_number: int
        """
        self._version_number = version_number

    @property
    def deletable(self):
        r"""Gets the deletable of this SnapshotsVO.

        是否可删除。

        :return: The deletable of this SnapshotsVO.
        :rtype: bool
        """
        return self._deletable

    @deletable.setter
    def deletable(self, deletable):
        r"""Sets the deletable of this SnapshotsVO.

        是否可删除。

        :param deletable: The deletable of this SnapshotsVO.
        :type deletable: bool
        """
        self._deletable = deletable

    @property
    def category_name(self):
        r"""Gets the category_name of this SnapshotsVO.

        工作项类型名称。

        :return: The category_name of this SnapshotsVO.
        :rtype: str
        """
        return self._category_name

    @category_name.setter
    def category_name(self, category_name):
        r"""Sets the category_name of this SnapshotsVO.

        工作项类型名称。

        :param category_name: The category_name of this SnapshotsVO.
        :type category_name: str
        """
        self._category_name = category_name

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SnapshotsVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
