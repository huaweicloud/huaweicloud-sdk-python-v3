# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAdhocQueryRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'session_id': 'str',
        'query': 'str',
        'query_type': 'str',
        '_from': 'int',
        'to': 'int',
        'script_params': 'list[ScriptParam]',
        'time_zone': 'str',
        'sql_render_from': 'int',
        'sql_render_to': 'int',
        'source_page': 'str'
    }

    attribute_map = {
        'session_id': 'session_id',
        'query': 'query',
        'query_type': 'query_type',
        '_from': 'from',
        'to': 'to',
        'script_params': 'script_params',
        'time_zone': 'time_zone',
        'sql_render_from': 'sql_render_from',
        'sql_render_to': 'sql_render_to',
        'source_page': 'source_page'
    }

    def __init__(self, session_id=None, query=None, query_type=None, _from=None, to=None, script_params=None, time_zone=None, sql_render_from=None, sql_render_to=None, source_page=None):
        r"""CreateAdhocQueryRequestBody

        The model defined in huaweicloud sdk

        :param session_id: UUID
        :type session_id: str
        :param query: 具体查询
        :type query: str
        :param query_type: 查询类型
        :type query_type: str
        :param _from: 起始范围
        :type _from: int
        :param to: 终止范围
        :type to: int
        :param script_params: 脚本参数列表
        :type script_params: list[:class:`huaweicloudsdksecmaster.v2.ScriptParam`]
        :param time_zone: 时区
        :type time_zone: str
        :param sql_render_from: 起始范围
        :type sql_render_from: int
        :param sql_render_to: 终止范围
        :type sql_render_to: int
        :param source_page: 源页
        :type source_page: str
        """
        
        

        self._session_id = None
        self._query = None
        self._query_type = None
        self.__from = None
        self._to = None
        self._script_params = None
        self._time_zone = None
        self._sql_render_from = None
        self._sql_render_to = None
        self._source_page = None
        self.discriminator = None

        if session_id is not None:
            self.session_id = session_id
        if query is not None:
            self.query = query
        if query_type is not None:
            self.query_type = query_type
        if _from is not None:
            self._from = _from
        if to is not None:
            self.to = to
        if script_params is not None:
            self.script_params = script_params
        if time_zone is not None:
            self.time_zone = time_zone
        if sql_render_from is not None:
            self.sql_render_from = sql_render_from
        if sql_render_to is not None:
            self.sql_render_to = sql_render_to
        if source_page is not None:
            self.source_page = source_page

    @property
    def session_id(self):
        r"""Gets the session_id of this CreateAdhocQueryRequestBody.

        UUID

        :return: The session_id of this CreateAdhocQueryRequestBody.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        r"""Sets the session_id of this CreateAdhocQueryRequestBody.

        UUID

        :param session_id: The session_id of this CreateAdhocQueryRequestBody.
        :type session_id: str
        """
        self._session_id = session_id

    @property
    def query(self):
        r"""Gets the query of this CreateAdhocQueryRequestBody.

        具体查询

        :return: The query of this CreateAdhocQueryRequestBody.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        r"""Sets the query of this CreateAdhocQueryRequestBody.

        具体查询

        :param query: The query of this CreateAdhocQueryRequestBody.
        :type query: str
        """
        self._query = query

    @property
    def query_type(self):
        r"""Gets the query_type of this CreateAdhocQueryRequestBody.

        查询类型

        :return: The query_type of this CreateAdhocQueryRequestBody.
        :rtype: str
        """
        return self._query_type

    @query_type.setter
    def query_type(self, query_type):
        r"""Sets the query_type of this CreateAdhocQueryRequestBody.

        查询类型

        :param query_type: The query_type of this CreateAdhocQueryRequestBody.
        :type query_type: str
        """
        self._query_type = query_type

    @property
    def _from(self):
        r"""Gets the _from of this CreateAdhocQueryRequestBody.

        起始范围

        :return: The _from of this CreateAdhocQueryRequestBody.
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        r"""Sets the _from of this CreateAdhocQueryRequestBody.

        起始范围

        :param _from: The _from of this CreateAdhocQueryRequestBody.
        :type _from: int
        """
        self.__from = _from

    @property
    def to(self):
        r"""Gets the to of this CreateAdhocQueryRequestBody.

        终止范围

        :return: The to of this CreateAdhocQueryRequestBody.
        :rtype: int
        """
        return self._to

    @to.setter
    def to(self, to):
        r"""Sets the to of this CreateAdhocQueryRequestBody.

        终止范围

        :param to: The to of this CreateAdhocQueryRequestBody.
        :type to: int
        """
        self._to = to

    @property
    def script_params(self):
        r"""Gets the script_params of this CreateAdhocQueryRequestBody.

        脚本参数列表

        :return: The script_params of this CreateAdhocQueryRequestBody.
        :rtype: list[:class:`huaweicloudsdksecmaster.v2.ScriptParam`]
        """
        return self._script_params

    @script_params.setter
    def script_params(self, script_params):
        r"""Sets the script_params of this CreateAdhocQueryRequestBody.

        脚本参数列表

        :param script_params: The script_params of this CreateAdhocQueryRequestBody.
        :type script_params: list[:class:`huaweicloudsdksecmaster.v2.ScriptParam`]
        """
        self._script_params = script_params

    @property
    def time_zone(self):
        r"""Gets the time_zone of this CreateAdhocQueryRequestBody.

        时区

        :return: The time_zone of this CreateAdhocQueryRequestBody.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        r"""Sets the time_zone of this CreateAdhocQueryRequestBody.

        时区

        :param time_zone: The time_zone of this CreateAdhocQueryRequestBody.
        :type time_zone: str
        """
        self._time_zone = time_zone

    @property
    def sql_render_from(self):
        r"""Gets the sql_render_from of this CreateAdhocQueryRequestBody.

        起始范围

        :return: The sql_render_from of this CreateAdhocQueryRequestBody.
        :rtype: int
        """
        return self._sql_render_from

    @sql_render_from.setter
    def sql_render_from(self, sql_render_from):
        r"""Sets the sql_render_from of this CreateAdhocQueryRequestBody.

        起始范围

        :param sql_render_from: The sql_render_from of this CreateAdhocQueryRequestBody.
        :type sql_render_from: int
        """
        self._sql_render_from = sql_render_from

    @property
    def sql_render_to(self):
        r"""Gets the sql_render_to of this CreateAdhocQueryRequestBody.

        终止范围

        :return: The sql_render_to of this CreateAdhocQueryRequestBody.
        :rtype: int
        """
        return self._sql_render_to

    @sql_render_to.setter
    def sql_render_to(self, sql_render_to):
        r"""Sets the sql_render_to of this CreateAdhocQueryRequestBody.

        终止范围

        :param sql_render_to: The sql_render_to of this CreateAdhocQueryRequestBody.
        :type sql_render_to: int
        """
        self._sql_render_to = sql_render_to

    @property
    def source_page(self):
        r"""Gets the source_page of this CreateAdhocQueryRequestBody.

        源页

        :return: The source_page of this CreateAdhocQueryRequestBody.
        :rtype: str
        """
        return self._source_page

    @source_page.setter
    def source_page(self, source_page):
        r"""Sets the source_page of this CreateAdhocQueryRequestBody.

        源页

        :param source_page: The source_page of this CreateAdhocQueryRequestBody.
        :type source_page: str
        """
        self._source_page = source_page

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
        if not isinstance(other, CreateAdhocQueryRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
