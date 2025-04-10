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
        r"""FolderQueryViewDTO

        The model defined in huaweicloud sdk

        :param business_code: **参数解释：**  编码。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type business_code: str
        :param class_name: **参数解释：**  类名。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type class_name: str
        :param create_time: **参数解释：**  创建时间。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type create_time: str
        :param creator: **参数解释：**  创建者。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type creator: str
        :param description: **参数解释：**  中文描述。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type description: str
        :param description_en: **参数解释：**  英文描述。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type description_en: str
        :param disable_flag: **参数解释：**  失效标识。  **取值范围：**  - true：失效。  - false：未失效。  **默认取值：**  false。 
        :type disable_flag: bool
        :param ext_attr_map: **参数解释：**  扩展属性映射集。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type ext_attr_map: object
        :param ext_attrs: **参数解释：**  扩展属性列表。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type ext_attrs: list[:class:`huaweicloudsdkidmeclassicapi.v1.EXAValueViewDTO`]
        :param id: **参数解释：**  唯一标识。  **取值范围：**  -9223372036854775808到9223372036854775807的整数。  **默认取值：**  不涉及。 
        :type id: str
        :param last_update_time: **参数解释：**  最后更新时间。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type last_update_time: str
        :param modifier: **参数解释：**  修改人。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type modifier: str
        :param name: **参数解释：**  中文名称。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type name: str
        :param name_en: **参数解释：**  英文名称。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type name_en: str
        :param rdm_extension_type: **参数解释：**  扩展类型。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type rdm_extension_type: str
        :param tenant: 
        :type tenant: :class:`huaweicloudsdkidmeclassicapi.v1.TenantQueryViewDTO`
        :param type: **参数解释：**  类别。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
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
        r"""Gets the business_code of this FolderQueryViewDTO.

        **参数解释：**  编码。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The business_code of this FolderQueryViewDTO.
        :rtype: str
        """
        return self._business_code

    @business_code.setter
    def business_code(self, business_code):
        r"""Sets the business_code of this FolderQueryViewDTO.

        **参数解释：**  编码。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param business_code: The business_code of this FolderQueryViewDTO.
        :type business_code: str
        """
        self._business_code = business_code

    @property
    def class_name(self):
        r"""Gets the class_name of this FolderQueryViewDTO.

        **参数解释：**  类名。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The class_name of this FolderQueryViewDTO.
        :rtype: str
        """
        return self._class_name

    @class_name.setter
    def class_name(self, class_name):
        r"""Sets the class_name of this FolderQueryViewDTO.

        **参数解释：**  类名。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param class_name: The class_name of this FolderQueryViewDTO.
        :type class_name: str
        """
        self._class_name = class_name

    @property
    def create_time(self):
        r"""Gets the create_time of this FolderQueryViewDTO.

        **参数解释：**  创建时间。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The create_time of this FolderQueryViewDTO.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this FolderQueryViewDTO.

        **参数解释：**  创建时间。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param create_time: The create_time of this FolderQueryViewDTO.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def creator(self):
        r"""Gets the creator of this FolderQueryViewDTO.

        **参数解释：**  创建者。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The creator of this FolderQueryViewDTO.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this FolderQueryViewDTO.

        **参数解释：**  创建者。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param creator: The creator of this FolderQueryViewDTO.
        :type creator: str
        """
        self._creator = creator

    @property
    def description(self):
        r"""Gets the description of this FolderQueryViewDTO.

        **参数解释：**  中文描述。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The description of this FolderQueryViewDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this FolderQueryViewDTO.

        **参数解释：**  中文描述。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param description: The description of this FolderQueryViewDTO.
        :type description: str
        """
        self._description = description

    @property
    def description_en(self):
        r"""Gets the description_en of this FolderQueryViewDTO.

        **参数解释：**  英文描述。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The description_en of this FolderQueryViewDTO.
        :rtype: str
        """
        return self._description_en

    @description_en.setter
    def description_en(self, description_en):
        r"""Sets the description_en of this FolderQueryViewDTO.

        **参数解释：**  英文描述。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param description_en: The description_en of this FolderQueryViewDTO.
        :type description_en: str
        """
        self._description_en = description_en

    @property
    def disable_flag(self):
        r"""Gets the disable_flag of this FolderQueryViewDTO.

        **参数解释：**  失效标识。  **取值范围：**  - true：失效。  - false：未失效。  **默认取值：**  false。 

        :return: The disable_flag of this FolderQueryViewDTO.
        :rtype: bool
        """
        return self._disable_flag

    @disable_flag.setter
    def disable_flag(self, disable_flag):
        r"""Sets the disable_flag of this FolderQueryViewDTO.

        **参数解释：**  失效标识。  **取值范围：**  - true：失效。  - false：未失效。  **默认取值：**  false。 

        :param disable_flag: The disable_flag of this FolderQueryViewDTO.
        :type disable_flag: bool
        """
        self._disable_flag = disable_flag

    @property
    def ext_attr_map(self):
        r"""Gets the ext_attr_map of this FolderQueryViewDTO.

        **参数解释：**  扩展属性映射集。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The ext_attr_map of this FolderQueryViewDTO.
        :rtype: object
        """
        return self._ext_attr_map

    @ext_attr_map.setter
    def ext_attr_map(self, ext_attr_map):
        r"""Sets the ext_attr_map of this FolderQueryViewDTO.

        **参数解释：**  扩展属性映射集。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param ext_attr_map: The ext_attr_map of this FolderQueryViewDTO.
        :type ext_attr_map: object
        """
        self._ext_attr_map = ext_attr_map

    @property
    def ext_attrs(self):
        r"""Gets the ext_attrs of this FolderQueryViewDTO.

        **参数解释：**  扩展属性列表。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The ext_attrs of this FolderQueryViewDTO.
        :rtype: list[:class:`huaweicloudsdkidmeclassicapi.v1.EXAValueViewDTO`]
        """
        return self._ext_attrs

    @ext_attrs.setter
    def ext_attrs(self, ext_attrs):
        r"""Sets the ext_attrs of this FolderQueryViewDTO.

        **参数解释：**  扩展属性列表。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param ext_attrs: The ext_attrs of this FolderQueryViewDTO.
        :type ext_attrs: list[:class:`huaweicloudsdkidmeclassicapi.v1.EXAValueViewDTO`]
        """
        self._ext_attrs = ext_attrs

    @property
    def id(self):
        r"""Gets the id of this FolderQueryViewDTO.

        **参数解释：**  唯一标识。  **取值范围：**  -9223372036854775808到9223372036854775807的整数。  **默认取值：**  不涉及。 

        :return: The id of this FolderQueryViewDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this FolderQueryViewDTO.

        **参数解释：**  唯一标识。  **取值范围：**  -9223372036854775808到9223372036854775807的整数。  **默认取值：**  不涉及。 

        :param id: The id of this FolderQueryViewDTO.
        :type id: str
        """
        self._id = id

    @property
    def last_update_time(self):
        r"""Gets the last_update_time of this FolderQueryViewDTO.

        **参数解释：**  最后更新时间。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The last_update_time of this FolderQueryViewDTO.
        :rtype: str
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        r"""Sets the last_update_time of this FolderQueryViewDTO.

        **参数解释：**  最后更新时间。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param last_update_time: The last_update_time of this FolderQueryViewDTO.
        :type last_update_time: str
        """
        self._last_update_time = last_update_time

    @property
    def modifier(self):
        r"""Gets the modifier of this FolderQueryViewDTO.

        **参数解释：**  修改人。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The modifier of this FolderQueryViewDTO.
        :rtype: str
        """
        return self._modifier

    @modifier.setter
    def modifier(self, modifier):
        r"""Sets the modifier of this FolderQueryViewDTO.

        **参数解释：**  修改人。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param modifier: The modifier of this FolderQueryViewDTO.
        :type modifier: str
        """
        self._modifier = modifier

    @property
    def name(self):
        r"""Gets the name of this FolderQueryViewDTO.

        **参数解释：**  中文名称。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The name of this FolderQueryViewDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this FolderQueryViewDTO.

        **参数解释：**  中文名称。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param name: The name of this FolderQueryViewDTO.
        :type name: str
        """
        self._name = name

    @property
    def name_en(self):
        r"""Gets the name_en of this FolderQueryViewDTO.

        **参数解释：**  英文名称。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The name_en of this FolderQueryViewDTO.
        :rtype: str
        """
        return self._name_en

    @name_en.setter
    def name_en(self, name_en):
        r"""Sets the name_en of this FolderQueryViewDTO.

        **参数解释：**  英文名称。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param name_en: The name_en of this FolderQueryViewDTO.
        :type name_en: str
        """
        self._name_en = name_en

    @property
    def rdm_extension_type(self):
        r"""Gets the rdm_extension_type of this FolderQueryViewDTO.

        **参数解释：**  扩展类型。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The rdm_extension_type of this FolderQueryViewDTO.
        :rtype: str
        """
        return self._rdm_extension_type

    @rdm_extension_type.setter
    def rdm_extension_type(self, rdm_extension_type):
        r"""Sets the rdm_extension_type of this FolderQueryViewDTO.

        **参数解释：**  扩展类型。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param rdm_extension_type: The rdm_extension_type of this FolderQueryViewDTO.
        :type rdm_extension_type: str
        """
        self._rdm_extension_type = rdm_extension_type

    @property
    def tenant(self):
        r"""Gets the tenant of this FolderQueryViewDTO.

        :return: The tenant of this FolderQueryViewDTO.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.TenantQueryViewDTO`
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        r"""Sets the tenant of this FolderQueryViewDTO.

        :param tenant: The tenant of this FolderQueryViewDTO.
        :type tenant: :class:`huaweicloudsdkidmeclassicapi.v1.TenantQueryViewDTO`
        """
        self._tenant = tenant

    @property
    def type(self):
        r"""Gets the type of this FolderQueryViewDTO.

        **参数解释：**  类别。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The type of this FolderQueryViewDTO.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this FolderQueryViewDTO.

        **参数解释：**  类别。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

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
