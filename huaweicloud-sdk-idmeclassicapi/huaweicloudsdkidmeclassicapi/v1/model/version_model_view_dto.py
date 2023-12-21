# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VersionModelViewDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'branch': 'VersionModelBranchViewDTO',
        'check_out_time': 'str',
        'check_out_user_name': 'str',
        'class_name': 'str',
        'create_time': 'str',
        'creator': 'str',
        'description': 'str',
        'id': 'str',
        'iteration': 'int',
        'kiaguid': 'str',
        'last_update_time': 'str',
        'latest': 'bool',
        'latest_iteration': 'bool',
        'latest_version': 'bool',
        'master': 'VersionModelMasterViewDTO',
        'modifier': 'str',
        'name': 'str',
        'pre_version_id': 'int',
        'rdm_delete_flag': 'int',
        'rdm_extension_type': 'str',
        'rdm_version': 'int',
        'security_level': 'str',
        'tenant': 'TenantViewDTO',
        'version': 'str',
        'version_code': 'int',
        'working_copy': 'bool',
        'working_state': 'WorkingState'
    }

    attribute_map = {
        'branch': 'branch',
        'check_out_time': 'checkOutTime',
        'check_out_user_name': 'checkOutUserName',
        'class_name': 'className',
        'create_time': 'createTime',
        'creator': 'creator',
        'description': 'description',
        'id': 'id',
        'iteration': 'iteration',
        'kiaguid': 'kiaguid',
        'last_update_time': 'lastUpdateTime',
        'latest': 'latest',
        'latest_iteration': 'latestIteration',
        'latest_version': 'latestVersion',
        'master': 'master',
        'modifier': 'modifier',
        'name': 'name',
        'pre_version_id': 'preVersionId',
        'rdm_delete_flag': 'rdmDeleteFlag',
        'rdm_extension_type': 'rdmExtensionType',
        'rdm_version': 'rdmVersion',
        'security_level': 'securityLevel',
        'tenant': 'tenant',
        'version': 'version',
        'version_code': 'versionCode',
        'working_copy': 'workingCopy',
        'working_state': 'workingState'
    }

    def __init__(self, branch=None, check_out_time=None, check_out_user_name=None, class_name=None, create_time=None, creator=None, description=None, id=None, iteration=None, kiaguid=None, last_update_time=None, latest=None, latest_iteration=None, latest_version=None, master=None, modifier=None, name=None, pre_version_id=None, rdm_delete_flag=None, rdm_extension_type=None, rdm_version=None, security_level=None, tenant=None, version=None, version_code=None, working_copy=None, working_state=None):
        """VersionModelViewDTO

        The model defined in huaweicloud sdk

        :param branch: 
        :type branch: :class:`huaweicloudsdkidmeclassicapi.v1.VersionModelBranchViewDTO`
        :param check_out_time: 检出时间。
        :type check_out_time: str
        :param check_out_user_name: 检出人。
        :type check_out_user_name: str
        :param class_name: 类名。
        :type class_name: str
        :param create_time: 创建时间。
        :type create_time: str
        :param creator: 创建者。
        :type creator: str
        :param description: 描述信息。
        :type description: str
        :param id: 唯一标识。
        :type id: str
        :param iteration: 迭代版本。
        :type iteration: int
        :param kiaguid: KIA密级。
        :type kiaguid: str
        :param last_update_time: 最后更新时间。
        :type last_update_time: str
        :param latest: 是否为最新版本。 - true：是最新版本。 - false：不是最新版本。
        :type latest: bool
        :param latest_iteration: 是否为最新迭代版本。 - true：是最新迭代版本。 - false：不是最新迭代版本。
        :type latest_iteration: bool
        :param latest_version: 是否为最新修订版本。 - true：是最新修订版本。 - false：不是最新修订版本。
        :type latest_version: bool
        :param master: 
        :type master: :class:`huaweicloudsdkidmeclassicapi.v1.VersionModelMasterViewDTO`
        :param modifier: 修改人。
        :type modifier: str
        :param name: 中文名称。
        :type name: str
        :param pre_version_id: 前序版本实例ID。
        :type pre_version_id: int
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
        :param version: 版本号。
        :type version: str
        :param version_code: 业务版本内码。
        :type version_code: int
        :param working_copy: 是否已检出。 - true：已检出。 - false：未检出。
        :type working_copy: bool
        :param working_state: 
        :type working_state: :class:`huaweicloudsdkidmeclassicapi.v1.WorkingState`
        """
        
        

        self._branch = None
        self._check_out_time = None
        self._check_out_user_name = None
        self._class_name = None
        self._create_time = None
        self._creator = None
        self._description = None
        self._id = None
        self._iteration = None
        self._kiaguid = None
        self._last_update_time = None
        self._latest = None
        self._latest_iteration = None
        self._latest_version = None
        self._master = None
        self._modifier = None
        self._name = None
        self._pre_version_id = None
        self._rdm_delete_flag = None
        self._rdm_extension_type = None
        self._rdm_version = None
        self._security_level = None
        self._tenant = None
        self._version = None
        self._version_code = None
        self._working_copy = None
        self._working_state = None
        self.discriminator = None

        if branch is not None:
            self.branch = branch
        if check_out_time is not None:
            self.check_out_time = check_out_time
        if check_out_user_name is not None:
            self.check_out_user_name = check_out_user_name
        if class_name is not None:
            self.class_name = class_name
        if create_time is not None:
            self.create_time = create_time
        if creator is not None:
            self.creator = creator
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if iteration is not None:
            self.iteration = iteration
        if kiaguid is not None:
            self.kiaguid = kiaguid
        if last_update_time is not None:
            self.last_update_time = last_update_time
        if latest is not None:
            self.latest = latest
        if latest_iteration is not None:
            self.latest_iteration = latest_iteration
        if latest_version is not None:
            self.latest_version = latest_version
        if master is not None:
            self.master = master
        if modifier is not None:
            self.modifier = modifier
        if name is not None:
            self.name = name
        if pre_version_id is not None:
            self.pre_version_id = pre_version_id
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
        if version is not None:
            self.version = version
        if version_code is not None:
            self.version_code = version_code
        if working_copy is not None:
            self.working_copy = working_copy
        if working_state is not None:
            self.working_state = working_state

    @property
    def branch(self):
        """Gets the branch of this VersionModelViewDTO.

        :return: The branch of this VersionModelViewDTO.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.VersionModelBranchViewDTO`
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        """Sets the branch of this VersionModelViewDTO.

        :param branch: The branch of this VersionModelViewDTO.
        :type branch: :class:`huaweicloudsdkidmeclassicapi.v1.VersionModelBranchViewDTO`
        """
        self._branch = branch

    @property
    def check_out_time(self):
        """Gets the check_out_time of this VersionModelViewDTO.

        检出时间。

        :return: The check_out_time of this VersionModelViewDTO.
        :rtype: str
        """
        return self._check_out_time

    @check_out_time.setter
    def check_out_time(self, check_out_time):
        """Sets the check_out_time of this VersionModelViewDTO.

        检出时间。

        :param check_out_time: The check_out_time of this VersionModelViewDTO.
        :type check_out_time: str
        """
        self._check_out_time = check_out_time

    @property
    def check_out_user_name(self):
        """Gets the check_out_user_name of this VersionModelViewDTO.

        检出人。

        :return: The check_out_user_name of this VersionModelViewDTO.
        :rtype: str
        """
        return self._check_out_user_name

    @check_out_user_name.setter
    def check_out_user_name(self, check_out_user_name):
        """Sets the check_out_user_name of this VersionModelViewDTO.

        检出人。

        :param check_out_user_name: The check_out_user_name of this VersionModelViewDTO.
        :type check_out_user_name: str
        """
        self._check_out_user_name = check_out_user_name

    @property
    def class_name(self):
        """Gets the class_name of this VersionModelViewDTO.

        类名。

        :return: The class_name of this VersionModelViewDTO.
        :rtype: str
        """
        return self._class_name

    @class_name.setter
    def class_name(self, class_name):
        """Sets the class_name of this VersionModelViewDTO.

        类名。

        :param class_name: The class_name of this VersionModelViewDTO.
        :type class_name: str
        """
        self._class_name = class_name

    @property
    def create_time(self):
        """Gets the create_time of this VersionModelViewDTO.

        创建时间。

        :return: The create_time of this VersionModelViewDTO.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this VersionModelViewDTO.

        创建时间。

        :param create_time: The create_time of this VersionModelViewDTO.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def creator(self):
        """Gets the creator of this VersionModelViewDTO.

        创建者。

        :return: The creator of this VersionModelViewDTO.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this VersionModelViewDTO.

        创建者。

        :param creator: The creator of this VersionModelViewDTO.
        :type creator: str
        """
        self._creator = creator

    @property
    def description(self):
        """Gets the description of this VersionModelViewDTO.

        描述信息。

        :return: The description of this VersionModelViewDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VersionModelViewDTO.

        描述信息。

        :param description: The description of this VersionModelViewDTO.
        :type description: str
        """
        self._description = description

    @property
    def id(self):
        """Gets the id of this VersionModelViewDTO.

        唯一标识。

        :return: The id of this VersionModelViewDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VersionModelViewDTO.

        唯一标识。

        :param id: The id of this VersionModelViewDTO.
        :type id: str
        """
        self._id = id

    @property
    def iteration(self):
        """Gets the iteration of this VersionModelViewDTO.

        迭代版本。

        :return: The iteration of this VersionModelViewDTO.
        :rtype: int
        """
        return self._iteration

    @iteration.setter
    def iteration(self, iteration):
        """Sets the iteration of this VersionModelViewDTO.

        迭代版本。

        :param iteration: The iteration of this VersionModelViewDTO.
        :type iteration: int
        """
        self._iteration = iteration

    @property
    def kiaguid(self):
        """Gets the kiaguid of this VersionModelViewDTO.

        KIA密级。

        :return: The kiaguid of this VersionModelViewDTO.
        :rtype: str
        """
        return self._kiaguid

    @kiaguid.setter
    def kiaguid(self, kiaguid):
        """Sets the kiaguid of this VersionModelViewDTO.

        KIA密级。

        :param kiaguid: The kiaguid of this VersionModelViewDTO.
        :type kiaguid: str
        """
        self._kiaguid = kiaguid

    @property
    def last_update_time(self):
        """Gets the last_update_time of this VersionModelViewDTO.

        最后更新时间。

        :return: The last_update_time of this VersionModelViewDTO.
        :rtype: str
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        """Sets the last_update_time of this VersionModelViewDTO.

        最后更新时间。

        :param last_update_time: The last_update_time of this VersionModelViewDTO.
        :type last_update_time: str
        """
        self._last_update_time = last_update_time

    @property
    def latest(self):
        """Gets the latest of this VersionModelViewDTO.

        是否为最新版本。 - true：是最新版本。 - false：不是最新版本。

        :return: The latest of this VersionModelViewDTO.
        :rtype: bool
        """
        return self._latest

    @latest.setter
    def latest(self, latest):
        """Sets the latest of this VersionModelViewDTO.

        是否为最新版本。 - true：是最新版本。 - false：不是最新版本。

        :param latest: The latest of this VersionModelViewDTO.
        :type latest: bool
        """
        self._latest = latest

    @property
    def latest_iteration(self):
        """Gets the latest_iteration of this VersionModelViewDTO.

        是否为最新迭代版本。 - true：是最新迭代版本。 - false：不是最新迭代版本。

        :return: The latest_iteration of this VersionModelViewDTO.
        :rtype: bool
        """
        return self._latest_iteration

    @latest_iteration.setter
    def latest_iteration(self, latest_iteration):
        """Sets the latest_iteration of this VersionModelViewDTO.

        是否为最新迭代版本。 - true：是最新迭代版本。 - false：不是最新迭代版本。

        :param latest_iteration: The latest_iteration of this VersionModelViewDTO.
        :type latest_iteration: bool
        """
        self._latest_iteration = latest_iteration

    @property
    def latest_version(self):
        """Gets the latest_version of this VersionModelViewDTO.

        是否为最新修订版本。 - true：是最新修订版本。 - false：不是最新修订版本。

        :return: The latest_version of this VersionModelViewDTO.
        :rtype: bool
        """
        return self._latest_version

    @latest_version.setter
    def latest_version(self, latest_version):
        """Sets the latest_version of this VersionModelViewDTO.

        是否为最新修订版本。 - true：是最新修订版本。 - false：不是最新修订版本。

        :param latest_version: The latest_version of this VersionModelViewDTO.
        :type latest_version: bool
        """
        self._latest_version = latest_version

    @property
    def master(self):
        """Gets the master of this VersionModelViewDTO.

        :return: The master of this VersionModelViewDTO.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.VersionModelMasterViewDTO`
        """
        return self._master

    @master.setter
    def master(self, master):
        """Sets the master of this VersionModelViewDTO.

        :param master: The master of this VersionModelViewDTO.
        :type master: :class:`huaweicloudsdkidmeclassicapi.v1.VersionModelMasterViewDTO`
        """
        self._master = master

    @property
    def modifier(self):
        """Gets the modifier of this VersionModelViewDTO.

        修改人。

        :return: The modifier of this VersionModelViewDTO.
        :rtype: str
        """
        return self._modifier

    @modifier.setter
    def modifier(self, modifier):
        """Sets the modifier of this VersionModelViewDTO.

        修改人。

        :param modifier: The modifier of this VersionModelViewDTO.
        :type modifier: str
        """
        self._modifier = modifier

    @property
    def name(self):
        """Gets the name of this VersionModelViewDTO.

        中文名称。

        :return: The name of this VersionModelViewDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VersionModelViewDTO.

        中文名称。

        :param name: The name of this VersionModelViewDTO.
        :type name: str
        """
        self._name = name

    @property
    def pre_version_id(self):
        """Gets the pre_version_id of this VersionModelViewDTO.

        前序版本实例ID。

        :return: The pre_version_id of this VersionModelViewDTO.
        :rtype: int
        """
        return self._pre_version_id

    @pre_version_id.setter
    def pre_version_id(self, pre_version_id):
        """Sets the pre_version_id of this VersionModelViewDTO.

        前序版本实例ID。

        :param pre_version_id: The pre_version_id of this VersionModelViewDTO.
        :type pre_version_id: int
        """
        self._pre_version_id = pre_version_id

    @property
    def rdm_delete_flag(self):
        """Gets the rdm_delete_flag of this VersionModelViewDTO.

        软删除标识，参数值为0或1。 - 0：表示未删除。 - 1：表示已删除。

        :return: The rdm_delete_flag of this VersionModelViewDTO.
        :rtype: int
        """
        return self._rdm_delete_flag

    @rdm_delete_flag.setter
    def rdm_delete_flag(self, rdm_delete_flag):
        """Sets the rdm_delete_flag of this VersionModelViewDTO.

        软删除标识，参数值为0或1。 - 0：表示未删除。 - 1：表示已删除。

        :param rdm_delete_flag: The rdm_delete_flag of this VersionModelViewDTO.
        :type rdm_delete_flag: int
        """
        self._rdm_delete_flag = rdm_delete_flag

    @property
    def rdm_extension_type(self):
        """Gets the rdm_extension_type of this VersionModelViewDTO.

        扩展类型。

        :return: The rdm_extension_type of this VersionModelViewDTO.
        :rtype: str
        """
        return self._rdm_extension_type

    @rdm_extension_type.setter
    def rdm_extension_type(self, rdm_extension_type):
        """Sets the rdm_extension_type of this VersionModelViewDTO.

        扩展类型。

        :param rdm_extension_type: The rdm_extension_type of this VersionModelViewDTO.
        :type rdm_extension_type: str
        """
        self._rdm_extension_type = rdm_extension_type

    @property
    def rdm_version(self):
        """Gets the rdm_version of this VersionModelViewDTO.

        系统版本。

        :return: The rdm_version of this VersionModelViewDTO.
        :rtype: int
        """
        return self._rdm_version

    @rdm_version.setter
    def rdm_version(self, rdm_version):
        """Sets the rdm_version of this VersionModelViewDTO.

        系统版本。

        :param rdm_version: The rdm_version of this VersionModelViewDTO.
        :type rdm_version: int
        """
        self._rdm_version = rdm_version

    @property
    def security_level(self):
        """Gets the security_level of this VersionModelViewDTO.

        安全密级。 - INTERNAL：内部公开。 - SECRET：秘密。 - CONFIDENTIAL：机密。 - TOP_SECRET：绝密。

        :return: The security_level of this VersionModelViewDTO.
        :rtype: str
        """
        return self._security_level

    @security_level.setter
    def security_level(self, security_level):
        """Sets the security_level of this VersionModelViewDTO.

        安全密级。 - INTERNAL：内部公开。 - SECRET：秘密。 - CONFIDENTIAL：机密。 - TOP_SECRET：绝密。

        :param security_level: The security_level of this VersionModelViewDTO.
        :type security_level: str
        """
        self._security_level = security_level

    @property
    def tenant(self):
        """Gets the tenant of this VersionModelViewDTO.

        :return: The tenant of this VersionModelViewDTO.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.TenantViewDTO`
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """Sets the tenant of this VersionModelViewDTO.

        :param tenant: The tenant of this VersionModelViewDTO.
        :type tenant: :class:`huaweicloudsdkidmeclassicapi.v1.TenantViewDTO`
        """
        self._tenant = tenant

    @property
    def version(self):
        """Gets the version of this VersionModelViewDTO.

        版本号。

        :return: The version of this VersionModelViewDTO.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this VersionModelViewDTO.

        版本号。

        :param version: The version of this VersionModelViewDTO.
        :type version: str
        """
        self._version = version

    @property
    def version_code(self):
        """Gets the version_code of this VersionModelViewDTO.

        业务版本内码。

        :return: The version_code of this VersionModelViewDTO.
        :rtype: int
        """
        return self._version_code

    @version_code.setter
    def version_code(self, version_code):
        """Sets the version_code of this VersionModelViewDTO.

        业务版本内码。

        :param version_code: The version_code of this VersionModelViewDTO.
        :type version_code: int
        """
        self._version_code = version_code

    @property
    def working_copy(self):
        """Gets the working_copy of this VersionModelViewDTO.

        是否已检出。 - true：已检出。 - false：未检出。

        :return: The working_copy of this VersionModelViewDTO.
        :rtype: bool
        """
        return self._working_copy

    @working_copy.setter
    def working_copy(self, working_copy):
        """Sets the working_copy of this VersionModelViewDTO.

        是否已检出。 - true：已检出。 - false：未检出。

        :param working_copy: The working_copy of this VersionModelViewDTO.
        :type working_copy: bool
        """
        self._working_copy = working_copy

    @property
    def working_state(self):
        """Gets the working_state of this VersionModelViewDTO.

        :return: The working_state of this VersionModelViewDTO.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.WorkingState`
        """
        return self._working_state

    @working_state.setter
    def working_state(self, working_state):
        """Sets the working_state of this VersionModelViewDTO.

        :param working_state: The working_state of this VersionModelViewDTO.
        :type working_state: :class:`huaweicloudsdkidmeclassicapi.v1.WorkingState`
        """
        self._working_state = working_state

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
        if not isinstance(other, VersionModelViewDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
