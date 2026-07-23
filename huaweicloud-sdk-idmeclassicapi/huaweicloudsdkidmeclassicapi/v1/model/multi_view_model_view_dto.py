# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MultiViewModelViewDTO:

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
        'name': 'str',
        'description': 'str',
        'class_name': 'str',
        'creator': 'str',
        'create_time': 'str',
        'modifier': 'str',
        'last_update_time': 'str',
        'rdm_version': 'int',
        'rdm_delete_flag': 'int',
        'rdm_extension_type': 'str',
        'kiaguid': 'str',
        'security_level': 'str',
        'version': 'str',
        'version_code': 'int',
        'iteration': 'int',
        'latest': 'bool',
        'latest_version': 'bool',
        'latest_iteration': 'bool',
        'working_copy': 'bool',
        'working_state': 'WorkingState',
        'check_out_user_name': 'str',
        'check_out_time': 'str',
        'pre_version_id': 'str',
        'master': 'MultiViewModelMasterViewDTO',
        'branch': 'MultiViewModelBranchViewDTO',
        'item': 'MultiViewItemViewDTO',
        'tenant': 'TenantViewDTO'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'class_name': 'className',
        'creator': 'creator',
        'create_time': 'createTime',
        'modifier': 'modifier',
        'last_update_time': 'lastUpdateTime',
        'rdm_version': 'rdmVersion',
        'rdm_delete_flag': 'rdmDeleteFlag',
        'rdm_extension_type': 'rdmExtensionType',
        'kiaguid': 'kiaguid',
        'security_level': 'securityLevel',
        'version': 'version',
        'version_code': 'versionCode',
        'iteration': 'iteration',
        'latest': 'latest',
        'latest_version': 'latestVersion',
        'latest_iteration': 'latestIteration',
        'working_copy': 'workingCopy',
        'working_state': 'workingState',
        'check_out_user_name': 'checkOutUserName',
        'check_out_time': 'checkOutTime',
        'pre_version_id': 'preVersionId',
        'master': 'master',
        'branch': 'branch',
        'item': 'item',
        'tenant': 'tenant'
    }

    def __init__(self, id=None, name=None, description=None, class_name=None, creator=None, create_time=None, modifier=None, last_update_time=None, rdm_version=None, rdm_delete_flag=None, rdm_extension_type=None, kiaguid=None, security_level=None, version=None, version_code=None, iteration=None, latest=None, latest_version=None, latest_iteration=None, working_copy=None, working_state=None, check_out_user_name=None, check_out_time=None, pre_version_id=None, master=None, branch=None, item=None, tenant=None):
        r"""MultiViewModelViewDTO

        The model defined in huaweicloud sdk

        :param id: **参数解释：**  视图实例的唯一标识。  **取值范围：**  -9223372036854775808到9223372036854775807的整数。
        :type id: str
        :param name: **参数解释：**  视图中文名称。  **取值范围：**  不涉及。
        :type name: str
        :param description: **参数解释：**  视图描述信息。  **取值范围：**  不涉及。
        :type description: str
        :param class_name: **参数解释：**  数据模型的类名称。  **取值范围：**  不涉及。
        :type class_name: str
        :param creator: **参数解释：**  视图的创建者账号。  **取值范围：**  不涉及。
        :type creator: str
        :param create_time: **参数解释：**  视图的创建时间，使用UTC+0时间格式，格式为yyyy-MM-ddTHH:mm:ss.SSSZ。  **取值范围：**  不涉及。
        :type create_time: str
        :param modifier: **参数解释：**  视图的更新者账号。  **取值范围：**  不涉及。
        :type modifier: str
        :param last_update_time: **参数解释：**  视图最后更新时间。使用UTC+0时间格式，格式为yyyy-MM-ddTHH:mm:ss.SSSZ。  **取值范围：**  不涉及。
        :type last_update_time: str
        :param rdm_version: **参数解释：**  系统版本号。  **取值范围：**  不涉及。
        :type rdm_version: int
        :param rdm_delete_flag: **参数解释：**  软删除标识。  **取值范围：**  - 0：表示未删除。 - 1：表示已删除。
        :type rdm_delete_flag: int
        :param rdm_extension_type: **参数解释：**  扩展类型，标识数据模型的扩展分类。  **取值范围：**  不涉及。
        :type rdm_extension_type: str
        :param kiaguid: **参数解释：**  KIA密级。  **取值范围：**
        :type kiaguid: str
        :param security_level: **参数解释：**  安全密级。  **取值范围：**  - internal：内部公开。 - secret：秘密。 - confidential：机密。 - top_secret：绝密。
        :type security_level: str
        :param version: **参数解释：**  版本号，标识该视图的版本标识。  **取值范围：**  不涉及。
        :type version: str
        :param version_code: **参数解释：**  业务版本内码，用于系统内部版本管理。  **取值范围：**  不涉及。
        :type version_code: int
        :param iteration: **参数解释：**  迭代版本号，标识该视图在当前版本下的迭代次数。  **取值范围：**  不涉及。
        :type iteration: int
        :param latest: **参数解释：**  是否为最新版本。  **取值范围：**  - true：是最新版本。 - false：不是最新版本。
        :type latest: bool
        :param latest_version: **参数解释：**  是否为最新修订版本。  **取值范围：**  - true：是最新修订版本。 - false：不是最新修订版本。
        :type latest_version: bool
        :param latest_iteration: **参数解释：**  是否为最新迭代版本。  **取值范围：**  - true：是最新迭代版本。 - false：不是最新迭代版本。
        :type latest_iteration: bool
        :param working_copy: **参数解释：**  是否已检出。  **取值范围：**  - true：已检出。 - false：未检出。
        :type working_copy: bool
        :param working_state: 
        :type working_state: :class:`huaweicloudsdkidmeclassicapi.v1.WorkingState`
        :param check_out_user_name: **参数解释：**  检出人。  **取值范围：**  不涉及。
        :type check_out_user_name: str
        :param check_out_time: **参数解释：**  检出时间。使用UTC+0时间格式，格式为yyyy-MM-ddTHH:mm:ss.SSSZ。  **取值范围：**  不涉及。
        :type check_out_time: str
        :param pre_version_id: **参数解释：**  前序版本实例ID。  **取值范围：**  不涉及。
        :type pre_version_id: str
        :param master: 
        :type master: :class:`huaweicloudsdkidmeclassicapi.v1.MultiViewModelMasterViewDTO`
        :param branch: 
        :type branch: :class:`huaweicloudsdkidmeclassicapi.v1.MultiViewModelBranchViewDTO`
        :param item: 
        :type item: :class:`huaweicloudsdkidmeclassicapi.v1.MultiViewItemViewDTO`
        :param tenant: 
        :type tenant: :class:`huaweicloudsdkidmeclassicapi.v1.TenantViewDTO`
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._class_name = None
        self._creator = None
        self._create_time = None
        self._modifier = None
        self._last_update_time = None
        self._rdm_version = None
        self._rdm_delete_flag = None
        self._rdm_extension_type = None
        self._kiaguid = None
        self._security_level = None
        self._version = None
        self._version_code = None
        self._iteration = None
        self._latest = None
        self._latest_version = None
        self._latest_iteration = None
        self._working_copy = None
        self._working_state = None
        self._check_out_user_name = None
        self._check_out_time = None
        self._pre_version_id = None
        self._master = None
        self._branch = None
        self._item = None
        self._tenant = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if class_name is not None:
            self.class_name = class_name
        if creator is not None:
            self.creator = creator
        if create_time is not None:
            self.create_time = create_time
        if modifier is not None:
            self.modifier = modifier
        if last_update_time is not None:
            self.last_update_time = last_update_time
        if rdm_version is not None:
            self.rdm_version = rdm_version
        if rdm_delete_flag is not None:
            self.rdm_delete_flag = rdm_delete_flag
        if rdm_extension_type is not None:
            self.rdm_extension_type = rdm_extension_type
        if kiaguid is not None:
            self.kiaguid = kiaguid
        if security_level is not None:
            self.security_level = security_level
        if version is not None:
            self.version = version
        if version_code is not None:
            self.version_code = version_code
        if iteration is not None:
            self.iteration = iteration
        if latest is not None:
            self.latest = latest
        if latest_version is not None:
            self.latest_version = latest_version
        if latest_iteration is not None:
            self.latest_iteration = latest_iteration
        if working_copy is not None:
            self.working_copy = working_copy
        if working_state is not None:
            self.working_state = working_state
        if check_out_user_name is not None:
            self.check_out_user_name = check_out_user_name
        if check_out_time is not None:
            self.check_out_time = check_out_time
        if pre_version_id is not None:
            self.pre_version_id = pre_version_id
        if master is not None:
            self.master = master
        if branch is not None:
            self.branch = branch
        if item is not None:
            self.item = item
        if tenant is not None:
            self.tenant = tenant

    @property
    def id(self):
        r"""Gets the id of this MultiViewModelViewDTO.

        **参数解释：**  视图实例的唯一标识。  **取值范围：**  -9223372036854775808到9223372036854775807的整数。

        :return: The id of this MultiViewModelViewDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this MultiViewModelViewDTO.

        **参数解释：**  视图实例的唯一标识。  **取值范围：**  -9223372036854775808到9223372036854775807的整数。

        :param id: The id of this MultiViewModelViewDTO.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this MultiViewModelViewDTO.

        **参数解释：**  视图中文名称。  **取值范围：**  不涉及。

        :return: The name of this MultiViewModelViewDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this MultiViewModelViewDTO.

        **参数解释：**  视图中文名称。  **取值范围：**  不涉及。

        :param name: The name of this MultiViewModelViewDTO.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this MultiViewModelViewDTO.

        **参数解释：**  视图描述信息。  **取值范围：**  不涉及。

        :return: The description of this MultiViewModelViewDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this MultiViewModelViewDTO.

        **参数解释：**  视图描述信息。  **取值范围：**  不涉及。

        :param description: The description of this MultiViewModelViewDTO.
        :type description: str
        """
        self._description = description

    @property
    def class_name(self):
        r"""Gets the class_name of this MultiViewModelViewDTO.

        **参数解释：**  数据模型的类名称。  **取值范围：**  不涉及。

        :return: The class_name of this MultiViewModelViewDTO.
        :rtype: str
        """
        return self._class_name

    @class_name.setter
    def class_name(self, class_name):
        r"""Sets the class_name of this MultiViewModelViewDTO.

        **参数解释：**  数据模型的类名称。  **取值范围：**  不涉及。

        :param class_name: The class_name of this MultiViewModelViewDTO.
        :type class_name: str
        """
        self._class_name = class_name

    @property
    def creator(self):
        r"""Gets the creator of this MultiViewModelViewDTO.

        **参数解释：**  视图的创建者账号。  **取值范围：**  不涉及。

        :return: The creator of this MultiViewModelViewDTO.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this MultiViewModelViewDTO.

        **参数解释：**  视图的创建者账号。  **取值范围：**  不涉及。

        :param creator: The creator of this MultiViewModelViewDTO.
        :type creator: str
        """
        self._creator = creator

    @property
    def create_time(self):
        r"""Gets the create_time of this MultiViewModelViewDTO.

        **参数解释：**  视图的创建时间，使用UTC+0时间格式，格式为yyyy-MM-ddTHH:mm:ss.SSSZ。  **取值范围：**  不涉及。

        :return: The create_time of this MultiViewModelViewDTO.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this MultiViewModelViewDTO.

        **参数解释：**  视图的创建时间，使用UTC+0时间格式，格式为yyyy-MM-ddTHH:mm:ss.SSSZ。  **取值范围：**  不涉及。

        :param create_time: The create_time of this MultiViewModelViewDTO.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def modifier(self):
        r"""Gets the modifier of this MultiViewModelViewDTO.

        **参数解释：**  视图的更新者账号。  **取值范围：**  不涉及。

        :return: The modifier of this MultiViewModelViewDTO.
        :rtype: str
        """
        return self._modifier

    @modifier.setter
    def modifier(self, modifier):
        r"""Sets the modifier of this MultiViewModelViewDTO.

        **参数解释：**  视图的更新者账号。  **取值范围：**  不涉及。

        :param modifier: The modifier of this MultiViewModelViewDTO.
        :type modifier: str
        """
        self._modifier = modifier

    @property
    def last_update_time(self):
        r"""Gets the last_update_time of this MultiViewModelViewDTO.

        **参数解释：**  视图最后更新时间。使用UTC+0时间格式，格式为yyyy-MM-ddTHH:mm:ss.SSSZ。  **取值范围：**  不涉及。

        :return: The last_update_time of this MultiViewModelViewDTO.
        :rtype: str
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        r"""Sets the last_update_time of this MultiViewModelViewDTO.

        **参数解释：**  视图最后更新时间。使用UTC+0时间格式，格式为yyyy-MM-ddTHH:mm:ss.SSSZ。  **取值范围：**  不涉及。

        :param last_update_time: The last_update_time of this MultiViewModelViewDTO.
        :type last_update_time: str
        """
        self._last_update_time = last_update_time

    @property
    def rdm_version(self):
        r"""Gets the rdm_version of this MultiViewModelViewDTO.

        **参数解释：**  系统版本号。  **取值范围：**  不涉及。

        :return: The rdm_version of this MultiViewModelViewDTO.
        :rtype: int
        """
        return self._rdm_version

    @rdm_version.setter
    def rdm_version(self, rdm_version):
        r"""Sets the rdm_version of this MultiViewModelViewDTO.

        **参数解释：**  系统版本号。  **取值范围：**  不涉及。

        :param rdm_version: The rdm_version of this MultiViewModelViewDTO.
        :type rdm_version: int
        """
        self._rdm_version = rdm_version

    @property
    def rdm_delete_flag(self):
        r"""Gets the rdm_delete_flag of this MultiViewModelViewDTO.

        **参数解释：**  软删除标识。  **取值范围：**  - 0：表示未删除。 - 1：表示已删除。

        :return: The rdm_delete_flag of this MultiViewModelViewDTO.
        :rtype: int
        """
        return self._rdm_delete_flag

    @rdm_delete_flag.setter
    def rdm_delete_flag(self, rdm_delete_flag):
        r"""Sets the rdm_delete_flag of this MultiViewModelViewDTO.

        **参数解释：**  软删除标识。  **取值范围：**  - 0：表示未删除。 - 1：表示已删除。

        :param rdm_delete_flag: The rdm_delete_flag of this MultiViewModelViewDTO.
        :type rdm_delete_flag: int
        """
        self._rdm_delete_flag = rdm_delete_flag

    @property
    def rdm_extension_type(self):
        r"""Gets the rdm_extension_type of this MultiViewModelViewDTO.

        **参数解释：**  扩展类型，标识数据模型的扩展分类。  **取值范围：**  不涉及。

        :return: The rdm_extension_type of this MultiViewModelViewDTO.
        :rtype: str
        """
        return self._rdm_extension_type

    @rdm_extension_type.setter
    def rdm_extension_type(self, rdm_extension_type):
        r"""Sets the rdm_extension_type of this MultiViewModelViewDTO.

        **参数解释：**  扩展类型，标识数据模型的扩展分类。  **取值范围：**  不涉及。

        :param rdm_extension_type: The rdm_extension_type of this MultiViewModelViewDTO.
        :type rdm_extension_type: str
        """
        self._rdm_extension_type = rdm_extension_type

    @property
    def kiaguid(self):
        r"""Gets the kiaguid of this MultiViewModelViewDTO.

        **参数解释：**  KIA密级。  **取值范围：**

        :return: The kiaguid of this MultiViewModelViewDTO.
        :rtype: str
        """
        return self._kiaguid

    @kiaguid.setter
    def kiaguid(self, kiaguid):
        r"""Sets the kiaguid of this MultiViewModelViewDTO.

        **参数解释：**  KIA密级。  **取值范围：**

        :param kiaguid: The kiaguid of this MultiViewModelViewDTO.
        :type kiaguid: str
        """
        self._kiaguid = kiaguid

    @property
    def security_level(self):
        r"""Gets the security_level of this MultiViewModelViewDTO.

        **参数解释：**  安全密级。  **取值范围：**  - internal：内部公开。 - secret：秘密。 - confidential：机密。 - top_secret：绝密。

        :return: The security_level of this MultiViewModelViewDTO.
        :rtype: str
        """
        return self._security_level

    @security_level.setter
    def security_level(self, security_level):
        r"""Sets the security_level of this MultiViewModelViewDTO.

        **参数解释：**  安全密级。  **取值范围：**  - internal：内部公开。 - secret：秘密。 - confidential：机密。 - top_secret：绝密。

        :param security_level: The security_level of this MultiViewModelViewDTO.
        :type security_level: str
        """
        self._security_level = security_level

    @property
    def version(self):
        r"""Gets the version of this MultiViewModelViewDTO.

        **参数解释：**  版本号，标识该视图的版本标识。  **取值范围：**  不涉及。

        :return: The version of this MultiViewModelViewDTO.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this MultiViewModelViewDTO.

        **参数解释：**  版本号，标识该视图的版本标识。  **取值范围：**  不涉及。

        :param version: The version of this MultiViewModelViewDTO.
        :type version: str
        """
        self._version = version

    @property
    def version_code(self):
        r"""Gets the version_code of this MultiViewModelViewDTO.

        **参数解释：**  业务版本内码，用于系统内部版本管理。  **取值范围：**  不涉及。

        :return: The version_code of this MultiViewModelViewDTO.
        :rtype: int
        """
        return self._version_code

    @version_code.setter
    def version_code(self, version_code):
        r"""Sets the version_code of this MultiViewModelViewDTO.

        **参数解释：**  业务版本内码，用于系统内部版本管理。  **取值范围：**  不涉及。

        :param version_code: The version_code of this MultiViewModelViewDTO.
        :type version_code: int
        """
        self._version_code = version_code

    @property
    def iteration(self):
        r"""Gets the iteration of this MultiViewModelViewDTO.

        **参数解释：**  迭代版本号，标识该视图在当前版本下的迭代次数。  **取值范围：**  不涉及。

        :return: The iteration of this MultiViewModelViewDTO.
        :rtype: int
        """
        return self._iteration

    @iteration.setter
    def iteration(self, iteration):
        r"""Sets the iteration of this MultiViewModelViewDTO.

        **参数解释：**  迭代版本号，标识该视图在当前版本下的迭代次数。  **取值范围：**  不涉及。

        :param iteration: The iteration of this MultiViewModelViewDTO.
        :type iteration: int
        """
        self._iteration = iteration

    @property
    def latest(self):
        r"""Gets the latest of this MultiViewModelViewDTO.

        **参数解释：**  是否为最新版本。  **取值范围：**  - true：是最新版本。 - false：不是最新版本。

        :return: The latest of this MultiViewModelViewDTO.
        :rtype: bool
        """
        return self._latest

    @latest.setter
    def latest(self, latest):
        r"""Sets the latest of this MultiViewModelViewDTO.

        **参数解释：**  是否为最新版本。  **取值范围：**  - true：是最新版本。 - false：不是最新版本。

        :param latest: The latest of this MultiViewModelViewDTO.
        :type latest: bool
        """
        self._latest = latest

    @property
    def latest_version(self):
        r"""Gets the latest_version of this MultiViewModelViewDTO.

        **参数解释：**  是否为最新修订版本。  **取值范围：**  - true：是最新修订版本。 - false：不是最新修订版本。

        :return: The latest_version of this MultiViewModelViewDTO.
        :rtype: bool
        """
        return self._latest_version

    @latest_version.setter
    def latest_version(self, latest_version):
        r"""Sets the latest_version of this MultiViewModelViewDTO.

        **参数解释：**  是否为最新修订版本。  **取值范围：**  - true：是最新修订版本。 - false：不是最新修订版本。

        :param latest_version: The latest_version of this MultiViewModelViewDTO.
        :type latest_version: bool
        """
        self._latest_version = latest_version

    @property
    def latest_iteration(self):
        r"""Gets the latest_iteration of this MultiViewModelViewDTO.

        **参数解释：**  是否为最新迭代版本。  **取值范围：**  - true：是最新迭代版本。 - false：不是最新迭代版本。

        :return: The latest_iteration of this MultiViewModelViewDTO.
        :rtype: bool
        """
        return self._latest_iteration

    @latest_iteration.setter
    def latest_iteration(self, latest_iteration):
        r"""Sets the latest_iteration of this MultiViewModelViewDTO.

        **参数解释：**  是否为最新迭代版本。  **取值范围：**  - true：是最新迭代版本。 - false：不是最新迭代版本。

        :param latest_iteration: The latest_iteration of this MultiViewModelViewDTO.
        :type latest_iteration: bool
        """
        self._latest_iteration = latest_iteration

    @property
    def working_copy(self):
        r"""Gets the working_copy of this MultiViewModelViewDTO.

        **参数解释：**  是否已检出。  **取值范围：**  - true：已检出。 - false：未检出。

        :return: The working_copy of this MultiViewModelViewDTO.
        :rtype: bool
        """
        return self._working_copy

    @working_copy.setter
    def working_copy(self, working_copy):
        r"""Sets the working_copy of this MultiViewModelViewDTO.

        **参数解释：**  是否已检出。  **取值范围：**  - true：已检出。 - false：未检出。

        :param working_copy: The working_copy of this MultiViewModelViewDTO.
        :type working_copy: bool
        """
        self._working_copy = working_copy

    @property
    def working_state(self):
        r"""Gets the working_state of this MultiViewModelViewDTO.

        :return: The working_state of this MultiViewModelViewDTO.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.WorkingState`
        """
        return self._working_state

    @working_state.setter
    def working_state(self, working_state):
        r"""Sets the working_state of this MultiViewModelViewDTO.

        :param working_state: The working_state of this MultiViewModelViewDTO.
        :type working_state: :class:`huaweicloudsdkidmeclassicapi.v1.WorkingState`
        """
        self._working_state = working_state

    @property
    def check_out_user_name(self):
        r"""Gets the check_out_user_name of this MultiViewModelViewDTO.

        **参数解释：**  检出人。  **取值范围：**  不涉及。

        :return: The check_out_user_name of this MultiViewModelViewDTO.
        :rtype: str
        """
        return self._check_out_user_name

    @check_out_user_name.setter
    def check_out_user_name(self, check_out_user_name):
        r"""Sets the check_out_user_name of this MultiViewModelViewDTO.

        **参数解释：**  检出人。  **取值范围：**  不涉及。

        :param check_out_user_name: The check_out_user_name of this MultiViewModelViewDTO.
        :type check_out_user_name: str
        """
        self._check_out_user_name = check_out_user_name

    @property
    def check_out_time(self):
        r"""Gets the check_out_time of this MultiViewModelViewDTO.

        **参数解释：**  检出时间。使用UTC+0时间格式，格式为yyyy-MM-ddTHH:mm:ss.SSSZ。  **取值范围：**  不涉及。

        :return: The check_out_time of this MultiViewModelViewDTO.
        :rtype: str
        """
        return self._check_out_time

    @check_out_time.setter
    def check_out_time(self, check_out_time):
        r"""Sets the check_out_time of this MultiViewModelViewDTO.

        **参数解释：**  检出时间。使用UTC+0时间格式，格式为yyyy-MM-ddTHH:mm:ss.SSSZ。  **取值范围：**  不涉及。

        :param check_out_time: The check_out_time of this MultiViewModelViewDTO.
        :type check_out_time: str
        """
        self._check_out_time = check_out_time

    @property
    def pre_version_id(self):
        r"""Gets the pre_version_id of this MultiViewModelViewDTO.

        **参数解释：**  前序版本实例ID。  **取值范围：**  不涉及。

        :return: The pre_version_id of this MultiViewModelViewDTO.
        :rtype: str
        """
        return self._pre_version_id

    @pre_version_id.setter
    def pre_version_id(self, pre_version_id):
        r"""Sets the pre_version_id of this MultiViewModelViewDTO.

        **参数解释：**  前序版本实例ID。  **取值范围：**  不涉及。

        :param pre_version_id: The pre_version_id of this MultiViewModelViewDTO.
        :type pre_version_id: str
        """
        self._pre_version_id = pre_version_id

    @property
    def master(self):
        r"""Gets the master of this MultiViewModelViewDTO.

        :return: The master of this MultiViewModelViewDTO.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.MultiViewModelMasterViewDTO`
        """
        return self._master

    @master.setter
    def master(self, master):
        r"""Sets the master of this MultiViewModelViewDTO.

        :param master: The master of this MultiViewModelViewDTO.
        :type master: :class:`huaweicloudsdkidmeclassicapi.v1.MultiViewModelMasterViewDTO`
        """
        self._master = master

    @property
    def branch(self):
        r"""Gets the branch of this MultiViewModelViewDTO.

        :return: The branch of this MultiViewModelViewDTO.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.MultiViewModelBranchViewDTO`
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        r"""Sets the branch of this MultiViewModelViewDTO.

        :param branch: The branch of this MultiViewModelViewDTO.
        :type branch: :class:`huaweicloudsdkidmeclassicapi.v1.MultiViewModelBranchViewDTO`
        """
        self._branch = branch

    @property
    def item(self):
        r"""Gets the item of this MultiViewModelViewDTO.

        :return: The item of this MultiViewModelViewDTO.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.MultiViewItemViewDTO`
        """
        return self._item

    @item.setter
    def item(self, item):
        r"""Sets the item of this MultiViewModelViewDTO.

        :param item: The item of this MultiViewModelViewDTO.
        :type item: :class:`huaweicloudsdkidmeclassicapi.v1.MultiViewItemViewDTO`
        """
        self._item = item

    @property
    def tenant(self):
        r"""Gets the tenant of this MultiViewModelViewDTO.

        :return: The tenant of this MultiViewModelViewDTO.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.TenantViewDTO`
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        r"""Sets the tenant of this MultiViewModelViewDTO.

        :param tenant: The tenant of this MultiViewModelViewDTO.
        :type tenant: :class:`huaweicloudsdkidmeclassicapi.v1.TenantViewDTO`
        """
        self._tenant = tenant

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MultiViewModelViewDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
