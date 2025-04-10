# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAdmetJobResponse(SdkResponse):

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
        'molecule_file': 'MoleculeFileDto',
        'job_result': 'JobResult',
        'part_failed_reason': 'list[FailedReasonRecord]',
        'base_model': 'BaseModel',
        'models': 'list[BasicDrugModel]',
        'cluster_result': 'ClusterJobRsp',
        'save_fingerprint': 'bool'
    }

    attribute_map = {
        'basic_info': 'basic_info',
        'molecule_file': 'molecule_file',
        'job_result': 'job_result',
        'part_failed_reason': 'part_failed_reason',
        'base_model': 'base_model',
        'models': 'models',
        'cluster_result': 'cluster_result',
        'save_fingerprint': 'save_fingerprint'
    }

    def __init__(self, basic_info=None, molecule_file=None, job_result=None, part_failed_reason=None, base_model=None, models=None, cluster_result=None, save_fingerprint=None):
        r"""ShowAdmetJobResponse

        The model defined in huaweicloud sdk

        :param basic_info: 
        :type basic_info: :class:`huaweicloudsdkeihealth.v1.DrugJobDto`
        :param molecule_file: 
        :type molecule_file: :class:`huaweicloudsdkeihealth.v1.MoleculeFileDto`
        :param job_result: 
        :type job_result: :class:`huaweicloudsdkeihealth.v1.JobResult`
        :param part_failed_reason: 作业结果信息
        :type part_failed_reason: list[:class:`huaweicloudsdkeihealth.v1.FailedReasonRecord`]
        :param base_model: 
        :type base_model: :class:`huaweicloudsdkeihealth.v1.BaseModel`
        :param models: 模型信息
        :type models: list[:class:`huaweicloudsdkeihealth.v1.BasicDrugModel`]
        :param cluster_result: 
        :type cluster_result: :class:`huaweicloudsdkeihealth.v1.ClusterJobRsp`
        :param save_fingerprint: 是否输出表征
        :type save_fingerprint: bool
        """
        
        super(ShowAdmetJobResponse, self).__init__()

        self._basic_info = None
        self._molecule_file = None
        self._job_result = None
        self._part_failed_reason = None
        self._base_model = None
        self._models = None
        self._cluster_result = None
        self._save_fingerprint = None
        self.discriminator = None

        if basic_info is not None:
            self.basic_info = basic_info
        if molecule_file is not None:
            self.molecule_file = molecule_file
        if job_result is not None:
            self.job_result = job_result
        if part_failed_reason is not None:
            self.part_failed_reason = part_failed_reason
        if base_model is not None:
            self.base_model = base_model
        if models is not None:
            self.models = models
        if cluster_result is not None:
            self.cluster_result = cluster_result
        if save_fingerprint is not None:
            self.save_fingerprint = save_fingerprint

    @property
    def basic_info(self):
        r"""Gets the basic_info of this ShowAdmetJobResponse.

        :return: The basic_info of this ShowAdmetJobResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.DrugJobDto`
        """
        return self._basic_info

    @basic_info.setter
    def basic_info(self, basic_info):
        r"""Sets the basic_info of this ShowAdmetJobResponse.

        :param basic_info: The basic_info of this ShowAdmetJobResponse.
        :type basic_info: :class:`huaweicloudsdkeihealth.v1.DrugJobDto`
        """
        self._basic_info = basic_info

    @property
    def molecule_file(self):
        r"""Gets the molecule_file of this ShowAdmetJobResponse.

        :return: The molecule_file of this ShowAdmetJobResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.MoleculeFileDto`
        """
        return self._molecule_file

    @molecule_file.setter
    def molecule_file(self, molecule_file):
        r"""Sets the molecule_file of this ShowAdmetJobResponse.

        :param molecule_file: The molecule_file of this ShowAdmetJobResponse.
        :type molecule_file: :class:`huaweicloudsdkeihealth.v1.MoleculeFileDto`
        """
        self._molecule_file = molecule_file

    @property
    def job_result(self):
        r"""Gets the job_result of this ShowAdmetJobResponse.

        :return: The job_result of this ShowAdmetJobResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.JobResult`
        """
        return self._job_result

    @job_result.setter
    def job_result(self, job_result):
        r"""Sets the job_result of this ShowAdmetJobResponse.

        :param job_result: The job_result of this ShowAdmetJobResponse.
        :type job_result: :class:`huaweicloudsdkeihealth.v1.JobResult`
        """
        self._job_result = job_result

    @property
    def part_failed_reason(self):
        r"""Gets the part_failed_reason of this ShowAdmetJobResponse.

        作业结果信息

        :return: The part_failed_reason of this ShowAdmetJobResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.FailedReasonRecord`]
        """
        return self._part_failed_reason

    @part_failed_reason.setter
    def part_failed_reason(self, part_failed_reason):
        r"""Sets the part_failed_reason of this ShowAdmetJobResponse.

        作业结果信息

        :param part_failed_reason: The part_failed_reason of this ShowAdmetJobResponse.
        :type part_failed_reason: list[:class:`huaweicloudsdkeihealth.v1.FailedReasonRecord`]
        """
        self._part_failed_reason = part_failed_reason

    @property
    def base_model(self):
        r"""Gets the base_model of this ShowAdmetJobResponse.

        :return: The base_model of this ShowAdmetJobResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.BaseModel`
        """
        return self._base_model

    @base_model.setter
    def base_model(self, base_model):
        r"""Sets the base_model of this ShowAdmetJobResponse.

        :param base_model: The base_model of this ShowAdmetJobResponse.
        :type base_model: :class:`huaweicloudsdkeihealth.v1.BaseModel`
        """
        self._base_model = base_model

    @property
    def models(self):
        r"""Gets the models of this ShowAdmetJobResponse.

        模型信息

        :return: The models of this ShowAdmetJobResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.BasicDrugModel`]
        """
        return self._models

    @models.setter
    def models(self, models):
        r"""Sets the models of this ShowAdmetJobResponse.

        模型信息

        :param models: The models of this ShowAdmetJobResponse.
        :type models: list[:class:`huaweicloudsdkeihealth.v1.BasicDrugModel`]
        """
        self._models = models

    @property
    def cluster_result(self):
        r"""Gets the cluster_result of this ShowAdmetJobResponse.

        :return: The cluster_result of this ShowAdmetJobResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.ClusterJobRsp`
        """
        return self._cluster_result

    @cluster_result.setter
    def cluster_result(self, cluster_result):
        r"""Sets the cluster_result of this ShowAdmetJobResponse.

        :param cluster_result: The cluster_result of this ShowAdmetJobResponse.
        :type cluster_result: :class:`huaweicloudsdkeihealth.v1.ClusterJobRsp`
        """
        self._cluster_result = cluster_result

    @property
    def save_fingerprint(self):
        r"""Gets the save_fingerprint of this ShowAdmetJobResponse.

        是否输出表征

        :return: The save_fingerprint of this ShowAdmetJobResponse.
        :rtype: bool
        """
        return self._save_fingerprint

    @save_fingerprint.setter
    def save_fingerprint(self, save_fingerprint):
        r"""Sets the save_fingerprint of this ShowAdmetJobResponse.

        是否输出表征

        :param save_fingerprint: The save_fingerprint of this ShowAdmetJobResponse.
        :type save_fingerprint: bool
        """
        self._save_fingerprint = save_fingerprint

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
        if not isinstance(other, ShowAdmetJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
