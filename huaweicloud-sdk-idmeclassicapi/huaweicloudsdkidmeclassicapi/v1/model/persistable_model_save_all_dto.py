# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PersistableModelSaveAllDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'acl_entry': 'str',
        'cls_attrs': 'list[object]',
        'create_time': 'str',
        'creator': 'str',
        'disable_flag': 'bool',
        'ext_attr_map': 'object',
        'ext_attrs': 'list[EXAValueParamDTO]',
        'folder': 'ObjectReferenceParamDTO',
        'id': 'str',
        'last_update_time': 'str',
        'lifecycle_state': 'ObjectReferenceParamDTO',
        'lifecycle_template': 'ObjectReferenceParamDTO',
        'modifier': 'str',
        'need_set_null_attrs': 'list[str]',
        'owner': 'str',
        'parent_node': 'ObjectReferenceParamDTO',
        'rdm_extension_type': 'str',
        'tenant': 'ObjectReferenceParamDTO',
        'unique_key': 'str'
    }

    attribute_map = {
        'acl_entry': 'aclEntry',
        'cls_attrs': 'clsAttrs',
        'create_time': 'createTime',
        'creator': 'creator',
        'disable_flag': 'disableFlag',
        'ext_attr_map': 'extAttrMap',
        'ext_attrs': 'extAttrs',
        'folder': 'folder',
        'id': 'id',
        'last_update_time': 'lastUpdateTime',
        'lifecycle_state': 'lifecycleState',
        'lifecycle_template': 'lifecycleTemplate',
        'modifier': 'modifier',
        'need_set_null_attrs': 'needSetNullAttrs',
        'owner': 'owner',
        'parent_node': 'parentNode',
        'rdm_extension_type': 'rdmExtensionType',
        'tenant': 'tenant',
        'unique_key': 'uniqueKey'
    }

    def __init__(self, acl_entry=None, cls_attrs=None, create_time=None, creator=None, disable_flag=None, ext_attr_map=None, ext_attrs=None, folder=None, id=None, last_update_time=None, lifecycle_state=None, lifecycle_template=None, modifier=None, need_set_null_attrs=None, owner=None, parent_node=None, rdm_extension_type=None, tenant=None, unique_key=None):
        """PersistableModelSaveAllDTO

        The model defined in huaweicloud sdk

        :param acl_entry: 访问控制列表。
        :type acl_entry: str
        :param cls_attrs: 分类属性。
        :type cls_attrs: list[object]
        :param create_time: 创建时间。
        :type create_time: str
        :param creator: 创建者。
        :type creator: str
        :param disable_flag: 失效标识。  - true：失效。  - false：未失效。
        :type disable_flag: bool
        :param ext_attr_map: 扩展属性映射集。
        :type ext_attr_map: object
        :param ext_attrs: 扩展属性列表。
        :type ext_attrs: list[:class:`huaweicloudsdkidmeclassicapi.v1.EXAValueParamDTO`]
        :param folder: 
        :type folder: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceParamDTO`
        :param id: 唯一标识。
        :type id: str
        :param last_update_time: 最后更新时间。
        :type last_update_time: str
        :param lifecycle_state: 
        :type lifecycle_state: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceParamDTO`
        :param lifecycle_template: 
        :type lifecycle_template: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceParamDTO`
        :param modifier: 更新者。
        :type modifier: str
        :param need_set_null_attrs: 设置NULL值的属性名称。
        :type need_set_null_attrs: list[str]
        :param owner: 拥有者。
        :type owner: str
        :param parent_node: 
        :type parent_node: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceParamDTO`
        :param rdm_extension_type: 扩展类型。
        :type rdm_extension_type: str
        :param tenant: 
        :type tenant: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceParamDTO`
        :param unique_key: 示例模型的唯一键属性。
        :type unique_key: str
        """
        
        

        self._acl_entry = None
        self._cls_attrs = None
        self._create_time = None
        self._creator = None
        self._disable_flag = None
        self._ext_attr_map = None
        self._ext_attrs = None
        self._folder = None
        self._id = None
        self._last_update_time = None
        self._lifecycle_state = None
        self._lifecycle_template = None
        self._modifier = None
        self._need_set_null_attrs = None
        self._owner = None
        self._parent_node = None
        self._rdm_extension_type = None
        self._tenant = None
        self._unique_key = None
        self.discriminator = None

        if acl_entry is not None:
            self.acl_entry = acl_entry
        if cls_attrs is not None:
            self.cls_attrs = cls_attrs
        if create_time is not None:
            self.create_time = create_time
        if creator is not None:
            self.creator = creator
        if disable_flag is not None:
            self.disable_flag = disable_flag
        if ext_attr_map is not None:
            self.ext_attr_map = ext_attr_map
        if ext_attrs is not None:
            self.ext_attrs = ext_attrs
        if folder is not None:
            self.folder = folder
        if id is not None:
            self.id = id
        if last_update_time is not None:
            self.last_update_time = last_update_time
        if lifecycle_state is not None:
            self.lifecycle_state = lifecycle_state
        if lifecycle_template is not None:
            self.lifecycle_template = lifecycle_template
        if modifier is not None:
            self.modifier = modifier
        if need_set_null_attrs is not None:
            self.need_set_null_attrs = need_set_null_attrs
        if owner is not None:
            self.owner = owner
        if parent_node is not None:
            self.parent_node = parent_node
        if rdm_extension_type is not None:
            self.rdm_extension_type = rdm_extension_type
        if tenant is not None:
            self.tenant = tenant
        if unique_key is not None:
            self.unique_key = unique_key

    @property
    def acl_entry(self):
        """Gets the acl_entry of this PersistableModelSaveAllDTO.

        访问控制列表。

        :return: The acl_entry of this PersistableModelSaveAllDTO.
        :rtype: str
        """
        return self._acl_entry

    @acl_entry.setter
    def acl_entry(self, acl_entry):
        """Sets the acl_entry of this PersistableModelSaveAllDTO.

        访问控制列表。

        :param acl_entry: The acl_entry of this PersistableModelSaveAllDTO.
        :type acl_entry: str
        """
        self._acl_entry = acl_entry

    @property
    def cls_attrs(self):
        """Gets the cls_attrs of this PersistableModelSaveAllDTO.

        分类属性。

        :return: The cls_attrs of this PersistableModelSaveAllDTO.
        :rtype: list[object]
        """
        return self._cls_attrs

    @cls_attrs.setter
    def cls_attrs(self, cls_attrs):
        """Sets the cls_attrs of this PersistableModelSaveAllDTO.

        分类属性。

        :param cls_attrs: The cls_attrs of this PersistableModelSaveAllDTO.
        :type cls_attrs: list[object]
        """
        self._cls_attrs = cls_attrs

    @property
    def create_time(self):
        """Gets the create_time of this PersistableModelSaveAllDTO.

        创建时间。

        :return: The create_time of this PersistableModelSaveAllDTO.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this PersistableModelSaveAllDTO.

        创建时间。

        :param create_time: The create_time of this PersistableModelSaveAllDTO.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def creator(self):
        """Gets the creator of this PersistableModelSaveAllDTO.

        创建者。

        :return: The creator of this PersistableModelSaveAllDTO.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this PersistableModelSaveAllDTO.

        创建者。

        :param creator: The creator of this PersistableModelSaveAllDTO.
        :type creator: str
        """
        self._creator = creator

    @property
    def disable_flag(self):
        """Gets the disable_flag of this PersistableModelSaveAllDTO.

        失效标识。  - true：失效。  - false：未失效。

        :return: The disable_flag of this PersistableModelSaveAllDTO.
        :rtype: bool
        """
        return self._disable_flag

    @disable_flag.setter
    def disable_flag(self, disable_flag):
        """Sets the disable_flag of this PersistableModelSaveAllDTO.

        失效标识。  - true：失效。  - false：未失效。

        :param disable_flag: The disable_flag of this PersistableModelSaveAllDTO.
        :type disable_flag: bool
        """
        self._disable_flag = disable_flag

    @property
    def ext_attr_map(self):
        """Gets the ext_attr_map of this PersistableModelSaveAllDTO.

        扩展属性映射集。

        :return: The ext_attr_map of this PersistableModelSaveAllDTO.
        :rtype: object
        """
        return self._ext_attr_map

    @ext_attr_map.setter
    def ext_attr_map(self, ext_attr_map):
        """Sets the ext_attr_map of this PersistableModelSaveAllDTO.

        扩展属性映射集。

        :param ext_attr_map: The ext_attr_map of this PersistableModelSaveAllDTO.
        :type ext_attr_map: object
        """
        self._ext_attr_map = ext_attr_map

    @property
    def ext_attrs(self):
        """Gets the ext_attrs of this PersistableModelSaveAllDTO.

        扩展属性列表。

        :return: The ext_attrs of this PersistableModelSaveAllDTO.
        :rtype: list[:class:`huaweicloudsdkidmeclassicapi.v1.EXAValueParamDTO`]
        """
        return self._ext_attrs

    @ext_attrs.setter
    def ext_attrs(self, ext_attrs):
        """Sets the ext_attrs of this PersistableModelSaveAllDTO.

        扩展属性列表。

        :param ext_attrs: The ext_attrs of this PersistableModelSaveAllDTO.
        :type ext_attrs: list[:class:`huaweicloudsdkidmeclassicapi.v1.EXAValueParamDTO`]
        """
        self._ext_attrs = ext_attrs

    @property
    def folder(self):
        """Gets the folder of this PersistableModelSaveAllDTO.

        :return: The folder of this PersistableModelSaveAllDTO.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceParamDTO`
        """
        return self._folder

    @folder.setter
    def folder(self, folder):
        """Sets the folder of this PersistableModelSaveAllDTO.

        :param folder: The folder of this PersistableModelSaveAllDTO.
        :type folder: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceParamDTO`
        """
        self._folder = folder

    @property
    def id(self):
        """Gets the id of this PersistableModelSaveAllDTO.

        唯一标识。

        :return: The id of this PersistableModelSaveAllDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PersistableModelSaveAllDTO.

        唯一标识。

        :param id: The id of this PersistableModelSaveAllDTO.
        :type id: str
        """
        self._id = id

    @property
    def last_update_time(self):
        """Gets the last_update_time of this PersistableModelSaveAllDTO.

        最后更新时间。

        :return: The last_update_time of this PersistableModelSaveAllDTO.
        :rtype: str
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        """Sets the last_update_time of this PersistableModelSaveAllDTO.

        最后更新时间。

        :param last_update_time: The last_update_time of this PersistableModelSaveAllDTO.
        :type last_update_time: str
        """
        self._last_update_time = last_update_time

    @property
    def lifecycle_state(self):
        """Gets the lifecycle_state of this PersistableModelSaveAllDTO.

        :return: The lifecycle_state of this PersistableModelSaveAllDTO.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceParamDTO`
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """Sets the lifecycle_state of this PersistableModelSaveAllDTO.

        :param lifecycle_state: The lifecycle_state of this PersistableModelSaveAllDTO.
        :type lifecycle_state: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceParamDTO`
        """
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_template(self):
        """Gets the lifecycle_template of this PersistableModelSaveAllDTO.

        :return: The lifecycle_template of this PersistableModelSaveAllDTO.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceParamDTO`
        """
        return self._lifecycle_template

    @lifecycle_template.setter
    def lifecycle_template(self, lifecycle_template):
        """Sets the lifecycle_template of this PersistableModelSaveAllDTO.

        :param lifecycle_template: The lifecycle_template of this PersistableModelSaveAllDTO.
        :type lifecycle_template: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceParamDTO`
        """
        self._lifecycle_template = lifecycle_template

    @property
    def modifier(self):
        """Gets the modifier of this PersistableModelSaveAllDTO.

        更新者。

        :return: The modifier of this PersistableModelSaveAllDTO.
        :rtype: str
        """
        return self._modifier

    @modifier.setter
    def modifier(self, modifier):
        """Sets the modifier of this PersistableModelSaveAllDTO.

        更新者。

        :param modifier: The modifier of this PersistableModelSaveAllDTO.
        :type modifier: str
        """
        self._modifier = modifier

    @property
    def need_set_null_attrs(self):
        """Gets the need_set_null_attrs of this PersistableModelSaveAllDTO.

        设置NULL值的属性名称。

        :return: The need_set_null_attrs of this PersistableModelSaveAllDTO.
        :rtype: list[str]
        """
        return self._need_set_null_attrs

    @need_set_null_attrs.setter
    def need_set_null_attrs(self, need_set_null_attrs):
        """Sets the need_set_null_attrs of this PersistableModelSaveAllDTO.

        设置NULL值的属性名称。

        :param need_set_null_attrs: The need_set_null_attrs of this PersistableModelSaveAllDTO.
        :type need_set_null_attrs: list[str]
        """
        self._need_set_null_attrs = need_set_null_attrs

    @property
    def owner(self):
        """Gets the owner of this PersistableModelSaveAllDTO.

        拥有者。

        :return: The owner of this PersistableModelSaveAllDTO.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this PersistableModelSaveAllDTO.

        拥有者。

        :param owner: The owner of this PersistableModelSaveAllDTO.
        :type owner: str
        """
        self._owner = owner

    @property
    def parent_node(self):
        """Gets the parent_node of this PersistableModelSaveAllDTO.

        :return: The parent_node of this PersistableModelSaveAllDTO.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceParamDTO`
        """
        return self._parent_node

    @parent_node.setter
    def parent_node(self, parent_node):
        """Sets the parent_node of this PersistableModelSaveAllDTO.

        :param parent_node: The parent_node of this PersistableModelSaveAllDTO.
        :type parent_node: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceParamDTO`
        """
        self._parent_node = parent_node

    @property
    def rdm_extension_type(self):
        """Gets the rdm_extension_type of this PersistableModelSaveAllDTO.

        扩展类型。

        :return: The rdm_extension_type of this PersistableModelSaveAllDTO.
        :rtype: str
        """
        return self._rdm_extension_type

    @rdm_extension_type.setter
    def rdm_extension_type(self, rdm_extension_type):
        """Sets the rdm_extension_type of this PersistableModelSaveAllDTO.

        扩展类型。

        :param rdm_extension_type: The rdm_extension_type of this PersistableModelSaveAllDTO.
        :type rdm_extension_type: str
        """
        self._rdm_extension_type = rdm_extension_type

    @property
    def tenant(self):
        """Gets the tenant of this PersistableModelSaveAllDTO.

        :return: The tenant of this PersistableModelSaveAllDTO.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceParamDTO`
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """Sets the tenant of this PersistableModelSaveAllDTO.

        :param tenant: The tenant of this PersistableModelSaveAllDTO.
        :type tenant: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceParamDTO`
        """
        self._tenant = tenant

    @property
    def unique_key(self):
        """Gets the unique_key of this PersistableModelSaveAllDTO.

        示例模型的唯一键属性。

        :return: The unique_key of this PersistableModelSaveAllDTO.
        :rtype: str
        """
        return self._unique_key

    @unique_key.setter
    def unique_key(self, unique_key):
        """Sets the unique_key of this PersistableModelSaveAllDTO.

        示例模型的唯一键属性。

        :param unique_key: The unique_key of this PersistableModelSaveAllDTO.
        :type unique_key: str
        """
        self._unique_key = unique_key

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
        if not isinstance(other, PersistableModelSaveAllDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
