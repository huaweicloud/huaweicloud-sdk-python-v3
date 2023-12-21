# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PersistableModelQueryViewDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'class_name': 'str',
        'create_time': 'str',
        'creator': 'str',
        'disable_flag': 'bool',
        'ext_attr_map': 'object',
        'ext_attrs': 'list[EXAValueViewDTO]',
        'folder': 'FolderQueryViewDTO',
        'id': 'str',
        'last_update_time': 'str',
        'modifier': 'str',
        'rdm_extension_type': 'str',
        'tenant': 'TenantQueryViewDTO'
    }

    attribute_map = {
        'class_name': 'className',
        'create_time': 'createTime',
        'creator': 'creator',
        'disable_flag': 'disableFlag',
        'ext_attr_map': 'extAttrMap',
        'ext_attrs': 'extAttrs',
        'folder': 'folder',
        'id': 'id',
        'last_update_time': 'lastUpdateTime',
        'modifier': 'modifier',
        'rdm_extension_type': 'rdmExtensionType',
        'tenant': 'tenant'
    }

    def __init__(self, class_name=None, create_time=None, creator=None, disable_flag=None, ext_attr_map=None, ext_attrs=None, folder=None, id=None, last_update_time=None, modifier=None, rdm_extension_type=None, tenant=None):
        """PersistableModelQueryViewDTO

        The model defined in huaweicloud sdk

        :param class_name: 类名。
        :type class_name: str
        :param create_time: 创建时间。
        :type create_time: str
        :param creator: 创建者。
        :type creator: str
        :param disable_flag: 失效标识。  - true：失效。  - false：未失效。
        :type disable_flag: bool
        :param ext_attr_map: 扩展属性映射集。
        :type ext_attr_map: object
        :param ext_attrs: 扩展属性列表。
        :type ext_attrs: list[:class:`huaweicloudsdkidmeclassicapi.v1.EXAValueViewDTO`]
        :param folder: 
        :type folder: :class:`huaweicloudsdkidmeclassicapi.v1.FolderQueryViewDTO`
        :param id: 唯一标识。
        :type id: str
        :param last_update_time: 最后更新时间。
        :type last_update_time: str
        :param modifier: 修改人。
        :type modifier: str
        :param rdm_extension_type: 扩展类型。
        :type rdm_extension_type: str
        :param tenant: 
        :type tenant: :class:`huaweicloudsdkidmeclassicapi.v1.TenantQueryViewDTO`
        """
        
        

        self._class_name = None
        self._create_time = None
        self._creator = None
        self._disable_flag = None
        self._ext_attr_map = None
        self._ext_attrs = None
        self._folder = None
        self._id = None
        self._last_update_time = None
        self._modifier = None
        self._rdm_extension_type = None
        self._tenant = None
        self.discriminator = None

        if class_name is not None:
            self.class_name = class_name
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
        if modifier is not None:
            self.modifier = modifier
        if rdm_extension_type is not None:
            self.rdm_extension_type = rdm_extension_type
        if tenant is not None:
            self.tenant = tenant

    @property
    def class_name(self):
        """Gets the class_name of this PersistableModelQueryViewDTO.

        类名。

        :return: The class_name of this PersistableModelQueryViewDTO.
        :rtype: str
        """
        return self._class_name

    @class_name.setter
    def class_name(self, class_name):
        """Sets the class_name of this PersistableModelQueryViewDTO.

        类名。

        :param class_name: The class_name of this PersistableModelQueryViewDTO.
        :type class_name: str
        """
        self._class_name = class_name

    @property
    def create_time(self):
        """Gets the create_time of this PersistableModelQueryViewDTO.

        创建时间。

        :return: The create_time of this PersistableModelQueryViewDTO.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this PersistableModelQueryViewDTO.

        创建时间。

        :param create_time: The create_time of this PersistableModelQueryViewDTO.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def creator(self):
        """Gets the creator of this PersistableModelQueryViewDTO.

        创建者。

        :return: The creator of this PersistableModelQueryViewDTO.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this PersistableModelQueryViewDTO.

        创建者。

        :param creator: The creator of this PersistableModelQueryViewDTO.
        :type creator: str
        """
        self._creator = creator

    @property
    def disable_flag(self):
        """Gets the disable_flag of this PersistableModelQueryViewDTO.

        失效标识。  - true：失效。  - false：未失效。

        :return: The disable_flag of this PersistableModelQueryViewDTO.
        :rtype: bool
        """
        return self._disable_flag

    @disable_flag.setter
    def disable_flag(self, disable_flag):
        """Sets the disable_flag of this PersistableModelQueryViewDTO.

        失效标识。  - true：失效。  - false：未失效。

        :param disable_flag: The disable_flag of this PersistableModelQueryViewDTO.
        :type disable_flag: bool
        """
        self._disable_flag = disable_flag

    @property
    def ext_attr_map(self):
        """Gets the ext_attr_map of this PersistableModelQueryViewDTO.

        扩展属性映射集。

        :return: The ext_attr_map of this PersistableModelQueryViewDTO.
        :rtype: object
        """
        return self._ext_attr_map

    @ext_attr_map.setter
    def ext_attr_map(self, ext_attr_map):
        """Sets the ext_attr_map of this PersistableModelQueryViewDTO.

        扩展属性映射集。

        :param ext_attr_map: The ext_attr_map of this PersistableModelQueryViewDTO.
        :type ext_attr_map: object
        """
        self._ext_attr_map = ext_attr_map

    @property
    def ext_attrs(self):
        """Gets the ext_attrs of this PersistableModelQueryViewDTO.

        扩展属性列表。

        :return: The ext_attrs of this PersistableModelQueryViewDTO.
        :rtype: list[:class:`huaweicloudsdkidmeclassicapi.v1.EXAValueViewDTO`]
        """
        return self._ext_attrs

    @ext_attrs.setter
    def ext_attrs(self, ext_attrs):
        """Sets the ext_attrs of this PersistableModelQueryViewDTO.

        扩展属性列表。

        :param ext_attrs: The ext_attrs of this PersistableModelQueryViewDTO.
        :type ext_attrs: list[:class:`huaweicloudsdkidmeclassicapi.v1.EXAValueViewDTO`]
        """
        self._ext_attrs = ext_attrs

    @property
    def folder(self):
        """Gets the folder of this PersistableModelQueryViewDTO.

        :return: The folder of this PersistableModelQueryViewDTO.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.FolderQueryViewDTO`
        """
        return self._folder

    @folder.setter
    def folder(self, folder):
        """Sets the folder of this PersistableModelQueryViewDTO.

        :param folder: The folder of this PersistableModelQueryViewDTO.
        :type folder: :class:`huaweicloudsdkidmeclassicapi.v1.FolderQueryViewDTO`
        """
        self._folder = folder

    @property
    def id(self):
        """Gets the id of this PersistableModelQueryViewDTO.

        唯一标识。

        :return: The id of this PersistableModelQueryViewDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PersistableModelQueryViewDTO.

        唯一标识。

        :param id: The id of this PersistableModelQueryViewDTO.
        :type id: str
        """
        self._id = id

    @property
    def last_update_time(self):
        """Gets the last_update_time of this PersistableModelQueryViewDTO.

        最后更新时间。

        :return: The last_update_time of this PersistableModelQueryViewDTO.
        :rtype: str
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        """Sets the last_update_time of this PersistableModelQueryViewDTO.

        最后更新时间。

        :param last_update_time: The last_update_time of this PersistableModelQueryViewDTO.
        :type last_update_time: str
        """
        self._last_update_time = last_update_time

    @property
    def modifier(self):
        """Gets the modifier of this PersistableModelQueryViewDTO.

        修改人。

        :return: The modifier of this PersistableModelQueryViewDTO.
        :rtype: str
        """
        return self._modifier

    @modifier.setter
    def modifier(self, modifier):
        """Sets the modifier of this PersistableModelQueryViewDTO.

        修改人。

        :param modifier: The modifier of this PersistableModelQueryViewDTO.
        :type modifier: str
        """
        self._modifier = modifier

    @property
    def rdm_extension_type(self):
        """Gets the rdm_extension_type of this PersistableModelQueryViewDTO.

        扩展类型。

        :return: The rdm_extension_type of this PersistableModelQueryViewDTO.
        :rtype: str
        """
        return self._rdm_extension_type

    @rdm_extension_type.setter
    def rdm_extension_type(self, rdm_extension_type):
        """Sets the rdm_extension_type of this PersistableModelQueryViewDTO.

        扩展类型。

        :param rdm_extension_type: The rdm_extension_type of this PersistableModelQueryViewDTO.
        :type rdm_extension_type: str
        """
        self._rdm_extension_type = rdm_extension_type

    @property
    def tenant(self):
        """Gets the tenant of this PersistableModelQueryViewDTO.

        :return: The tenant of this PersistableModelQueryViewDTO.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.TenantQueryViewDTO`
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """Sets the tenant of this PersistableModelQueryViewDTO.

        :param tenant: The tenant of this PersistableModelQueryViewDTO.
        :type tenant: :class:`huaweicloudsdkidmeclassicapi.v1.TenantQueryViewDTO`
        """
        self._tenant = tenant

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
        if not isinstance(other, PersistableModelQueryViewDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
