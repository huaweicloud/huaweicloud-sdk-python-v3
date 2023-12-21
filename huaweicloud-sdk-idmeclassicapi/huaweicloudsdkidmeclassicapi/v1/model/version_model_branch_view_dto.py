# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VersionModelBranchViewDTO:

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
        'id': 'str',
        'last_update_time': 'object',
        'modifier': 'str',
        'rdm_delete_flag': 'int',
        'rdm_extension_type': 'str',
        'rdm_version': 'int',
        'tenant': 'TenantViewDTO',
        'version': 'str'
    }

    attribute_map = {
        'class_name': 'className',
        'create_time': 'createTime',
        'creator': 'creator',
        'id': 'id',
        'last_update_time': 'lastUpdateTime',
        'modifier': 'modifier',
        'rdm_delete_flag': 'rdmDeleteFlag',
        'rdm_extension_type': 'rdmExtensionType',
        'rdm_version': 'rdmVersion',
        'tenant': 'tenant',
        'version': 'version'
    }

    def __init__(self, class_name=None, create_time=None, creator=None, id=None, last_update_time=None, modifier=None, rdm_delete_flag=None, rdm_extension_type=None, rdm_version=None, tenant=None, version=None):
        """VersionModelBranchViewDTO

        The model defined in huaweicloud sdk

        :param class_name: 类名。
        :type class_name: str
        :param create_time: 创建时间。
        :type create_time: str
        :param creator: 创建者。
        :type creator: str
        :param id: 唯一标识。
        :type id: str
        :param last_update_time: 最后更新时间。
        :type last_update_time: object
        :param modifier: 修改人。
        :type modifier: str
        :param rdm_delete_flag: 软删除标识，参数值为0或1。 - 0：表示未删除。 - 1：表示已删除。
        :type rdm_delete_flag: int
        :param rdm_extension_type: 扩展类型。
        :type rdm_extension_type: str
        :param rdm_version: 系统版本。
        :type rdm_version: int
        :param tenant: 
        :type tenant: :class:`huaweicloudsdkidmeclassicapi.v1.TenantViewDTO`
        :param version: 版本号。
        :type version: str
        """
        
        

        self._class_name = None
        self._create_time = None
        self._creator = None
        self._id = None
        self._last_update_time = None
        self._modifier = None
        self._rdm_delete_flag = None
        self._rdm_extension_type = None
        self._rdm_version = None
        self._tenant = None
        self._version = None
        self.discriminator = None

        if class_name is not None:
            self.class_name = class_name
        if create_time is not None:
            self.create_time = create_time
        if creator is not None:
            self.creator = creator
        if id is not None:
            self.id = id
        if last_update_time is not None:
            self.last_update_time = last_update_time
        if modifier is not None:
            self.modifier = modifier
        if rdm_delete_flag is not None:
            self.rdm_delete_flag = rdm_delete_flag
        if rdm_extension_type is not None:
            self.rdm_extension_type = rdm_extension_type
        if rdm_version is not None:
            self.rdm_version = rdm_version
        if tenant is not None:
            self.tenant = tenant
        if version is not None:
            self.version = version

    @property
    def class_name(self):
        """Gets the class_name of this VersionModelBranchViewDTO.

        类名。

        :return: The class_name of this VersionModelBranchViewDTO.
        :rtype: str
        """
        return self._class_name

    @class_name.setter
    def class_name(self, class_name):
        """Sets the class_name of this VersionModelBranchViewDTO.

        类名。

        :param class_name: The class_name of this VersionModelBranchViewDTO.
        :type class_name: str
        """
        self._class_name = class_name

    @property
    def create_time(self):
        """Gets the create_time of this VersionModelBranchViewDTO.

        创建时间。

        :return: The create_time of this VersionModelBranchViewDTO.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this VersionModelBranchViewDTO.

        创建时间。

        :param create_time: The create_time of this VersionModelBranchViewDTO.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def creator(self):
        """Gets the creator of this VersionModelBranchViewDTO.

        创建者。

        :return: The creator of this VersionModelBranchViewDTO.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this VersionModelBranchViewDTO.

        创建者。

        :param creator: The creator of this VersionModelBranchViewDTO.
        :type creator: str
        """
        self._creator = creator

    @property
    def id(self):
        """Gets the id of this VersionModelBranchViewDTO.

        唯一标识。

        :return: The id of this VersionModelBranchViewDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VersionModelBranchViewDTO.

        唯一标识。

        :param id: The id of this VersionModelBranchViewDTO.
        :type id: str
        """
        self._id = id

    @property
    def last_update_time(self):
        """Gets the last_update_time of this VersionModelBranchViewDTO.

        最后更新时间。

        :return: The last_update_time of this VersionModelBranchViewDTO.
        :rtype: object
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        """Sets the last_update_time of this VersionModelBranchViewDTO.

        最后更新时间。

        :param last_update_time: The last_update_time of this VersionModelBranchViewDTO.
        :type last_update_time: object
        """
        self._last_update_time = last_update_time

    @property
    def modifier(self):
        """Gets the modifier of this VersionModelBranchViewDTO.

        修改人。

        :return: The modifier of this VersionModelBranchViewDTO.
        :rtype: str
        """
        return self._modifier

    @modifier.setter
    def modifier(self, modifier):
        """Sets the modifier of this VersionModelBranchViewDTO.

        修改人。

        :param modifier: The modifier of this VersionModelBranchViewDTO.
        :type modifier: str
        """
        self._modifier = modifier

    @property
    def rdm_delete_flag(self):
        """Gets the rdm_delete_flag of this VersionModelBranchViewDTO.

        软删除标识，参数值为0或1。 - 0：表示未删除。 - 1：表示已删除。

        :return: The rdm_delete_flag of this VersionModelBranchViewDTO.
        :rtype: int
        """
        return self._rdm_delete_flag

    @rdm_delete_flag.setter
    def rdm_delete_flag(self, rdm_delete_flag):
        """Sets the rdm_delete_flag of this VersionModelBranchViewDTO.

        软删除标识，参数值为0或1。 - 0：表示未删除。 - 1：表示已删除。

        :param rdm_delete_flag: The rdm_delete_flag of this VersionModelBranchViewDTO.
        :type rdm_delete_flag: int
        """
        self._rdm_delete_flag = rdm_delete_flag

    @property
    def rdm_extension_type(self):
        """Gets the rdm_extension_type of this VersionModelBranchViewDTO.

        扩展类型。

        :return: The rdm_extension_type of this VersionModelBranchViewDTO.
        :rtype: str
        """
        return self._rdm_extension_type

    @rdm_extension_type.setter
    def rdm_extension_type(self, rdm_extension_type):
        """Sets the rdm_extension_type of this VersionModelBranchViewDTO.

        扩展类型。

        :param rdm_extension_type: The rdm_extension_type of this VersionModelBranchViewDTO.
        :type rdm_extension_type: str
        """
        self._rdm_extension_type = rdm_extension_type

    @property
    def rdm_version(self):
        """Gets the rdm_version of this VersionModelBranchViewDTO.

        系统版本。

        :return: The rdm_version of this VersionModelBranchViewDTO.
        :rtype: int
        """
        return self._rdm_version

    @rdm_version.setter
    def rdm_version(self, rdm_version):
        """Sets the rdm_version of this VersionModelBranchViewDTO.

        系统版本。

        :param rdm_version: The rdm_version of this VersionModelBranchViewDTO.
        :type rdm_version: int
        """
        self._rdm_version = rdm_version

    @property
    def tenant(self):
        """Gets the tenant of this VersionModelBranchViewDTO.

        :return: The tenant of this VersionModelBranchViewDTO.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.TenantViewDTO`
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """Sets the tenant of this VersionModelBranchViewDTO.

        :param tenant: The tenant of this VersionModelBranchViewDTO.
        :type tenant: :class:`huaweicloudsdkidmeclassicapi.v1.TenantViewDTO`
        """
        self._tenant = tenant

    @property
    def version(self):
        """Gets the version of this VersionModelBranchViewDTO.

        版本号。

        :return: The version of this VersionModelBranchViewDTO.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this VersionModelBranchViewDTO.

        版本号。

        :param version: The version of this VersionModelBranchViewDTO.
        :type version: str
        """
        self._version = version

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
        if not isinstance(other, VersionModelBranchViewDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
