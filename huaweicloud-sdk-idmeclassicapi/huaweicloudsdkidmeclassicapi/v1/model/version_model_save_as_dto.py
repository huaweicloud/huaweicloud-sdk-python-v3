# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VersionModelSaveAsDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'branch': 'VersionModelBranchSaveAsDTO',
        'check_out_time': 'str',
        'check_out_user_name': 'str',
        'create_time': 'str',
        'creator': 'str',
        'description': 'str',
        'entity_to_return': 'object',
        'entity_to_save': 'object',
        'id': 'str',
        'kiaguid': 'str',
        'last_update_time': 'str',
        'master': 'VersionModelMasterSaveAsDTO',
        'modifier': 'str',
        'name': 'str',
        'rdm_extension_type': 'str',
        'security_level': 'str',
        'source_instance_id': 'str',
        'source_master_id': 'str',
        'tenant': 'ObjectReferenceParamDTO',
        'working_copy': 'bool'
    }

    attribute_map = {
        'branch': 'branch',
        'check_out_time': 'checkOutTime',
        'check_out_user_name': 'checkOutUserName',
        'create_time': 'createTime',
        'creator': 'creator',
        'description': 'description',
        'entity_to_return': 'entityToReturn',
        'entity_to_save': 'entityToSave',
        'id': 'id',
        'kiaguid': 'kiaguid',
        'last_update_time': 'lastUpdateTime',
        'master': 'master',
        'modifier': 'modifier',
        'name': 'name',
        'rdm_extension_type': 'rdmExtensionType',
        'security_level': 'securityLevel',
        'source_instance_id': 'sourceInstanceId',
        'source_master_id': 'sourceMasterId',
        'tenant': 'tenant',
        'working_copy': 'workingCopy'
    }

    def __init__(self, branch=None, check_out_time=None, check_out_user_name=None, create_time=None, creator=None, description=None, entity_to_return=None, entity_to_save=None, id=None, kiaguid=None, last_update_time=None, master=None, modifier=None, name=None, rdm_extension_type=None, security_level=None, source_instance_id=None, source_master_id=None, tenant=None, working_copy=None):
        """VersionModelSaveAsDTO

        The model defined in huaweicloud sdk

        :param branch: 
        :type branch: :class:`huaweicloudsdkidmeclassicapi.v1.VersionModelBranchSaveAsDTO`
        :param check_out_time: 检出时间。
        :type check_out_time: str
        :param check_out_user_name: 检出人。
        :type check_out_user_name: str
        :param create_time: 创建时间。
        :type create_time: str
        :param creator: 创建者。
        :type creator: str
        :param description: 描述信息。
        :type description: str
        :param entity_to_return: 需要返回的实体。
        :type entity_to_return: object
        :param entity_to_save: 需要保存的实体。
        :type entity_to_save: object
        :param id: 唯一标识。
        :type id: str
        :param kiaguid: 关键信息资产ID。
        :type kiaguid: str
        :param last_update_time: 最后更新时间。
        :type last_update_time: str
        :param master: 
        :type master: :class:`huaweicloudsdkidmeclassicapi.v1.VersionModelMasterSaveAsDTO`
        :param modifier: 修改人。
        :type modifier: str
        :param name: 中文名称。
        :type name: str
        :param rdm_extension_type: 扩展类型。
        :type rdm_extension_type: str
        :param security_level: 安全密级。 - INTERNAL：内部公开。 - SECRET：秘密。 - CONFIDENTIAL：机密。 - TOP_SECRET：绝密。
        :type security_level: str
        :param source_instance_id: version.唯一编码。
        :type source_instance_id: str
        :param source_master_id: master.唯一编码。
        :type source_master_id: str
        :param tenant: 
        :type tenant: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceParamDTO`
        :param working_copy: 是否已检出。 - true：已检出。 - false：未检出。
        :type working_copy: bool
        """
        
        

        self._branch = None
        self._check_out_time = None
        self._check_out_user_name = None
        self._create_time = None
        self._creator = None
        self._description = None
        self._entity_to_return = None
        self._entity_to_save = None
        self._id = None
        self._kiaguid = None
        self._last_update_time = None
        self._master = None
        self._modifier = None
        self._name = None
        self._rdm_extension_type = None
        self._security_level = None
        self._source_instance_id = None
        self._source_master_id = None
        self._tenant = None
        self._working_copy = None
        self.discriminator = None

        if branch is not None:
            self.branch = branch
        if check_out_time is not None:
            self.check_out_time = check_out_time
        if check_out_user_name is not None:
            self.check_out_user_name = check_out_user_name
        if create_time is not None:
            self.create_time = create_time
        if creator is not None:
            self.creator = creator
        if description is not None:
            self.description = description
        if entity_to_return is not None:
            self.entity_to_return = entity_to_return
        if entity_to_save is not None:
            self.entity_to_save = entity_to_save
        if id is not None:
            self.id = id
        if kiaguid is not None:
            self.kiaguid = kiaguid
        if last_update_time is not None:
            self.last_update_time = last_update_time
        if master is not None:
            self.master = master
        if modifier is not None:
            self.modifier = modifier
        if name is not None:
            self.name = name
        if rdm_extension_type is not None:
            self.rdm_extension_type = rdm_extension_type
        if security_level is not None:
            self.security_level = security_level
        self.source_instance_id = source_instance_id
        if source_master_id is not None:
            self.source_master_id = source_master_id
        if tenant is not None:
            self.tenant = tenant
        if working_copy is not None:
            self.working_copy = working_copy

    @property
    def branch(self):
        """Gets the branch of this VersionModelSaveAsDTO.

        :return: The branch of this VersionModelSaveAsDTO.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.VersionModelBranchSaveAsDTO`
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        """Sets the branch of this VersionModelSaveAsDTO.

        :param branch: The branch of this VersionModelSaveAsDTO.
        :type branch: :class:`huaweicloudsdkidmeclassicapi.v1.VersionModelBranchSaveAsDTO`
        """
        self._branch = branch

    @property
    def check_out_time(self):
        """Gets the check_out_time of this VersionModelSaveAsDTO.

        检出时间。

        :return: The check_out_time of this VersionModelSaveAsDTO.
        :rtype: str
        """
        return self._check_out_time

    @check_out_time.setter
    def check_out_time(self, check_out_time):
        """Sets the check_out_time of this VersionModelSaveAsDTO.

        检出时间。

        :param check_out_time: The check_out_time of this VersionModelSaveAsDTO.
        :type check_out_time: str
        """
        self._check_out_time = check_out_time

    @property
    def check_out_user_name(self):
        """Gets the check_out_user_name of this VersionModelSaveAsDTO.

        检出人。

        :return: The check_out_user_name of this VersionModelSaveAsDTO.
        :rtype: str
        """
        return self._check_out_user_name

    @check_out_user_name.setter
    def check_out_user_name(self, check_out_user_name):
        """Sets the check_out_user_name of this VersionModelSaveAsDTO.

        检出人。

        :param check_out_user_name: The check_out_user_name of this VersionModelSaveAsDTO.
        :type check_out_user_name: str
        """
        self._check_out_user_name = check_out_user_name

    @property
    def create_time(self):
        """Gets the create_time of this VersionModelSaveAsDTO.

        创建时间。

        :return: The create_time of this VersionModelSaveAsDTO.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this VersionModelSaveAsDTO.

        创建时间。

        :param create_time: The create_time of this VersionModelSaveAsDTO.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def creator(self):
        """Gets the creator of this VersionModelSaveAsDTO.

        创建者。

        :return: The creator of this VersionModelSaveAsDTO.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this VersionModelSaveAsDTO.

        创建者。

        :param creator: The creator of this VersionModelSaveAsDTO.
        :type creator: str
        """
        self._creator = creator

    @property
    def description(self):
        """Gets the description of this VersionModelSaveAsDTO.

        描述信息。

        :return: The description of this VersionModelSaveAsDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VersionModelSaveAsDTO.

        描述信息。

        :param description: The description of this VersionModelSaveAsDTO.
        :type description: str
        """
        self._description = description

    @property
    def entity_to_return(self):
        """Gets the entity_to_return of this VersionModelSaveAsDTO.

        需要返回的实体。

        :return: The entity_to_return of this VersionModelSaveAsDTO.
        :rtype: object
        """
        return self._entity_to_return

    @entity_to_return.setter
    def entity_to_return(self, entity_to_return):
        """Sets the entity_to_return of this VersionModelSaveAsDTO.

        需要返回的实体。

        :param entity_to_return: The entity_to_return of this VersionModelSaveAsDTO.
        :type entity_to_return: object
        """
        self._entity_to_return = entity_to_return

    @property
    def entity_to_save(self):
        """Gets the entity_to_save of this VersionModelSaveAsDTO.

        需要保存的实体。

        :return: The entity_to_save of this VersionModelSaveAsDTO.
        :rtype: object
        """
        return self._entity_to_save

    @entity_to_save.setter
    def entity_to_save(self, entity_to_save):
        """Sets the entity_to_save of this VersionModelSaveAsDTO.

        需要保存的实体。

        :param entity_to_save: The entity_to_save of this VersionModelSaveAsDTO.
        :type entity_to_save: object
        """
        self._entity_to_save = entity_to_save

    @property
    def id(self):
        """Gets the id of this VersionModelSaveAsDTO.

        唯一标识。

        :return: The id of this VersionModelSaveAsDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VersionModelSaveAsDTO.

        唯一标识。

        :param id: The id of this VersionModelSaveAsDTO.
        :type id: str
        """
        self._id = id

    @property
    def kiaguid(self):
        """Gets the kiaguid of this VersionModelSaveAsDTO.

        关键信息资产ID。

        :return: The kiaguid of this VersionModelSaveAsDTO.
        :rtype: str
        """
        return self._kiaguid

    @kiaguid.setter
    def kiaguid(self, kiaguid):
        """Sets the kiaguid of this VersionModelSaveAsDTO.

        关键信息资产ID。

        :param kiaguid: The kiaguid of this VersionModelSaveAsDTO.
        :type kiaguid: str
        """
        self._kiaguid = kiaguid

    @property
    def last_update_time(self):
        """Gets the last_update_time of this VersionModelSaveAsDTO.

        最后更新时间。

        :return: The last_update_time of this VersionModelSaveAsDTO.
        :rtype: str
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        """Sets the last_update_time of this VersionModelSaveAsDTO.

        最后更新时间。

        :param last_update_time: The last_update_time of this VersionModelSaveAsDTO.
        :type last_update_time: str
        """
        self._last_update_time = last_update_time

    @property
    def master(self):
        """Gets the master of this VersionModelSaveAsDTO.

        :return: The master of this VersionModelSaveAsDTO.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.VersionModelMasterSaveAsDTO`
        """
        return self._master

    @master.setter
    def master(self, master):
        """Sets the master of this VersionModelSaveAsDTO.

        :param master: The master of this VersionModelSaveAsDTO.
        :type master: :class:`huaweicloudsdkidmeclassicapi.v1.VersionModelMasterSaveAsDTO`
        """
        self._master = master

    @property
    def modifier(self):
        """Gets the modifier of this VersionModelSaveAsDTO.

        修改人。

        :return: The modifier of this VersionModelSaveAsDTO.
        :rtype: str
        """
        return self._modifier

    @modifier.setter
    def modifier(self, modifier):
        """Sets the modifier of this VersionModelSaveAsDTO.

        修改人。

        :param modifier: The modifier of this VersionModelSaveAsDTO.
        :type modifier: str
        """
        self._modifier = modifier

    @property
    def name(self):
        """Gets the name of this VersionModelSaveAsDTO.

        中文名称。

        :return: The name of this VersionModelSaveAsDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VersionModelSaveAsDTO.

        中文名称。

        :param name: The name of this VersionModelSaveAsDTO.
        :type name: str
        """
        self._name = name

    @property
    def rdm_extension_type(self):
        """Gets the rdm_extension_type of this VersionModelSaveAsDTO.

        扩展类型。

        :return: The rdm_extension_type of this VersionModelSaveAsDTO.
        :rtype: str
        """
        return self._rdm_extension_type

    @rdm_extension_type.setter
    def rdm_extension_type(self, rdm_extension_type):
        """Sets the rdm_extension_type of this VersionModelSaveAsDTO.

        扩展类型。

        :param rdm_extension_type: The rdm_extension_type of this VersionModelSaveAsDTO.
        :type rdm_extension_type: str
        """
        self._rdm_extension_type = rdm_extension_type

    @property
    def security_level(self):
        """Gets the security_level of this VersionModelSaveAsDTO.

        安全密级。 - INTERNAL：内部公开。 - SECRET：秘密。 - CONFIDENTIAL：机密。 - TOP_SECRET：绝密。

        :return: The security_level of this VersionModelSaveAsDTO.
        :rtype: str
        """
        return self._security_level

    @security_level.setter
    def security_level(self, security_level):
        """Sets the security_level of this VersionModelSaveAsDTO.

        安全密级。 - INTERNAL：内部公开。 - SECRET：秘密。 - CONFIDENTIAL：机密。 - TOP_SECRET：绝密。

        :param security_level: The security_level of this VersionModelSaveAsDTO.
        :type security_level: str
        """
        self._security_level = security_level

    @property
    def source_instance_id(self):
        """Gets the source_instance_id of this VersionModelSaveAsDTO.

        version.唯一编码。

        :return: The source_instance_id of this VersionModelSaveAsDTO.
        :rtype: str
        """
        return self._source_instance_id

    @source_instance_id.setter
    def source_instance_id(self, source_instance_id):
        """Sets the source_instance_id of this VersionModelSaveAsDTO.

        version.唯一编码。

        :param source_instance_id: The source_instance_id of this VersionModelSaveAsDTO.
        :type source_instance_id: str
        """
        self._source_instance_id = source_instance_id

    @property
    def source_master_id(self):
        """Gets the source_master_id of this VersionModelSaveAsDTO.

        master.唯一编码。

        :return: The source_master_id of this VersionModelSaveAsDTO.
        :rtype: str
        """
        return self._source_master_id

    @source_master_id.setter
    def source_master_id(self, source_master_id):
        """Sets the source_master_id of this VersionModelSaveAsDTO.

        master.唯一编码。

        :param source_master_id: The source_master_id of this VersionModelSaveAsDTO.
        :type source_master_id: str
        """
        self._source_master_id = source_master_id

    @property
    def tenant(self):
        """Gets the tenant of this VersionModelSaveAsDTO.

        :return: The tenant of this VersionModelSaveAsDTO.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceParamDTO`
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """Sets the tenant of this VersionModelSaveAsDTO.

        :param tenant: The tenant of this VersionModelSaveAsDTO.
        :type tenant: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceParamDTO`
        """
        self._tenant = tenant

    @property
    def working_copy(self):
        """Gets the working_copy of this VersionModelSaveAsDTO.

        是否已检出。 - true：已检出。 - false：未检出。

        :return: The working_copy of this VersionModelSaveAsDTO.
        :rtype: bool
        """
        return self._working_copy

    @working_copy.setter
    def working_copy(self, working_copy):
        """Sets the working_copy of this VersionModelSaveAsDTO.

        是否已检出。 - true：已检出。 - false：未检出。

        :param working_copy: The working_copy of this VersionModelSaveAsDTO.
        :type working_copy: bool
        """
        self._working_copy = working_copy

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
        if not isinstance(other, VersionModelSaveAsDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
