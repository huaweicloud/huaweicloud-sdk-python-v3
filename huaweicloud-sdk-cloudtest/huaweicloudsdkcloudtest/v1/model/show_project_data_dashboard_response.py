# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowProjectDataDashboardResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'defect': 'DefectVo',
        'case_pass_rate': 'CasePassRateVo',
        'case_completion_rate': 'CaseCompletionRateVo',
        'project_type': 'str',
        'issue_cover_rate': 'IssueCoverRateVo'
    }

    attribute_map = {
        'defect': 'defect',
        'case_pass_rate': 'case_pass_rate',
        'case_completion_rate': 'case_completion_rate',
        'project_type': 'project_type',
        'issue_cover_rate': 'issue_cover_rate'
    }

    def __init__(self, defect=None, case_pass_rate=None, case_completion_rate=None, project_type=None, issue_cover_rate=None):
        r"""ShowProjectDataDashboardResponse

        The model defined in huaweicloud sdk

        :param defect: 
        :type defect: :class:`huaweicloudsdkcloudtest.v1.DefectVo`
        :param case_pass_rate: 
        :type case_pass_rate: :class:`huaweicloudsdkcloudtest.v1.CasePassRateVo`
        :param case_completion_rate: 
        :type case_completion_rate: :class:`huaweicloudsdkcloudtest.v1.CaseCompletionRateVo`
        :param project_type: 项目类型
        :type project_type: str
        :param issue_cover_rate: 
        :type issue_cover_rate: :class:`huaweicloudsdkcloudtest.v1.IssueCoverRateVo`
        """
        
        super(ShowProjectDataDashboardResponse, self).__init__()

        self._defect = None
        self._case_pass_rate = None
        self._case_completion_rate = None
        self._project_type = None
        self._issue_cover_rate = None
        self.discriminator = None

        if defect is not None:
            self.defect = defect
        if case_pass_rate is not None:
            self.case_pass_rate = case_pass_rate
        if case_completion_rate is not None:
            self.case_completion_rate = case_completion_rate
        if project_type is not None:
            self.project_type = project_type
        if issue_cover_rate is not None:
            self.issue_cover_rate = issue_cover_rate

    @property
    def defect(self):
        r"""Gets the defect of this ShowProjectDataDashboardResponse.

        :return: The defect of this ShowProjectDataDashboardResponse.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.DefectVo`
        """
        return self._defect

    @defect.setter
    def defect(self, defect):
        r"""Sets the defect of this ShowProjectDataDashboardResponse.

        :param defect: The defect of this ShowProjectDataDashboardResponse.
        :type defect: :class:`huaweicloudsdkcloudtest.v1.DefectVo`
        """
        self._defect = defect

    @property
    def case_pass_rate(self):
        r"""Gets the case_pass_rate of this ShowProjectDataDashboardResponse.

        :return: The case_pass_rate of this ShowProjectDataDashboardResponse.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.CasePassRateVo`
        """
        return self._case_pass_rate

    @case_pass_rate.setter
    def case_pass_rate(self, case_pass_rate):
        r"""Sets the case_pass_rate of this ShowProjectDataDashboardResponse.

        :param case_pass_rate: The case_pass_rate of this ShowProjectDataDashboardResponse.
        :type case_pass_rate: :class:`huaweicloudsdkcloudtest.v1.CasePassRateVo`
        """
        self._case_pass_rate = case_pass_rate

    @property
    def case_completion_rate(self):
        r"""Gets the case_completion_rate of this ShowProjectDataDashboardResponse.

        :return: The case_completion_rate of this ShowProjectDataDashboardResponse.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.CaseCompletionRateVo`
        """
        return self._case_completion_rate

    @case_completion_rate.setter
    def case_completion_rate(self, case_completion_rate):
        r"""Sets the case_completion_rate of this ShowProjectDataDashboardResponse.

        :param case_completion_rate: The case_completion_rate of this ShowProjectDataDashboardResponse.
        :type case_completion_rate: :class:`huaweicloudsdkcloudtest.v1.CaseCompletionRateVo`
        """
        self._case_completion_rate = case_completion_rate

    @property
    def project_type(self):
        r"""Gets the project_type of this ShowProjectDataDashboardResponse.

        项目类型

        :return: The project_type of this ShowProjectDataDashboardResponse.
        :rtype: str
        """
        return self._project_type

    @project_type.setter
    def project_type(self, project_type):
        r"""Sets the project_type of this ShowProjectDataDashboardResponse.

        项目类型

        :param project_type: The project_type of this ShowProjectDataDashboardResponse.
        :type project_type: str
        """
        self._project_type = project_type

    @property
    def issue_cover_rate(self):
        r"""Gets the issue_cover_rate of this ShowProjectDataDashboardResponse.

        :return: The issue_cover_rate of this ShowProjectDataDashboardResponse.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.IssueCoverRateVo`
        """
        return self._issue_cover_rate

    @issue_cover_rate.setter
    def issue_cover_rate(self, issue_cover_rate):
        r"""Sets the issue_cover_rate of this ShowProjectDataDashboardResponse.

        :param issue_cover_rate: The issue_cover_rate of this ShowProjectDataDashboardResponse.
        :type issue_cover_rate: :class:`huaweicloudsdkcloudtest.v1.IssueCoverRateVo`
        """
        self._issue_cover_rate = issue_cover_rate

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
        if not isinstance(other, ShowProjectDataDashboardResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
