# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDataclassTypeResponse(SdkResponse):

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
        'dataclass_id': 'str',
        'domain_id': 'str',
        'project_id': 'str',
        'workspace_id': 'str',
        'region_id': 'str',
        'layout_id': 'str',
        'layout_name': 'str',
        'category': 'str',
        'category_code': 'str',
        'sub_category': 'str',
        'sub_category_code': 'str',
        'description': 'str',
        'enabled': 'bool',
        'level': 'int',
        'is_built_in': 'bool',
        'sla': 'int',
        'creator_id': 'str',
        'creator_name': 'str',
        'modifier_id': 'str',
        'modifier_name': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'dataclass_business_code': 'str'
    }

    attribute_map = {
        'id': 'id',
        'dataclass_id': 'dataclass_id',
        'domain_id': 'domain_id',
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'region_id': 'region_id',
        'layout_id': 'layout_id',
        'layout_name': 'layout_name',
        'category': 'category',
        'category_code': 'category_code',
        'sub_category': 'sub_category',
        'sub_category_code': 'sub_category_code',
        'description': 'description',
        'enabled': 'enabled',
        'level': 'level',
        'is_built_in': 'is_built_in',
        'sla': 'sla',
        'creator_id': 'creator_id',
        'creator_name': 'creator_name',
        'modifier_id': 'modifier_id',
        'modifier_name': 'modifier_name',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'dataclass_business_code': 'dataclass_business_code'
    }

    def __init__(self, id=None, dataclass_id=None, domain_id=None, project_id=None, workspace_id=None, region_id=None, layout_id=None, layout_name=None, category=None, category_code=None, sub_category=None, sub_category_code=None, description=None, enabled=None, level=None, is_built_in=None, sla=None, creator_id=None, creator_name=None, modifier_id=None, modifier_name=None, create_time=None, update_time=None, dataclass_business_code=None):
        r"""CreateDataclassTypeResponse

        The model defined in huaweicloud sdk

        :param id: 类型id
        :type id: str
        :param dataclass_id: 数据类id
        :type dataclass_id: str
        :param domain_id: 账号id
        :type domain_id: str
        :param project_id: 项目id
        :type project_id: str
        :param workspace_id: 工作空间id
        :type workspace_id: str
        :param region_id: 局点id
        :type region_id: str
        :param layout_id: 布局id
        :type layout_id: str
        :param layout_name: 布局名称
        :type layout_name: str
        :param category: 数据类类型分类
        :type category: str
        :param category_code: 数据类类型分类编码
        :type category_code: str
        :param sub_category: 数据类类型名称
        :type sub_category: str
        :param sub_category_code: 数据类类型业务编码
        :type sub_category_code: str
        :param description: 数据类类型描述
        :type description: str
        :param enabled: 状态
        :type enabled: bool
        :param level: 事件等级
        :type level: int
        :param is_built_in: 是否内置，true内置，false非内置
        :type is_built_in: bool
        :param sla: 响应时长
        :type sla: int
        :param creator_id: 创建人id
        :type creator_id: str
        :param creator_name: 创建人名称
        :type creator_name: str
        :param modifier_id: 修改人id
        :type modifier_id: str
        :param modifier_name: 修改人名称
        :type modifier_name: str
        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 修改时间
        :type update_time: str
        :param dataclass_business_code: 所属数据类业务编码
        :type dataclass_business_code: str
        """
        
        super().__init__()

        self._id = None
        self._dataclass_id = None
        self._domain_id = None
        self._project_id = None
        self._workspace_id = None
        self._region_id = None
        self._layout_id = None
        self._layout_name = None
        self._category = None
        self._category_code = None
        self._sub_category = None
        self._sub_category_code = None
        self._description = None
        self._enabled = None
        self._level = None
        self._is_built_in = None
        self._sla = None
        self._creator_id = None
        self._creator_name = None
        self._modifier_id = None
        self._modifier_name = None
        self._create_time = None
        self._update_time = None
        self._dataclass_business_code = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if dataclass_id is not None:
            self.dataclass_id = dataclass_id
        if domain_id is not None:
            self.domain_id = domain_id
        if project_id is not None:
            self.project_id = project_id
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if region_id is not None:
            self.region_id = region_id
        if layout_id is not None:
            self.layout_id = layout_id
        if layout_name is not None:
            self.layout_name = layout_name
        if category is not None:
            self.category = category
        if category_code is not None:
            self.category_code = category_code
        if sub_category is not None:
            self.sub_category = sub_category
        if sub_category_code is not None:
            self.sub_category_code = sub_category_code
        if description is not None:
            self.description = description
        if enabled is not None:
            self.enabled = enabled
        if level is not None:
            self.level = level
        if is_built_in is not None:
            self.is_built_in = is_built_in
        if sla is not None:
            self.sla = sla
        if creator_id is not None:
            self.creator_id = creator_id
        if creator_name is not None:
            self.creator_name = creator_name
        if modifier_id is not None:
            self.modifier_id = modifier_id
        if modifier_name is not None:
            self.modifier_name = modifier_name
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if dataclass_business_code is not None:
            self.dataclass_business_code = dataclass_business_code

    @property
    def id(self):
        r"""Gets the id of this CreateDataclassTypeResponse.

        类型id

        :return: The id of this CreateDataclassTypeResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateDataclassTypeResponse.

        类型id

        :param id: The id of this CreateDataclassTypeResponse.
        :type id: str
        """
        self._id = id

    @property
    def dataclass_id(self):
        r"""Gets the dataclass_id of this CreateDataclassTypeResponse.

        数据类id

        :return: The dataclass_id of this CreateDataclassTypeResponse.
        :rtype: str
        """
        return self._dataclass_id

    @dataclass_id.setter
    def dataclass_id(self, dataclass_id):
        r"""Sets the dataclass_id of this CreateDataclassTypeResponse.

        数据类id

        :param dataclass_id: The dataclass_id of this CreateDataclassTypeResponse.
        :type dataclass_id: str
        """
        self._dataclass_id = dataclass_id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this CreateDataclassTypeResponse.

        账号id

        :return: The domain_id of this CreateDataclassTypeResponse.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this CreateDataclassTypeResponse.

        账号id

        :param domain_id: The domain_id of this CreateDataclassTypeResponse.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def project_id(self):
        r"""Gets the project_id of this CreateDataclassTypeResponse.

        项目id

        :return: The project_id of this CreateDataclassTypeResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this CreateDataclassTypeResponse.

        项目id

        :param project_id: The project_id of this CreateDataclassTypeResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this CreateDataclassTypeResponse.

        工作空间id

        :return: The workspace_id of this CreateDataclassTypeResponse.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this CreateDataclassTypeResponse.

        工作空间id

        :param workspace_id: The workspace_id of this CreateDataclassTypeResponse.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def region_id(self):
        r"""Gets the region_id of this CreateDataclassTypeResponse.

        局点id

        :return: The region_id of this CreateDataclassTypeResponse.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this CreateDataclassTypeResponse.

        局点id

        :param region_id: The region_id of this CreateDataclassTypeResponse.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def layout_id(self):
        r"""Gets the layout_id of this CreateDataclassTypeResponse.

        布局id

        :return: The layout_id of this CreateDataclassTypeResponse.
        :rtype: str
        """
        return self._layout_id

    @layout_id.setter
    def layout_id(self, layout_id):
        r"""Sets the layout_id of this CreateDataclassTypeResponse.

        布局id

        :param layout_id: The layout_id of this CreateDataclassTypeResponse.
        :type layout_id: str
        """
        self._layout_id = layout_id

    @property
    def layout_name(self):
        r"""Gets the layout_name of this CreateDataclassTypeResponse.

        布局名称

        :return: The layout_name of this CreateDataclassTypeResponse.
        :rtype: str
        """
        return self._layout_name

    @layout_name.setter
    def layout_name(self, layout_name):
        r"""Sets the layout_name of this CreateDataclassTypeResponse.

        布局名称

        :param layout_name: The layout_name of this CreateDataclassTypeResponse.
        :type layout_name: str
        """
        self._layout_name = layout_name

    @property
    def category(self):
        r"""Gets the category of this CreateDataclassTypeResponse.

        数据类类型分类

        :return: The category of this CreateDataclassTypeResponse.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this CreateDataclassTypeResponse.

        数据类类型分类

        :param category: The category of this CreateDataclassTypeResponse.
        :type category: str
        """
        self._category = category

    @property
    def category_code(self):
        r"""Gets the category_code of this CreateDataclassTypeResponse.

        数据类类型分类编码

        :return: The category_code of this CreateDataclassTypeResponse.
        :rtype: str
        """
        return self._category_code

    @category_code.setter
    def category_code(self, category_code):
        r"""Sets the category_code of this CreateDataclassTypeResponse.

        数据类类型分类编码

        :param category_code: The category_code of this CreateDataclassTypeResponse.
        :type category_code: str
        """
        self._category_code = category_code

    @property
    def sub_category(self):
        r"""Gets the sub_category of this CreateDataclassTypeResponse.

        数据类类型名称

        :return: The sub_category of this CreateDataclassTypeResponse.
        :rtype: str
        """
        return self._sub_category

    @sub_category.setter
    def sub_category(self, sub_category):
        r"""Sets the sub_category of this CreateDataclassTypeResponse.

        数据类类型名称

        :param sub_category: The sub_category of this CreateDataclassTypeResponse.
        :type sub_category: str
        """
        self._sub_category = sub_category

    @property
    def sub_category_code(self):
        r"""Gets the sub_category_code of this CreateDataclassTypeResponse.

        数据类类型业务编码

        :return: The sub_category_code of this CreateDataclassTypeResponse.
        :rtype: str
        """
        return self._sub_category_code

    @sub_category_code.setter
    def sub_category_code(self, sub_category_code):
        r"""Sets the sub_category_code of this CreateDataclassTypeResponse.

        数据类类型业务编码

        :param sub_category_code: The sub_category_code of this CreateDataclassTypeResponse.
        :type sub_category_code: str
        """
        self._sub_category_code = sub_category_code

    @property
    def description(self):
        r"""Gets the description of this CreateDataclassTypeResponse.

        数据类类型描述

        :return: The description of this CreateDataclassTypeResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateDataclassTypeResponse.

        数据类类型描述

        :param description: The description of this CreateDataclassTypeResponse.
        :type description: str
        """
        self._description = description

    @property
    def enabled(self):
        r"""Gets the enabled of this CreateDataclassTypeResponse.

        状态

        :return: The enabled of this CreateDataclassTypeResponse.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this CreateDataclassTypeResponse.

        状态

        :param enabled: The enabled of this CreateDataclassTypeResponse.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def level(self):
        r"""Gets the level of this CreateDataclassTypeResponse.

        事件等级

        :return: The level of this CreateDataclassTypeResponse.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this CreateDataclassTypeResponse.

        事件等级

        :param level: The level of this CreateDataclassTypeResponse.
        :type level: int
        """
        self._level = level

    @property
    def is_built_in(self):
        r"""Gets the is_built_in of this CreateDataclassTypeResponse.

        是否内置，true内置，false非内置

        :return: The is_built_in of this CreateDataclassTypeResponse.
        :rtype: bool
        """
        return self._is_built_in

    @is_built_in.setter
    def is_built_in(self, is_built_in):
        r"""Sets the is_built_in of this CreateDataclassTypeResponse.

        是否内置，true内置，false非内置

        :param is_built_in: The is_built_in of this CreateDataclassTypeResponse.
        :type is_built_in: bool
        """
        self._is_built_in = is_built_in

    @property
    def sla(self):
        r"""Gets the sla of this CreateDataclassTypeResponse.

        响应时长

        :return: The sla of this CreateDataclassTypeResponse.
        :rtype: int
        """
        return self._sla

    @sla.setter
    def sla(self, sla):
        r"""Sets the sla of this CreateDataclassTypeResponse.

        响应时长

        :param sla: The sla of this CreateDataclassTypeResponse.
        :type sla: int
        """
        self._sla = sla

    @property
    def creator_id(self):
        r"""Gets the creator_id of this CreateDataclassTypeResponse.

        创建人id

        :return: The creator_id of this CreateDataclassTypeResponse.
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        r"""Sets the creator_id of this CreateDataclassTypeResponse.

        创建人id

        :param creator_id: The creator_id of this CreateDataclassTypeResponse.
        :type creator_id: str
        """
        self._creator_id = creator_id

    @property
    def creator_name(self):
        r"""Gets the creator_name of this CreateDataclassTypeResponse.

        创建人名称

        :return: The creator_name of this CreateDataclassTypeResponse.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        r"""Sets the creator_name of this CreateDataclassTypeResponse.

        创建人名称

        :param creator_name: The creator_name of this CreateDataclassTypeResponse.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def modifier_id(self):
        r"""Gets the modifier_id of this CreateDataclassTypeResponse.

        修改人id

        :return: The modifier_id of this CreateDataclassTypeResponse.
        :rtype: str
        """
        return self._modifier_id

    @modifier_id.setter
    def modifier_id(self, modifier_id):
        r"""Sets the modifier_id of this CreateDataclassTypeResponse.

        修改人id

        :param modifier_id: The modifier_id of this CreateDataclassTypeResponse.
        :type modifier_id: str
        """
        self._modifier_id = modifier_id

    @property
    def modifier_name(self):
        r"""Gets the modifier_name of this CreateDataclassTypeResponse.

        修改人名称

        :return: The modifier_name of this CreateDataclassTypeResponse.
        :rtype: str
        """
        return self._modifier_name

    @modifier_name.setter
    def modifier_name(self, modifier_name):
        r"""Sets the modifier_name of this CreateDataclassTypeResponse.

        修改人名称

        :param modifier_name: The modifier_name of this CreateDataclassTypeResponse.
        :type modifier_name: str
        """
        self._modifier_name = modifier_name

    @property
    def create_time(self):
        r"""Gets the create_time of this CreateDataclassTypeResponse.

        创建时间

        :return: The create_time of this CreateDataclassTypeResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this CreateDataclassTypeResponse.

        创建时间

        :param create_time: The create_time of this CreateDataclassTypeResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this CreateDataclassTypeResponse.

        修改时间

        :return: The update_time of this CreateDataclassTypeResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this CreateDataclassTypeResponse.

        修改时间

        :param update_time: The update_time of this CreateDataclassTypeResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def dataclass_business_code(self):
        r"""Gets the dataclass_business_code of this CreateDataclassTypeResponse.

        所属数据类业务编码

        :return: The dataclass_business_code of this CreateDataclassTypeResponse.
        :rtype: str
        """
        return self._dataclass_business_code

    @dataclass_business_code.setter
    def dataclass_business_code(self, dataclass_business_code):
        r"""Sets the dataclass_business_code of this CreateDataclassTypeResponse.

        所属数据类业务编码

        :param dataclass_business_code: The dataclass_business_code of this CreateDataclassTypeResponse.
        :type dataclass_business_code: str
        """
        self._dataclass_business_code = dataclass_business_code

    def to_dict(self):
        import warnings
        warnings.warn("CreateDataclassTypeResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, CreateDataclassTypeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
