# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAuditSummaryInfosResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'audit_duration': 'int',
        'total_sql': 'int',
        'total_risk': 'int',
        'today_sql': 'int',
        'today_risk': 'int',
        'today_session': 'int',
        'update_time': 'int',
        'data_list': 'list[AuditSummaryResponseDataList]',
        'total': 'int'
    }

    attribute_map = {
        'project_id': 'project_id',
        'audit_duration': 'audit_duration',
        'total_sql': 'total_sql',
        'total_risk': 'total_risk',
        'today_sql': 'today_sql',
        'today_risk': 'today_risk',
        'today_session': 'today_session',
        'update_time': 'update_time',
        'data_list': 'data_list',
        'total': 'total'
    }

    def __init__(self, project_id=None, audit_duration=None, total_sql=None, total_risk=None, today_sql=None, today_risk=None, today_session=None, update_time=None, data_list=None, total=None):
        r"""ListAuditSummaryInfosResponse

        The model defined in huaweicloud sdk

        :param project_id: 项目ID
        :type project_id: str
        :param audit_duration: 审计总时长
        :type audit_duration: int
        :param total_sql: 语句总量
        :type total_sql: int
        :param total_risk: 风险总量
        :type total_risk: int
        :param today_sql: 今日语句
        :type today_sql: int
        :param today_risk: 今日风险
        :type today_risk: int
        :param today_session: 今日会话
        :type today_session: int
        :param update_time: 更新时间
        :type update_time: int
        :param data_list: 列表信息
        :type data_list: list[:class:`huaweicloudsdkdbss.v1.AuditSummaryResponseDataList`]
        :param total: 总数
        :type total: int
        """
        
        super(ListAuditSummaryInfosResponse, self).__init__()

        self._project_id = None
        self._audit_duration = None
        self._total_sql = None
        self._total_risk = None
        self._today_sql = None
        self._today_risk = None
        self._today_session = None
        self._update_time = None
        self._data_list = None
        self._total = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        if audit_duration is not None:
            self.audit_duration = audit_duration
        if total_sql is not None:
            self.total_sql = total_sql
        if total_risk is not None:
            self.total_risk = total_risk
        if today_sql is not None:
            self.today_sql = today_sql
        if today_risk is not None:
            self.today_risk = today_risk
        if today_session is not None:
            self.today_session = today_session
        if update_time is not None:
            self.update_time = update_time
        if data_list is not None:
            self.data_list = data_list
        if total is not None:
            self.total = total

    @property
    def project_id(self):
        r"""Gets the project_id of this ListAuditSummaryInfosResponse.

        项目ID

        :return: The project_id of this ListAuditSummaryInfosResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListAuditSummaryInfosResponse.

        项目ID

        :param project_id: The project_id of this ListAuditSummaryInfosResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def audit_duration(self):
        r"""Gets the audit_duration of this ListAuditSummaryInfosResponse.

        审计总时长

        :return: The audit_duration of this ListAuditSummaryInfosResponse.
        :rtype: int
        """
        return self._audit_duration

    @audit_duration.setter
    def audit_duration(self, audit_duration):
        r"""Sets the audit_duration of this ListAuditSummaryInfosResponse.

        审计总时长

        :param audit_duration: The audit_duration of this ListAuditSummaryInfosResponse.
        :type audit_duration: int
        """
        self._audit_duration = audit_duration

    @property
    def total_sql(self):
        r"""Gets the total_sql of this ListAuditSummaryInfosResponse.

        语句总量

        :return: The total_sql of this ListAuditSummaryInfosResponse.
        :rtype: int
        """
        return self._total_sql

    @total_sql.setter
    def total_sql(self, total_sql):
        r"""Sets the total_sql of this ListAuditSummaryInfosResponse.

        语句总量

        :param total_sql: The total_sql of this ListAuditSummaryInfosResponse.
        :type total_sql: int
        """
        self._total_sql = total_sql

    @property
    def total_risk(self):
        r"""Gets the total_risk of this ListAuditSummaryInfosResponse.

        风险总量

        :return: The total_risk of this ListAuditSummaryInfosResponse.
        :rtype: int
        """
        return self._total_risk

    @total_risk.setter
    def total_risk(self, total_risk):
        r"""Sets the total_risk of this ListAuditSummaryInfosResponse.

        风险总量

        :param total_risk: The total_risk of this ListAuditSummaryInfosResponse.
        :type total_risk: int
        """
        self._total_risk = total_risk

    @property
    def today_sql(self):
        r"""Gets the today_sql of this ListAuditSummaryInfosResponse.

        今日语句

        :return: The today_sql of this ListAuditSummaryInfosResponse.
        :rtype: int
        """
        return self._today_sql

    @today_sql.setter
    def today_sql(self, today_sql):
        r"""Sets the today_sql of this ListAuditSummaryInfosResponse.

        今日语句

        :param today_sql: The today_sql of this ListAuditSummaryInfosResponse.
        :type today_sql: int
        """
        self._today_sql = today_sql

    @property
    def today_risk(self):
        r"""Gets the today_risk of this ListAuditSummaryInfosResponse.

        今日风险

        :return: The today_risk of this ListAuditSummaryInfosResponse.
        :rtype: int
        """
        return self._today_risk

    @today_risk.setter
    def today_risk(self, today_risk):
        r"""Sets the today_risk of this ListAuditSummaryInfosResponse.

        今日风险

        :param today_risk: The today_risk of this ListAuditSummaryInfosResponse.
        :type today_risk: int
        """
        self._today_risk = today_risk

    @property
    def today_session(self):
        r"""Gets the today_session of this ListAuditSummaryInfosResponse.

        今日会话

        :return: The today_session of this ListAuditSummaryInfosResponse.
        :rtype: int
        """
        return self._today_session

    @today_session.setter
    def today_session(self, today_session):
        r"""Sets the today_session of this ListAuditSummaryInfosResponse.

        今日会话

        :param today_session: The today_session of this ListAuditSummaryInfosResponse.
        :type today_session: int
        """
        self._today_session = today_session

    @property
    def update_time(self):
        r"""Gets the update_time of this ListAuditSummaryInfosResponse.

        更新时间

        :return: The update_time of this ListAuditSummaryInfosResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ListAuditSummaryInfosResponse.

        更新时间

        :param update_time: The update_time of this ListAuditSummaryInfosResponse.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def data_list(self):
        r"""Gets the data_list of this ListAuditSummaryInfosResponse.

        列表信息

        :return: The data_list of this ListAuditSummaryInfosResponse.
        :rtype: list[:class:`huaweicloudsdkdbss.v1.AuditSummaryResponseDataList`]
        """
        return self._data_list

    @data_list.setter
    def data_list(self, data_list):
        r"""Sets the data_list of this ListAuditSummaryInfosResponse.

        列表信息

        :param data_list: The data_list of this ListAuditSummaryInfosResponse.
        :type data_list: list[:class:`huaweicloudsdkdbss.v1.AuditSummaryResponseDataList`]
        """
        self._data_list = data_list

    @property
    def total(self):
        r"""Gets the total of this ListAuditSummaryInfosResponse.

        总数

        :return: The total of this ListAuditSummaryInfosResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListAuditSummaryInfosResponse.

        总数

        :param total: The total of this ListAuditSummaryInfosResponse.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, ListAuditSummaryInfosResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
