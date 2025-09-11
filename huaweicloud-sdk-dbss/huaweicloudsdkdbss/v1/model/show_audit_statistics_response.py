# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAuditStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'db_risk_statistics': 'list[DatabaseRiskStatisticsDto]',
        'high_risk_total': 'int',
        'low_risk_total': 'int',
        'medium_risk_total': 'int',
        'project_id': 'str',
        'rule_risk_statistics': 'list[RuleRiskStatisticsDto]',
        'unsupported_audit_infos': 'UnSupportAuditInfoResponse',
        'update_time': 'int'
    }

    attribute_map = {
        'db_risk_statistics': 'db_risk_statistics',
        'high_risk_total': 'high_risk_total',
        'low_risk_total': 'low_risk_total',
        'medium_risk_total': 'medium_risk_total',
        'project_id': 'project_id',
        'rule_risk_statistics': 'rule_risk_statistics',
        'unsupported_audit_infos': 'unsupported_audit_infos',
        'update_time': 'update_time'
    }

    def __init__(self, db_risk_statistics=None, high_risk_total=None, low_risk_total=None, medium_risk_total=None, project_id=None, rule_risk_statistics=None, unsupported_audit_infos=None, update_time=None):
        r"""ShowAuditStatisticsResponse

        The model defined in huaweicloud sdk

        :param db_risk_statistics: 数据库风险统计
        :type db_risk_statistics: list[:class:`huaweicloudsdkdbss.v1.DatabaseRiskStatisticsDto`]
        :param high_risk_total: 高风险总量
        :type high_risk_total: int
        :param low_risk_total: 低风险总量
        :type low_risk_total: int
        :param medium_risk_total: 中风险总量
        :type medium_risk_total: int
        :param project_id: 项目ID
        :type project_id: str
        :param rule_risk_statistics: 风险规则统计
        :type rule_risk_statistics: list[:class:`huaweicloudsdkdbss.v1.RuleRiskStatisticsDto`]
        :param unsupported_audit_infos: 
        :type unsupported_audit_infos: :class:`huaweicloudsdkdbss.v1.UnSupportAuditInfoResponse`
        :param update_time: 更新时间
        :type update_time: int
        """
        
        super(ShowAuditStatisticsResponse, self).__init__()

        self._db_risk_statistics = None
        self._high_risk_total = None
        self._low_risk_total = None
        self._medium_risk_total = None
        self._project_id = None
        self._rule_risk_statistics = None
        self._unsupported_audit_infos = None
        self._update_time = None
        self.discriminator = None

        if db_risk_statistics is not None:
            self.db_risk_statistics = db_risk_statistics
        if high_risk_total is not None:
            self.high_risk_total = high_risk_total
        if low_risk_total is not None:
            self.low_risk_total = low_risk_total
        if medium_risk_total is not None:
            self.medium_risk_total = medium_risk_total
        if project_id is not None:
            self.project_id = project_id
        if rule_risk_statistics is not None:
            self.rule_risk_statistics = rule_risk_statistics
        if unsupported_audit_infos is not None:
            self.unsupported_audit_infos = unsupported_audit_infos
        if update_time is not None:
            self.update_time = update_time

    @property
    def db_risk_statistics(self):
        r"""Gets the db_risk_statistics of this ShowAuditStatisticsResponse.

        数据库风险统计

        :return: The db_risk_statistics of this ShowAuditStatisticsResponse.
        :rtype: list[:class:`huaweicloudsdkdbss.v1.DatabaseRiskStatisticsDto`]
        """
        return self._db_risk_statistics

    @db_risk_statistics.setter
    def db_risk_statistics(self, db_risk_statistics):
        r"""Sets the db_risk_statistics of this ShowAuditStatisticsResponse.

        数据库风险统计

        :param db_risk_statistics: The db_risk_statistics of this ShowAuditStatisticsResponse.
        :type db_risk_statistics: list[:class:`huaweicloudsdkdbss.v1.DatabaseRiskStatisticsDto`]
        """
        self._db_risk_statistics = db_risk_statistics

    @property
    def high_risk_total(self):
        r"""Gets the high_risk_total of this ShowAuditStatisticsResponse.

        高风险总量

        :return: The high_risk_total of this ShowAuditStatisticsResponse.
        :rtype: int
        """
        return self._high_risk_total

    @high_risk_total.setter
    def high_risk_total(self, high_risk_total):
        r"""Sets the high_risk_total of this ShowAuditStatisticsResponse.

        高风险总量

        :param high_risk_total: The high_risk_total of this ShowAuditStatisticsResponse.
        :type high_risk_total: int
        """
        self._high_risk_total = high_risk_total

    @property
    def low_risk_total(self):
        r"""Gets the low_risk_total of this ShowAuditStatisticsResponse.

        低风险总量

        :return: The low_risk_total of this ShowAuditStatisticsResponse.
        :rtype: int
        """
        return self._low_risk_total

    @low_risk_total.setter
    def low_risk_total(self, low_risk_total):
        r"""Sets the low_risk_total of this ShowAuditStatisticsResponse.

        低风险总量

        :param low_risk_total: The low_risk_total of this ShowAuditStatisticsResponse.
        :type low_risk_total: int
        """
        self._low_risk_total = low_risk_total

    @property
    def medium_risk_total(self):
        r"""Gets the medium_risk_total of this ShowAuditStatisticsResponse.

        中风险总量

        :return: The medium_risk_total of this ShowAuditStatisticsResponse.
        :rtype: int
        """
        return self._medium_risk_total

    @medium_risk_total.setter
    def medium_risk_total(self, medium_risk_total):
        r"""Sets the medium_risk_total of this ShowAuditStatisticsResponse.

        中风险总量

        :param medium_risk_total: The medium_risk_total of this ShowAuditStatisticsResponse.
        :type medium_risk_total: int
        """
        self._medium_risk_total = medium_risk_total

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowAuditStatisticsResponse.

        项目ID

        :return: The project_id of this ShowAuditStatisticsResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowAuditStatisticsResponse.

        项目ID

        :param project_id: The project_id of this ShowAuditStatisticsResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def rule_risk_statistics(self):
        r"""Gets the rule_risk_statistics of this ShowAuditStatisticsResponse.

        风险规则统计

        :return: The rule_risk_statistics of this ShowAuditStatisticsResponse.
        :rtype: list[:class:`huaweicloudsdkdbss.v1.RuleRiskStatisticsDto`]
        """
        return self._rule_risk_statistics

    @rule_risk_statistics.setter
    def rule_risk_statistics(self, rule_risk_statistics):
        r"""Sets the rule_risk_statistics of this ShowAuditStatisticsResponse.

        风险规则统计

        :param rule_risk_statistics: The rule_risk_statistics of this ShowAuditStatisticsResponse.
        :type rule_risk_statistics: list[:class:`huaweicloudsdkdbss.v1.RuleRiskStatisticsDto`]
        """
        self._rule_risk_statistics = rule_risk_statistics

    @property
    def unsupported_audit_infos(self):
        r"""Gets the unsupported_audit_infos of this ShowAuditStatisticsResponse.

        :return: The unsupported_audit_infos of this ShowAuditStatisticsResponse.
        :rtype: :class:`huaweicloudsdkdbss.v1.UnSupportAuditInfoResponse`
        """
        return self._unsupported_audit_infos

    @unsupported_audit_infos.setter
    def unsupported_audit_infos(self, unsupported_audit_infos):
        r"""Sets the unsupported_audit_infos of this ShowAuditStatisticsResponse.

        :param unsupported_audit_infos: The unsupported_audit_infos of this ShowAuditStatisticsResponse.
        :type unsupported_audit_infos: :class:`huaweicloudsdkdbss.v1.UnSupportAuditInfoResponse`
        """
        self._unsupported_audit_infos = unsupported_audit_infos

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowAuditStatisticsResponse.

        更新时间

        :return: The update_time of this ShowAuditStatisticsResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowAuditStatisticsResponse.

        更新时间

        :param update_time: The update_time of this ShowAuditStatisticsResponse.
        :type update_time: int
        """
        self._update_time = update_time

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
        if not isinstance(other, ShowAuditStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
