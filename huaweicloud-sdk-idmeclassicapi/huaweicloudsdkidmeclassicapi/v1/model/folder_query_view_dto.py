# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FolderQueryViewDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'business_code': 'str',
        'class_name': 'str',
        'create_time': 'str',
        'creator': 'str',
        'description': 'str',
        'description_en': 'str',
        'disable_flag': 'bool',
        'ext_attr_map': 'object',
        'ext_attrs': 'list[EXAValueViewDTO]',
        'id': 'str',
        'last_update_time': 'str',
        'modifier': 'str',
        'name': 'str',
        'name_en': 'str',
        'rdm_extension_type': 'str',
        'tenant': 'TenantQueryViewDTO',
        'type': 'str'
    }

    attribute_map = {
        'business_code': 'businessCode',
        'class_name': 'className',
        'create_time': 'createTime',
        'creator': 'creator',
        'description': 'description',
        'description_en': 'descriptionEn',
        'disable_flag': 'disableFlag',
        'ext_attr_map': 'extAttrMap',
        'ext_attrs': 'extAttrs',
        'id': 'id',
        'last_update_time': 'lastUpdateTime',
        'modifier': 'modifier',
        'name': 'name',
        'name_en': 'nameEn',
        'rdm_extension_type': 'rdmExtensionType',
        'tenant': 'tenant',
        'type': 'type'
    }

    def __init__(self, business_code=None, class_name=None, create_time=None, creator=None, description=None, description_en=None, disable_flag=None, ext_attr_map=None, ext_attrs=None, id=None, last_update_time=None, modifier=None, name=None, name_en=None, rdm_extension_type=None, tenant=None, type=None):
        """FolderQueryViewDTO

        The model defined in huaweicloud sdk

        :param business_code: 编码。
        :type business_code: str
        :param class_name: 类名。
        :type class_name: str
        :param create_time: 创建时间。
        :type create_time: str
        :param creator: 创建者。
        :type creator: str
        :param description: 中文描述。
        :type description: str
        :param description_en: 英文描述。
        :type description_en: str
        :param disable_flag: 失效标识。  - true：失效。  - false：未失效。
        :type disable_flag: bool
        :param ext_attr_map: 扩展属性映射集。
        :type ext_attr_map: object
        :param ext_attrs: 扩展属性列表。
        :type ext_attrs: list[:class:`huaweicloudsdkidmeclassicapi.v1.EXAValueViewDTO`]
        :param id: 唯一标识。
        :type id: str
        :param last_update_time: 最后更新时间。
        :type last_update_time: str
        :param modifier: 修改人。
        :type modifier: str
        :param name: 中文名称。
        :type name: str
        :param name_en: 英文名称。
        :type name_en: str
        :param rdm_extension_type: 扩展类型。
        :type rdm_extension_type: str
        :param tenant: 
        :type tenant: :class:`huaweicloudsdkidmeclassicapi.v1.TenantQueryViewDTO`
        :param type: 类别。
        :type type: str
        """
        
        

        self._business_code = None
        self._class_name = None
        self._create_time = None
        self._creator = None
        self._description = None
        self._description_en = None
        self._disable_flag = None
        self._ext_attr_map = None
        self._ext_attrs = None
        self._id = None
        self._last_update_time = None
        self._modifier = None
        self._name = None
        self._name_en = None
        self._rdm_extension_type = None
        self._tenant = None
        self._type = None
        self.discriminator = None

        self.business_code = business_code
        if class_name is not None:
            self.class_name = class_name
        if create_time is not None:
            self.create_time = create_time
        if creator is not None:
            self.creator = creator
        if description is not None:
            self.description = description
        if description_en is not None:
            self.description_en = description_en
        if disable_flag is not None:
            self.disable_flag = disable_flag
        if ext_attr_map is not None:
            self.ext_attr_map = ext_attr_map
        if ext_attrs is not None:
            self.ext_attrs = ext_attrs
        if id is not None:
            self.id = id
        if last_update_time is not None:
            self.last_update_time = last_update_time
        if modifier is not None:
            self.modifier = modifier
        self.name = name
        if name_en is not None:
            self.name_en = name_en
        if rdm_extension_type is not None:
            self.rdm_extension_type = rdm_extension_type
        if tenant is not None:
            self.tenant = tenant
        if type is not None:
            self.type = type

    @property
    def business_code(self):
        """Gets the business_code of this FolderQueryViewDTO.

        编码。

        :return: The business_code of this FolderQueryViewDTO.
        :rtype: str
        """
        return self._business_code

    @business_code.setter
    def business_code(self, business_code):
        """Sets the business_code of this FolderQueryViewDTO.

        编码。

        :param business_code: The business_code of this FolderQueryViewDTO.
        :type business_code: str
        """
        self._business_code = business_code

    @property
    def class_name(self):
        """Gets the class_name of this FolderQueryViewDTO.

        类名。

        :return: The class_name of this FolderQueryViewDTO.
        :rtype: str
        """
        return self._class_name

    @class_name.setter
    def class_name(self, class_name):
        """Sets the class_name of this FolderQueryViewDTO.

        类名。

        :param class_name: The class_name of this FolderQueryViewDTO.
        :type class_name: str
        """
        self._class_name = class_name

    @property
    def create_time(self):
        """Gets the create_time of this FolderQueryViewDTO.

        创建时间。

        :return: The create_time of this FolderQueryViewDTO.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this FolderQueryViewDTO.

        创建时间。

        :param create_time: The create_time of this FolderQueryViewDTO.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def creator(self):
        """Gets the creator of this FolderQueryViewDTO.

        创建者。

        :return: The creator of this FolderQueryViewDTO.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this FolderQueryViewDTO.

        创建者。

        :param creator: The creator of this FolderQueryViewDTO.
        :type creator: str
        """
        self._creator = creator

    @property
    def description(self):
        """Gets the description of this FolderQueryViewDTO.

        中文描述。

        :return: The description of this FolderQueryViewDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FolderQueryViewDTO.

        中文描述。

        :param description: The description of this FolderQueryViewDTO.
        :type description: str
        """
        self._description = description

    @property
    def description_en(self):
        """Gets the description_en of this FolderQueryViewDTO.

        英文描述。

        :return: The description_en of this FolderQueryViewDTO.
        :rtype: str
        """
        return self._description_en

    @description_en.setter
    def description_en(self, description_en):
        """Sets the description_en of this FolderQueryViewDTO.

        英文描述。

        :param description_en: The description_en of this FolderQueryViewDTO.
        :type description_en: str
        """
        self._description_en = description_en

    @property
    def disable_flag(self):
        """Gets the disable_flag of this FolderQueryViewDTO.

        失效标识。  - true：失效。  - false：未失效。

        :return: The disable_flag of this FolderQueryViewDTO.
        :rtype: bool
        """
        return self._disable_flag

    @disable_flag.setter
    def disable_flag(self, disable_flag):
        """Sets the disable_flag of this FolderQueryViewDTO.

        失效标识。  - true：失效。  - false：未失效。

        :param disable_flag: The disable_flag of this FolderQueryViewDTO.
        :type disable_flag: bool
        """
        self._disable_flag = disable_flag

    @property
    def ext_attr_map(self):
        """Gets the ext_attr_map of this FolderQueryViewDTO.

        扩展属性映射集。

        :return: The ext_attr_map of this FolderQueryViewDTO.
        :rtype: object
        """
        return self._ext_attr_map

    @ext_attr_map.setter
    def ext_attr_map(self, ext_attr_map):
        """Sets the ext_attr_map of this FolderQueryViewDTO.

        扩展属性映射集。

        :param ext_attr_map: The ext_attr_map of this FolderQueryViewDTO.
        :type ext_attr_map: object
        """
        self._ext_attr_map = ext_attr_map

    @property
    def ext_attrs(self):
        """Gets the ext_attrs of this FolderQueryViewDTO.

        扩展属性列表。

        :return: The ext_attrs of this FolderQueryViewDTO.
        :rtype: list[:class:`huaweicloudsdkidmeclassicapi.v1.EXAValueViewDTO`]
        """
        return self._ext_attrs

    @ext_attrs.setter
    def ext_attrs(self, ext_attrs):
        """Sets the ext_attrs of this FolderQueryViewDTO.

        扩展属性列表。

        :param ext_attrs: The ext_attrs of this FolderQueryViewDTO.
        :type ext_attrs: list[:class:`huaweicloudsdkidmeclassicapi.v1.EXAValueViewDTO`]
        """
        self._ext_attrs = ext_attrs

    @property
    def id(self):
        """Gets the id of this FolderQueryViewDTO.

        唯一标识。

        :return: The id of this FolderQueryViewDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FolderQueryViewDTO.

        唯一标识。

        :param id: The id of this FolderQueryViewDTO.
        :type id: str
        """
        self._id = id

    @property
    def last_update_time(self):
        """Gets the last_update_time of this FolderQueryViewDTO.

        最后更新时间。

        :return: The last_update_time of this FolderQueryViewDTO.
        :rtype: str
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        """Sets the last_update_time of this FolderQueryViewDTO.

        最后更新时间。

        :param last_update_time: The last_update_time of this FolderQueryViewDTO.
        :type last_update_time: str
        """
        self._last_update_time = last_update_time

    @property
    def modifier(self):
        """Gets the modifier of this FolderQueryViewDTO.

        修改人。

        :return: The modifier of this FolderQueryViewDTO.
        :rtype: str
        """
        return self._modifier

    @modifier.setter
    def modifier(self, modifier):
        """Sets the modifier of this FolderQueryViewDTO.

        修改人。

        :param modifier: The modifier of this FolderQueryViewDTO.
        :type modifier: str
        """
        self._modifier = modifier

    @property
    def name(self):
        """Gets the name of this FolderQueryViewDTO.

        中文名称。

        :return: The name of this FolderQueryViewDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FolderQueryViewDTO.

        中文名称。

        :param name: The name of this FolderQueryViewDTO.
        :type name: str
        """
        self._name = name

    @property
    def name_en(self):
        """Gets the name_en of this FolderQueryViewDTO.

        英文名称。

        :return: The name_en of this FolderQueryViewDTO.
        :rtype: str
        """
        return self._name_en

    @name_en.setter
    def name_en(self, name_en):
        """Sets the name_en of this FolderQueryViewDTO.

        英文名称。

        :param name_en: The name_en of this FolderQueryViewDTO.
        :type name_en: str
        """
        self._name_en = name_en

    @property
    def rdm_extension_type(self):
        """Gets the rdm_extension_type of this FolderQueryViewDTO.

        扩展类型。

        :return: The rdm_extension_type of this FolderQueryViewDTO.
        :rtype: str
        """
        return self._rdm_extension_type

    @rdm_extension_type.setter
    def rdm_extension_type(self, rdm_extension_type):
        """Sets the rdm_extension_type of this FolderQueryViewDTO.

        扩展类型。

        :param rdm_extension_type: The rdm_extension_type of this FolderQueryViewDTO.
        :type rdm_extension_type: str
        """
        self._rdm_extension_type = rdm_extension_type

    @property
    def tenant(self):
        """Gets the tenant of this FolderQueryViewDTO.

        :return: The tenant of this FolderQueryViewDTO.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.TenantQueryViewDTO`
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """Sets the tenant of this FolderQueryViewDTO.

        :param tenant: The tenant of this FolderQueryViewDTO.
        :type tenant: :class:`huaweicloudsdkidmeclassicapi.v1.TenantQueryViewDTO`
        """
        self._tenant = tenant

    @property
    def type(self):
        """Gets the type of this FolderQueryViewDTO.

        类别。

        :return: The type of this FolderQueryViewDTO.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FolderQueryViewDTO.

        类别。

        :param type: The type of this FolderQueryViewDTO.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, FolderQueryViewDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
