# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LayoutCreateRequestPojo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'create_time': 'str',
        'creator_name': 'str',
        'cloud_pack_id': 'str',
        'cloud_pack_name': 'str',
        'cloud_pack_version': 'str',
        'is_built_in': 'bool',
        'layout_json': 'object',
        'region_id': 'str',
        'domain_id': 'str',
        'thumbnail': 'str',
        'used_by': 'str',
        'layout_type': 'str',
        'binding_id': 'str',
        'binding_code': 'str',
        'fields_sum': 'int',
        'wizards_sum': 'int',
        'sections_sum': 'int',
        'tabs_sum': 'int',
        'boa_version': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'create_time': 'create_time',
        'creator_name': 'creator_name',
        'cloud_pack_id': 'cloud_pack_id',
        'cloud_pack_name': 'cloud_pack_name',
        'cloud_pack_version': 'cloud_pack_version',
        'is_built_in': 'is_built_in',
        'layout_json': 'layout_json',
        'region_id': 'region_id',
        'domain_id': 'domain_id',
        'thumbnail': 'thumbnail',
        'used_by': 'used_by',
        'layout_type': 'layout_type',
        'binding_id': 'binding_id',
        'binding_code': 'binding_code',
        'fields_sum': 'fields_sum',
        'wizards_sum': 'wizards_sum',
        'sections_sum': 'sections_sum',
        'tabs_sum': 'tabs_sum',
        'boa_version': 'boa_version'
    }

    def __init__(self, name=None, description=None, create_time=None, creator_name=None, cloud_pack_id=None, cloud_pack_name=None, cloud_pack_version=None, is_built_in=None, layout_json=None, region_id=None, domain_id=None, thumbnail=None, used_by=None, layout_type=None, binding_id=None, binding_code=None, fields_sum=None, wizards_sum=None, sections_sum=None, tabs_sum=None, boa_version=None):
        r"""LayoutCreateRequestPojo

        The model defined in huaweicloud sdk

        :param name: 布局名称
        :type name: str
        :param description: 描述信息
        :type description: str
        :param create_time: 创建时间
        :type create_time: str
        :param creator_name: 创建者
        :type creator_name: str
        :param cloud_pack_id: 订阅包id
        :type cloud_pack_id: str
        :param cloud_pack_name: 订阅包名称
        :type cloud_pack_name: str
        :param cloud_pack_version: 订阅包版本
        :type cloud_pack_version: str
        :param is_built_in: 是否内置，true内置，false非内置
        :type is_built_in: bool
        :param layout_json: 布局信息
        :type layout_json: object
        :param region_id: 区域ID
        :type region_id: str
        :param domain_id: 用户ID
        :type domain_id: str
        :param thumbnail: 模板缩略图，当布局为模板时不为空
        :type thumbnail: str
        :param used_by: 被什么业务使用，DATACLASS/AOP_WORKFLOW/SECURITY_REPORT/DASHBOARD，及对应的字段
        :type used_by: str
        :param layout_type: 布局类型；used_by为SECURITY_REPORT/DASHBOARD时不返回该字段
        :type layout_type: str
        :param binding_id: 数据类ID或流程ID；used_by为SECURITY_REPORT/DASHBOARD时不返回该字段
        :type binding_id: str
        :param binding_code: 数据类名称business_code；used_by为SECURITY_REPORT/DASHBOARD时不返回该字段
        :type binding_code: str
        :param fields_sum: 字段总数；used_by为SECURITY_REPORT/DASHBOARD时不返回该字段
        :type fields_sum: int
        :param wizards_sum: 页面总数；used_by为SECURITY_REPORT/DASHBOARD时不返回该字段
        :type wizards_sum: int
        :param sections_sum: 系统指标总数
        :type sections_sum: int
        :param tabs_sum: 自定义指标总数
        :type tabs_sum: int
        :param boa_version: BOA底座版本
        :type boa_version: str
        """
        
        

        self._name = None
        self._description = None
        self._create_time = None
        self._creator_name = None
        self._cloud_pack_id = None
        self._cloud_pack_name = None
        self._cloud_pack_version = None
        self._is_built_in = None
        self._layout_json = None
        self._region_id = None
        self._domain_id = None
        self._thumbnail = None
        self._used_by = None
        self._layout_type = None
        self._binding_id = None
        self._binding_code = None
        self._fields_sum = None
        self._wizards_sum = None
        self._sections_sum = None
        self._tabs_sum = None
        self._boa_version = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if create_time is not None:
            self.create_time = create_time
        if creator_name is not None:
            self.creator_name = creator_name
        if cloud_pack_id is not None:
            self.cloud_pack_id = cloud_pack_id
        if cloud_pack_name is not None:
            self.cloud_pack_name = cloud_pack_name
        if cloud_pack_version is not None:
            self.cloud_pack_version = cloud_pack_version
        if is_built_in is not None:
            self.is_built_in = is_built_in
        if layout_json is not None:
            self.layout_json = layout_json
        if region_id is not None:
            self.region_id = region_id
        if domain_id is not None:
            self.domain_id = domain_id
        if thumbnail is not None:
            self.thumbnail = thumbnail
        self.used_by = used_by
        if layout_type is not None:
            self.layout_type = layout_type
        if binding_id is not None:
            self.binding_id = binding_id
        if binding_code is not None:
            self.binding_code = binding_code
        if fields_sum is not None:
            self.fields_sum = fields_sum
        if wizards_sum is not None:
            self.wizards_sum = wizards_sum
        if sections_sum is not None:
            self.sections_sum = sections_sum
        if tabs_sum is not None:
            self.tabs_sum = tabs_sum
        if boa_version is not None:
            self.boa_version = boa_version

    @property
    def name(self):
        r"""Gets the name of this LayoutCreateRequestPojo.

        布局名称

        :return: The name of this LayoutCreateRequestPojo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this LayoutCreateRequestPojo.

        布局名称

        :param name: The name of this LayoutCreateRequestPojo.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this LayoutCreateRequestPojo.

        描述信息

        :return: The description of this LayoutCreateRequestPojo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this LayoutCreateRequestPojo.

        描述信息

        :param description: The description of this LayoutCreateRequestPojo.
        :type description: str
        """
        self._description = description

    @property
    def create_time(self):
        r"""Gets the create_time of this LayoutCreateRequestPojo.

        创建时间

        :return: The create_time of this LayoutCreateRequestPojo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this LayoutCreateRequestPojo.

        创建时间

        :param create_time: The create_time of this LayoutCreateRequestPojo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def creator_name(self):
        r"""Gets the creator_name of this LayoutCreateRequestPojo.

        创建者

        :return: The creator_name of this LayoutCreateRequestPojo.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        r"""Sets the creator_name of this LayoutCreateRequestPojo.

        创建者

        :param creator_name: The creator_name of this LayoutCreateRequestPojo.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def cloud_pack_id(self):
        r"""Gets the cloud_pack_id of this LayoutCreateRequestPojo.

        订阅包id

        :return: The cloud_pack_id of this LayoutCreateRequestPojo.
        :rtype: str
        """
        return self._cloud_pack_id

    @cloud_pack_id.setter
    def cloud_pack_id(self, cloud_pack_id):
        r"""Sets the cloud_pack_id of this LayoutCreateRequestPojo.

        订阅包id

        :param cloud_pack_id: The cloud_pack_id of this LayoutCreateRequestPojo.
        :type cloud_pack_id: str
        """
        self._cloud_pack_id = cloud_pack_id

    @property
    def cloud_pack_name(self):
        r"""Gets the cloud_pack_name of this LayoutCreateRequestPojo.

        订阅包名称

        :return: The cloud_pack_name of this LayoutCreateRequestPojo.
        :rtype: str
        """
        return self._cloud_pack_name

    @cloud_pack_name.setter
    def cloud_pack_name(self, cloud_pack_name):
        r"""Sets the cloud_pack_name of this LayoutCreateRequestPojo.

        订阅包名称

        :param cloud_pack_name: The cloud_pack_name of this LayoutCreateRequestPojo.
        :type cloud_pack_name: str
        """
        self._cloud_pack_name = cloud_pack_name

    @property
    def cloud_pack_version(self):
        r"""Gets the cloud_pack_version of this LayoutCreateRequestPojo.

        订阅包版本

        :return: The cloud_pack_version of this LayoutCreateRequestPojo.
        :rtype: str
        """
        return self._cloud_pack_version

    @cloud_pack_version.setter
    def cloud_pack_version(self, cloud_pack_version):
        r"""Sets the cloud_pack_version of this LayoutCreateRequestPojo.

        订阅包版本

        :param cloud_pack_version: The cloud_pack_version of this LayoutCreateRequestPojo.
        :type cloud_pack_version: str
        """
        self._cloud_pack_version = cloud_pack_version

    @property
    def is_built_in(self):
        r"""Gets the is_built_in of this LayoutCreateRequestPojo.

        是否内置，true内置，false非内置

        :return: The is_built_in of this LayoutCreateRequestPojo.
        :rtype: bool
        """
        return self._is_built_in

    @is_built_in.setter
    def is_built_in(self, is_built_in):
        r"""Sets the is_built_in of this LayoutCreateRequestPojo.

        是否内置，true内置，false非内置

        :param is_built_in: The is_built_in of this LayoutCreateRequestPojo.
        :type is_built_in: bool
        """
        self._is_built_in = is_built_in

    @property
    def layout_json(self):
        r"""Gets the layout_json of this LayoutCreateRequestPojo.

        布局信息

        :return: The layout_json of this LayoutCreateRequestPojo.
        :rtype: object
        """
        return self._layout_json

    @layout_json.setter
    def layout_json(self, layout_json):
        r"""Sets the layout_json of this LayoutCreateRequestPojo.

        布局信息

        :param layout_json: The layout_json of this LayoutCreateRequestPojo.
        :type layout_json: object
        """
        self._layout_json = layout_json

    @property
    def region_id(self):
        r"""Gets the region_id of this LayoutCreateRequestPojo.

        区域ID

        :return: The region_id of this LayoutCreateRequestPojo.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this LayoutCreateRequestPojo.

        区域ID

        :param region_id: The region_id of this LayoutCreateRequestPojo.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this LayoutCreateRequestPojo.

        用户ID

        :return: The domain_id of this LayoutCreateRequestPojo.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this LayoutCreateRequestPojo.

        用户ID

        :param domain_id: The domain_id of this LayoutCreateRequestPojo.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def thumbnail(self):
        r"""Gets the thumbnail of this LayoutCreateRequestPojo.

        模板缩略图，当布局为模板时不为空

        :return: The thumbnail of this LayoutCreateRequestPojo.
        :rtype: str
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        r"""Sets the thumbnail of this LayoutCreateRequestPojo.

        模板缩略图，当布局为模板时不为空

        :param thumbnail: The thumbnail of this LayoutCreateRequestPojo.
        :type thumbnail: str
        """
        self._thumbnail = thumbnail

    @property
    def used_by(self):
        r"""Gets the used_by of this LayoutCreateRequestPojo.

        被什么业务使用，DATACLASS/AOP_WORKFLOW/SECURITY_REPORT/DASHBOARD，及对应的字段

        :return: The used_by of this LayoutCreateRequestPojo.
        :rtype: str
        """
        return self._used_by

    @used_by.setter
    def used_by(self, used_by):
        r"""Sets the used_by of this LayoutCreateRequestPojo.

        被什么业务使用，DATACLASS/AOP_WORKFLOW/SECURITY_REPORT/DASHBOARD，及对应的字段

        :param used_by: The used_by of this LayoutCreateRequestPojo.
        :type used_by: str
        """
        self._used_by = used_by

    @property
    def layout_type(self):
        r"""Gets the layout_type of this LayoutCreateRequestPojo.

        布局类型；used_by为SECURITY_REPORT/DASHBOARD时不返回该字段

        :return: The layout_type of this LayoutCreateRequestPojo.
        :rtype: str
        """
        return self._layout_type

    @layout_type.setter
    def layout_type(self, layout_type):
        r"""Sets the layout_type of this LayoutCreateRequestPojo.

        布局类型；used_by为SECURITY_REPORT/DASHBOARD时不返回该字段

        :param layout_type: The layout_type of this LayoutCreateRequestPojo.
        :type layout_type: str
        """
        self._layout_type = layout_type

    @property
    def binding_id(self):
        r"""Gets the binding_id of this LayoutCreateRequestPojo.

        数据类ID或流程ID；used_by为SECURITY_REPORT/DASHBOARD时不返回该字段

        :return: The binding_id of this LayoutCreateRequestPojo.
        :rtype: str
        """
        return self._binding_id

    @binding_id.setter
    def binding_id(self, binding_id):
        r"""Sets the binding_id of this LayoutCreateRequestPojo.

        数据类ID或流程ID；used_by为SECURITY_REPORT/DASHBOARD时不返回该字段

        :param binding_id: The binding_id of this LayoutCreateRequestPojo.
        :type binding_id: str
        """
        self._binding_id = binding_id

    @property
    def binding_code(self):
        r"""Gets the binding_code of this LayoutCreateRequestPojo.

        数据类名称business_code；used_by为SECURITY_REPORT/DASHBOARD时不返回该字段

        :return: The binding_code of this LayoutCreateRequestPojo.
        :rtype: str
        """
        return self._binding_code

    @binding_code.setter
    def binding_code(self, binding_code):
        r"""Sets the binding_code of this LayoutCreateRequestPojo.

        数据类名称business_code；used_by为SECURITY_REPORT/DASHBOARD时不返回该字段

        :param binding_code: The binding_code of this LayoutCreateRequestPojo.
        :type binding_code: str
        """
        self._binding_code = binding_code

    @property
    def fields_sum(self):
        r"""Gets the fields_sum of this LayoutCreateRequestPojo.

        字段总数；used_by为SECURITY_REPORT/DASHBOARD时不返回该字段

        :return: The fields_sum of this LayoutCreateRequestPojo.
        :rtype: int
        """
        return self._fields_sum

    @fields_sum.setter
    def fields_sum(self, fields_sum):
        r"""Sets the fields_sum of this LayoutCreateRequestPojo.

        字段总数；used_by为SECURITY_REPORT/DASHBOARD时不返回该字段

        :param fields_sum: The fields_sum of this LayoutCreateRequestPojo.
        :type fields_sum: int
        """
        self._fields_sum = fields_sum

    @property
    def wizards_sum(self):
        r"""Gets the wizards_sum of this LayoutCreateRequestPojo.

        页面总数；used_by为SECURITY_REPORT/DASHBOARD时不返回该字段

        :return: The wizards_sum of this LayoutCreateRequestPojo.
        :rtype: int
        """
        return self._wizards_sum

    @wizards_sum.setter
    def wizards_sum(self, wizards_sum):
        r"""Sets the wizards_sum of this LayoutCreateRequestPojo.

        页面总数；used_by为SECURITY_REPORT/DASHBOARD时不返回该字段

        :param wizards_sum: The wizards_sum of this LayoutCreateRequestPojo.
        :type wizards_sum: int
        """
        self._wizards_sum = wizards_sum

    @property
    def sections_sum(self):
        r"""Gets the sections_sum of this LayoutCreateRequestPojo.

        系统指标总数

        :return: The sections_sum of this LayoutCreateRequestPojo.
        :rtype: int
        """
        return self._sections_sum

    @sections_sum.setter
    def sections_sum(self, sections_sum):
        r"""Sets the sections_sum of this LayoutCreateRequestPojo.

        系统指标总数

        :param sections_sum: The sections_sum of this LayoutCreateRequestPojo.
        :type sections_sum: int
        """
        self._sections_sum = sections_sum

    @property
    def tabs_sum(self):
        r"""Gets the tabs_sum of this LayoutCreateRequestPojo.

        自定义指标总数

        :return: The tabs_sum of this LayoutCreateRequestPojo.
        :rtype: int
        """
        return self._tabs_sum

    @tabs_sum.setter
    def tabs_sum(self, tabs_sum):
        r"""Sets the tabs_sum of this LayoutCreateRequestPojo.

        自定义指标总数

        :param tabs_sum: The tabs_sum of this LayoutCreateRequestPojo.
        :type tabs_sum: int
        """
        self._tabs_sum = tabs_sum

    @property
    def boa_version(self):
        r"""Gets the boa_version of this LayoutCreateRequestPojo.

        BOA底座版本

        :return: The boa_version of this LayoutCreateRequestPojo.
        :rtype: str
        """
        return self._boa_version

    @boa_version.setter
    def boa_version(self, boa_version):
        r"""Sets the boa_version of this LayoutCreateRequestPojo.

        BOA底座版本

        :param boa_version: The boa_version of this LayoutCreateRequestPojo.
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
        if not isinstance(other, LayoutCreateRequestPojo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
