# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAiAppsLogsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_id': 'str',
        'request_id': 'str',
        'detect_type': 'str',
        'attack_types': 'list[str]',
        'suggestion': 'str',
        'app_name': 'str',
        '_from': 'int',
        'to': 'int',
        'limit': 'int',
        'offset': 'int',
        'marker': 'str',
        'sort_by': 'str',
        'sort_direction': 'str'
    }

    attribute_map = {
        'app_id': 'app_id',
        'request_id': 'request_id',
        'detect_type': 'detect_type',
        'attack_types': 'attack_types',
        'suggestion': 'suggestion',
        'app_name': 'app_name',
        '_from': 'from',
        'to': 'to',
        'limit': 'limit',
        'offset': 'offset',
        'marker': 'marker',
        'sort_by': 'sort_by',
        'sort_direction': 'sort_direction'
    }

    def __init__(self, app_id=None, request_id=None, detect_type=None, attack_types=None, suggestion=None, app_name=None, _from=None, to=None, limit=None, offset=None, marker=None, sort_by=None, sort_direction=None):
        r"""ListAiAppsLogsRequest

        The model defined in huaweicloud sdk

        :param app_id: **参数解释：** APP ID筛选 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type app_id: str
        :param request_id: **参数解释：** 请求ID精确筛选，返回匹配该request_id的检测日志 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type request_id: str
        :param detect_type: **参数解释：** 检测类型筛选，可选值：text, image, text_image **约束限制：** 不涉及 **取值范围：** - text: 文本检测 - image: 图片检测 - text_image: 文本图片混合检测 **默认取值：** 不涉及
        :type detect_type: str
        :param attack_types: **参数解释：** 攻击类型筛选，多个用逗号分隔 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type attack_types: list[str]
        :param suggestion: **参数解释：** 执行动作筛选，可选值：pass, block, log, desensitize **约束限制：** 不涉及 **取值范围：** - pass: 放行 - block: 拦截 - log: 记录 - desensitize: 脱敏 **默认取值：** 不涉及
        :type suggestion: str
        :param app_name: **参数解释：** APP名称筛选，按应用名称精确匹配查询 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type app_name: str
        :param _from: **参数解释：** 开始时间，时间格式为毫秒时间戳 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type _from: int
        :param to: **参数解释：** 截止时间，时间格式为毫秒时间戳 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type to: int
        :param limit: **参数解释：** 每页数量，默认10，最大1000 **约束限制：** 最大1000 **取值范围：** 1-1000 **默认取值：** 10
        :type limit: int
        :param offset: **参数解释：** 偏移量，默认0 **约束限制：** 不涉及 **取值范围：** &gt;&#x3D;0 **默认取值：** 0
        :type offset: int
        :param marker: **参数解释：** 游标标记，标记到ES的request_id字段，传入时忽略offset参数 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type marker: str
        :param sort_by: **参数解释：** 排序字段，仅支持timestamp **约束限制：** 仅支持timestamp **取值范围：** - timestamp: 按时间排序 **默认取值：** timestamp
        :type sort_by: str
        :param sort_direction: **参数解释：** 排序方向，可选值：asc, desc **约束限制：** 不涉及 **取值范围：** - asc: 升序 - desc: 降序 **默认取值：** desc
        :type sort_direction: str
        """
        
        

        self._app_id = None
        self._request_id = None
        self._detect_type = None
        self._attack_types = None
        self._suggestion = None
        self._app_name = None
        self.__from = None
        self._to = None
        self._limit = None
        self._offset = None
        self._marker = None
        self._sort_by = None
        self._sort_direction = None
        self.discriminator = None

        if app_id is not None:
            self.app_id = app_id
        if request_id is not None:
            self.request_id = request_id
        if detect_type is not None:
            self.detect_type = detect_type
        if attack_types is not None:
            self.attack_types = attack_types
        if suggestion is not None:
            self.suggestion = suggestion
        if app_name is not None:
            self.app_name = app_name
        if _from is not None:
            self._from = _from
        if to is not None:
            self.to = to
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if marker is not None:
            self.marker = marker
        if sort_by is not None:
            self.sort_by = sort_by
        if sort_direction is not None:
            self.sort_direction = sort_direction

    @property
    def app_id(self):
        r"""Gets the app_id of this ListAiAppsLogsRequest.

        **参数解释：** APP ID筛选 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The app_id of this ListAiAppsLogsRequest.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this ListAiAppsLogsRequest.

        **参数解释：** APP ID筛选 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param app_id: The app_id of this ListAiAppsLogsRequest.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def request_id(self):
        r"""Gets the request_id of this ListAiAppsLogsRequest.

        **参数解释：** 请求ID精确筛选，返回匹配该request_id的检测日志 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The request_id of this ListAiAppsLogsRequest.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListAiAppsLogsRequest.

        **参数解释：** 请求ID精确筛选，返回匹配该request_id的检测日志 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param request_id: The request_id of this ListAiAppsLogsRequest.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def detect_type(self):
        r"""Gets the detect_type of this ListAiAppsLogsRequest.

        **参数解释：** 检测类型筛选，可选值：text, image, text_image **约束限制：** 不涉及 **取值范围：** - text: 文本检测 - image: 图片检测 - text_image: 文本图片混合检测 **默认取值：** 不涉及

        :return: The detect_type of this ListAiAppsLogsRequest.
        :rtype: str
        """
        return self._detect_type

    @detect_type.setter
    def detect_type(self, detect_type):
        r"""Sets the detect_type of this ListAiAppsLogsRequest.

        **参数解释：** 检测类型筛选，可选值：text, image, text_image **约束限制：** 不涉及 **取值范围：** - text: 文本检测 - image: 图片检测 - text_image: 文本图片混合检测 **默认取值：** 不涉及

        :param detect_type: The detect_type of this ListAiAppsLogsRequest.
        :type detect_type: str
        """
        self._detect_type = detect_type

    @property
    def attack_types(self):
        r"""Gets the attack_types of this ListAiAppsLogsRequest.

        **参数解释：** 攻击类型筛选，多个用逗号分隔 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The attack_types of this ListAiAppsLogsRequest.
        :rtype: list[str]
        """
        return self._attack_types

    @attack_types.setter
    def attack_types(self, attack_types):
        r"""Sets the attack_types of this ListAiAppsLogsRequest.

        **参数解释：** 攻击类型筛选，多个用逗号分隔 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param attack_types: The attack_types of this ListAiAppsLogsRequest.
        :type attack_types: list[str]
        """
        self._attack_types = attack_types

    @property
    def suggestion(self):
        r"""Gets the suggestion of this ListAiAppsLogsRequest.

        **参数解释：** 执行动作筛选，可选值：pass, block, log, desensitize **约束限制：** 不涉及 **取值范围：** - pass: 放行 - block: 拦截 - log: 记录 - desensitize: 脱敏 **默认取值：** 不涉及

        :return: The suggestion of this ListAiAppsLogsRequest.
        :rtype: str
        """
        return self._suggestion

    @suggestion.setter
    def suggestion(self, suggestion):
        r"""Sets the suggestion of this ListAiAppsLogsRequest.

        **参数解释：** 执行动作筛选，可选值：pass, block, log, desensitize **约束限制：** 不涉及 **取值范围：** - pass: 放行 - block: 拦截 - log: 记录 - desensitize: 脱敏 **默认取值：** 不涉及

        :param suggestion: The suggestion of this ListAiAppsLogsRequest.
        :type suggestion: str
        """
        self._suggestion = suggestion

    @property
    def app_name(self):
        r"""Gets the app_name of this ListAiAppsLogsRequest.

        **参数解释：** APP名称筛选，按应用名称精确匹配查询 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The app_name of this ListAiAppsLogsRequest.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this ListAiAppsLogsRequest.

        **参数解释：** APP名称筛选，按应用名称精确匹配查询 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param app_name: The app_name of this ListAiAppsLogsRequest.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def _from(self):
        r"""Gets the _from of this ListAiAppsLogsRequest.

        **参数解释：** 开始时间，时间格式为毫秒时间戳 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The _from of this ListAiAppsLogsRequest.
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        r"""Sets the _from of this ListAiAppsLogsRequest.

        **参数解释：** 开始时间，时间格式为毫秒时间戳 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param _from: The _from of this ListAiAppsLogsRequest.
        :type _from: int
        """
        self.__from = _from

    @property
    def to(self):
        r"""Gets the to of this ListAiAppsLogsRequest.

        **参数解释：** 截止时间，时间格式为毫秒时间戳 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The to of this ListAiAppsLogsRequest.
        :rtype: int
        """
        return self._to

    @to.setter
    def to(self, to):
        r"""Sets the to of this ListAiAppsLogsRequest.

        **参数解释：** 截止时间，时间格式为毫秒时间戳 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param to: The to of this ListAiAppsLogsRequest.
        :type to: int
        """
        self._to = to

    @property
    def limit(self):
        r"""Gets the limit of this ListAiAppsLogsRequest.

        **参数解释：** 每页数量，默认10，最大1000 **约束限制：** 最大1000 **取值范围：** 1-1000 **默认取值：** 10

        :return: The limit of this ListAiAppsLogsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAiAppsLogsRequest.

        **参数解释：** 每页数量，默认10，最大1000 **约束限制：** 最大1000 **取值范围：** 1-1000 **默认取值：** 10

        :param limit: The limit of this ListAiAppsLogsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListAiAppsLogsRequest.

        **参数解释：** 偏移量，默认0 **约束限制：** 不涉及 **取值范围：** >=0 **默认取值：** 0

        :return: The offset of this ListAiAppsLogsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAiAppsLogsRequest.

        **参数解释：** 偏移量，默认0 **约束限制：** 不涉及 **取值范围：** >=0 **默认取值：** 0

        :param offset: The offset of this ListAiAppsLogsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def marker(self):
        r"""Gets the marker of this ListAiAppsLogsRequest.

        **参数解释：** 游标标记，标记到ES的request_id字段，传入时忽略offset参数 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The marker of this ListAiAppsLogsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListAiAppsLogsRequest.

        **参数解释：** 游标标记，标记到ES的request_id字段，传入时忽略offset参数 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param marker: The marker of this ListAiAppsLogsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def sort_by(self):
        r"""Gets the sort_by of this ListAiAppsLogsRequest.

        **参数解释：** 排序字段，仅支持timestamp **约束限制：** 仅支持timestamp **取值范围：** - timestamp: 按时间排序 **默认取值：** timestamp

        :return: The sort_by of this ListAiAppsLogsRequest.
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        r"""Sets the sort_by of this ListAiAppsLogsRequest.

        **参数解释：** 排序字段，仅支持timestamp **约束限制：** 仅支持timestamp **取值范围：** - timestamp: 按时间排序 **默认取值：** timestamp

        :param sort_by: The sort_by of this ListAiAppsLogsRequest.
        :type sort_by: str
        """
        self._sort_by = sort_by

    @property
    def sort_direction(self):
        r"""Gets the sort_direction of this ListAiAppsLogsRequest.

        **参数解释：** 排序方向，可选值：asc, desc **约束限制：** 不涉及 **取值范围：** - asc: 升序 - desc: 降序 **默认取值：** desc

        :return: The sort_direction of this ListAiAppsLogsRequest.
        :rtype: str
        """
        return self._sort_direction

    @sort_direction.setter
    def sort_direction(self, sort_direction):
        r"""Sets the sort_direction of this ListAiAppsLogsRequest.

        **参数解释：** 排序方向，可选值：asc, desc **约束限制：** 不涉及 **取值范围：** - asc: 升序 - desc: 降序 **默认取值：** desc

        :param sort_direction: The sort_direction of this ListAiAppsLogsRequest.
        :type sort_direction: str
        """
        self._sort_direction = sort_direction

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
        if not isinstance(other, ListAiAppsLogsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
