# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceReportResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_report_base_info': 'JobReportBaseInfoVo',
        'job_report_env': 'JobReportEnvVo',
        'job_report_output': 'JobReportOutputVo',
        'job_report_partners': 'list[JobReportPartnerVo]',
        'round_deploys': 'list[RoundDeployVo]'
    }

    attribute_map = {
        'job_report_base_info': 'job_report_base_info',
        'job_report_env': 'job_report_env',
        'job_report_output': 'job_report_output',
        'job_report_partners': 'job_report_partners',
        'round_deploys': 'round_deploys'
    }

    def __init__(self, job_report_base_info=None, job_report_env=None, job_report_output=None, job_report_partners=None, round_deploys=None):
        """ShowInstanceReportResponse

        The model defined in huaweicloud sdk

        :param job_report_base_info: 
        :type job_report_base_info: :class:`huaweicloudsdktics.v1.JobReportBaseInfoVo`
        :param job_report_env: 
        :type job_report_env: :class:`huaweicloudsdktics.v1.JobReportEnvVo`
        :param job_report_output: 
        :type job_report_output: :class:`huaweicloudsdktics.v1.JobReportOutputVo`
        :param job_report_partners: 合作方信息
        :type job_report_partners: list[:class:`huaweicloudsdktics.v1.JobReportPartnerVo`]
        :param round_deploys: 计算过程
        :type round_deploys: list[:class:`huaweicloudsdktics.v1.RoundDeployVo`]
        """
        
        super(ShowInstanceReportResponse, self).__init__()

        self._job_report_base_info = None
        self._job_report_env = None
        self._job_report_output = None
        self._job_report_partners = None
        self._round_deploys = None
        self.discriminator = None

        if job_report_base_info is not None:
            self.job_report_base_info = job_report_base_info
        if job_report_env is not None:
            self.job_report_env = job_report_env
        if job_report_output is not None:
            self.job_report_output = job_report_output
        if job_report_partners is not None:
            self.job_report_partners = job_report_partners
        if round_deploys is not None:
            self.round_deploys = round_deploys

    @property
    def job_report_base_info(self):
        """Gets the job_report_base_info of this ShowInstanceReportResponse.

        :return: The job_report_base_info of this ShowInstanceReportResponse.
        :rtype: :class:`huaweicloudsdktics.v1.JobReportBaseInfoVo`
        """
        return self._job_report_base_info

    @job_report_base_info.setter
    def job_report_base_info(self, job_report_base_info):
        """Sets the job_report_base_info of this ShowInstanceReportResponse.

        :param job_report_base_info: The job_report_base_info of this ShowInstanceReportResponse.
        :type job_report_base_info: :class:`huaweicloudsdktics.v1.JobReportBaseInfoVo`
        """
        self._job_report_base_info = job_report_base_info

    @property
    def job_report_env(self):
        """Gets the job_report_env of this ShowInstanceReportResponse.

        :return: The job_report_env of this ShowInstanceReportResponse.
        :rtype: :class:`huaweicloudsdktics.v1.JobReportEnvVo`
        """
        return self._job_report_env

    @job_report_env.setter
    def job_report_env(self, job_report_env):
        """Sets the job_report_env of this ShowInstanceReportResponse.

        :param job_report_env: The job_report_env of this ShowInstanceReportResponse.
        :type job_report_env: :class:`huaweicloudsdktics.v1.JobReportEnvVo`
        """
        self._job_report_env = job_report_env

    @property
    def job_report_output(self):
        """Gets the job_report_output of this ShowInstanceReportResponse.

        :return: The job_report_output of this ShowInstanceReportResponse.
        :rtype: :class:`huaweicloudsdktics.v1.JobReportOutputVo`
        """
        return self._job_report_output

    @job_report_output.setter
    def job_report_output(self, job_report_output):
        """Sets the job_report_output of this ShowInstanceReportResponse.

        :param job_report_output: The job_report_output of this ShowInstanceReportResponse.
        :type job_report_output: :class:`huaweicloudsdktics.v1.JobReportOutputVo`
        """
        self._job_report_output = job_report_output

    @property
    def job_report_partners(self):
        """Gets the job_report_partners of this ShowInstanceReportResponse.

        合作方信息

        :return: The job_report_partners of this ShowInstanceReportResponse.
        :rtype: list[:class:`huaweicloudsdktics.v1.JobReportPartnerVo`]
        """
        return self._job_report_partners

    @job_report_partners.setter
    def job_report_partners(self, job_report_partners):
        """Sets the job_report_partners of this ShowInstanceReportResponse.

        合作方信息

        :param job_report_partners: The job_report_partners of this ShowInstanceReportResponse.
        :type job_report_partners: list[:class:`huaweicloudsdktics.v1.JobReportPartnerVo`]
        """
        self._job_report_partners = job_report_partners

    @property
    def round_deploys(self):
        """Gets the round_deploys of this ShowInstanceReportResponse.

        计算过程

        :return: The round_deploys of this ShowInstanceReportResponse.
        :rtype: list[:class:`huaweicloudsdktics.v1.RoundDeployVo`]
        """
        return self._round_deploys

    @round_deploys.setter
    def round_deploys(self, round_deploys):
        """Sets the round_deploys of this ShowInstanceReportResponse.

        计算过程

        :param round_deploys: The round_deploys of this ShowInstanceReportResponse.
        :type round_deploys: list[:class:`huaweicloudsdktics.v1.RoundDeployVo`]
        """
        self._round_deploys = round_deploys

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
        if not isinstance(other, ShowInstanceReportResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
