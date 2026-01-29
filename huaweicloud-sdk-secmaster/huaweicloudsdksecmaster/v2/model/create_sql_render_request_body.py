# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSqlRenderRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'query': 'str',
        'script_params': 'list[ScriptParam]',
        'transform_query': 'str',
        'session_id': 'str',
        'time_zone': 'str',
        'inter_active_params': 'list[InterActiveParams]',
        '_from': 'int',
        'to': 'int'
    }

    attribute_map = {
        'query': 'query',
        'script_params': 'script_params',
        'transform_query': 'transform_query',
        'session_id': 'session_id',
        'time_zone': 'time_zone',
        'inter_active_params': 'inter_active_params',
        '_from': 'from',
        'to': 'to'
    }

    def __init__(self, query=None, script_params=None, transform_query=None, session_id=None, time_zone=None, inter_active_params=None, _from=None, to=None):
        r"""CreateSqlRenderRequestBody

        The model defined in huaweicloud sdk

        :param query: 查询语句
        :type query: str
        :param script_params: 脚本参数
        :type script_params: list[:class:`huaweicloudsdksecmaster.v2.ScriptParam`]
        :param transform_query: 查询语句
        :type transform_query: str
        :param session_id: Console会话ID
        :type session_id: str
        :param time_zone: 时区
        :type time_zone: str
        :param inter_active_params: 交互参数列表
        :type inter_active_params: list[:class:`huaweicloudsdksecmaster.v2.InterActiveParams`]
        :param _from: 起始
        :type _from: int
        :param to: 终止
        :type to: int
        """
        
        

        self._query = None
        self._script_params = None
        self._transform_query = None
        self._session_id = None
        self._time_zone = None
        self._inter_active_params = None
        self.__from = None
        self._to = None
        self.discriminator = None

        if query is not None:
            self.query = query
        if script_params is not None:
            self.script_params = script_params
        if transform_query is not None:
            self.transform_query = transform_query
        if session_id is not None:
            self.session_id = session_id
        if time_zone is not None:
            self.time_zone = time_zone
        if inter_active_params is not None:
            self.inter_active_params = inter_active_params
        if _from is not None:
            self._from = _from
        if to is not None:
            self.to = to

    @property
    def query(self):
        r"""Gets the query of this CreateSqlRenderRequestBody.

        查询语句

        :return: The query of this CreateSqlRenderRequestBody.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        r"""Sets the query of this CreateSqlRenderRequestBody.

        查询语句

        :param query: The query of this CreateSqlRenderRequestBody.
        :type query: str
        """
        self._query = query

    @property
    def script_params(self):
        r"""Gets the script_params of this CreateSqlRenderRequestBody.

        脚本参数

        :return: The script_params of this CreateSqlRenderRequestBody.
        :rtype: list[:class:`huaweicloudsdksecmaster.v2.ScriptParam`]
        """
        return self._script_params

    @script_params.setter
    def script_params(self, script_params):
        r"""Sets the script_params of this CreateSqlRenderRequestBody.

        脚本参数

        :param script_params: The script_params of this CreateSqlRenderRequestBody.
        :type script_params: list[:class:`huaweicloudsdksecmaster.v2.ScriptParam`]
        """
        self._script_params = script_params

    @property
    def transform_query(self):
        r"""Gets the transform_query of this CreateSqlRenderRequestBody.

        查询语句

        :return: The transform_query of this CreateSqlRenderRequestBody.
        :rtype: str
        """
        return self._transform_query

    @transform_query.setter
    def transform_query(self, transform_query):
        r"""Sets the transform_query of this CreateSqlRenderRequestBody.

        查询语句

        :param transform_query: The transform_query of this CreateSqlRenderRequestBody.
        :type transform_query: str
        """
        self._transform_query = transform_query

    @property
    def session_id(self):
        r"""Gets the session_id of this CreateSqlRenderRequestBody.

        Console会话ID

        :return: The session_id of this CreateSqlRenderRequestBody.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        r"""Sets the session_id of this CreateSqlRenderRequestBody.

        Console会话ID

        :param session_id: The session_id of this CreateSqlRenderRequestBody.
        :type session_id: str
        """
        self._session_id = session_id

    @property
    def time_zone(self):
        r"""Gets the time_zone of this CreateSqlRenderRequestBody.

        时区

        :return: The time_zone of this CreateSqlRenderRequestBody.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        r"""Sets the time_zone of this CreateSqlRenderRequestBody.

        时区

        :param time_zone: The time_zone of this CreateSqlRenderRequestBody.
        :type time_zone: str
        """
        self._time_zone = time_zone

    @property
    def inter_active_params(self):
        r"""Gets the inter_active_params of this CreateSqlRenderRequestBody.

        交互参数列表

        :return: The inter_active_params of this CreateSqlRenderRequestBody.
        :rtype: list[:class:`huaweicloudsdksecmaster.v2.InterActiveParams`]
        """
        return self._inter_active_params

    @inter_active_params.setter
    def inter_active_params(self, inter_active_params):
        r"""Sets the inter_active_params of this CreateSqlRenderRequestBody.

        交互参数列表

        :param inter_active_params: The inter_active_params of this CreateSqlRenderRequestBody.
        :type inter_active_params: list[:class:`huaweicloudsdksecmaster.v2.InterActiveParams`]
        """
        self._inter_active_params = inter_active_params

    @property
    def _from(self):
        r"""Gets the _from of this CreateSqlRenderRequestBody.

        起始

        :return: The _from of this CreateSqlRenderRequestBody.
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        r"""Sets the _from of this CreateSqlRenderRequestBody.

        起始

        :param _from: The _from of this CreateSqlRenderRequestBody.
        :type _from: int
        """
        self.__from = _from

    @property
    def to(self):
        r"""Gets the to of this CreateSqlRenderRequestBody.

        终止

        :return: The to of this CreateSqlRenderRequestBody.
        :rtype: int
        """
        return self._to

    @to.setter
    def to(self, to):
        r"""Sets the to of this CreateSqlRenderRequestBody.

        终止

        :param to: The to of this CreateSqlRenderRequestBody.
        :type to: int
        """
        self._to = to

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
        if not isinstance(other, CreateSqlRenderRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
