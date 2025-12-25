# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LayoutDetailInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cloud_pack_id': 'str',
        'cloud_pack_name': 'str',
        'cloud_pack_version': 'str',
        'is_built_in': 'bool',
        'is_template': 'bool',
        'create_time': 'str',
        'creator_id': 'str',
        'parent_id': 'str',
        'creator_name': 'str',
        'description': 'str',
        'en_description': 'str',
        'id': 'str',
        'name': 'str',
        'en_name': 'str',
        'layout_json': 'str',
        'project_id': 'str',
        'update_time': 'str',
        'workspace_id': 'str',
        'region_id': 'str',
        'domain_id': 'str',
        'thumbnail': 'str',
        'used_by': 'str',
        'layout_cfg': 'str',
        'layout_type': 'str',
        'binding_id': 'str',
        'binding_name': 'str',
        'binding_code': 'str',
        'fields_sum': 'int',
        'wizards_sum': 'int',
        'sections_sum': 'int',
        'modules_sum': 'int',
        'tabs_sum': 'int',
        'version': 'str',
        'boa_version': 'str'
    }

    attribute_map = {
        'cloud_pack_id': 'cloud_pack_id',
        'cloud_pack_name': 'cloud_pack_name',
        'cloud_pack_version': 'cloud_pack_version',
        'is_built_in': 'is_built_in',
        'is_template': 'is_template',
        'create_time': 'create_time',
        'creator_id': 'creator_id',
        'parent_id': 'parent_id',
        'creator_name': 'creator_name',
        'description': 'description',
        'en_description': 'en_description',
        'id': 'id',
        'name': 'name',
        'en_name': 'en_name',
        'layout_json': 'layout_json',
        'project_id': 'project_id',
        'update_time': 'update_time',
        'workspace_id': 'workspace_id',
        'region_id': 'region_id',
        'domain_id': 'domain_id',
        'thumbnail': 'thumbnail',
        'used_by': 'used_by',
        'layout_cfg': 'layout_cfg',
        'layout_type': 'layout_type',
        'binding_id': 'binding_id',
        'binding_name': 'binding_name',
        'binding_code': 'binding_code',
        'fields_sum': 'fields_sum',
        'wizards_sum': 'wizards_sum',
        'sections_sum': 'sections_sum',
        'modules_sum': 'modules_sum',
        'tabs_sum': 'tabs_sum',
        'version': 'version',
        'boa_version': 'boa_version'
    }

    def __init__(self, cloud_pack_id=None, cloud_pack_name=None, cloud_pack_version=None, is_built_in=None, is_template=None, create_time=None, creator_id=None, parent_id=None, creator_name=None, description=None, en_description=None, id=None, name=None, en_name=None, layout_json=None, project_id=None, update_time=None, workspace_id=None, region_id=None, domain_id=None, thumbnail=None, used_by=None, layout_cfg=None, layout_type=None, binding_id=None, binding_name=None, binding_code=None, fields_sum=None, wizards_sum=None, sections_sum=None, modules_sum=None, tabs_sum=None, version=None, boa_version=None):
        r"""LayoutDetailInfo

        The model defined in huaweicloud sdk

        :param cloud_pack_id: 订阅包id
        :type cloud_pack_id: str
        :param cloud_pack_name: 订阅包名称
        :type cloud_pack_name: str
        :param cloud_pack_version: 订阅包版本
        :type cloud_pack_version: str
        :param is_built_in: 是否内置，true内置，false非内置
        :type is_built_in: bool
        :param is_template: 是否为模板
        :type is_template: bool
        :param create_time: 创建时间
        :type create_time: str
        :param creator_id: 创建者ID
        :type creator_id: str
        :param parent_id: 父布局ID
        :type parent_id: str
        :param creator_name: 创建者名称
        :type creator_name: str
        :param description: 描述信息
        :type description: str
        :param en_description: 英文描述信息
        :type en_description: str
        :param id: 订阅包id
        :type id: str
        :param name: 名称
        :type name: str
        :param en_name: 英文名称
        :type en_name: str
        :param layout_json: 布局下的wizard id列表
        :type layout_json: str
        :param project_id: 租户ID
        :type project_id: str
        :param update_time: 更新时间
        :type update_time: str
        :param workspace_id: 工作空间ID
        :type workspace_id: str
        :param region_id: 区域ID
        :type region_id: str
        :param domain_id: 用户ID
        :type domain_id: str
        :param thumbnail: 模板缩略图，当布局为模板时不为空
        :type thumbnail: str
        :param used_by: 被什么业务使用，DATACLASS/AOP_WORKFLOW/SECURITY_REPORT/DASHBOARD，及对应的字段
        :type used_by: str
        :param layout_cfg: 前端根据该值绑定图标
        :type layout_cfg: str
        :param layout_type: 布局类型；used_by为SECURITY_REPORT/DASHBOARD时不返回该字段
        :type layout_type: str
        :param binding_id: 数据类ID或流程ID；used_by为SECURITY_REPORT/DASHBOARD时不返回该字段
        :type binding_id: str
        :param binding_name: 数据类名称或流程名称；used_by为SECURITY_REPORT/DASHBOARD时不返回该字段
        :type binding_name: str
        :param binding_code: 数据类或流程英文名称；used_by为SECURITY_REPORT/DASHBOARD时不返回该字段
        :type binding_code: str
        :param fields_sum: 字段总数；used_by为SECURITY_REPORT/DASHBOARD时不返回该字段
        :type fields_sum: int
        :param wizards_sum: 页面总数；used_by为SECURITY_REPORT/DASHBOARD时不返回该字段
        :type wizards_sum: int
        :param sections_sum: 系统区块总数
        :type sections_sum: int
        :param modules_sum: 系统模块总数
        :type modules_sum: int
        :param tabs_sum: 自定义指标总数
        :type tabs_sum: int
        :param version: 安全云脑版本
        :type version: str
        :param boa_version: BOA底座版本
        :type boa_version: str
        """
        
        

        self._cloud_pack_id = None
        self._cloud_pack_name = None
        self._cloud_pack_version = None
        self._is_built_in = None
        self._is_template = None
        self._create_time = None
        self._creator_id = None
        self._parent_id = None
        self._creator_name = None
        self._description = None
        self._en_description = None
        self._id = None
        self._name = None
        self._en_name = None
        self._layout_json = None
        self._project_id = None
        self._update_time = None
        self._workspace_id = None
        self._region_id = None
        self._domain_id = None
        self._thumbnail = None
        self._used_by = None
        self._layout_cfg = None
        self._layout_type = None
        self._binding_id = None
        self._binding_name = None
        self._binding_code = None
        self._fields_sum = None
        self._wizards_sum = None
        self._sections_sum = None
        self._modules_sum = None
        self._tabs_sum = None
        self._version = None
        self._boa_version = None
        self.discriminator = None

        if cloud_pack_id is not None:
            self.cloud_pack_id = cloud_pack_id
        if cloud_pack_name is not None:
            self.cloud_pack_name = cloud_pack_name
        if cloud_pack_version is not None:
            self.cloud_pack_version = cloud_pack_version
        if is_built_in is not None:
            self.is_built_in = is_built_in
        if is_template is not None:
            self.is_template = is_template
        if create_time is not None:
            self.create_time = create_time
        if creator_id is not None:
            self.creator_id = creator_id
        if parent_id is not None:
            self.parent_id = parent_id
        if creator_name is not None:
            self.creator_name = creator_name
        if description is not None:
            self.description = description
        if en_description is not None:
            self.en_description = en_description
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if en_name is not None:
            self.en_name = en_name
        if layout_json is not None:
            self.layout_json = layout_json
        if project_id is not None:
            self.project_id = project_id
        if update_time is not None:
            self.update_time = update_time
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if region_id is not None:
            self.region_id = region_id
        if domain_id is not None:
            self.domain_id = domain_id
        if thumbnail is not None:
            self.thumbnail = thumbnail
        if used_by is not None:
            self.used_by = used_by
        if layout_cfg is not None:
            self.layout_cfg = layout_cfg
        if layout_type is not None:
            self.layout_type = layout_type
        if binding_id is not None:
            self.binding_id = binding_id
        if binding_name is not None:
            self.binding_name = binding_name
        if binding_code is not None:
            self.binding_code = binding_code
        if fields_sum is not None:
            self.fields_sum = fields_sum
        if wizards_sum is not None:
            self.wizards_sum = wizards_sum
        if sections_sum is not None:
            self.sections_sum = sections_sum
        if modules_sum is not None:
            self.modules_sum = modules_sum
        if tabs_sum is not None:
            self.tabs_sum = tabs_sum
        if version is not None:
            self.version = version
        if boa_version is not None:
            self.boa_version = boa_version

    @property
    def cloud_pack_id(self):
        r"""Gets the cloud_pack_id of this LayoutDetailInfo.

        订阅包id

        :return: The cloud_pack_id of this LayoutDetailInfo.
        :rtype: str
        """
        return self._cloud_pack_id

    @cloud_pack_id.setter
    def cloud_pack_id(self, cloud_pack_id):
        r"""Sets the cloud_pack_id of this LayoutDetailInfo.

        订阅包id

        :param cloud_pack_id: The cloud_pack_id of this LayoutDetailInfo.
        :type cloud_pack_id: str
        """
        self._cloud_pack_id = cloud_pack_id

    @property
    def cloud_pack_name(self):
        r"""Gets the cloud_pack_name of this LayoutDetailInfo.

        订阅包名称

        :return: The cloud_pack_name of this LayoutDetailInfo.
        :rtype: str
        """
        return self._cloud_pack_name

    @cloud_pack_name.setter
    def cloud_pack_name(self, cloud_pack_name):
        r"""Sets the cloud_pack_name of this LayoutDetailInfo.

        订阅包名称

        :param cloud_pack_name: The cloud_pack_name of this LayoutDetailInfo.
        :type cloud_pack_name: str
        """
        self._cloud_pack_name = cloud_pack_name

    @property
    def cloud_pack_version(self):
        r"""Gets the cloud_pack_version of this LayoutDetailInfo.

        订阅包版本

        :return: The cloud_pack_version of this LayoutDetailInfo.
        :rtype: str
        """
        return self._cloud_pack_version

    @cloud_pack_version.setter
    def cloud_pack_version(self, cloud_pack_version):
        r"""Sets the cloud_pack_version of this LayoutDetailInfo.

        订阅包版本

        :param cloud_pack_version: The cloud_pack_version of this LayoutDetailInfo.
        :type cloud_pack_version: str
        """
        self._cloud_pack_version = cloud_pack_version

    @property
    def is_built_in(self):
        r"""Gets the is_built_in of this LayoutDetailInfo.

        是否内置，true内置，false非内置

        :return: The is_built_in of this LayoutDetailInfo.
        :rtype: bool
        """
        return self._is_built_in

    @is_built_in.setter
    def is_built_in(self, is_built_in):
        r"""Sets the is_built_in of this LayoutDetailInfo.

        是否内置，true内置，false非内置

        :param is_built_in: The is_built_in of this LayoutDetailInfo.
        :type is_built_in: bool
        """
        self._is_built_in = is_built_in

    @property
    def is_template(self):
        r"""Gets the is_template of this LayoutDetailInfo.

        是否为模板

        :return: The is_template of this LayoutDetailInfo.
        :rtype: bool
        """
        return self._is_template

    @is_template.setter
    def is_template(self, is_template):
        r"""Sets the is_template of this LayoutDetailInfo.

        是否为模板

        :param is_template: The is_template of this LayoutDetailInfo.
        :type is_template: bool
        """
        self._is_template = is_template

    @property
    def create_time(self):
        r"""Gets the create_time of this LayoutDetailInfo.

        创建时间

        :return: The create_time of this LayoutDetailInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this LayoutDetailInfo.

        创建时间

        :param create_time: The create_time of this LayoutDetailInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def creator_id(self):
        r"""Gets the creator_id of this LayoutDetailInfo.

        创建者ID

        :return: The creator_id of this LayoutDetailInfo.
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        r"""Sets the creator_id of this LayoutDetailInfo.

        创建者ID

        :param creator_id: The creator_id of this LayoutDetailInfo.
        :type creator_id: str
        """
        self._creator_id = creator_id

    @property
    def parent_id(self):
        r"""Gets the parent_id of this LayoutDetailInfo.

        父布局ID

        :return: The parent_id of this LayoutDetailInfo.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this LayoutDetailInfo.

        父布局ID

        :param parent_id: The parent_id of this LayoutDetailInfo.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def creator_name(self):
        r"""Gets the creator_name of this LayoutDetailInfo.

        创建者名称

        :return: The creator_name of this LayoutDetailInfo.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        r"""Sets the creator_name of this LayoutDetailInfo.

        创建者名称

        :param creator_name: The creator_name of this LayoutDetailInfo.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def description(self):
        r"""Gets the description of this LayoutDetailInfo.

        描述信息

        :return: The description of this LayoutDetailInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this LayoutDetailInfo.

        描述信息

        :param description: The description of this LayoutDetailInfo.
        :type description: str
        """
        self._description = description

    @property
    def en_description(self):
        r"""Gets the en_description of this LayoutDetailInfo.

        英文描述信息

        :return: The en_description of this LayoutDetailInfo.
        :rtype: str
        """
        return self._en_description

    @en_description.setter
    def en_description(self, en_description):
        r"""Sets the en_description of this LayoutDetailInfo.

        英文描述信息

        :param en_description: The en_description of this LayoutDetailInfo.
        :type en_description: str
        """
        self._en_description = en_description

    @property
    def id(self):
        r"""Gets the id of this LayoutDetailInfo.

        订阅包id

        :return: The id of this LayoutDetailInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this LayoutDetailInfo.

        订阅包id

        :param id: The id of this LayoutDetailInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this LayoutDetailInfo.

        名称

        :return: The name of this LayoutDetailInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this LayoutDetailInfo.

        名称

        :param name: The name of this LayoutDetailInfo.
        :type name: str
        """
        self._name = name

    @property
    def en_name(self):
        r"""Gets the en_name of this LayoutDetailInfo.

        英文名称

        :return: The en_name of this LayoutDetailInfo.
        :rtype: str
        """
        return self._en_name

    @en_name.setter
    def en_name(self, en_name):
        r"""Sets the en_name of this LayoutDetailInfo.

        英文名称

        :param en_name: The en_name of this LayoutDetailInfo.
        :type en_name: str
        """
        self._en_name = en_name

    @property
    def layout_json(self):
        r"""Gets the layout_json of this LayoutDetailInfo.

        布局下的wizard id列表

        :return: The layout_json of this LayoutDetailInfo.
        :rtype: str
        """
        return self._layout_json

    @layout_json.setter
    def layout_json(self, layout_json):
        r"""Sets the layout_json of this LayoutDetailInfo.

        布局下的wizard id列表

        :param layout_json: The layout_json of this LayoutDetailInfo.
        :type layout_json: str
        """
        self._layout_json = layout_json

    @property
    def project_id(self):
        r"""Gets the project_id of this LayoutDetailInfo.

        租户ID

        :return: The project_id of this LayoutDetailInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this LayoutDetailInfo.

        租户ID

        :param project_id: The project_id of this LayoutDetailInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def update_time(self):
        r"""Gets the update_time of this LayoutDetailInfo.

        更新时间

        :return: The update_time of this LayoutDetailInfo.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this LayoutDetailInfo.

        更新时间

        :param update_time: The update_time of this LayoutDetailInfo.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this LayoutDetailInfo.

        工作空间ID

        :return: The workspace_id of this LayoutDetailInfo.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this LayoutDetailInfo.

        工作空间ID

        :param workspace_id: The workspace_id of this LayoutDetailInfo.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def region_id(self):
        r"""Gets the region_id of this LayoutDetailInfo.

        区域ID

        :return: The region_id of this LayoutDetailInfo.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this LayoutDetailInfo.

        区域ID

        :param region_id: The region_id of this LayoutDetailInfo.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this LayoutDetailInfo.

        用户ID

        :return: The domain_id of this LayoutDetailInfo.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this LayoutDetailInfo.

        用户ID

        :param domain_id: The domain_id of this LayoutDetailInfo.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def thumbnail(self):
        r"""Gets the thumbnail of this LayoutDetailInfo.

        模板缩略图，当布局为模板时不为空

        :return: The thumbnail of this LayoutDetailInfo.
        :rtype: str
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        r"""Sets the thumbnail of this LayoutDetailInfo.

        模板缩略图，当布局为模板时不为空

        :param thumbnail: The thumbnail of this LayoutDetailInfo.
        :type thumbnail: str
        """
        self._thumbnail = thumbnail

    @property
    def used_by(self):
        r"""Gets the used_by of this LayoutDetailInfo.

        被什么业务使用，DATACLASS/AOP_WORKFLOW/SECURITY_REPORT/DASHBOARD，及对应的字段

        :return: The used_by of this LayoutDetailInfo.
        :rtype: str
        """
        return self._used_by

    @used_by.setter
    def used_by(self, used_by):
        r"""Sets the used_by of this LayoutDetailInfo.

        被什么业务使用，DATACLASS/AOP_WORKFLOW/SECURITY_REPORT/DASHBOARD，及对应的字段

        :param used_by: The used_by of this LayoutDetailInfo.
        :type used_by: str
        """
        self._used_by = used_by

    @property
    def layout_cfg(self):
        r"""Gets the layout_cfg of this LayoutDetailInfo.

        前端根据该值绑定图标

        :return: The layout_cfg of this LayoutDetailInfo.
        :rtype: str
        """
        return self._layout_cfg

    @layout_cfg.setter
    def layout_cfg(self, layout_cfg):
        r"""Sets the layout_cfg of this LayoutDetailInfo.

        前端根据该值绑定图标

        :param layout_cfg: The layout_cfg of this LayoutDetailInfo.
        :type layout_cfg: str
        """
        self._layout_cfg = layout_cfg

    @property
    def layout_type(self):
        r"""Gets the layout_type of this LayoutDetailInfo.

        布局类型；used_by为SECURITY_REPORT/DASHBOARD时不返回该字段

        :return: The layout_type of this LayoutDetailInfo.
        :rtype: str
        """
        return self._layout_type

    @layout_type.setter
    def layout_type(self, layout_type):
        r"""Sets the layout_type of this LayoutDetailInfo.

        布局类型；used_by为SECURITY_REPORT/DASHBOARD时不返回该字段

        :param layout_type: The layout_type of this LayoutDetailInfo.
        :type layout_type: str
        """
        self._layout_type = layout_type

    @property
    def binding_id(self):
        r"""Gets the binding_id of this LayoutDetailInfo.

        数据类ID或流程ID；used_by为SECURITY_REPORT/DASHBOARD时不返回该字段

        :return: The binding_id of this LayoutDetailInfo.
        :rtype: str
        """
        return self._binding_id

    @binding_id.setter
    def binding_id(self, binding_id):
        r"""Sets the binding_id of this LayoutDetailInfo.

        数据类ID或流程ID；used_by为SECURITY_REPORT/DASHBOARD时不返回该字段

        :param binding_id: The binding_id of this LayoutDetailInfo.
        :type binding_id: str
        """
        self._binding_id = binding_id

    @property
    def binding_name(self):
        r"""Gets the binding_name of this LayoutDetailInfo.

        数据类名称或流程名称；used_by为SECURITY_REPORT/DASHBOARD时不返回该字段

        :return: The binding_name of this LayoutDetailInfo.
        :rtype: str
        """
        return self._binding_name

    @binding_name.setter
    def binding_name(self, binding_name):
        r"""Sets the binding_name of this LayoutDetailInfo.

        数据类名称或流程名称；used_by为SECURITY_REPORT/DASHBOARD时不返回该字段

        :param binding_name: The binding_name of this LayoutDetailInfo.
        :type binding_name: str
        """
        self._binding_name = binding_name

    @property
    def binding_code(self):
        r"""Gets the binding_code of this LayoutDetailInfo.

        数据类或流程英文名称；used_by为SECURITY_REPORT/DASHBOARD时不返回该字段

        :return: The binding_code of this LayoutDetailInfo.
        :rtype: str
        """
        return self._binding_code

    @binding_code.setter
    def binding_code(self, binding_code):
        r"""Sets the binding_code of this LayoutDetailInfo.

        数据类或流程英文名称；used_by为SECURITY_REPORT/DASHBOARD时不返回该字段

        :param binding_code: The binding_code of this LayoutDetailInfo.
        :type binding_code: str
        """
        self._binding_code = binding_code

    @property
    def fields_sum(self):
        r"""Gets the fields_sum of this LayoutDetailInfo.

        字段总数；used_by为SECURITY_REPORT/DASHBOARD时不返回该字段

        :return: The fields_sum of this LayoutDetailInfo.
        :rtype: int
        """
        return self._fields_sum

    @fields_sum.setter
    def fields_sum(self, fields_sum):
        r"""Sets the fields_sum of this LayoutDetailInfo.

        字段总数；used_by为SECURITY_REPORT/DASHBOARD时不返回该字段

        :param fields_sum: The fields_sum of this LayoutDetailInfo.
        :type fields_sum: int
        """
        self._fields_sum = fields_sum

    @property
    def wizards_sum(self):
        r"""Gets the wizards_sum of this LayoutDetailInfo.

        页面总数；used_by为SECURITY_REPORT/DASHBOARD时不返回该字段

        :return: The wizards_sum of this LayoutDetailInfo.
        :rtype: int
        """
        return self._wizards_sum

    @wizards_sum.setter
    def wizards_sum(self, wizards_sum):
        r"""Sets the wizards_sum of this LayoutDetailInfo.

        页面总数；used_by为SECURITY_REPORT/DASHBOARD时不返回该字段

        :param wizards_sum: The wizards_sum of this LayoutDetailInfo.
        :type wizards_sum: int
        """
        self._wizards_sum = wizards_sum

    @property
    def sections_sum(self):
        r"""Gets the sections_sum of this LayoutDetailInfo.

        系统区块总数

        :return: The sections_sum of this LayoutDetailInfo.
        :rtype: int
        """
        return self._sections_sum

    @sections_sum.setter
    def sections_sum(self, sections_sum):
        r"""Sets the sections_sum of this LayoutDetailInfo.

        系统区块总数

        :param sections_sum: The sections_sum of this LayoutDetailInfo.
        :type sections_sum: int
        """
        self._sections_sum = sections_sum

    @property
    def modules_sum(self):
        r"""Gets the modules_sum of this LayoutDetailInfo.

        系统模块总数

        :return: The modules_sum of this LayoutDetailInfo.
        :rtype: int
        """
        return self._modules_sum

    @modules_sum.setter
    def modules_sum(self, modules_sum):
        r"""Sets the modules_sum of this LayoutDetailInfo.

        系统模块总数

        :param modules_sum: The modules_sum of this LayoutDetailInfo.
        :type modules_sum: int
        """
        self._modules_sum = modules_sum

    @property
    def tabs_sum(self):
        r"""Gets the tabs_sum of this LayoutDetailInfo.

        自定义指标总数

        :return: The tabs_sum of this LayoutDetailInfo.
        :rtype: int
        """
        return self._tabs_sum

    @tabs_sum.setter
    def tabs_sum(self, tabs_sum):
        r"""Sets the tabs_sum of this LayoutDetailInfo.

        自定义指标总数

        :param tabs_sum: The tabs_sum of this LayoutDetailInfo.
        :type tabs_sum: int
        """
        self._tabs_sum = tabs_sum

    @property
    def version(self):
        r"""Gets the version of this LayoutDetailInfo.

        安全云脑版本

        :return: The version of this LayoutDetailInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this LayoutDetailInfo.

        安全云脑版本

        :param version: The version of this LayoutDetailInfo.
        :type version: str
        """
        self._version = version

    @property
    def boa_version(self):
        r"""Gets the boa_version of this LayoutDetailInfo.

        BOA底座版本

        :return: The boa_version of this LayoutDetailInfo.
        :rtype: str
        """
        return self._boa_version

    @boa_version.setter
    def boa_version(self, boa_version):
        r"""Sets the boa_version of this LayoutDetailInfo.

        BOA底座版本

        :param boa_version: The boa_version of this LayoutDetailInfo.
        :type boa_version: str
        """
        self._boa_version = boa_version

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
        if not isinstance(other, LayoutDetailInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
