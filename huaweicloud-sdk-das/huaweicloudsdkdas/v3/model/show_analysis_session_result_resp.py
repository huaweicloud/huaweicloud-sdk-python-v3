# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAnalysisSessionResultResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'top_state_duration': 'list[ShowAnalysisSessionResultRespTopStateDuration]',
        'top_transaction_duration': 'list[ShowAnalysisSessionResultRespTopTransactionDuration]',
        'sql_templates': 'list[ShowAnalysisSessionResultRespSqlTemplates]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'top_state_duration': 'top_state_duration',
        'top_transaction_duration': 'top_transaction_duration',
        'sql_templates': 'sql_templates'
    }

    def __init__(self, total_count=None, top_state_duration=None, top_transaction_duration=None, sql_templates=None):
        r"""ShowAnalysisSessionResultResp

        The model defined in huaweicloud sdk

        :param total_count: 分析的会话总数
        :type total_count: int
        :param top_state_duration: 状态持续时间长TOP会话列表
        :type top_state_duration: list[:class:`huaweicloudsdkdas.v3.ShowAnalysisSessionResultRespTopStateDuration`]
        :param top_transaction_duration: 事务持续时间长TOP会话列表
        :type top_transaction_duration: list[:class:`huaweicloudsdkdas.v3.ShowAnalysisSessionResultRespTopTransactionDuration`]
        :param sql_templates: SQL模板列表
        :type sql_templates: list[:class:`huaweicloudsdkdas.v3.ShowAnalysisSessionResultRespSqlTemplates`]
        """
        
        

        self._total_count = None
        self._top_state_duration = None
        self._top_transaction_duration = None
        self._sql_templates = None
        self.discriminator = None

        self.total_count = total_count
        self.top_state_duration = top_state_duration
        self.top_transaction_duration = top_transaction_duration
        self.sql_templates = sql_templates

    @property
    def total_count(self):
        r"""Gets the total_count of this ShowAnalysisSessionResultResp.

        分析的会话总数

        :return: The total_count of this ShowAnalysisSessionResultResp.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ShowAnalysisSessionResultResp.

        分析的会话总数

        :param total_count: The total_count of this ShowAnalysisSessionResultResp.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def top_state_duration(self):
        r"""Gets the top_state_duration of this ShowAnalysisSessionResultResp.

        状态持续时间长TOP会话列表

        :return: The top_state_duration of this ShowAnalysisSessionResultResp.
        :rtype: list[:class:`huaweicloudsdkdas.v3.ShowAnalysisSessionResultRespTopStateDuration`]
        """
        return self._top_state_duration

    @top_state_duration.setter
    def top_state_duration(self, top_state_duration):
        r"""Sets the top_state_duration of this ShowAnalysisSessionResultResp.

        状态持续时间长TOP会话列表

        :param top_state_duration: The top_state_duration of this ShowAnalysisSessionResultResp.
        :type top_state_duration: list[:class:`huaweicloudsdkdas.v3.ShowAnalysisSessionResultRespTopStateDuration`]
        """
        self._top_state_duration = top_state_duration

    @property
    def top_transaction_duration(self):
        r"""Gets the top_transaction_duration of this ShowAnalysisSessionResultResp.

        事务持续时间长TOP会话列表

        :return: The top_transaction_duration of this ShowAnalysisSessionResultResp.
        :rtype: list[:class:`huaweicloudsdkdas.v3.ShowAnalysisSessionResultRespTopTransactionDuration`]
        """
        return self._top_transaction_duration

    @top_transaction_duration.setter
    def top_transaction_duration(self, top_transaction_duration):
        r"""Sets the top_transaction_duration of this ShowAnalysisSessionResultResp.

        事务持续时间长TOP会话列表

        :param top_transaction_duration: The top_transaction_duration of this ShowAnalysisSessionResultResp.
        :type top_transaction_duration: list[:class:`huaweicloudsdkdas.v3.ShowAnalysisSessionResultRespTopTransactionDuration`]
        """
        self._top_transaction_duration = top_transaction_duration

    @property
    def sql_templates(self):
        r"""Gets the sql_templates of this ShowAnalysisSessionResultResp.

        SQL模板列表

        :return: The sql_templates of this ShowAnalysisSessionResultResp.
        :rtype: list[:class:`huaweicloudsdkdas.v3.ShowAnalysisSessionResultRespSqlTemplates`]
        """
        return self._sql_templates

    @sql_templates.setter
    def sql_templates(self, sql_templates):
        r"""Sets the sql_templates of this ShowAnalysisSessionResultResp.

        SQL模板列表

        :param sql_templates: The sql_templates of this ShowAnalysisSessionResultResp.
        :type sql_templates: list[:class:`huaweicloudsdkdas.v3.ShowAnalysisSessionResultRespSqlTemplates`]
        """
        self._sql_templates = sql_templates

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
        if not isinstance(other, ShowAnalysisSessionResultResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
