# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateChartResponse(SdkResponse):

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
        'values': 'str',
        'translate': 'str',
        'instruction': 'str',
        'version': 'str',
        'description': 'str',
        'source': 'str',
        'icon_url': 'str',
        'public': 'bool',
        'chart_url': 'str',
        'create_at': 'str',
        'update_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'values': 'values',
        'translate': 'translate',
        'instruction': 'instruction',
        'version': 'version',
        'description': 'description',
        'source': 'source',
        'icon_url': 'icon_url',
        'public': 'public',
        'chart_url': 'chart_url',
        'create_at': 'create_at',
        'update_at': 'update_at'
    }

    def __init__(self, id=None, name=None, values=None, translate=None, instruction=None, version=None, description=None, source=None, icon_url=None, public=None, chart_url=None, create_at=None, update_at=None):
        r"""UpdateChartResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 模板ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type id: str
        :param name: **参数解释：** 模板名称 **约束限制：** 最长64个字符 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type name: str
        :param values: **参数解释：** 模板值 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type values: str
        :param translate: **参数解释：** 模板翻译资源 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type translate: str
        :param instruction: **参数解释：** 模板介绍 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type instruction: str
        :param version: **参数解释：** 模板版本 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type version: str
        :param description: **参数解释：** 模板描述 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type description: str
        :param source: **参数解释：** 模板的来源 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type source: str
        :param icon_url: **参数解释：** 模板的图标链接 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type icon_url: str
        :param public: **参数解释：** 是否公开模板 **约束限制：** 不涉及 **取值范围：** - true：公开模板 - false：不公开模板  **默认取值：** false
        :type public: bool
        :param chart_url: **参数解释：** 模板的链接 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type chart_url: str
        :param create_at: **参数解释：** 创建时间 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type create_at: str
        :param update_at: **参数解释：** 更新时间 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type update_at: str
        """
        
        super().__init__()

        self._id = None
        self._name = None
        self._values = None
        self._translate = None
        self._instruction = None
        self._version = None
        self._description = None
        self._source = None
        self._icon_url = None
        self._public = None
        self._chart_url = None
        self._create_at = None
        self._update_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if values is not None:
            self.values = values
        if translate is not None:
            self.translate = translate
        if instruction is not None:
            self.instruction = instruction
        if version is not None:
            self.version = version
        if description is not None:
            self.description = description
        if source is not None:
            self.source = source
        if icon_url is not None:
            self.icon_url = icon_url
        if public is not None:
            self.public = public
        if chart_url is not None:
            self.chart_url = chart_url
        if create_at is not None:
            self.create_at = create_at
        if update_at is not None:
            self.update_at = update_at

    @property
    def id(self):
        r"""Gets the id of this UpdateChartResponse.

        **参数解释：** 模板ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The id of this UpdateChartResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UpdateChartResponse.

        **参数解释：** 模板ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param id: The id of this UpdateChartResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this UpdateChartResponse.

        **参数解释：** 模板名称 **约束限制：** 最长64个字符 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The name of this UpdateChartResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateChartResponse.

        **参数解释：** 模板名称 **约束限制：** 最长64个字符 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param name: The name of this UpdateChartResponse.
        :type name: str
        """
        self._name = name

    @property
    def values(self):
        r"""Gets the values of this UpdateChartResponse.

        **参数解释：** 模板值 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The values of this UpdateChartResponse.
        :rtype: str
        """
        return self._values

    @values.setter
    def values(self, values):
        r"""Sets the values of this UpdateChartResponse.

        **参数解释：** 模板值 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param values: The values of this UpdateChartResponse.
        :type values: str
        """
        self._values = values

    @property
    def translate(self):
        r"""Gets the translate of this UpdateChartResponse.

        **参数解释：** 模板翻译资源 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The translate of this UpdateChartResponse.
        :rtype: str
        """
        return self._translate

    @translate.setter
    def translate(self, translate):
        r"""Sets the translate of this UpdateChartResponse.

        **参数解释：** 模板翻译资源 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param translate: The translate of this UpdateChartResponse.
        :type translate: str
        """
        self._translate = translate

    @property
    def instruction(self):
        r"""Gets the instruction of this UpdateChartResponse.

        **参数解释：** 模板介绍 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The instruction of this UpdateChartResponse.
        :rtype: str
        """
        return self._instruction

    @instruction.setter
    def instruction(self, instruction):
        r"""Sets the instruction of this UpdateChartResponse.

        **参数解释：** 模板介绍 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param instruction: The instruction of this UpdateChartResponse.
        :type instruction: str
        """
        self._instruction = instruction

    @property
    def version(self):
        r"""Gets the version of this UpdateChartResponse.

        **参数解释：** 模板版本 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The version of this UpdateChartResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this UpdateChartResponse.

        **参数解释：** 模板版本 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param version: The version of this UpdateChartResponse.
        :type version: str
        """
        self._version = version

    @property
    def description(self):
        r"""Gets the description of this UpdateChartResponse.

        **参数解释：** 模板描述 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The description of this UpdateChartResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateChartResponse.

        **参数解释：** 模板描述 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param description: The description of this UpdateChartResponse.
        :type description: str
        """
        self._description = description

    @property
    def source(self):
        r"""Gets the source of this UpdateChartResponse.

        **参数解释：** 模板的来源 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The source of this UpdateChartResponse.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this UpdateChartResponse.

        **参数解释：** 模板的来源 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param source: The source of this UpdateChartResponse.
        :type source: str
        """
        self._source = source

    @property
    def icon_url(self):
        r"""Gets the icon_url of this UpdateChartResponse.

        **参数解释：** 模板的图标链接 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The icon_url of this UpdateChartResponse.
        :rtype: str
        """
        return self._icon_url

    @icon_url.setter
    def icon_url(self, icon_url):
        r"""Sets the icon_url of this UpdateChartResponse.

        **参数解释：** 模板的图标链接 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param icon_url: The icon_url of this UpdateChartResponse.
        :type icon_url: str
        """
        self._icon_url = icon_url

    @property
    def public(self):
        r"""Gets the public of this UpdateChartResponse.

        **参数解释：** 是否公开模板 **约束限制：** 不涉及 **取值范围：** - true：公开模板 - false：不公开模板  **默认取值：** false

        :return: The public of this UpdateChartResponse.
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        r"""Sets the public of this UpdateChartResponse.

        **参数解释：** 是否公开模板 **约束限制：** 不涉及 **取值范围：** - true：公开模板 - false：不公开模板  **默认取值：** false

        :param public: The public of this UpdateChartResponse.
        :type public: bool
        """
        self._public = public

    @property
    def chart_url(self):
        r"""Gets the chart_url of this UpdateChartResponse.

        **参数解释：** 模板的链接 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The chart_url of this UpdateChartResponse.
        :rtype: str
        """
        return self._chart_url

    @chart_url.setter
    def chart_url(self, chart_url):
        r"""Sets the chart_url of this UpdateChartResponse.

        **参数解释：** 模板的链接 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param chart_url: The chart_url of this UpdateChartResponse.
        :type chart_url: str
        """
        self._chart_url = chart_url

    @property
    def create_at(self):
        r"""Gets the create_at of this UpdateChartResponse.

        **参数解释：** 创建时间 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The create_at of this UpdateChartResponse.
        :rtype: str
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this UpdateChartResponse.

        **参数解释：** 创建时间 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param create_at: The create_at of this UpdateChartResponse.
        :type create_at: str
        """
        self._create_at = create_at

    @property
    def update_at(self):
        r"""Gets the update_at of this UpdateChartResponse.

        **参数解释：** 更新时间 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The update_at of this UpdateChartResponse.
        :rtype: str
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        r"""Sets the update_at of this UpdateChartResponse.

        **参数解释：** 更新时间 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param update_at: The update_at of this UpdateChartResponse.
        :type update_at: str
        """
        self._update_at = update_at

    def to_dict(self):
        import warnings
        warnings.warn("UpdateChartResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, UpdateChartResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
