# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PersistableModelListViewDTO:

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
        'class_name': 'str',
        'cls_attrs': 'list[object]',
        'create_time': 'str',
        'creator': 'str',
        'disable_flag': 'bool',
        'folder': 'ObjectReferenceViewDTO',
        'full_path': 'str',
        'id': 'str',
        'last_update_time': 'str',
        'leaf_flag': 'bool',
        'lifecycle_state': 'ObjectReferenceViewDTO',
        'lifecycle_template': 'ObjectReferenceViewDTO',
        'modifier': 'str',
        'owner': 'str',
        'parent_node': 'ObjectReferenceViewDTO',
        'raw_full_path': 'str',
        'rdm_delete_flag': 'int',
        'rdm_extension_type': 'str',
        'rdm_version': 'int',
        'root_node': 'ObjectReferenceViewDTO',
        'tenant': 'ObjectReferenceViewDTO',
        'unique_key': 'str'
    }

    attribute_map = {
        'acl_entry': 'aclEntry',
        'class_name': 'className',
        'cls_attrs': 'clsAttrs',
        'create_time': 'createTime',
        'creator': 'creator',
        'disable_flag': 'disableFlag',
        'folder': 'folder',
        'full_path': 'fullPath',
        'id': 'id',
        'last_update_time': 'lastUpdateTime',
        'leaf_flag': 'leafFlag',
        'lifecycle_state': 'lifecycleState',
        'lifecycle_template': 'lifecycleTemplate',
        'modifier': 'modifier',
        'owner': 'owner',
        'parent_node': 'parentNode',
        'raw_full_path': 'rawFullPath',
        'rdm_delete_flag': 'rdmDeleteFlag',
        'rdm_extension_type': 'rdmExtensionType',
        'rdm_version': 'rdmVersion',
        'root_node': 'rootNode',
        'tenant': 'tenant',
        'unique_key': 'uniqueKey'
    }

    def __init__(self, acl_entry=None, class_name=None, cls_attrs=None, create_time=None, creator=None, disable_flag=None, folder=None, full_path=None, id=None, last_update_time=None, leaf_flag=None, lifecycle_state=None, lifecycle_template=None, modifier=None, owner=None, parent_node=None, raw_full_path=None, rdm_delete_flag=None, rdm_extension_type=None, rdm_version=None, root_node=None, tenant=None, unique_key=None):
        r"""PersistableModelListViewDTO

        The model defined in huaweicloud sdk

        :param acl_entry: **参数解释：**  访问控制列表。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type acl_entry: str
        :param class_name: **参数解释：**  类名。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type class_name: str
        :param cls_attrs: **参数解释：**  分类属性。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type cls_attrs: list[object]
        :param create_time: **参数解释：**  创建时间。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type create_time: str
        :param creator: **参数解释：**  创建者。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type creator: str
        :param disable_flag: **参数解释：**  失效标识。   **取值范围：**  - true：失效。  - false：未失效。  **默认取值：**  不涉及。 
        :type disable_flag: bool
        :param folder: 
        :type folder: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceViewDTO`
        :param full_path: **参数解释：**  用于存储当前节点全路径。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type full_path: str
        :param id: **参数解释：**  唯一标识。  **取值范围：**  -9223372036854775808到9223372036854775807的整数。  **默认取值：**  不涉及。 
        :type id: str
        :param last_update_time: **参数解释：**  最后更新时间。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type last_update_time: str
        :param leaf_flag: **参数解释：**  是否为叶子节点。  **取值范围：**  - true：是叶子节点。 - false：不是叶子节点。  **默认取值：**  false。 
        :type leaf_flag: bool
        :param lifecycle_state: 
        :type lifecycle_state: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceViewDTO`
        :param lifecycle_template: 
        :type lifecycle_template: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceViewDTO`
        :param modifier: **参数解释：**  更新者。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type modifier: str
        :param owner: **参数解释：**  拥有者。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type owner: str
        :param parent_node: 
        :type parent_node: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceViewDTO`
        :param raw_full_path: **参数解释：**  用于存储当前节点原始全路径。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type raw_full_path: str
        :param rdm_delete_flag: **参数解释：**  软删除标识。  **取值范围：**  - 0：表示未删除。 - 1：表示已删除。  **默认取值：**  0。 
        :type rdm_delete_flag: int
        :param rdm_extension_type: **参数解释：**  扩展类型。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type rdm_extension_type: str
        :param rdm_version: **参数解释：**  系统版本。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type rdm_version: int
        :param root_node: 
        :type root_node: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceViewDTO`
        :param tenant: 
        :type tenant: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceViewDTO`
        :param unique_key: **参数解释：**  示例模型的唯一键约束属性。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type unique_key: str
        """
        
        

        self._acl_entry = None
        self._class_name = None
        self._cls_attrs = None
        self._create_time = None
        self._creator = None
        self._disable_flag = None
        self._folder = None
        self._full_path = None
        self._id = None
        self._last_update_time = None
        self._leaf_flag = None
        self._lifecycle_state = None
        self._lifecycle_template = None
        self._modifier = None
        self._owner = None
        self._parent_node = None
        self._raw_full_path = None
        self._rdm_delete_flag = None
        self._rdm_extension_type = None
        self._rdm_version = None
        self._root_node = None
        self._tenant = None
        self._unique_key = None
        self.discriminator = None

        if acl_entry is not None:
            self.acl_entry = acl_entry
        if class_name is not None:
            self.class_name = class_name
        if cls_attrs is not None:
            self.cls_attrs = cls_attrs
        if create_time is not None:
            self.create_time = create_time
        if creator is not None:
            self.creator = creator
        if disable_flag is not None:
            self.disable_flag = disable_flag
        if folder is not None:
            self.folder = folder
        if full_path is not None:
            self.full_path = full_path
        if id is not None:
            self.id = id
        if last_update_time is not None:
            self.last_update_time = last_update_time
        if leaf_flag is not None:
            self.leaf_flag = leaf_flag
        if lifecycle_state is not None:
            self.lifecycle_state = lifecycle_state
        if lifecycle_template is not None:
            self.lifecycle_template = lifecycle_template
        if modifier is not None:
            self.modifier = modifier
        if owner is not None:
            self.owner = owner
        if parent_node is not None:
            self.parent_node = parent_node
        if raw_full_path is not None:
            self.raw_full_path = raw_full_path
        if rdm_delete_flag is not None:
            self.rdm_delete_flag = rdm_delete_flag
        if rdm_extension_type is not None:
            self.rdm_extension_type = rdm_extension_type
        if rdm_version is not None:
            self.rdm_version = rdm_version
        if root_node is not None:
            self.root_node = root_node
        if tenant is not None:
            self.tenant = tenant
        if unique_key is not None:
            self.unique_key = unique_key

    @property
    def acl_entry(self):
        r"""Gets the acl_entry of this PersistableModelListViewDTO.

        **参数解释：**  访问控制列表。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The acl_entry of this PersistableModelListViewDTO.
        :rtype: str
        """
        return self._acl_entry

    @acl_entry.setter
    def acl_entry(self, acl_entry):
        r"""Sets the acl_entry of this PersistableModelListViewDTO.

        **参数解释：**  访问控制列表。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param acl_entry: The acl_entry of this PersistableModelListViewDTO.
        :type acl_entry: str
        """
        self._acl_entry = acl_entry

    @property
    def class_name(self):
        r"""Gets the class_name of this PersistableModelListViewDTO.

        **参数解释：**  类名。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The class_name of this PersistableModelListViewDTO.
        :rtype: str
        """
        return self._class_name

    @class_name.setter
    def class_name(self, class_name):
        r"""Sets the class_name of this PersistableModelListViewDTO.

        **参数解释：**  类名。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param class_name: The class_name of this PersistableModelListViewDTO.
        :type class_name: str
        """
        self._class_name = class_name

    @property
    def cls_attrs(self):
        r"""Gets the cls_attrs of this PersistableModelListViewDTO.

        **参数解释：**  分类属性。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The cls_attrs of this PersistableModelListViewDTO.
        :rtype: list[object]
        """
        return self._cls_attrs

    @cls_attrs.setter
    def cls_attrs(self, cls_attrs):
        r"""Sets the cls_attrs of this PersistableModelListViewDTO.

        **参数解释：**  分类属性。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param cls_attrs: The cls_attrs of this PersistableModelListViewDTO.
        :type cls_attrs: list[object]
        """
        self._cls_attrs = cls_attrs

    @property
    def create_time(self):
        r"""Gets the create_time of this PersistableModelListViewDTO.

        **参数解释：**  创建时间。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The create_time of this PersistableModelListViewDTO.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this PersistableModelListViewDTO.

        **参数解释：**  创建时间。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param create_time: The create_time of this PersistableModelListViewDTO.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def creator(self):
        r"""Gets the creator of this PersistableModelListViewDTO.

        **参数解释：**  创建者。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The creator of this PersistableModelListViewDTO.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this PersistableModelListViewDTO.

        **参数解释：**  创建者。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param creator: The creator of this PersistableModelListViewDTO.
        :type creator: str
        """
        self._creator = creator

    @property
    def disable_flag(self):
        r"""Gets the disable_flag of this PersistableModelListViewDTO.

        **参数解释：**  失效标识。   **取值范围：**  - true：失效。  - false：未失效。  **默认取值：**  不涉及。 

        :return: The disable_flag of this PersistableModelListViewDTO.
        :rtype: bool
        """
        return self._disable_flag

    @disable_flag.setter
    def disable_flag(self, disable_flag):
        r"""Sets the disable_flag of this PersistableModelListViewDTO.

        **参数解释：**  失效标识。   **取值范围：**  - true：失效。  - false：未失效。  **默认取值：**  不涉及。 

        :param disable_flag: The disable_flag of this PersistableModelListViewDTO.
        :type disable_flag: bool
        """
        self._disable_flag = disable_flag

    @property
    def folder(self):
        r"""Gets the folder of this PersistableModelListViewDTO.

        :return: The folder of this PersistableModelListViewDTO.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceViewDTO`
        """
        return self._folder

    @folder.setter
    def folder(self, folder):
        r"""Sets the folder of this PersistableModelListViewDTO.

        :param folder: The folder of this PersistableModelListViewDTO.
        :type folder: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceViewDTO`
        """
        self._folder = folder

    @property
    def full_path(self):
        r"""Gets the full_path of this PersistableModelListViewDTO.

        **参数解释：**  用于存储当前节点全路径。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The full_path of this PersistableModelListViewDTO.
        :rtype: str
        """
        return self._full_path

    @full_path.setter
    def full_path(self, full_path):
        r"""Sets the full_path of this PersistableModelListViewDTO.

        **参数解释：**  用于存储当前节点全路径。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param full_path: The full_path of this PersistableModelListViewDTO.
        :type full_path: str
        """
        self._full_path = full_path

    @property
    def id(self):
        r"""Gets the id of this PersistableModelListViewDTO.

        **参数解释：**  唯一标识。  **取值范围：**  -9223372036854775808到9223372036854775807的整数。  **默认取值：**  不涉及。 

        :return: The id of this PersistableModelListViewDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this PersistableModelListViewDTO.

        **参数解释：**  唯一标识。  **取值范围：**  -9223372036854775808到9223372036854775807的整数。  **默认取值：**  不涉及。 

        :param id: The id of this PersistableModelListViewDTO.
        :type id: str
        """
        self._id = id

    @property
    def last_update_time(self):
        r"""Gets the last_update_time of this PersistableModelListViewDTO.

        **参数解释：**  最后更新时间。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The last_update_time of this PersistableModelListViewDTO.
        :rtype: str
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        r"""Sets the last_update_time of this PersistableModelListViewDTO.

        **参数解释：**  最后更新时间。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param last_update_time: The last_update_time of this PersistableModelListViewDTO.
        :type last_update_time: str
        """
        self._last_update_time = last_update_time

    @property
    def leaf_flag(self):
        r"""Gets the leaf_flag of this PersistableModelListViewDTO.

        **参数解释：**  是否为叶子节点。  **取值范围：**  - true：是叶子节点。 - false：不是叶子节点。  **默认取值：**  false。 

        :return: The leaf_flag of this PersistableModelListViewDTO.
        :rtype: bool
        """
        return self._leaf_flag

    @leaf_flag.setter
    def leaf_flag(self, leaf_flag):
        r"""Sets the leaf_flag of this PersistableModelListViewDTO.

        **参数解释：**  是否为叶子节点。  **取值范围：**  - true：是叶子节点。 - false：不是叶子节点。  **默认取值：**  false。 

        :param leaf_flag: The leaf_flag of this PersistableModelListViewDTO.
        :type leaf_flag: bool
        """
        self._leaf_flag = leaf_flag

    @property
    def lifecycle_state(self):
        r"""Gets the lifecycle_state of this PersistableModelListViewDTO.

        :return: The lifecycle_state of this PersistableModelListViewDTO.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceViewDTO`
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        r"""Sets the lifecycle_state of this PersistableModelListViewDTO.

        :param lifecycle_state: The lifecycle_state of this PersistableModelListViewDTO.
        :type lifecycle_state: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceViewDTO`
        """
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_template(self):
        r"""Gets the lifecycle_template of this PersistableModelListViewDTO.

        :return: The lifecycle_template of this PersistableModelListViewDTO.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceViewDTO`
        """
        return self._lifecycle_template

    @lifecycle_template.setter
    def lifecycle_template(self, lifecycle_template):
        r"""Sets the lifecycle_template of this PersistableModelListViewDTO.

        :param lifecycle_template: The lifecycle_template of this PersistableModelListViewDTO.
        :type lifecycle_template: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceViewDTO`
        """
        self._lifecycle_template = lifecycle_template

    @property
    def modifier(self):
        r"""Gets the modifier of this PersistableModelListViewDTO.

        **参数解释：**  更新者。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The modifier of this PersistableModelListViewDTO.
        :rtype: str
        """
        return self._modifier

    @modifier.setter
    def modifier(self, modifier):
        r"""Sets the modifier of this PersistableModelListViewDTO.

        **参数解释：**  更新者。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param modifier: The modifier of this PersistableModelListViewDTO.
        :type modifier: str
        """
        self._modifier = modifier

    @property
    def owner(self):
        r"""Gets the owner of this PersistableModelListViewDTO.

        **参数解释：**  拥有者。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The owner of this PersistableModelListViewDTO.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this PersistableModelListViewDTO.

        **参数解释：**  拥有者。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param owner: The owner of this PersistableModelListViewDTO.
        :type owner: str
        """
        self._owner = owner

    @property
    def parent_node(self):
        r"""Gets the parent_node of this PersistableModelListViewDTO.

        :return: The parent_node of this PersistableModelListViewDTO.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceViewDTO`
        """
        return self._parent_node

    @parent_node.setter
    def parent_node(self, parent_node):
        r"""Sets the parent_node of this PersistableModelListViewDTO.

        :param parent_node: The parent_node of this PersistableModelListViewDTO.
        :type parent_node: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceViewDTO`
        """
        self._parent_node = parent_node

    @property
    def raw_full_path(self):
        r"""Gets the raw_full_path of this PersistableModelListViewDTO.

        **参数解释：**  用于存储当前节点原始全路径。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The raw_full_path of this PersistableModelListViewDTO.
        :rtype: str
        """
        return self._raw_full_path

    @raw_full_path.setter
    def raw_full_path(self, raw_full_path):
        r"""Sets the raw_full_path of this PersistableModelListViewDTO.

        **参数解释：**  用于存储当前节点原始全路径。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param raw_full_path: The raw_full_path of this PersistableModelListViewDTO.
        :type raw_full_path: str
        """
        self._raw_full_path = raw_full_path

    @property
    def rdm_delete_flag(self):
        r"""Gets the rdm_delete_flag of this PersistableModelListViewDTO.

        **参数解释：**  软删除标识。  **取值范围：**  - 0：表示未删除。 - 1：表示已删除。  **默认取值：**  0。 

        :return: The rdm_delete_flag of this PersistableModelListViewDTO.
        :rtype: int
        """
        return self._rdm_delete_flag

    @rdm_delete_flag.setter
    def rdm_delete_flag(self, rdm_delete_flag):
        r"""Sets the rdm_delete_flag of this PersistableModelListViewDTO.

        **参数解释：**  软删除标识。  **取值范围：**  - 0：表示未删除。 - 1：表示已删除。  **默认取值：**  0。 

        :param rdm_delete_flag: The rdm_delete_flag of this PersistableModelListViewDTO.
        :type rdm_delete_flag: int
        """
        self._rdm_delete_flag = rdm_delete_flag

    @property
    def rdm_extension_type(self):
        r"""Gets the rdm_extension_type of this PersistableModelListViewDTO.

        **参数解释：**  扩展类型。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The rdm_extension_type of this PersistableModelListViewDTO.
        :rtype: str
        """
        return self._rdm_extension_type

    @rdm_extension_type.setter
    def rdm_extension_type(self, rdm_extension_type):
        r"""Sets the rdm_extension_type of this PersistableModelListViewDTO.

        **参数解释：**  扩展类型。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param rdm_extension_type: The rdm_extension_type of this PersistableModelListViewDTO.
        :type rdm_extension_type: str
        """
        self._rdm_extension_type = rdm_extension_type

    @property
    def rdm_version(self):
        r"""Gets the rdm_version of this PersistableModelListViewDTO.

        **参数解释：**  系统版本。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The rdm_version of this PersistableModelListViewDTO.
        :rtype: int
        """
        return self._rdm_version

    @rdm_version.setter
    def rdm_version(self, rdm_version):
        r"""Sets the rdm_version of this PersistableModelListViewDTO.

        **参数解释：**  系统版本。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param rdm_version: The rdm_version of this PersistableModelListViewDTO.
        :type rdm_version: int
        """
        self._rdm_version = rdm_version

    @property
    def root_node(self):
        r"""Gets the root_node of this PersistableModelListViewDTO.

        :return: The root_node of this PersistableModelListViewDTO.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceViewDTO`
        """
        return self._root_node

    @root_node.setter
    def root_node(self, root_node):
        r"""Sets the root_node of this PersistableModelListViewDTO.

        :param root_node: The root_node of this PersistableModelListViewDTO.
        :type root_node: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceViewDTO`
        """
        self._root_node = root_node

    @property
    def tenant(self):
        r"""Gets the tenant of this PersistableModelListViewDTO.

        :return: The tenant of this PersistableModelListViewDTO.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceViewDTO`
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        r"""Sets the tenant of this PersistableModelListViewDTO.

        :param tenant: The tenant of this PersistableModelListViewDTO.
        :type tenant: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceViewDTO`
        """
        self._tenant = tenant

    @property
    def unique_key(self):
        r"""Gets the unique_key of this PersistableModelListViewDTO.

        **参数解释：**  示例模型的唯一键约束属性。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The unique_key of this PersistableModelListViewDTO.
        :rtype: str
        """
        return self._unique_key

    @unique_key.setter
    def unique_key(self, unique_key):
        r"""Sets the unique_key of this PersistableModelListViewDTO.

        **参数解释：**  示例模型的唯一键约束属性。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param unique_key: The unique_key of this PersistableModelListViewDTO.
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
        if not isinstance(other, PersistableModelListViewDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
