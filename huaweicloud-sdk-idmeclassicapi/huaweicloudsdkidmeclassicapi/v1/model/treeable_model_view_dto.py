# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TreeableModelViewDTO:

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
        'creator': 'str',
        'modifier': 'str',
        'create_time': 'str',
        'last_update_time': 'str',
        'rdm_version': 'int',
        'rdm_delete_flag': 'int',
        'rdm_extension_type': 'str',
        'tenant': 'TenantViewDTO',
        'class_name': 'str',
        'root_node': 'ObjectReferenceViewDTO',
        'parent_node': 'ObjectReferenceViewDTO',
        'leaf_flag': 'bool',
        'full_path': 'str',
        'raw_full_path': 'str'
    }

    attribute_map = {
        'id': 'id',
        'creator': 'creator',
        'modifier': 'modifier',
        'create_time': 'createTime',
        'last_update_time': 'lastUpdateTime',
        'rdm_version': 'rdmVersion',
        'rdm_delete_flag': 'rdmDeleteFlag',
        'rdm_extension_type': 'rdmExtensionType',
        'tenant': 'tenant',
        'class_name': 'className',
        'root_node': 'rootNode',
        'parent_node': 'parentNode',
        'leaf_flag': 'leafFlag',
        'full_path': 'fullPath',
        'raw_full_path': 'rawFullPath'
    }

    def __init__(self, id=None, creator=None, modifier=None, create_time=None, last_update_time=None, rdm_version=None, rdm_delete_flag=None, rdm_extension_type=None, tenant=None, class_name=None, root_node=None, parent_node=None, leaf_flag=None, full_path=None, raw_full_path=None):
        """TreeableModelViewDTO

        The model defined in huaweicloud sdk

        :param id: 实例ID。
        :type id: str
        :param creator: 创建人。
        :type creator: str
        :param modifier: 修改人。
        :type modifier: str
        :param create_time: 创建时间。
        :type create_time: str
        :param last_update_time: 最新更新时间。
        :type last_update_time: str
        :param rdm_version: 系统版本。
        :type rdm_version: int
        :param rdm_delete_flag: 软删除标识，参数值为0或1。 - 0：表示未删除。 - 1：表示已删除。
        :type rdm_delete_flag: int
        :param rdm_extension_type: 扩展类型。
        :type rdm_extension_type: str
        :param tenant: 
        :type tenant: :class:`huaweicloudsdkidmeclassicapi.v1.TenantViewDTO`
        :param class_name: 类名。
        :type class_name: str
        :param root_node: 
        :type root_node: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceViewDTO`
        :param parent_node: 
        :type parent_node: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceViewDTO`
        :param leaf_flag: 是否为叶子节点。 - true：是叶子节点。 - false：不是叶子节点。
        :type leaf_flag: bool
        :param full_path: 用于存储当前节点全路径。
        :type full_path: str
        :param raw_full_path: 用于存储当前节点原始全路径。
        :type raw_full_path: str
        """
        
        

        self._id = None
        self._creator = None
        self._modifier = None
        self._create_time = None
        self._last_update_time = None
        self._rdm_version = None
        self._rdm_delete_flag = None
        self._rdm_extension_type = None
        self._tenant = None
        self._class_name = None
        self._root_node = None
        self._parent_node = None
        self._leaf_flag = None
        self._full_path = None
        self._raw_full_path = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if creator is not None:
            self.creator = creator
        if modifier is not None:
            self.modifier = modifier
        if create_time is not None:
            self.create_time = create_time
        if last_update_time is not None:
            self.last_update_time = last_update_time
        if rdm_version is not None:
            self.rdm_version = rdm_version
        if rdm_delete_flag is not None:
            self.rdm_delete_flag = rdm_delete_flag
        if rdm_extension_type is not None:
            self.rdm_extension_type = rdm_extension_type
        if tenant is not None:
            self.tenant = tenant
        if class_name is not None:
            self.class_name = class_name
        if root_node is not None:
            self.root_node = root_node
        if parent_node is not None:
            self.parent_node = parent_node
        if leaf_flag is not None:
            self.leaf_flag = leaf_flag
        if full_path is not None:
            self.full_path = full_path
        if raw_full_path is not None:
            self.raw_full_path = raw_full_path

    @property
    def id(self):
        """Gets the id of this TreeableModelViewDTO.

        实例ID。

        :return: The id of this TreeableModelViewDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TreeableModelViewDTO.

        实例ID。

        :param id: The id of this TreeableModelViewDTO.
        :type id: str
        """
        self._id = id

    @property
    def creator(self):
        """Gets the creator of this TreeableModelViewDTO.

        创建人。

        :return: The creator of this TreeableModelViewDTO.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this TreeableModelViewDTO.

        创建人。

        :param creator: The creator of this TreeableModelViewDTO.
        :type creator: str
        """
        self._creator = creator

    @property
    def modifier(self):
        """Gets the modifier of this TreeableModelViewDTO.

        修改人。

        :return: The modifier of this TreeableModelViewDTO.
        :rtype: str
        """
        return self._modifier

    @modifier.setter
    def modifier(self, modifier):
        """Sets the modifier of this TreeableModelViewDTO.

        修改人。

        :param modifier: The modifier of this TreeableModelViewDTO.
        :type modifier: str
        """
        self._modifier = modifier

    @property
    def create_time(self):
        """Gets the create_time of this TreeableModelViewDTO.

        创建时间。

        :return: The create_time of this TreeableModelViewDTO.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this TreeableModelViewDTO.

        创建时间。

        :param create_time: The create_time of this TreeableModelViewDTO.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def last_update_time(self):
        """Gets the last_update_time of this TreeableModelViewDTO.

        最新更新时间。

        :return: The last_update_time of this TreeableModelViewDTO.
        :rtype: str
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        """Sets the last_update_time of this TreeableModelViewDTO.

        最新更新时间。

        :param last_update_time: The last_update_time of this TreeableModelViewDTO.
        :type last_update_time: str
        """
        self._last_update_time = last_update_time

    @property
    def rdm_version(self):
        """Gets the rdm_version of this TreeableModelViewDTO.

        系统版本。

        :return: The rdm_version of this TreeableModelViewDTO.
        :rtype: int
        """
        return self._rdm_version

    @rdm_version.setter
    def rdm_version(self, rdm_version):
        """Sets the rdm_version of this TreeableModelViewDTO.

        系统版本。

        :param rdm_version: The rdm_version of this TreeableModelViewDTO.
        :type rdm_version: int
        """
        self._rdm_version = rdm_version

    @property
    def rdm_delete_flag(self):
        """Gets the rdm_delete_flag of this TreeableModelViewDTO.

        软删除标识，参数值为0或1。 - 0：表示未删除。 - 1：表示已删除。

        :return: The rdm_delete_flag of this TreeableModelViewDTO.
        :rtype: int
        """
        return self._rdm_delete_flag

    @rdm_delete_flag.setter
    def rdm_delete_flag(self, rdm_delete_flag):
        """Sets the rdm_delete_flag of this TreeableModelViewDTO.

        软删除标识，参数值为0或1。 - 0：表示未删除。 - 1：表示已删除。

        :param rdm_delete_flag: The rdm_delete_flag of this TreeableModelViewDTO.
        :type rdm_delete_flag: int
        """
        self._rdm_delete_flag = rdm_delete_flag

    @property
    def rdm_extension_type(self):
        """Gets the rdm_extension_type of this TreeableModelViewDTO.

        扩展类型。

        :return: The rdm_extension_type of this TreeableModelViewDTO.
        :rtype: str
        """
        return self._rdm_extension_type

    @rdm_extension_type.setter
    def rdm_extension_type(self, rdm_extension_type):
        """Sets the rdm_extension_type of this TreeableModelViewDTO.

        扩展类型。

        :param rdm_extension_type: The rdm_extension_type of this TreeableModelViewDTO.
        :type rdm_extension_type: str
        """
        self._rdm_extension_type = rdm_extension_type

    @property
    def tenant(self):
        """Gets the tenant of this TreeableModelViewDTO.

        :return: The tenant of this TreeableModelViewDTO.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.TenantViewDTO`
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """Sets the tenant of this TreeableModelViewDTO.

        :param tenant: The tenant of this TreeableModelViewDTO.
        :type tenant: :class:`huaweicloudsdkidmeclassicapi.v1.TenantViewDTO`
        """
        self._tenant = tenant

    @property
    def class_name(self):
        """Gets the class_name of this TreeableModelViewDTO.

        类名。

        :return: The class_name of this TreeableModelViewDTO.
        :rtype: str
        """
        return self._class_name

    @class_name.setter
    def class_name(self, class_name):
        """Sets the class_name of this TreeableModelViewDTO.

        类名。

        :param class_name: The class_name of this TreeableModelViewDTO.
        :type class_name: str
        """
        self._class_name = class_name

    @property
    def root_node(self):
        """Gets the root_node of this TreeableModelViewDTO.

        :return: The root_node of this TreeableModelViewDTO.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceViewDTO`
        """
        return self._root_node

    @root_node.setter
    def root_node(self, root_node):
        """Sets the root_node of this TreeableModelViewDTO.

        :param root_node: The root_node of this TreeableModelViewDTO.
        :type root_node: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceViewDTO`
        """
        self._root_node = root_node

    @property
    def parent_node(self):
        """Gets the parent_node of this TreeableModelViewDTO.

        :return: The parent_node of this TreeableModelViewDTO.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceViewDTO`
        """
        return self._parent_node

    @parent_node.setter
    def parent_node(self, parent_node):
        """Sets the parent_node of this TreeableModelViewDTO.

        :param parent_node: The parent_node of this TreeableModelViewDTO.
        :type parent_node: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceViewDTO`
        """
        self._parent_node = parent_node

    @property
    def leaf_flag(self):
        """Gets the leaf_flag of this TreeableModelViewDTO.

        是否为叶子节点。 - true：是叶子节点。 - false：不是叶子节点。

        :return: The leaf_flag of this TreeableModelViewDTO.
        :rtype: bool
        """
        return self._leaf_flag

    @leaf_flag.setter
    def leaf_flag(self, leaf_flag):
        """Sets the leaf_flag of this TreeableModelViewDTO.

        是否为叶子节点。 - true：是叶子节点。 - false：不是叶子节点。

        :param leaf_flag: The leaf_flag of this TreeableModelViewDTO.
        :type leaf_flag: bool
        """
        self._leaf_flag = leaf_flag

    @property
    def full_path(self):
        """Gets the full_path of this TreeableModelViewDTO.

        用于存储当前节点全路径。

        :return: The full_path of this TreeableModelViewDTO.
        :rtype: str
        """
        return self._full_path

    @full_path.setter
    def full_path(self, full_path):
        """Sets the full_path of this TreeableModelViewDTO.

        用于存储当前节点全路径。

        :param full_path: The full_path of this TreeableModelViewDTO.
        :type full_path: str
        """
        self._full_path = full_path

    @property
    def raw_full_path(self):
        """Gets the raw_full_path of this TreeableModelViewDTO.

        用于存储当前节点原始全路径。

        :return: The raw_full_path of this TreeableModelViewDTO.
        :rtype: str
        """
        return self._raw_full_path

    @raw_full_path.setter
    def raw_full_path(self, raw_full_path):
        """Sets the raw_full_path of this TreeableModelViewDTO.

        用于存储当前节点原始全路径。

        :param raw_full_path: The raw_full_path of this TreeableModelViewDTO.
        :type raw_full_path: str
        """
        self._raw_full_path = raw_full_path

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
        if not isinstance(other, TreeableModelViewDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
