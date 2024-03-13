# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDockingJobResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'basic_info': 'DrugJobDto',
        'receptors': 'list[DockingReceptorDto]',
        'ligands': 'list[LigandDto]',
        'job_result': 'JobResult',
        'part_failed_reason': 'list[FailedReasonRecord]',
        'cluster_result': 'ClusterJobRsp'
    }

    attribute_map = {
        'basic_info': 'basic_info',
        'receptors': 'receptors',
        'ligands': 'ligands',
        'job_result': 'job_result',
        'part_failed_reason': 'part_failed_reason',
        'cluster_result': 'cluster_result'
    }

    def __init__(self, basic_info=None, receptors=None, ligands=None, job_result=None, part_failed_reason=None, cluster_result=None):
        """ShowDockingJobResponse

        The model defined in huaweicloud sdk

        :param basic_info: 
        :type basic_info: :class:`huaweicloudsdkeihealth.v1.DrugJobDto`
        :param receptors: 受体文件列表
        :type receptors: list[:class:`huaweicloudsdkeihealth.v1.DockingReceptorDto`]
        :param ligands: 配体文件列表，当前仅支持1个
        :type ligands: list[:class:`huaweicloudsdkeihealth.v1.LigandDto`]
        :param job_result: 
        :type job_result: :class:`huaweicloudsdkeihealth.v1.JobResult`
        :param part_failed_reason: 部分失败原因和数量
        :type part_failed_reason: list[:class:`huaweicloudsdkeihealth.v1.FailedReasonRecord`]
        :param cluster_result: 
        :type cluster_result: :class:`huaweicloudsdkeihealth.v1.ClusterJobRsp`
        """
        
        super(ShowDockingJobResponse, self).__init__()

        self._basic_info = None
        self._receptors = None
        self._ligands = None
        self._job_result = None
        self._part_failed_reason = None
        self._cluster_result = None
        self.discriminator = None

        if basic_info is not None:
            self.basic_info = basic_info
        if receptors is not None:
            self.receptors = receptors
        if ligands is not None:
            self.ligands = ligands
        if job_result is not None:
            self.job_result = job_result
        if part_failed_reason is not None:
            self.part_failed_reason = part_failed_reason
        if cluster_result is not None:
            self.cluster_result = cluster_result

    @property
    def basic_info(self):
        """Gets the basic_info of this ShowDockingJobResponse.

        :return: The basic_info of this ShowDockingJobResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.DrugJobDto`
        """
        return self._basic_info

    @basic_info.setter
    def basic_info(self, basic_info):
        """Sets the basic_info of this ShowDockingJobResponse.

        :param basic_info: The basic_info of this ShowDockingJobResponse.
        :type basic_info: :class:`huaweicloudsdkeihealth.v1.DrugJobDto`
        """
        self._basic_info = basic_info

    @property
    def receptors(self):
        """Gets the receptors of this ShowDockingJobResponse.

        受体文件列表

        :return: The receptors of this ShowDockingJobResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.DockingReceptorDto`]
        """
        return self._receptors

    @receptors.setter
    def receptors(self, receptors):
        """Sets the receptors of this ShowDockingJobResponse.

        受体文件列表

        :param receptors: The receptors of this ShowDockingJobResponse.
        :type receptors: list[:class:`huaweicloudsdkeihealth.v1.DockingReceptorDto`]
        """
        self._receptors = receptors

    @property
    def ligands(self):
        """Gets the ligands of this ShowDockingJobResponse.

        配体文件列表，当前仅支持1个

        :return: The ligands of this ShowDockingJobResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.LigandDto`]
        """
        return self._ligands

    @ligands.setter
    def ligands(self, ligands):
        """Sets the ligands of this ShowDockingJobResponse.

        配体文件列表，当前仅支持1个

        :param ligands: The ligands of this ShowDockingJobResponse.
        :type ligands: list[:class:`huaweicloudsdkeihealth.v1.LigandDto`]
        """
        self._ligands = ligands

    @property
    def job_result(self):
        """Gets the job_result of this ShowDockingJobResponse.

        :return: The job_result of this ShowDockingJobResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.JobResult`
        """
        return self._job_result

    @job_result.setter
    def job_result(self, job_result):
        """Sets the job_result of this ShowDockingJobResponse.

        :param job_result: The job_result of this ShowDockingJobResponse.
        :type job_result: :class:`huaweicloudsdkeihealth.v1.JobResult`
        """
        self._job_result = job_result

    @property
    def part_failed_reason(self):
        """Gets the part_failed_reason of this ShowDockingJobResponse.

        部分失败原因和数量

        :return: The part_failed_reason of this ShowDockingJobResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.FailedReasonRecord`]
        """
        return self._part_failed_reason

    @part_failed_reason.setter
    def part_failed_reason(self, part_failed_reason):
        """Sets the part_failed_reason of this ShowDockingJobResponse.

        部分失败原因和数量

        :param part_failed_reason: The part_failed_reason of this ShowDockingJobResponse.
        :type part_failed_reason: list[:class:`huaweicloudsdkeihealth.v1.FailedReasonRecord`]
        """
        self._part_failed_reason = part_failed_reason

    @property
    def cluster_result(self):
        """Gets the cluster_result of this ShowDockingJobResponse.

        :return: The cluster_result of this ShowDockingJobResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.ClusterJobRsp`
        """
        return self._cluster_result

    @cluster_result.setter
    def cluster_result(self, cluster_result):
        """Sets the cluster_result of this ShowDockingJobResponse.

        :param cluster_result: The cluster_result of this ShowDockingJobResponse.
        :type cluster_result: :class:`huaweicloudsdkeihealth.v1.ClusterJobRsp`
        """
        self._cluster_result = cluster_result

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
        if not isinstance(other, ShowDockingJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
