# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChartResp:

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
        """ChartResp

        The model defined in huaweicloud sdk

        :param id: 模板ID
        :type id: str
        :param name: 模板名称
        :type name: str
        :param values: 模板值
        :type values: str
        :param translate: 模板翻译资源
        :type translate: str
        :param instruction: 模板介绍
        :type instruction: str
        :param version: 模板版本
        :type version: str
        :param description: 模板描述
        :type description: str
        :param source: 模板的来源
        :type source: str
        :param icon_url: 模板的图标链接
        :type icon_url: str
        :param public: 是否公开模板
        :type public: bool
        :param chart_url: 模板的链接
        :type chart_url: str
        :param create_at: 创建时间
        :type create_at: str
        :param update_at: 更新时间
        :type update_at: str
        """
        
        

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
        """Gets the id of this ChartResp.

        模板ID

        :return: The id of this ChartResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ChartResp.

        模板ID

        :param id: The id of this ChartResp.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ChartResp.

        模板名称

        :return: The name of this ChartResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ChartResp.

        模板名称

        :param name: The name of this ChartResp.
        :type name: str
        """
        self._name = name

    @property
    def values(self):
        """Gets the values of this ChartResp.

        模板值

        :return: The values of this ChartResp.
        :rtype: str
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this ChartResp.

        模板值

        :param values: The values of this ChartResp.
        :type values: str
        """
        self._values = values

    @property
    def translate(self):
        """Gets the translate of this ChartResp.

        模板翻译资源

        :return: The translate of this ChartResp.
        :rtype: str
        """
        return self._translate

    @translate.setter
    def translate(self, translate):
        """Sets the translate of this ChartResp.

        模板翻译资源

        :param translate: The translate of this ChartResp.
        :type translate: str
        """
        self._translate = translate

    @property
    def instruction(self):
        """Gets the instruction of this ChartResp.

        模板介绍

        :return: The instruction of this ChartResp.
        :rtype: str
        """
        return self._instruction

    @instruction.setter
    def instruction(self, instruction):
        """Sets the instruction of this ChartResp.

        模板介绍

        :param instruction: The instruction of this ChartResp.
        :type instruction: str
        """
        self._instruction = instruction

    @property
    def version(self):
        """Gets the version of this ChartResp.

        模板版本

        :return: The version of this ChartResp.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ChartResp.

        模板版本

        :param version: The version of this ChartResp.
        :type version: str
        """
        self._version = version

    @property
    def description(self):
        """Gets the description of this ChartResp.

        模板描述

        :return: The description of this ChartResp.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ChartResp.

        模板描述

        :param description: The description of this ChartResp.
        :type description: str
        """
        self._description = description

    @property
    def source(self):
        """Gets the source of this ChartResp.

        模板的来源

        :return: The source of this ChartResp.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this ChartResp.

        模板的来源

        :param source: The source of this ChartResp.
        :type source: str
        """
        self._source = source

    @property
    def icon_url(self):
        """Gets the icon_url of this ChartResp.

        模板的图标链接

        :return: The icon_url of this ChartResp.
        :rtype: str
        """
        return self._icon_url

    @icon_url.setter
    def icon_url(self, icon_url):
        """Sets the icon_url of this ChartResp.

        模板的图标链接

        :param icon_url: The icon_url of this ChartResp.
        :type icon_url: str
        """
        self._icon_url = icon_url

    @property
    def public(self):
        """Gets the public of this ChartResp.

        是否公开模板

        :return: The public of this ChartResp.
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this ChartResp.

        是否公开模板

        :param public: The public of this ChartResp.
        :type public: bool
        """
        self._public = public

    @property
    def chart_url(self):
        """Gets the chart_url of this ChartResp.

        模板的链接

        :return: The chart_url of this ChartResp.
        :rtype: str
        """
        return self._chart_url

    @chart_url.setter
    def chart_url(self, chart_url):
        """Sets the chart_url of this ChartResp.

        模板的链接

        :param chart_url: The chart_url of this ChartResp.
        :type chart_url: str
        """
        self._chart_url = chart_url

    @property
    def create_at(self):
        """Gets the create_at of this ChartResp.

        创建时间

        :return: The create_at of this ChartResp.
        :rtype: str
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        """Sets the create_at of this ChartResp.

        创建时间

        :param create_at: The create_at of this ChartResp.
        :type create_at: str
        """
        self._create_at = create_at

    @property
    def update_at(self):
        """Gets the update_at of this ChartResp.

        更新时间

        :return: The update_at of this ChartResp.
        :rtype: str
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        """Sets the update_at of this ChartResp.

        更新时间

        :param update_at: The update_at of this ChartResp.
        :type update_at: str
        """
        self._update_at = update_at

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
        if not isinstance(other, ChartResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
