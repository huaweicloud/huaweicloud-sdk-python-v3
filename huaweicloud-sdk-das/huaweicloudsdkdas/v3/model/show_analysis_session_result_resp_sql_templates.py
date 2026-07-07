# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAnalysisSessionResultRespSqlTemplates:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sql_template': 'str',
        'database_name': 'str',
        'total_count': 'int',
        'top_state_duration_list': 'list[ShowAnalysisSessionResultRespTopStateDuration]',
        'top_transaction_duration_list': 'list[ShowAnalysisSessionResultRespTopStateDuration]'
    }

    attribute_map = {
        'sql_template': 'sql_template',
        'database_name': 'database_name',
        'total_count': 'total_count',
        'top_state_duration_list': 'top_state_duration_list',
        'top_transaction_duration_list': 'top_transaction_duration_list'
    }

    def __init__(self, sql_template=None, database_name=None, total_count=None, top_state_duration_list=None, top_transaction_duration_list=None):
        r"""ShowAnalysisSessionResultRespSqlTemplates

        The model defined in huaweicloud sdk

        :param sql_template: SQL模板
        :type sql_template: str
        :param database_name: 数据库名
        :type database_name: str
        :param total_count: 总执行次数
        :type total_count: int
        :param top_state_duration_list: 当前模板下状态持续时间长TOP会话列表
        :type top_state_duration_list: list[:class:`huaweicloudsdkdas.v3.ShowAnalysisSessionResultRespTopStateDuration`]
        :param top_transaction_duration_list: 当前模板下事务持续时间长TOP会话列表
        :type top_transaction_duration_list: list[:class:`huaweicloudsdkdas.v3.ShowAnalysisSessionResultRespTopStateDuration`]
        """
        
        

        self._sql_template = None
        self._database_name = None
        self._total_count = None
        self._top_state_duration_list = None
        self._top_transaction_duration_list = None
        self.discriminator = None

        self.sql_template = sql_template
        self.database_name = database_name
        self.total_count = total_count
        self.top_state_duration_list = top_state_duration_list
        self.top_transaction_duration_list = top_transaction_duration_list

    @property
    def sql_template(self):
        r"""Gets the sql_template of this ShowAnalysisSessionResultRespSqlTemplates.

        SQL模板

        :return: The sql_template of this ShowAnalysisSessionResultRespSqlTemplates.
        :rtype: str
        """
        return self._sql_template

    @sql_template.setter
    def sql_template(self, sql_template):
        r"""Sets the sql_template of this ShowAnalysisSessionResultRespSqlTemplates.

        SQL模板

        :param sql_template: The sql_template of this ShowAnalysisSessionResultRespSqlTemplates.
        :type sql_template: str
        """
        self._sql_template = sql_template

    @property
    def database_name(self):
        r"""Gets the database_name of this ShowAnalysisSessionResultRespSqlTemplates.

        数据库名

        :return: The database_name of this ShowAnalysisSessionResultRespSqlTemplates.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this ShowAnalysisSessionResultRespSqlTemplates.

        数据库名

        :param database_name: The database_name of this ShowAnalysisSessionResultRespSqlTemplates.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def total_count(self):
        r"""Gets the total_count of this ShowAnalysisSessionResultRespSqlTemplates.

        总执行次数

        :return: The total_count of this ShowAnalysisSessionResultRespSqlTemplates.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ShowAnalysisSessionResultRespSqlTemplates.

        总执行次数

        :param total_count: The total_count of this ShowAnalysisSessionResultRespSqlTemplates.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def top_state_duration_list(self):
        r"""Gets the top_state_duration_list of this ShowAnalysisSessionResultRespSqlTemplates.

        当前模板下状态持续时间长TOP会话列表

        :return: The top_state_duration_list of this ShowAnalysisSessionResultRespSqlTemplates.
        :rtype: list[:class:`huaweicloudsdkdas.v3.ShowAnalysisSessionResultRespTopStateDuration`]
        """
        return self._top_state_duration_list

    @top_state_duration_list.setter
    def top_state_duration_list(self, top_state_duration_list):
        r"""Sets the top_state_duration_list of this ShowAnalysisSessionResultRespSqlTemplates.

        当前模板下状态持续时间长TOP会话列表

        :param top_state_duration_list: The top_state_duration_list of this ShowAnalysisSessionResultRespSqlTemplates.
        :type top_state_duration_list: list[:class:`huaweicloudsdkdas.v3.ShowAnalysisSessionResultRespTopStateDuration`]
        """
        self._top_state_duration_list = top_state_duration_list

    @property
    def top_transaction_duration_list(self):
        r"""Gets the top_transaction_duration_list of this ShowAnalysisSessionResultRespSqlTemplates.

        当前模板下事务持续时间长TOP会话列表

        :return: The top_transaction_duration_list of this ShowAnalysisSessionResultRespSqlTemplates.
        :rtype: list[:class:`huaweicloudsdkdas.v3.ShowAnalysisSessionResultRespTopStateDuration`]
        """
        return self._top_transaction_duration_list

    @top_transaction_duration_list.setter
    def top_transaction_duration_list(self, top_transaction_duration_list):
        r"""Sets the top_transaction_duration_list of this ShowAnalysisSessionResultRespSqlTemplates.

        当前模板下事务持续时间长TOP会话列表

        :param top_transaction_duration_list: The top_transaction_duration_list of this ShowAnalysisSessionResultRespSqlTemplates.
        :type top_transaction_duration_list: list[:class:`huaweicloudsdkdas.v3.ShowAnalysisSessionResultRespTopStateDuration`]
        """
        self._top_transaction_duration_list = top_transaction_duration_list

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
        if not isinstance(other, ShowAnalysisSessionResultRespSqlTemplates):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
