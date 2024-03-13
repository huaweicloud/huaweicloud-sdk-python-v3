# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TenantViewDTO:

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
        'code': 'str',
        'create_time': 'str',
        'creator': 'str',
        'data_source': 'str',
        'description': 'str',
        'disable_flag': 'bool',
        'id': 'str',
        'kiaguid': 'str',
        'last_update_time': 'str',
        'modifier': 'str',
        'name': 'str',
        'rdm_delete_flag': 'int',
        'rdm_extension_type': 'str',
        'rdm_version': 'int',
        'security_level': 'str',
        'tenant': 'TenantViewDTO'
    }

    attribute_map = {
        'class_name': 'className',
        'code': 'code',
        'create_time': 'createTime',
        'creator': 'creator',
        'data_source': 'dataSource',
        'description': 'description',
        'disable_flag': 'disableFlag',
        'id': 'id',
        'kiaguid': 'kiaguid',
        'last_update_time': 'lastUpdateTime',
        'modifier': 'modifier',
        'name': 'name',
        'rdm_delete_flag': 'rdmDeleteFlag',
        'rdm_extension_type': 'rdmExtensionType',
        'rdm_version': 'rdmVersion',
        'security_level': 'securityLevel',
        'tenant': 'tenant'
    }

    def __init__(self, class_name=None, code=None, create_time=None, creator=None, data_source=None, description=None, disable_flag=None, id=None, kiaguid=None, last_update_time=None, modifier=None, name=None, rdm_delete_flag=None, rdm_extension_type=None, rdm_version=None, security_level=None, tenant=None):
        """TenantViewDTO

        The model defined in huaweicloud sdk

        :param class_name: 类名。
        :type class_name: str
        :param code: 租户编码。
        :type code: str
        :param create_time: 创建时间。
        :type create_time: str
        :param creator: 创建者。
        :type creator: str
        :param data_source: 租户使用的数据源名称。
        :type data_source: str
        :param description: 描述信息。
        :type description: str
        :param disable_flag: 失效标识。  - true：失效。  - false：未失效。
        :type disable_flag: bool
        :param id: 唯一标识。
        :type id: str
        :param kiaguid: KIA密级。
        :type kiaguid: str
        :param last_update_time: 最后更新时间。
        :type last_update_time: str
        :param modifier: 修改人。
        :type modifier: str
        :param name: 中文名称。
        :type name: str
        :param rdm_delete_flag: 软删除标识，参数值为0或1。 - 0：表示未删除。 - 1：表示已删除。
        :type rdm_delete_flag: int
        :param rdm_extension_type: 扩展类型。
        :type rdm_extension_type: str
        :param rdm_version: 系统版本。
        :type rdm_version: int
        :param security_level: 安全密级。 - INTERNAL：内部公开。 - SECRET：秘密。 - CONFIDENTIAL：机密。 - TOP_SECRET：绝密。
        :type security_level: str
        :param tenant: 
        :type tenant: :class:`huaweicloudsdkidmeclassicapi.v1.TenantViewDTO`
        """
        
        

        self._class_name = None
        self._code = None
        self._create_time = None
        self._creator = None
        self._data_source = None
        self._description = None
        self._disable_flag = None
        self._id = None
        self._kiaguid = None
        self._last_update_time = None
        self._modifier = None
        self._name = None
        self._rdm_delete_flag = None
        self._rdm_extension_type = None
        self._rdm_version = None
        self._security_level = None
        self._tenant = None
        self.discriminator = None

        if class_name is not None:
            self.class_name = class_name
        self.code = code
        if create_time is not None:
            self.create_time = create_time
        if creator is not None:
            self.creator = creator
        self.data_source = data_source
        if description is not None:
            self.description = description
        if disable_flag is not None:
            self.disable_flag = disable_flag
        if id is not None:
            self.id = id
        if kiaguid is not None:
            self.kiaguid = kiaguid
        if last_update_time is not None:
            self.last_update_time = last_update_time
        if modifier is not None:
            self.modifier = modifier
        if name is not None:
            self.name = name
        if rdm_delete_flag is not None:
            self.rdm_delete_flag = rdm_delete_flag
        if rdm_extension_type is not None:
            self.rdm_extension_type = rdm_extension_type
        if rdm_version is not None:
            self.rdm_version = rdm_version
        if security_level is not None:
            self.security_level = security_level
        if tenant is not None:
            self.tenant = tenant

    @property
    def class_name(self):
        """Gets the class_name of this TenantViewDTO.

        类名。

        :return: The class_name of this TenantViewDTO.
        :rtype: str
        """
        return self._class_name

    @class_name.setter
    def class_name(self, class_name):
        """Sets the class_name of this TenantViewDTO.

        类名。

        :param class_name: The class_name of this TenantViewDTO.
        :type class_name: str
        """
        self._class_name = class_name

    @property
    def code(self):
        """Gets the code of this TenantViewDTO.

        租户编码。

        :return: The code of this TenantViewDTO.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this TenantViewDTO.

        租户编码。

        :param code: The code of this TenantViewDTO.
        :type code: str
        """
        self._code = code

    @property
    def create_time(self):
        """Gets the create_time of this TenantViewDTO.

        创建时间。

        :return: The create_time of this TenantViewDTO.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this TenantViewDTO.

        创建时间。

        :param create_time: The create_time of this TenantViewDTO.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def creator(self):
        """Gets the creator of this TenantViewDTO.

        创建者。

        :return: The creator of this TenantViewDTO.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this TenantViewDTO.

        创建者。

        :param creator: The creator of this TenantViewDTO.
        :type creator: str
        """
        self._creator = creator

    @property
    def data_source(self):
        """Gets the data_source of this TenantViewDTO.

        租户使用的数据源名称。

        :return: The data_source of this TenantViewDTO.
        :rtype: str
        """
        return self._data_source

    @data_source.setter
    def data_source(self, data_source):
        """Sets the data_source of this TenantViewDTO.

        租户使用的数据源名称。

        :param data_source: The data_source of this TenantViewDTO.
        :type data_source: str
        """
        self._data_source = data_source

    @property
    def description(self):
        """Gets the description of this TenantViewDTO.

        描述信息。

        :return: The description of this TenantViewDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TenantViewDTO.

        描述信息。

        :param description: The description of this TenantViewDTO.
        :type description: str
        """
        self._description = description

    @property
    def disable_flag(self):
        """Gets the disable_flag of this TenantViewDTO.

        失效标识。  - true：失效。  - false：未失效。

        :return: The disable_flag of this TenantViewDTO.
        :rtype: bool
        """
        return self._disable_flag

    @disable_flag.setter
    def disable_flag(self, disable_flag):
        """Sets the disable_flag of this TenantViewDTO.

        失效标识。  - true：失效。  - false：未失效。

        :param disable_flag: The disable_flag of this TenantViewDTO.
        :type disable_flag: bool
        """
        self._disable_flag = disable_flag

    @property
    def id(self):
        """Gets the id of this TenantViewDTO.

        唯一标识。

        :return: The id of this TenantViewDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TenantViewDTO.

        唯一标识。

        :param id: The id of this TenantViewDTO.
        :type id: str
        """
        self._id = id

    @property
    def kiaguid(self):
        """Gets the kiaguid of this TenantViewDTO.

        KIA密级。

        :return: The kiaguid of this TenantViewDTO.
        :rtype: str
        """
        return self._kiaguid

    @kiaguid.setter
    def kiaguid(self, kiaguid):
        """Sets the kiaguid of this TenantViewDTO.

        KIA密级。

        :param kiaguid: The kiaguid of this TenantViewDTO.
        :type kiaguid: str
        """
        self._kiaguid = kiaguid

    @property
    def last_update_time(self):
        """Gets the last_update_time of this TenantViewDTO.

        最后更新时间。

        :return: The last_update_time of this TenantViewDTO.
        :rtype: str
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        """Sets the last_update_time of this TenantViewDTO.

        最后更新时间。

        :param last_update_time: The last_update_time of this TenantViewDTO.
        :type last_update_time: str
        """
        self._last_update_time = last_update_time

    @property
    def modifier(self):
        """Gets the modifier of this TenantViewDTO.

        修改人。

        :return: The modifier of this TenantViewDTO.
        :rtype: str
        """
        return self._modifier

    @modifier.setter
    def modifier(self, modifier):
        """Sets the modifier of this TenantViewDTO.

        修改人。

        :param modifier: The modifier of this TenantViewDTO.
        :type modifier: str
        """
        self._modifier = modifier

    @property
    def name(self):
        """Gets the name of this TenantViewDTO.

        中文名称。

        :return: The name of this TenantViewDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TenantViewDTO.

        中文名称。

        :param name: The name of this TenantViewDTO.
        :type name: str
        """
        self._name = name

    @property
    def rdm_delete_flag(self):
        """Gets the rdm_delete_flag of this TenantViewDTO.

        软删除标识，参数值为0或1。 - 0：表示未删除。 - 1：表示已删除。

        :return: The rdm_delete_flag of this TenantViewDTO.
        :rtype: int
        """
        return self._rdm_delete_flag

    @rdm_delete_flag.setter
    def rdm_delete_flag(self, rdm_delete_flag):
        """Sets the rdm_delete_flag of this TenantViewDTO.

        软删除标识，参数值为0或1。 - 0：表示未删除。 - 1：表示已删除。

        :param rdm_delete_flag: The rdm_delete_flag of this TenantViewDTO.
        :type rdm_delete_flag: int
        """
        self._rdm_delete_flag = rdm_delete_flag

    @property
    def rdm_extension_type(self):
        """Gets the rdm_extension_type of this TenantViewDTO.

        扩展类型。

        :return: The rdm_extension_type of this TenantViewDTO.
        :rtype: str
        """
        return self._rdm_extension_type

    @rdm_extension_type.setter
    def rdm_extension_type(self, rdm_extension_type):
        """Sets the rdm_extension_type of this TenantViewDTO.

        扩展类型。

        :param rdm_extension_type: The rdm_extension_type of this TenantViewDTO.
        :type rdm_extension_type: str
        """
        self._rdm_extension_type = rdm_extension_type

    @property
    def rdm_version(self):
        """Gets the rdm_version of this TenantViewDTO.

        系统版本。

        :return: The rdm_version of this TenantViewDTO.
        :rtype: int
        """
        return self._rdm_version

    @rdm_version.setter
    def rdm_version(self, rdm_version):
        """Sets the rdm_version of this TenantViewDTO.

        系统版本。

        :param rdm_version: The rdm_version of this TenantViewDTO.
        :type rdm_version: int
        """
        self._rdm_version = rdm_version

    @property
    def security_level(self):
        """Gets the security_level of this TenantViewDTO.

        安全密级。 - INTERNAL：内部公开。 - SECRET：秘密。 - CONFIDENTIAL：机密。 - TOP_SECRET：绝密。

        :return: The security_level of this TenantViewDTO.
        :rtype: str
        """
        return self._security_level

    @security_level.setter
    def security_level(self, security_level):
        """Sets the security_level of this TenantViewDTO.

        安全密级。 - INTERNAL：内部公开。 - SECRET：秘密。 - CONFIDENTIAL：机密。 - TOP_SECRET：绝密。

        :param security_level: The security_level of this TenantViewDTO.
        :type security_level: str
        """
        self._security_level = security_level

    @property
    def tenant(self):
        """Gets the tenant of this TenantViewDTO.

        :return: The tenant of this TenantViewDTO.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.TenantViewDTO`
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """Sets the tenant of this TenantViewDTO.

        :param tenant: The tenant of this TenantViewDTO.
        :type tenant: :class:`huaweicloudsdkidmeclassicapi.v1.TenantViewDTO`
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
        if not isinstance(other, TenantViewDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
