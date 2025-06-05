# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CategoryInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'guid': 'str',
        'name': 'str',
        'description': 'str',
        'code': 'str',
        'path': 'str',
        'alias': 'str',
        'level': 'str',
        'ordinal': 'int',
        'name_eng': 'str',
        'qualified_name': 'str',
        'create_time': 'int',
        'update_time': 'int',
        'business_meaning': 'str',
        'parent_guid': 'str',
        'department': 'str',
        'data_owner': 'str',
        'data_steward': 'str',
        'database': 'list[str]',
        'obs_bucket': 'str',
        'obs_encrypt_bucket': 'str',
        'workspace': 'list[str]',
        'children': 'list[CategoryInfo]'
    }

    attribute_map = {
        'guid': 'guid',
        'name': 'name',
        'description': 'description',
        'code': 'code',
        'path': 'path',
        'alias': 'alias',
        'level': 'level',
        'ordinal': 'ordinal',
        'name_eng': 'name_eng',
        'qualified_name': 'qualified_name',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'business_meaning': 'business_meaning',
        'parent_guid': 'parent_guid',
        'department': 'department',
        'data_owner': 'data_owner',
        'data_steward': 'data_steward',
        'database': 'database',
        'obs_bucket': 'obs_bucket',
        'obs_encrypt_bucket': 'obs_encrypt_bucket',
        'workspace': 'workspace',
        'children': 'children'
    }

    def __init__(self, guid=None, name=None, description=None, code=None, path=None, alias=None, level=None, ordinal=None, name_eng=None, qualified_name=None, create_time=None, update_time=None, business_meaning=None, parent_guid=None, department=None, data_owner=None, data_steward=None, database=None, obs_bucket=None, obs_encrypt_bucket=None, workspace=None, children=None):
        r"""CategoryInfo

        The model defined in huaweicloud sdk

        :param guid: 主题目录guid。
        :type guid: str
        :param name: 主题目录名称。
        :type name: str
        :param description: 主题目录描述信息。
        :type description: str
        :param code: 主题目录编码。
        :type code: str
        :param path: 主题目录路径。
        :type path: str
        :param alias: 主题目录别名。
        :type alias: str
        :param level: 主题目录级别。
        :type level: str
        :param ordinal: 主题目录排序。
        :type ordinal: int
        :param name_eng: 主题目录英文名称。
        :type name_eng: str
        :param qualified_name: 主题目录唯一标识名称。
        :type qualified_name: str
        :param create_time: 资产创建时间。
        :type create_time: int
        :param update_time: 资产修改时间。
        :type update_time: int
        :param business_meaning: 业务意义。
        :type business_meaning: str
        :param parent_guid: 父级目录guid。
        :type parent_guid: str
        :param department: 主题目录部门。
        :type department: str
        :param data_owner: 数据owner所属部门。
        :type data_owner: str
        :param data_steward: 数据管家。
        :type data_steward: str
        :param database: 数据库。
        :type database: list[str]
        :param obs_bucket: obs桶。
        :type obs_bucket: str
        :param obs_encrypt_bucket: obs加密桶。
        :type obs_encrypt_bucket: str
        :param workspace: 所属空间。
        :type workspace: list[str]
        :param children: 子级目录列表。
        :type children: list[:class:`huaweicloudsdkdataartsstudio.v1.CategoryInfo`]
        """
        
        

        self._guid = None
        self._name = None
        self._description = None
        self._code = None
        self._path = None
        self._alias = None
        self._level = None
        self._ordinal = None
        self._name_eng = None
        self._qualified_name = None
        self._create_time = None
        self._update_time = None
        self._business_meaning = None
        self._parent_guid = None
        self._department = None
        self._data_owner = None
        self._data_steward = None
        self._database = None
        self._obs_bucket = None
        self._obs_encrypt_bucket = None
        self._workspace = None
        self._children = None
        self.discriminator = None

        if guid is not None:
            self.guid = guid
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if code is not None:
            self.code = code
        if path is not None:
            self.path = path
        if alias is not None:
            self.alias = alias
        if level is not None:
            self.level = level
        if ordinal is not None:
            self.ordinal = ordinal
        if name_eng is not None:
            self.name_eng = name_eng
        if qualified_name is not None:
            self.qualified_name = qualified_name
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if business_meaning is not None:
            self.business_meaning = business_meaning
        if parent_guid is not None:
            self.parent_guid = parent_guid
        if department is not None:
            self.department = department
        if data_owner is not None:
            self.data_owner = data_owner
        if data_steward is not None:
            self.data_steward = data_steward
        if database is not None:
            self.database = database
        if obs_bucket is not None:
            self.obs_bucket = obs_bucket
        if obs_encrypt_bucket is not None:
            self.obs_encrypt_bucket = obs_encrypt_bucket
        if workspace is not None:
            self.workspace = workspace
        if children is not None:
            self.children = children

    @property
    def guid(self):
        r"""Gets the guid of this CategoryInfo.

        主题目录guid。

        :return: The guid of this CategoryInfo.
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        r"""Sets the guid of this CategoryInfo.

        主题目录guid。

        :param guid: The guid of this CategoryInfo.
        :type guid: str
        """
        self._guid = guid

    @property
    def name(self):
        r"""Gets the name of this CategoryInfo.

        主题目录名称。

        :return: The name of this CategoryInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CategoryInfo.

        主题目录名称。

        :param name: The name of this CategoryInfo.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CategoryInfo.

        主题目录描述信息。

        :return: The description of this CategoryInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CategoryInfo.

        主题目录描述信息。

        :param description: The description of this CategoryInfo.
        :type description: str
        """
        self._description = description

    @property
    def code(self):
        r"""Gets the code of this CategoryInfo.

        主题目录编码。

        :return: The code of this CategoryInfo.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this CategoryInfo.

        主题目录编码。

        :param code: The code of this CategoryInfo.
        :type code: str
        """
        self._code = code

    @property
    def path(self):
        r"""Gets the path of this CategoryInfo.

        主题目录路径。

        :return: The path of this CategoryInfo.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this CategoryInfo.

        主题目录路径。

        :param path: The path of this CategoryInfo.
        :type path: str
        """
        self._path = path

    @property
    def alias(self):
        r"""Gets the alias of this CategoryInfo.

        主题目录别名。

        :return: The alias of this CategoryInfo.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        r"""Sets the alias of this CategoryInfo.

        主题目录别名。

        :param alias: The alias of this CategoryInfo.
        :type alias: str
        """
        self._alias = alias

    @property
    def level(self):
        r"""Gets the level of this CategoryInfo.

        主题目录级别。

        :return: The level of this CategoryInfo.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this CategoryInfo.

        主题目录级别。

        :param level: The level of this CategoryInfo.
        :type level: str
        """
        self._level = level

    @property
    def ordinal(self):
        r"""Gets the ordinal of this CategoryInfo.

        主题目录排序。

        :return: The ordinal of this CategoryInfo.
        :rtype: int
        """
        return self._ordinal

    @ordinal.setter
    def ordinal(self, ordinal):
        r"""Sets the ordinal of this CategoryInfo.

        主题目录排序。

        :param ordinal: The ordinal of this CategoryInfo.
        :type ordinal: int
        """
        self._ordinal = ordinal

    @property
    def name_eng(self):
        r"""Gets the name_eng of this CategoryInfo.

        主题目录英文名称。

        :return: The name_eng of this CategoryInfo.
        :rtype: str
        """
        return self._name_eng

    @name_eng.setter
    def name_eng(self, name_eng):
        r"""Sets the name_eng of this CategoryInfo.

        主题目录英文名称。

        :param name_eng: The name_eng of this CategoryInfo.
        :type name_eng: str
        """
        self._name_eng = name_eng

    @property
    def qualified_name(self):
        r"""Gets the qualified_name of this CategoryInfo.

        主题目录唯一标识名称。

        :return: The qualified_name of this CategoryInfo.
        :rtype: str
        """
        return self._qualified_name

    @qualified_name.setter
    def qualified_name(self, qualified_name):
        r"""Sets the qualified_name of this CategoryInfo.

        主题目录唯一标识名称。

        :param qualified_name: The qualified_name of this CategoryInfo.
        :type qualified_name: str
        """
        self._qualified_name = qualified_name

    @property
    def create_time(self):
        r"""Gets the create_time of this CategoryInfo.

        资产创建时间。

        :return: The create_time of this CategoryInfo.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this CategoryInfo.

        资产创建时间。

        :param create_time: The create_time of this CategoryInfo.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this CategoryInfo.

        资产修改时间。

        :return: The update_time of this CategoryInfo.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this CategoryInfo.

        资产修改时间。

        :param update_time: The update_time of this CategoryInfo.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def business_meaning(self):
        r"""Gets the business_meaning of this CategoryInfo.

        业务意义。

        :return: The business_meaning of this CategoryInfo.
        :rtype: str
        """
        return self._business_meaning

    @business_meaning.setter
    def business_meaning(self, business_meaning):
        r"""Sets the business_meaning of this CategoryInfo.

        业务意义。

        :param business_meaning: The business_meaning of this CategoryInfo.
        :type business_meaning: str
        """
        self._business_meaning = business_meaning

    @property
    def parent_guid(self):
        r"""Gets the parent_guid of this CategoryInfo.

        父级目录guid。

        :return: The parent_guid of this CategoryInfo.
        :rtype: str
        """
        return self._parent_guid

    @parent_guid.setter
    def parent_guid(self, parent_guid):
        r"""Sets the parent_guid of this CategoryInfo.

        父级目录guid。

        :param parent_guid: The parent_guid of this CategoryInfo.
        :type parent_guid: str
        """
        self._parent_guid = parent_guid

    @property
    def department(self):
        r"""Gets the department of this CategoryInfo.

        主题目录部门。

        :return: The department of this CategoryInfo.
        :rtype: str
        """
        return self._department

    @department.setter
    def department(self, department):
        r"""Sets the department of this CategoryInfo.

        主题目录部门。

        :param department: The department of this CategoryInfo.
        :type department: str
        """
        self._department = department

    @property
    def data_owner(self):
        r"""Gets the data_owner of this CategoryInfo.

        数据owner所属部门。

        :return: The data_owner of this CategoryInfo.
        :rtype: str
        """
        return self._data_owner

    @data_owner.setter
    def data_owner(self, data_owner):
        r"""Sets the data_owner of this CategoryInfo.

        数据owner所属部门。

        :param data_owner: The data_owner of this CategoryInfo.
        :type data_owner: str
        """
        self._data_owner = data_owner

    @property
    def data_steward(self):
        r"""Gets the data_steward of this CategoryInfo.

        数据管家。

        :return: The data_steward of this CategoryInfo.
        :rtype: str
        """
        return self._data_steward

    @data_steward.setter
    def data_steward(self, data_steward):
        r"""Sets the data_steward of this CategoryInfo.

        数据管家。

        :param data_steward: The data_steward of this CategoryInfo.
        :type data_steward: str
        """
        self._data_steward = data_steward

    @property
    def database(self):
        r"""Gets the database of this CategoryInfo.

        数据库。

        :return: The database of this CategoryInfo.
        :rtype: list[str]
        """
        return self._database

    @database.setter
    def database(self, database):
        r"""Sets the database of this CategoryInfo.

        数据库。

        :param database: The database of this CategoryInfo.
        :type database: list[str]
        """
        self._database = database

    @property
    def obs_bucket(self):
        r"""Gets the obs_bucket of this CategoryInfo.

        obs桶。

        :return: The obs_bucket of this CategoryInfo.
        :rtype: str
        """
        return self._obs_bucket

    @obs_bucket.setter
    def obs_bucket(self, obs_bucket):
        r"""Sets the obs_bucket of this CategoryInfo.

        obs桶。

        :param obs_bucket: The obs_bucket of this CategoryInfo.
        :type obs_bucket: str
        """
        self._obs_bucket = obs_bucket

    @property
    def obs_encrypt_bucket(self):
        r"""Gets the obs_encrypt_bucket of this CategoryInfo.

        obs加密桶。

        :return: The obs_encrypt_bucket of this CategoryInfo.
        :rtype: str
        """
        return self._obs_encrypt_bucket

    @obs_encrypt_bucket.setter
    def obs_encrypt_bucket(self, obs_encrypt_bucket):
        r"""Sets the obs_encrypt_bucket of this CategoryInfo.

        obs加密桶。

        :param obs_encrypt_bucket: The obs_encrypt_bucket of this CategoryInfo.
        :type obs_encrypt_bucket: str
        """
        self._obs_encrypt_bucket = obs_encrypt_bucket

    @property
    def workspace(self):
        r"""Gets the workspace of this CategoryInfo.

        所属空间。

        :return: The workspace of this CategoryInfo.
        :rtype: list[str]
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this CategoryInfo.

        所属空间。

        :param workspace: The workspace of this CategoryInfo.
        :type workspace: list[str]
        """
        self._workspace = workspace

    @property
    def children(self):
        r"""Gets the children of this CategoryInfo.

        子级目录列表。

        :return: The children of this CategoryInfo.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.CategoryInfo`]
        """
        return self._children

    @children.setter
    def children(self, children):
        r"""Sets the children of this CategoryInfo.

        子级目录列表。

        :param children: The children of this CategoryInfo.
        :type children: list[:class:`huaweicloudsdkdataartsstudio.v1.CategoryInfo`]
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
        if not isinstance(other, CategoryInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
