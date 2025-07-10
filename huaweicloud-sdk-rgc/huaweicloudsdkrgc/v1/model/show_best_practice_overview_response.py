# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBestPracticeOverviewResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_score': 'float',
        'detect_time': 'str',
        'organization_account': 'BestPracticeOverviewItem',
        'identity_permission': 'BestPracticeOverviewItem',
        'network_planning': 'BestPracticeOverviewItem',
        'compliance_audit': 'BestPracticeOverviewItem',
        'financial_governance': 'BestPracticeOverviewItem',
        'data_boundary': 'BestPracticeOverviewItem',
        'om_monitor': 'BestPracticeOverviewItem',
        'security_management': 'BestPracticeOverviewItem'
    }

    attribute_map = {
        'total_score': 'total_score',
        'detect_time': 'detect_time',
        'organization_account': 'organization_account',
        'identity_permission': 'identity_permission',
        'network_planning': 'network_planning',
        'compliance_audit': 'compliance_audit',
        'financial_governance': 'financial_governance',
        'data_boundary': 'data_boundary',
        'om_monitor': 'om_monitor',
        'security_management': 'security_management'
    }

    def __init__(self, total_score=None, detect_time=None, organization_account=None, identity_permission=None, network_planning=None, compliance_audit=None, financial_governance=None, data_boundary=None, om_monitor=None, security_management=None):
        r"""ShowBestPracticeOverviewResponse

        The model defined in huaweicloud sdk

        :param total_score: 总分数
        :type total_score: float
        :param detect_time: 检测完成时间
        :type detect_time: str
        :param organization_account: 
        :type organization_account: :class:`huaweicloudsdkrgc.v1.BestPracticeOverviewItem`
        :param identity_permission: 
        :type identity_permission: :class:`huaweicloudsdkrgc.v1.BestPracticeOverviewItem`
        :param network_planning: 
        :type network_planning: :class:`huaweicloudsdkrgc.v1.BestPracticeOverviewItem`
        :param compliance_audit: 
        :type compliance_audit: :class:`huaweicloudsdkrgc.v1.BestPracticeOverviewItem`
        :param financial_governance: 
        :type financial_governance: :class:`huaweicloudsdkrgc.v1.BestPracticeOverviewItem`
        :param data_boundary: 
        :type data_boundary: :class:`huaweicloudsdkrgc.v1.BestPracticeOverviewItem`
        :param om_monitor: 
        :type om_monitor: :class:`huaweicloudsdkrgc.v1.BestPracticeOverviewItem`
        :param security_management: 
        :type security_management: :class:`huaweicloudsdkrgc.v1.BestPracticeOverviewItem`
        """
        
        super(ShowBestPracticeOverviewResponse, self).__init__()

        self._total_score = None
        self._detect_time = None
        self._organization_account = None
        self._identity_permission = None
        self._network_planning = None
        self._compliance_audit = None
        self._financial_governance = None
        self._data_boundary = None
        self._om_monitor = None
        self._security_management = None
        self.discriminator = None

        if total_score is not None:
            self.total_score = total_score
        if detect_time is not None:
            self.detect_time = detect_time
        if organization_account is not None:
            self.organization_account = organization_account
        if identity_permission is not None:
            self.identity_permission = identity_permission
        if network_planning is not None:
            self.network_planning = network_planning
        if compliance_audit is not None:
            self.compliance_audit = compliance_audit
        if financial_governance is not None:
            self.financial_governance = financial_governance
        if data_boundary is not None:
            self.data_boundary = data_boundary
        if om_monitor is not None:
            self.om_monitor = om_monitor
        if security_management is not None:
            self.security_management = security_management

    @property
    def total_score(self):
        r"""Gets the total_score of this ShowBestPracticeOverviewResponse.

        总分数

        :return: The total_score of this ShowBestPracticeOverviewResponse.
        :rtype: float
        """
        return self._total_score

    @total_score.setter
    def total_score(self, total_score):
        r"""Sets the total_score of this ShowBestPracticeOverviewResponse.

        总分数

        :param total_score: The total_score of this ShowBestPracticeOverviewResponse.
        :type total_score: float
        """
        self._total_score = total_score

    @property
    def detect_time(self):
        r"""Gets the detect_time of this ShowBestPracticeOverviewResponse.

        检测完成时间

        :return: The detect_time of this ShowBestPracticeOverviewResponse.
        :rtype: str
        """
        return self._detect_time

    @detect_time.setter
    def detect_time(self, detect_time):
        r"""Sets the detect_time of this ShowBestPracticeOverviewResponse.

        检测完成时间

        :param detect_time: The detect_time of this ShowBestPracticeOverviewResponse.
        :type detect_time: str
        """
        self._detect_time = detect_time

    @property
    def organization_account(self):
        r"""Gets the organization_account of this ShowBestPracticeOverviewResponse.

        :return: The organization_account of this ShowBestPracticeOverviewResponse.
        :rtype: :class:`huaweicloudsdkrgc.v1.BestPracticeOverviewItem`
        """
        return self._organization_account

    @organization_account.setter
    def organization_account(self, organization_account):
        r"""Sets the organization_account of this ShowBestPracticeOverviewResponse.

        :param organization_account: The organization_account of this ShowBestPracticeOverviewResponse.
        :type organization_account: :class:`huaweicloudsdkrgc.v1.BestPracticeOverviewItem`
        """
        self._organization_account = organization_account

    @property
    def identity_permission(self):
        r"""Gets the identity_permission of this ShowBestPracticeOverviewResponse.

        :return: The identity_permission of this ShowBestPracticeOverviewResponse.
        :rtype: :class:`huaweicloudsdkrgc.v1.BestPracticeOverviewItem`
        """
        return self._identity_permission

    @identity_permission.setter
    def identity_permission(self, identity_permission):
        r"""Sets the identity_permission of this ShowBestPracticeOverviewResponse.

        :param identity_permission: The identity_permission of this ShowBestPracticeOverviewResponse.
        :type identity_permission: :class:`huaweicloudsdkrgc.v1.BestPracticeOverviewItem`
        """
        self._identity_permission = identity_permission

    @property
    def network_planning(self):
        r"""Gets the network_planning of this ShowBestPracticeOverviewResponse.

        :return: The network_planning of this ShowBestPracticeOverviewResponse.
        :rtype: :class:`huaweicloudsdkrgc.v1.BestPracticeOverviewItem`
        """
        return self._network_planning

    @network_planning.setter
    def network_planning(self, network_planning):
        r"""Sets the network_planning of this ShowBestPracticeOverviewResponse.

        :param network_planning: The network_planning of this ShowBestPracticeOverviewResponse.
        :type network_planning: :class:`huaweicloudsdkrgc.v1.BestPracticeOverviewItem`
        """
        self._network_planning = network_planning

    @property
    def compliance_audit(self):
        r"""Gets the compliance_audit of this ShowBestPracticeOverviewResponse.

        :return: The compliance_audit of this ShowBestPracticeOverviewResponse.
        :rtype: :class:`huaweicloudsdkrgc.v1.BestPracticeOverviewItem`
        """
        return self._compliance_audit

    @compliance_audit.setter
    def compliance_audit(self, compliance_audit):
        r"""Sets the compliance_audit of this ShowBestPracticeOverviewResponse.

        :param compliance_audit: The compliance_audit of this ShowBestPracticeOverviewResponse.
        :type compliance_audit: :class:`huaweicloudsdkrgc.v1.BestPracticeOverviewItem`
        """
        self._compliance_audit = compliance_audit

    @property
    def financial_governance(self):
        r"""Gets the financial_governance of this ShowBestPracticeOverviewResponse.

        :return: The financial_governance of this ShowBestPracticeOverviewResponse.
        :rtype: :class:`huaweicloudsdkrgc.v1.BestPracticeOverviewItem`
        """
        return self._financial_governance

    @financial_governance.setter
    def financial_governance(self, financial_governance):
        r"""Sets the financial_governance of this ShowBestPracticeOverviewResponse.

        :param financial_governance: The financial_governance of this ShowBestPracticeOverviewResponse.
        :type financial_governance: :class:`huaweicloudsdkrgc.v1.BestPracticeOverviewItem`
        """
        self._financial_governance = financial_governance

    @property
    def data_boundary(self):
        r"""Gets the data_boundary of this ShowBestPracticeOverviewResponse.

        :return: The data_boundary of this ShowBestPracticeOverviewResponse.
        :rtype: :class:`huaweicloudsdkrgc.v1.BestPracticeOverviewItem`
        """
        return self._data_boundary

    @data_boundary.setter
    def data_boundary(self, data_boundary):
        r"""Sets the data_boundary of this ShowBestPracticeOverviewResponse.

        :param data_boundary: The data_boundary of this ShowBestPracticeOverviewResponse.
        :type data_boundary: :class:`huaweicloudsdkrgc.v1.BestPracticeOverviewItem`
        """
        self._data_boundary = data_boundary

    @property
    def om_monitor(self):
        r"""Gets the om_monitor of this ShowBestPracticeOverviewResponse.

        :return: The om_monitor of this ShowBestPracticeOverviewResponse.
        :rtype: :class:`huaweicloudsdkrgc.v1.BestPracticeOverviewItem`
        """
        return self._om_monitor

    @om_monitor.setter
    def om_monitor(self, om_monitor):
        r"""Sets the om_monitor of this ShowBestPracticeOverviewResponse.

        :param om_monitor: The om_monitor of this ShowBestPracticeOverviewResponse.
        :type om_monitor: :class:`huaweicloudsdkrgc.v1.BestPracticeOverviewItem`
        """
        self._om_monitor = om_monitor

    @property
    def security_management(self):
        r"""Gets the security_management of this ShowBestPracticeOverviewResponse.

        :return: The security_management of this ShowBestPracticeOverviewResponse.
        :rtype: :class:`huaweicloudsdkrgc.v1.BestPracticeOverviewItem`
        """
        return self._security_management

    @security_management.setter
    def security_management(self, security_management):
        r"""Sets the security_management of this ShowBestPracticeOverviewResponse.

        :param security_management: The security_management of this ShowBestPracticeOverviewResponse.
        :type security_management: :class:`huaweicloudsdkrgc.v1.BestPracticeOverviewItem`
        """
        self._security_management = security_management

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
        if not isinstance(other, ShowBestPracticeOverviewResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
