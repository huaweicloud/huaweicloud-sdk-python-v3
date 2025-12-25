# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LayoutUpdateRequestPojo:

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
        'cloud_pack_id': 'str',
        'cloud_pack_name': 'str',
        'cloud_pack_version': 'str',
        'is_built_in': 'bool',
        'is_template': 'bool',
        'layout_json': 'object',
        'fields_sum': 'int',
        'wizards_sum': 'int',
        'sections_sum': 'int',
        'tabs_sum': 'int',
        'boa_version': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'cloud_pack_id': 'cloud_pack_id',
        'cloud_pack_name': 'cloud_pack_name',
        'cloud_pack_version': 'cloud_pack_version',
        'is_built_in': 'is_built_in',
        'is_template': 'is_template',
        'layout_json': 'layout_json',
        'fields_sum': 'fields_sum',
        'wizards_sum': 'wizards_sum',
        'sections_sum': 'sections_sum',
        'tabs_sum': 'tabs_sum',
        'boa_version': 'boa_version'
    }

    def __init__(self, name=None, description=None, cloud_pack_id=None, cloud_pack_name=None, cloud_pack_version=None, is_built_in=None, is_template=None, layout_json=None, fields_sum=None, wizards_sum=None, sections_sum=None, tabs_sum=None, boa_version=None):
        r"""LayoutUpdateRequestPojo

        The model defined in huaweicloud sdk

        :param name: 布局名称
        :type name: str
        :param description: 描述信息
        :type description: str
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
        :param layout_json: 布局信息
        :type layout_json: object
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
        self._cloud_pack_id = None
        self._cloud_pack_name = None
        self._cloud_pack_version = None
        self._is_built_in = None
        self._is_template = None
        self._layout_json = None
        self._fields_sum = None
        self._wizards_sum = None
        self._sections_sum = None
        self._tabs_sum = None
        self._boa_version = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
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
        if layout_json is not None:
            self.layout_json = layout_json
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
        r"""Gets the name of this LayoutUpdateRequestPojo.

        布局名称

        :return: The name of this LayoutUpdateRequestPojo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this LayoutUpdateRequestPojo.

        布局名称

        :param name: The name of this LayoutUpdateRequestPojo.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this LayoutUpdateRequestPojo.

        描述信息

        :return: The description of this LayoutUpdateRequestPojo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this LayoutUpdateRequestPojo.

        描述信息

        :param description: The description of this LayoutUpdateRequestPojo.
        :type description: str
        """
        self._description = description

    @property
    def cloud_pack_id(self):
        r"""Gets the cloud_pack_id of this LayoutUpdateRequestPojo.

        订阅包id

        :return: The cloud_pack_id of this LayoutUpdateRequestPojo.
        :rtype: str
        """
        return self._cloud_pack_id

    @cloud_pack_id.setter
    def cloud_pack_id(self, cloud_pack_id):
        r"""Sets the cloud_pack_id of this LayoutUpdateRequestPojo.

        订阅包id

        :param cloud_pack_id: The cloud_pack_id of this LayoutUpdateRequestPojo.
        :type cloud_pack_id: str
        """
        self._cloud_pack_id = cloud_pack_id

    @property
    def cloud_pack_name(self):
        r"""Gets the cloud_pack_name of this LayoutUpdateRequestPojo.

        订阅包名称

        :return: The cloud_pack_name of this LayoutUpdateRequestPojo.
        :rtype: str
        """
        return self._cloud_pack_name

    @cloud_pack_name.setter
    def cloud_pack_name(self, cloud_pack_name):
        r"""Sets the cloud_pack_name of this LayoutUpdateRequestPojo.

        订阅包名称

        :param cloud_pack_name: The cloud_pack_name of this LayoutUpdateRequestPojo.
        :type cloud_pack_name: str
        """
        self._cloud_pack_name = cloud_pack_name

    @property
    def cloud_pack_version(self):
        r"""Gets the cloud_pack_version of this LayoutUpdateRequestPojo.

        订阅包版本

        :return: The cloud_pack_version of this LayoutUpdateRequestPojo.
        :rtype: str
        """
        return self._cloud_pack_version

    @cloud_pack_version.setter
    def cloud_pack_version(self, cloud_pack_version):
        r"""Sets the cloud_pack_version of this LayoutUpdateRequestPojo.

        订阅包版本

        :param cloud_pack_version: The cloud_pack_version of this LayoutUpdateRequestPojo.
        :type cloud_pack_version: str
        """
        self._cloud_pack_version = cloud_pack_version

    @property
    def is_built_in(self):
        r"""Gets the is_built_in of this LayoutUpdateRequestPojo.

        是否内置，true内置，false非内置

        :return: The is_built_in of this LayoutUpdateRequestPojo.
        :rtype: bool
        """
        return self._is_built_in

    @is_built_in.setter
    def is_built_in(self, is_built_in):
        r"""Sets the is_built_in of this LayoutUpdateRequestPojo.

        是否内置，true内置，false非内置

        :param is_built_in: The is_built_in of this LayoutUpdateRequestPojo.
        :type is_built_in: bool
        """
        self._is_built_in = is_built_in

    @property
    def is_template(self):
        r"""Gets the is_template of this LayoutUpdateRequestPojo.

        是否为模板

        :return: The is_template of this LayoutUpdateRequestPojo.
        :rtype: bool
        """
        return self._is_template

    @is_template.setter
    def is_template(self, is_template):
        r"""Sets the is_template of this LayoutUpdateRequestPojo.

        是否为模板

        :param is_template: The is_template of this LayoutUpdateRequestPojo.
        :type is_template: bool
        """
        self._is_template = is_template

    @property
    def layout_json(self):
        r"""Gets the layout_json of this LayoutUpdateRequestPojo.

        布局信息

        :return: The layout_json of this LayoutUpdateRequestPojo.
        :rtype: object
        """
        return self._layout_json

    @layout_json.setter
    def layout_json(self, layout_json):
        r"""Sets the layout_json of this LayoutUpdateRequestPojo.

        布局信息

        :param layout_json: The layout_json of this LayoutUpdateRequestPojo.
        :type layout_json: object
        """
        self._layout_json = layout_json

    @property
    def fields_sum(self):
        r"""Gets the fields_sum of this LayoutUpdateRequestPojo.

        字段总数；used_by为SECURITY_REPORT/DASHBOARD时不返回该字段

        :return: The fields_sum of this LayoutUpdateRequestPojo.
        :rtype: int
        """
        return self._fields_sum

    @fields_sum.setter
    def fields_sum(self, fields_sum):
        r"""Sets the fields_sum of this LayoutUpdateRequestPojo.

        字段总数；used_by为SECURITY_REPORT/DASHBOARD时不返回该字段

        :param fields_sum: The fields_sum of this LayoutUpdateRequestPojo.
        :type fields_sum: int
        """
        self._fields_sum = fields_sum

    @property
    def wizards_sum(self):
        r"""Gets the wizards_sum of this LayoutUpdateRequestPojo.

        页面总数；used_by为SECURITY_REPORT/DASHBOARD时不返回该字段

        :return: The wizards_sum of this LayoutUpdateRequestPojo.
        :rtype: int
        """
        return self._wizards_sum

    @wizards_sum.setter
    def wizards_sum(self, wizards_sum):
        r"""Sets the wizards_sum of this LayoutUpdateRequestPojo.

        页面总数；used_by为SECURITY_REPORT/DASHBOARD时不返回该字段

        :param wizards_sum: The wizards_sum of this LayoutUpdateRequestPojo.
        :type wizards_sum: int
        """
        self._wizards_sum = wizards_sum

    @property
    def sections_sum(self):
        r"""Gets the sections_sum of this LayoutUpdateRequestPojo.

        系统指标总数

        :return: The sections_sum of this LayoutUpdateRequestPojo.
        :rtype: int
        """
        return self._sections_sum

    @sections_sum.setter
    def sections_sum(self, sections_sum):
        r"""Sets the sections_sum of this LayoutUpdateRequestPojo.

        系统指标总数

        :param sections_sum: The sections_sum of this LayoutUpdateRequestPojo.
        :type sections_sum: int
        """
        self._sections_sum = sections_sum

    @property
    def tabs_sum(self):
        r"""Gets the tabs_sum of this LayoutUpdateRequestPojo.

        自定义指标总数

        :return: The tabs_sum of this LayoutUpdateRequestPojo.
        :rtype: int
        """
        return self._tabs_sum

    @tabs_sum.setter
    def tabs_sum(self, tabs_sum):
        r"""Sets the tabs_sum of this LayoutUpdateRequestPojo.

        自定义指标总数

        :param tabs_sum: The tabs_sum of this LayoutUpdateRequestPojo.
        :type tabs_sum: int
        """
        self._tabs_sum = tabs_sum

    @property
    def boa_version(self):
        r"""Gets the boa_version of this LayoutUpdateRequestPojo.

        BOA底座版本

        :return: The boa_version of this LayoutUpdateRequestPojo.
        :rtype: str
        """
        return self._boa_version

    @boa_version.setter
    def boa_version(self, boa_version):
        r"""Sets the boa_version of this LayoutUpdateRequestPojo.

        BOA底座版本

        :param boa_version: The boa_version of this LayoutUpdateRequestPojo.
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
        if not isinstance(other, LayoutUpdateRequestPojo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
