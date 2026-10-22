# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LogItem:

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
        'timestamp': 'int',
        'request_id': 'str',
        'region_id': 'str',
        'engine_id': 'str',
        'app_id': 'str',
        'app_name': 'str',
        'tenant_id': 'str',
        'project_id': 'str',
        'detect_type': 'str',
        'detect_content': 'str',
        'history': 'list[HistoryItem]',
        'attack_types': 'list[str]',
        'suggestion': 'str',
        'custom_resp': 'str',
        'hit_details': 'list[HitDetail]'
    }

    attribute_map = {
        'id': 'id',
        'timestamp': 'timestamp',
        'request_id': 'request_id',
        'region_id': 'region_id',
        'engine_id': 'engine_id',
        'app_id': 'app_id',
        'app_name': 'app_name',
        'tenant_id': 'tenant_id',
        'project_id': 'project_id',
        'detect_type': 'detect_type',
        'detect_content': 'detect_content',
        'history': 'history',
        'attack_types': 'attack_types',
        'suggestion': 'suggestion',
        'custom_resp': 'custom_resp',
        'hit_details': 'hit_details'
    }

    def __init__(self, id=None, timestamp=None, request_id=None, region_id=None, engine_id=None, app_id=None, app_name=None, tenant_id=None, project_id=None, detect_type=None, detect_content=None, history=None, attack_types=None, suggestion=None, custom_resp=None, hit_details=None):
        r"""LogItem

        The model defined in huaweicloud sdk

        :param id: 日志唯一标识
        :type id: str
        :param timestamp: 检测时间（毫秒时间戳）
        :type timestamp: int
        :param request_id: 请求ID
        :type request_id: str
        :param region_id: 区域ID
        :type region_id: str
        :param engine_id: 引擎ID
        :type engine_id: str
        :param app_id: APP ID
        :type app_id: str
        :param app_name: APP名称
        :type app_name: str
        :param tenant_id: 租户ID
        :type tenant_id: str
        :param project_id: 项目ID
        :type project_id: str
        :param detect_type: 检测类型
        :type detect_type: str
        :param detect_content: 检测内容原文
        :type detect_content: str
        :param history: 多轮对话历史上下文，与检测内容原文一一对应
        :type history: list[:class:`huaweicloudsdkwaf.v1.HistoryItem`]
        :param attack_types: 检测分类
        :type attack_types: list[str]
        :param suggestion: 执行动作
        :type suggestion: str
        :param custom_resp: 安全代答
        :type custom_resp: str
        :param hit_details: 检测命中详情
        :type hit_details: list[:class:`huaweicloudsdkwaf.v1.HitDetail`]
        """
        
        

        self._id = None
        self._timestamp = None
        self._request_id = None
        self._region_id = None
        self._engine_id = None
        self._app_id = None
        self._app_name = None
        self._tenant_id = None
        self._project_id = None
        self._detect_type = None
        self._detect_content = None
        self._history = None
        self._attack_types = None
        self._suggestion = None
        self._custom_resp = None
        self._hit_details = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if timestamp is not None:
            self.timestamp = timestamp
        if request_id is not None:
            self.request_id = request_id
        if region_id is not None:
            self.region_id = region_id
        if engine_id is not None:
            self.engine_id = engine_id
        if app_id is not None:
            self.app_id = app_id
        if app_name is not None:
            self.app_name = app_name
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if project_id is not None:
            self.project_id = project_id
        if detect_type is not None:
            self.detect_type = detect_type
        if detect_content is not None:
            self.detect_content = detect_content
        if history is not None:
            self.history = history
        if attack_types is not None:
            self.attack_types = attack_types
        if suggestion is not None:
            self.suggestion = suggestion
        if custom_resp is not None:
            self.custom_resp = custom_resp
        if hit_details is not None:
            self.hit_details = hit_details

    @property
    def id(self):
        r"""Gets the id of this LogItem.

        日志唯一标识

        :return: The id of this LogItem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this LogItem.

        日志唯一标识

        :param id: The id of this LogItem.
        :type id: str
        """
        self._id = id

    @property
    def timestamp(self):
        r"""Gets the timestamp of this LogItem.

        检测时间（毫秒时间戳）

        :return: The timestamp of this LogItem.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        r"""Sets the timestamp of this LogItem.

        检测时间（毫秒时间戳）

        :param timestamp: The timestamp of this LogItem.
        :type timestamp: int
        """
        self._timestamp = timestamp

    @property
    def request_id(self):
        r"""Gets the request_id of this LogItem.

        请求ID

        :return: The request_id of this LogItem.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this LogItem.

        请求ID

        :param request_id: The request_id of this LogItem.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def region_id(self):
        r"""Gets the region_id of this LogItem.

        区域ID

        :return: The region_id of this LogItem.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this LogItem.

        区域ID

        :param region_id: The region_id of this LogItem.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def engine_id(self):
        r"""Gets the engine_id of this LogItem.

        引擎ID

        :return: The engine_id of this LogItem.
        :rtype: str
        """
        return self._engine_id

    @engine_id.setter
    def engine_id(self, engine_id):
        r"""Sets the engine_id of this LogItem.

        引擎ID

        :param engine_id: The engine_id of this LogItem.
        :type engine_id: str
        """
        self._engine_id = engine_id

    @property
    def app_id(self):
        r"""Gets the app_id of this LogItem.

        APP ID

        :return: The app_id of this LogItem.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this LogItem.

        APP ID

        :param app_id: The app_id of this LogItem.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def app_name(self):
        r"""Gets the app_name of this LogItem.

        APP名称

        :return: The app_name of this LogItem.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this LogItem.

        APP名称

        :param app_name: The app_name of this LogItem.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this LogItem.

        租户ID

        :return: The tenant_id of this LogItem.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this LogItem.

        租户ID

        :param tenant_id: The tenant_id of this LogItem.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def project_id(self):
        r"""Gets the project_id of this LogItem.

        项目ID

        :return: The project_id of this LogItem.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this LogItem.

        项目ID

        :param project_id: The project_id of this LogItem.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def detect_type(self):
        r"""Gets the detect_type of this LogItem.

        检测类型

        :return: The detect_type of this LogItem.
        :rtype: str
        """
        return self._detect_type

    @detect_type.setter
    def detect_type(self, detect_type):
        r"""Sets the detect_type of this LogItem.

        检测类型

        :param detect_type: The detect_type of this LogItem.
        :type detect_type: str
        """
        self._detect_type = detect_type

    @property
    def detect_content(self):
        r"""Gets the detect_content of this LogItem.

        检测内容原文

        :return: The detect_content of this LogItem.
        :rtype: str
        """
        return self._detect_content

    @detect_content.setter
    def detect_content(self, detect_content):
        r"""Sets the detect_content of this LogItem.

        检测内容原文

        :param detect_content: The detect_content of this LogItem.
        :type detect_content: str
        """
        self._detect_content = detect_content

    @property
    def history(self):
        r"""Gets the history of this LogItem.

        多轮对话历史上下文，与检测内容原文一一对应

        :return: The history of this LogItem.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.HistoryItem`]
        """
        return self._history

    @history.setter
    def history(self, history):
        r"""Sets the history of this LogItem.

        多轮对话历史上下文，与检测内容原文一一对应

        :param history: The history of this LogItem.
        :type history: list[:class:`huaweicloudsdkwaf.v1.HistoryItem`]
        """
        self._history = history

    @property
    def attack_types(self):
        r"""Gets the attack_types of this LogItem.

        检测分类

        :return: The attack_types of this LogItem.
        :rtype: list[str]
        """
        return self._attack_types

    @attack_types.setter
    def attack_types(self, attack_types):
        r"""Sets the attack_types of this LogItem.

        检测分类

        :param attack_types: The attack_types of this LogItem.
        :type attack_types: list[str]
        """
        self._attack_types = attack_types

    @property
    def suggestion(self):
        r"""Gets the suggestion of this LogItem.

        执行动作

        :return: The suggestion of this LogItem.
        :rtype: str
        """
        return self._suggestion

    @suggestion.setter
    def suggestion(self, suggestion):
        r"""Sets the suggestion of this LogItem.

        执行动作

        :param suggestion: The suggestion of this LogItem.
        :type suggestion: str
        """
        self._suggestion = suggestion

    @property
    def custom_resp(self):
        r"""Gets the custom_resp of this LogItem.

        安全代答

        :return: The custom_resp of this LogItem.
        :rtype: str
        """
        return self._custom_resp

    @custom_resp.setter
    def custom_resp(self, custom_resp):
        r"""Sets the custom_resp of this LogItem.

        安全代答

        :param custom_resp: The custom_resp of this LogItem.
        :type custom_resp: str
        """
        self._custom_resp = custom_resp

    @property
    def hit_details(self):
        r"""Gets the hit_details of this LogItem.

        检测命中详情

        :return: The hit_details of this LogItem.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.HitDetail`]
        """
        return self._hit_details

    @hit_details.setter
    def hit_details(self, hit_details):
        r"""Sets the hit_details of this LogItem.

        检测命中详情

        :param hit_details: The hit_details of this LogItem.
        :type hit_details: list[:class:`huaweicloudsdkwaf.v1.HitDetail`]
        """
        self._hit_details = hit_details

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
        if not isinstance(other, LogItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
