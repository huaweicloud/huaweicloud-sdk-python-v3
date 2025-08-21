# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRepositoryTemplatesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'platform': 'str',
        'pipeline': 'str',
        'type': 'str',
        'search': 'str',
        'enter_type': 'str',
        'date_order': 'str',
        'language': 'str',
        'project_id': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'platform': 'platform',
        'pipeline': 'pipeline',
        'type': 'type',
        'search': 'search',
        'enter_type': 'enter_type',
        'date_order': 'date_order',
        'language': 'language',
        'project_id': 'project_id'
    }

    def __init__(self, offset=None, limit=None, platform=None, pipeline=None, type=None, search=None, enter_type=None, date_order=None, language=None, project_id=None):
        r"""ListRepositoryTemplatesRequest

        The model defined in huaweicloud sdk

        :param offset: **参数解释：** 偏移量，从0开始。
        :type offset: int
        :param limit: **参数解释：** 返回数量。
        :type limit: int
        :param platform: **参数解释：** 应用类型。 **约束限制：** 不涉及 **取值范围：** - Android。 - Console。 - HarmonyOS。 - OTHERS。 - REST API。 - ServiceStage。 - Web网站。 - 图形用户界面。 **默认取值：** 不涉及
        :type platform: str
        :param pipeline: **参数解释：** 是否支持自动创建流水线。 **约束限制：** 不涉及 **取值范围：** - SupportPipeline，支持自动创建流水线。 - UnsupportedPipeline 不支持自动创建流水线。 **默认取值：** 不涉及
        :type pipeline: str
        :param type: **参数解释：** 自动创建流水线。 **约束限制：** 不涉及 **取值范围：** - SYSTEM,USER，个人和官方模版。 - SYSTEM，官方模版。 - USER，个人模版。 **默认取值：** 不涉及
        :type type: str
        :param search: **参数解释：** 查询关键字，按模板仓标题搜索。 **约束限制：** 不涉及 **取值范围：** 字符串长度0至50。 **默认取值：** 不涉及
        :type search: str
        :param enter_type: **参数解释：** 参赛类型。 **约束限制：** 不涉及 **取值范围：** - AI。 - 大数据。 - 小程序。 - 微服务。 **默认取值：** 不涉及
        :type enter_type: str
        :param date_order: **参数解释：** 按照模板仓的创建时间进行排序。 **约束限制：** 不涉及 **取值范围：** - up，升序。 - down，降序。 **默认取值：** 不涉及
        :type date_order: str
        :param language: **参数解释：** 编程语言。 **约束限制：** 不涉及 **取值范围：** - ArkTS。 - ASP.NET。 - C。 - C#。 - C++。 - Go。 - Groovy。 - HTML。 - Java。 - NodeJS。 - OTHERS。 - PHP。 - Python。 **默认取值：** 不涉及
        :type language: str
        :param project_id: **参数解释：** 项目的32位uuid，项目唯一标识，通过[[查询项目列表](https://support.huaweicloud.com/api-projectman/ListProjectsV4.html)](tag:hws)[[查询项目列表](https://support.huaweicloud.com/intl/en-us/api-projectman/ListProjectsV4.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 当该参数不为空时，仅返回当前项目下符合搜索条件的模版仓 **取值范围：** 字符串长度32。 **取值范围：** 不涉及
        :type project_id: str
        """
        
        

        self._offset = None
        self._limit = None
        self._platform = None
        self._pipeline = None
        self._type = None
        self._search = None
        self._enter_type = None
        self._date_order = None
        self._language = None
        self._project_id = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if platform is not None:
            self.platform = platform
        if pipeline is not None:
            self.pipeline = pipeline
        self.type = type
        if search is not None:
            self.search = search
        if enter_type is not None:
            self.enter_type = enter_type
        if date_order is not None:
            self.date_order = date_order
        if language is not None:
            self.language = language
        if project_id is not None:
            self.project_id = project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListRepositoryTemplatesRequest.

        **参数解释：** 偏移量，从0开始。

        :return: The offset of this ListRepositoryTemplatesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListRepositoryTemplatesRequest.

        **参数解释：** 偏移量，从0开始。

        :param offset: The offset of this ListRepositoryTemplatesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListRepositoryTemplatesRequest.

        **参数解释：** 返回数量。

        :return: The limit of this ListRepositoryTemplatesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListRepositoryTemplatesRequest.

        **参数解释：** 返回数量。

        :param limit: The limit of this ListRepositoryTemplatesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def platform(self):
        r"""Gets the platform of this ListRepositoryTemplatesRequest.

        **参数解释：** 应用类型。 **约束限制：** 不涉及 **取值范围：** - Android。 - Console。 - HarmonyOS。 - OTHERS。 - REST API。 - ServiceStage。 - Web网站。 - 图形用户界面。 **默认取值：** 不涉及

        :return: The platform of this ListRepositoryTemplatesRequest.
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        r"""Sets the platform of this ListRepositoryTemplatesRequest.

        **参数解释：** 应用类型。 **约束限制：** 不涉及 **取值范围：** - Android。 - Console。 - HarmonyOS。 - OTHERS。 - REST API。 - ServiceStage。 - Web网站。 - 图形用户界面。 **默认取值：** 不涉及

        :param platform: The platform of this ListRepositoryTemplatesRequest.
        :type platform: str
        """
        self._platform = platform

    @property
    def pipeline(self):
        r"""Gets the pipeline of this ListRepositoryTemplatesRequest.

        **参数解释：** 是否支持自动创建流水线。 **约束限制：** 不涉及 **取值范围：** - SupportPipeline，支持自动创建流水线。 - UnsupportedPipeline 不支持自动创建流水线。 **默认取值：** 不涉及

        :return: The pipeline of this ListRepositoryTemplatesRequest.
        :rtype: str
        """
        return self._pipeline

    @pipeline.setter
    def pipeline(self, pipeline):
        r"""Sets the pipeline of this ListRepositoryTemplatesRequest.

        **参数解释：** 是否支持自动创建流水线。 **约束限制：** 不涉及 **取值范围：** - SupportPipeline，支持自动创建流水线。 - UnsupportedPipeline 不支持自动创建流水线。 **默认取值：** 不涉及

        :param pipeline: The pipeline of this ListRepositoryTemplatesRequest.
        :type pipeline: str
        """
        self._pipeline = pipeline

    @property
    def type(self):
        r"""Gets the type of this ListRepositoryTemplatesRequest.

        **参数解释：** 自动创建流水线。 **约束限制：** 不涉及 **取值范围：** - SYSTEM,USER，个人和官方模版。 - SYSTEM，官方模版。 - USER，个人模版。 **默认取值：** 不涉及

        :return: The type of this ListRepositoryTemplatesRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListRepositoryTemplatesRequest.

        **参数解释：** 自动创建流水线。 **约束限制：** 不涉及 **取值范围：** - SYSTEM,USER，个人和官方模版。 - SYSTEM，官方模版。 - USER，个人模版。 **默认取值：** 不涉及

        :param type: The type of this ListRepositoryTemplatesRequest.
        :type type: str
        """
        self._type = type

    @property
    def search(self):
        r"""Gets the search of this ListRepositoryTemplatesRequest.

        **参数解释：** 查询关键字，按模板仓标题搜索。 **约束限制：** 不涉及 **取值范围：** 字符串长度0至50。 **默认取值：** 不涉及

        :return: The search of this ListRepositoryTemplatesRequest.
        :rtype: str
        """
        return self._search

    @search.setter
    def search(self, search):
        r"""Sets the search of this ListRepositoryTemplatesRequest.

        **参数解释：** 查询关键字，按模板仓标题搜索。 **约束限制：** 不涉及 **取值范围：** 字符串长度0至50。 **默认取值：** 不涉及

        :param search: The search of this ListRepositoryTemplatesRequest.
        :type search: str
        """
        self._search = search

    @property
    def enter_type(self):
        r"""Gets the enter_type of this ListRepositoryTemplatesRequest.

        **参数解释：** 参赛类型。 **约束限制：** 不涉及 **取值范围：** - AI。 - 大数据。 - 小程序。 - 微服务。 **默认取值：** 不涉及

        :return: The enter_type of this ListRepositoryTemplatesRequest.
        :rtype: str
        """
        return self._enter_type

    @enter_type.setter
    def enter_type(self, enter_type):
        r"""Sets the enter_type of this ListRepositoryTemplatesRequest.

        **参数解释：** 参赛类型。 **约束限制：** 不涉及 **取值范围：** - AI。 - 大数据。 - 小程序。 - 微服务。 **默认取值：** 不涉及

        :param enter_type: The enter_type of this ListRepositoryTemplatesRequest.
        :type enter_type: str
        """
        self._enter_type = enter_type

    @property
    def date_order(self):
        r"""Gets the date_order of this ListRepositoryTemplatesRequest.

        **参数解释：** 按照模板仓的创建时间进行排序。 **约束限制：** 不涉及 **取值范围：** - up，升序。 - down，降序。 **默认取值：** 不涉及

        :return: The date_order of this ListRepositoryTemplatesRequest.
        :rtype: str
        """
        return self._date_order

    @date_order.setter
    def date_order(self, date_order):
        r"""Sets the date_order of this ListRepositoryTemplatesRequest.

        **参数解释：** 按照模板仓的创建时间进行排序。 **约束限制：** 不涉及 **取值范围：** - up，升序。 - down，降序。 **默认取值：** 不涉及

        :param date_order: The date_order of this ListRepositoryTemplatesRequest.
        :type date_order: str
        """
        self._date_order = date_order

    @property
    def language(self):
        r"""Gets the language of this ListRepositoryTemplatesRequest.

        **参数解释：** 编程语言。 **约束限制：** 不涉及 **取值范围：** - ArkTS。 - ASP.NET。 - C。 - C#。 - C++。 - Go。 - Groovy。 - HTML。 - Java。 - NodeJS。 - OTHERS。 - PHP。 - Python。 **默认取值：** 不涉及

        :return: The language of this ListRepositoryTemplatesRequest.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this ListRepositoryTemplatesRequest.

        **参数解释：** 编程语言。 **约束限制：** 不涉及 **取值范围：** - ArkTS。 - ASP.NET。 - C。 - C#。 - C++。 - Go。 - Groovy。 - HTML。 - Java。 - NodeJS。 - OTHERS。 - PHP。 - Python。 **默认取值：** 不涉及

        :param language: The language of this ListRepositoryTemplatesRequest.
        :type language: str
        """
        self._language = language

    @property
    def project_id(self):
        r"""Gets the project_id of this ListRepositoryTemplatesRequest.

        **参数解释：** 项目的32位uuid，项目唯一标识，通过[[查询项目列表](https://support.huaweicloud.com/api-projectman/ListProjectsV4.html)](tag:hws)[[查询项目列表](https://support.huaweicloud.com/intl/en-us/api-projectman/ListProjectsV4.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 当该参数不为空时，仅返回当前项目下符合搜索条件的模版仓 **取值范围：** 字符串长度32。 **取值范围：** 不涉及

        :return: The project_id of this ListRepositoryTemplatesRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListRepositoryTemplatesRequest.

        **参数解释：** 项目的32位uuid，项目唯一标识，通过[[查询项目列表](https://support.huaweicloud.com/api-projectman/ListProjectsV4.html)](tag:hws)[[查询项目列表](https://support.huaweicloud.com/intl/en-us/api-projectman/ListProjectsV4.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 当该参数不为空时，仅返回当前项目下符合搜索条件的模版仓 **取值范围：** 字符串长度32。 **取值范围：** 不涉及

        :param project_id: The project_id of this ListRepositoryTemplatesRequest.
        :type project_id: str
        """
        self._project_id = project_id

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
        if not isinstance(other, ListRepositoryTemplatesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
