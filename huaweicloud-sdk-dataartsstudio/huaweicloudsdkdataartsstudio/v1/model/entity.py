# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Entity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version': 'float',
        'relationship_attributes': 'object',
        'super_type_names': 'list[str]',
        'business_attributes': 'object',
        'multi_attributes': 'object',
        'privilege_info': 'EntityPrivilegeInfo',
        'extended_attributes': 'object',
        'guid': 'str',
        'type_name': 'str',
        'type_display_name': 'str',
        'display_text': 'str',
        'attributes': 'object',
        'updated_attributes': 'list[str]',
        'project_id': 'str',
        'domain_id': 'str',
        'instance_id': 'list[str]',
        'workspace_id': 'list[str]',
        'status': 'str',
        'created_by': 'str',
        'updated_by': 'str',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'version': 'version',
        'relationship_attributes': 'relationship_attributes',
        'super_type_names': 'super_type_names',
        'business_attributes': 'business_attributes',
        'multi_attributes': 'multi_attributes',
        'privilege_info': 'privilege_info',
        'extended_attributes': 'extended_attributes',
        'guid': 'guid',
        'type_name': 'type_name',
        'type_display_name': 'type_display_name',
        'display_text': 'display_text',
        'attributes': 'attributes',
        'updated_attributes': 'updated_attributes',
        'project_id': 'project_id',
        'domain_id': 'domain_id',
        'instance_id': 'instance_id',
        'workspace_id': 'workspace_id',
        'status': 'status',
        'created_by': 'created_by',
        'updated_by': 'updated_by',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, version=None, relationship_attributes=None, super_type_names=None, business_attributes=None, multi_attributes=None, privilege_info=None, extended_attributes=None, guid=None, type_name=None, type_display_name=None, display_text=None, attributes=None, updated_attributes=None, project_id=None, domain_id=None, instance_id=None, workspace_id=None, status=None, created_by=None, updated_by=None, create_time=None, update_time=None):
        r"""Entity

        The model defined in huaweicloud sdk

        :param version: 数据版本
        :type version: float
        :param relationship_attributes: 关联关系属性，数据类型Map&lt;String, Object&gt;
        :type relationship_attributes: object
        :param super_type_names: 父类资产类型
        :type super_type_names: list[str]
        :param business_attributes: 业务属性，数据类型Map&lt;String, Map&lt;String, Object&gt;&gt;
        :type business_attributes: object
        :param multi_attributes: 承担密级和标签的多值对象数据结构，数据结构Map&lt;String, List&lt;Map&lt;String, Object&gt;&gt;&gt;
        :type multi_attributes: object
        :param privilege_info: 
        :type privilege_info: :class:`huaweicloudsdkdataartsstudio.v1.EntityPrivilegeInfo`
        :param extended_attributes: 拓展属性，数据结构Map&lt;String, Object&gt;
        :type extended_attributes: object
        :param guid: 资产guid
        :type guid: str
        :param type_name: 资产类型名称
        :type type_name: str
        :param type_display_name: 类型展示名称
        :type type_display_name: str
        :param display_text: 展示名称
        :type display_text: str
        :param attributes: 资产属性，Map&lt;String, Object&gt;
        :type attributes: object
        :param updated_attributes: 修改属性列表
        :type updated_attributes: list[str]
        :param project_id: 项目id
        :type project_id: str
        :param domain_id: 主账号id
        :type domain_id: str
        :param instance_id: 实例化id
        :type instance_id: list[str]
        :param workspace_id: 空间id列表
        :type workspace_id: list[str]
        :param status: 状态
        :type status: str
        :param created_by: 创建人
        :type created_by: str
        :param updated_by: 修改人
        :type updated_by: str
        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 修改时间
        :type update_time: str
        """
        
        

        self._version = None
        self._relationship_attributes = None
        self._super_type_names = None
        self._business_attributes = None
        self._multi_attributes = None
        self._privilege_info = None
        self._extended_attributes = None
        self._guid = None
        self._type_name = None
        self._type_display_name = None
        self._display_text = None
        self._attributes = None
        self._updated_attributes = None
        self._project_id = None
        self._domain_id = None
        self._instance_id = None
        self._workspace_id = None
        self._status = None
        self._created_by = None
        self._updated_by = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if relationship_attributes is not None:
            self.relationship_attributes = relationship_attributes
        if super_type_names is not None:
            self.super_type_names = super_type_names
        if business_attributes is not None:
            self.business_attributes = business_attributes
        if multi_attributes is not None:
            self.multi_attributes = multi_attributes
        if privilege_info is not None:
            self.privilege_info = privilege_info
        if extended_attributes is not None:
            self.extended_attributes = extended_attributes
        if guid is not None:
            self.guid = guid
        if type_name is not None:
            self.type_name = type_name
        if type_display_name is not None:
            self.type_display_name = type_display_name
        if display_text is not None:
            self.display_text = display_text
        if attributes is not None:
            self.attributes = attributes
        if updated_attributes is not None:
            self.updated_attributes = updated_attributes
        if project_id is not None:
            self.project_id = project_id
        if domain_id is not None:
            self.domain_id = domain_id
        if instance_id is not None:
            self.instance_id = instance_id
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if status is not None:
            self.status = status
        if created_by is not None:
            self.created_by = created_by
        if updated_by is not None:
            self.updated_by = updated_by
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def version(self):
        r"""Gets the version of this Entity.

        数据版本

        :return: The version of this Entity.
        :rtype: float
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this Entity.

        数据版本

        :param version: The version of this Entity.
        :type version: float
        """
        self._version = version

    @property
    def relationship_attributes(self):
        r"""Gets the relationship_attributes of this Entity.

        关联关系属性，数据类型Map<String, Object>

        :return: The relationship_attributes of this Entity.
        :rtype: object
        """
        return self._relationship_attributes

    @relationship_attributes.setter
    def relationship_attributes(self, relationship_attributes):
        r"""Sets the relationship_attributes of this Entity.

        关联关系属性，数据类型Map<String, Object>

        :param relationship_attributes: The relationship_attributes of this Entity.
        :type relationship_attributes: object
        """
        self._relationship_attributes = relationship_attributes

    @property
    def super_type_names(self):
        r"""Gets the super_type_names of this Entity.

        父类资产类型

        :return: The super_type_names of this Entity.
        :rtype: list[str]
        """
        return self._super_type_names

    @super_type_names.setter
    def super_type_names(self, super_type_names):
        r"""Sets the super_type_names of this Entity.

        父类资产类型

        :param super_type_names: The super_type_names of this Entity.
        :type super_type_names: list[str]
        """
        self._super_type_names = super_type_names

    @property
    def business_attributes(self):
        r"""Gets the business_attributes of this Entity.

        业务属性，数据类型Map<String, Map<String, Object>>

        :return: The business_attributes of this Entity.
        :rtype: object
        """
        return self._business_attributes

    @business_attributes.setter
    def business_attributes(self, business_attributes):
        r"""Sets the business_attributes of this Entity.

        业务属性，数据类型Map<String, Map<String, Object>>

        :param business_attributes: The business_attributes of this Entity.
        :type business_attributes: object
        """
        self._business_attributes = business_attributes

    @property
    def multi_attributes(self):
        r"""Gets the multi_attributes of this Entity.

        承担密级和标签的多值对象数据结构，数据结构Map<String, List<Map<String, Object>>>

        :return: The multi_attributes of this Entity.
        :rtype: object
        """
        return self._multi_attributes

    @multi_attributes.setter
    def multi_attributes(self, multi_attributes):
        r"""Sets the multi_attributes of this Entity.

        承担密级和标签的多值对象数据结构，数据结构Map<String, List<Map<String, Object>>>

        :param multi_attributes: The multi_attributes of this Entity.
        :type multi_attributes: object
        """
        self._multi_attributes = multi_attributes

    @property
    def privilege_info(self):
        r"""Gets the privilege_info of this Entity.

        :return: The privilege_info of this Entity.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.EntityPrivilegeInfo`
        """
        return self._privilege_info

    @privilege_info.setter
    def privilege_info(self, privilege_info):
        r"""Sets the privilege_info of this Entity.

        :param privilege_info: The privilege_info of this Entity.
        :type privilege_info: :class:`huaweicloudsdkdataartsstudio.v1.EntityPrivilegeInfo`
        """
        self._privilege_info = privilege_info

    @property
    def extended_attributes(self):
        r"""Gets the extended_attributes of this Entity.

        拓展属性，数据结构Map<String, Object>

        :return: The extended_attributes of this Entity.
        :rtype: object
        """
        return self._extended_attributes

    @extended_attributes.setter
    def extended_attributes(self, extended_attributes):
        r"""Sets the extended_attributes of this Entity.

        拓展属性，数据结构Map<String, Object>

        :param extended_attributes: The extended_attributes of this Entity.
        :type extended_attributes: object
        """
        self._extended_attributes = extended_attributes

    @property
    def guid(self):
        r"""Gets the guid of this Entity.

        资产guid

        :return: The guid of this Entity.
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        r"""Sets the guid of this Entity.

        资产guid

        :param guid: The guid of this Entity.
        :type guid: str
        """
        self._guid = guid

    @property
    def type_name(self):
        r"""Gets the type_name of this Entity.

        资产类型名称

        :return: The type_name of this Entity.
        :rtype: str
        """
        return self._type_name

    @type_name.setter
    def type_name(self, type_name):
        r"""Sets the type_name of this Entity.

        资产类型名称

        :param type_name: The type_name of this Entity.
        :type type_name: str
        """
        self._type_name = type_name

    @property
    def type_display_name(self):
        r"""Gets the type_display_name of this Entity.

        类型展示名称

        :return: The type_display_name of this Entity.
        :rtype: str
        """
        return self._type_display_name

    @type_display_name.setter
    def type_display_name(self, type_display_name):
        r"""Sets the type_display_name of this Entity.

        类型展示名称

        :param type_display_name: The type_display_name of this Entity.
        :type type_display_name: str
        """
        self._type_display_name = type_display_name

    @property
    def display_text(self):
        r"""Gets the display_text of this Entity.

        展示名称

        :return: The display_text of this Entity.
        :rtype: str
        """
        return self._display_text

    @display_text.setter
    def display_text(self, display_text):
        r"""Sets the display_text of this Entity.

        展示名称

        :param display_text: The display_text of this Entity.
        :type display_text: str
        """
        self._display_text = display_text

    @property
    def attributes(self):
        r"""Gets the attributes of this Entity.

        资产属性，Map<String, Object>

        :return: The attributes of this Entity.
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        r"""Sets the attributes of this Entity.

        资产属性，Map<String, Object>

        :param attributes: The attributes of this Entity.
        :type attributes: object
        """
        self._attributes = attributes

    @property
    def updated_attributes(self):
        r"""Gets the updated_attributes of this Entity.

        修改属性列表

        :return: The updated_attributes of this Entity.
        :rtype: list[str]
        """
        return self._updated_attributes

    @updated_attributes.setter
    def updated_attributes(self, updated_attributes):
        r"""Sets the updated_attributes of this Entity.

        修改属性列表

        :param updated_attributes: The updated_attributes of this Entity.
        :type updated_attributes: list[str]
        """
        self._updated_attributes = updated_attributes

    @property
    def project_id(self):
        r"""Gets the project_id of this Entity.

        项目id

        :return: The project_id of this Entity.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this Entity.

        项目id

        :param project_id: The project_id of this Entity.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this Entity.

        主账号id

        :return: The domain_id of this Entity.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this Entity.

        主账号id

        :param domain_id: The domain_id of this Entity.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this Entity.

        实例化id

        :return: The instance_id of this Entity.
        :rtype: list[str]
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this Entity.

        实例化id

        :param instance_id: The instance_id of this Entity.
        :type instance_id: list[str]
        """
        self._instance_id = instance_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this Entity.

        空间id列表

        :return: The workspace_id of this Entity.
        :rtype: list[str]
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this Entity.

        空间id列表

        :param workspace_id: The workspace_id of this Entity.
        :type workspace_id: list[str]
        """
        self._workspace_id = workspace_id

    @property
    def status(self):
        r"""Gets the status of this Entity.

        状态

        :return: The status of this Entity.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this Entity.

        状态

        :param status: The status of this Entity.
        :type status: str
        """
        self._status = status

    @property
    def created_by(self):
        r"""Gets the created_by of this Entity.

        创建人

        :return: The created_by of this Entity.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        r"""Sets the created_by of this Entity.

        创建人

        :param created_by: The created_by of this Entity.
        :type created_by: str
        """
        self._created_by = created_by

    @property
    def updated_by(self):
        r"""Gets the updated_by of this Entity.

        修改人

        :return: The updated_by of this Entity.
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        r"""Sets the updated_by of this Entity.

        修改人

        :param updated_by: The updated_by of this Entity.
        :type updated_by: str
        """
        self._updated_by = updated_by

    @property
    def create_time(self):
        r"""Gets the create_time of this Entity.

        创建时间

        :return: The create_time of this Entity.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this Entity.

        创建时间

        :param create_time: The create_time of this Entity.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this Entity.

        修改时间

        :return: The update_time of this Entity.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this Entity.

        修改时间

        :param update_time: The update_time of this Entity.
        :type update_time: str
        """
        self._update_time = update_time

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
        if not isinstance(other, Entity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
