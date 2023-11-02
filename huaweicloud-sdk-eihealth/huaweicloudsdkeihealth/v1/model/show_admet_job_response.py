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
        'models': 'list[BasicDrugModel]'
    }

    attribute_map = {
        'basic_info': 'basic_info',
        'molecule_file': 'molecule_file',
        'job_result': 'job_result',
        'part_failed_reason': 'part_failed_reason',
        'models': 'models'
    }

    def __init__(self, basic_info=None, molecule_file=None, job_result=None, part_failed_reason=None, models=None):
        """ShowAdmetJobResponse

        The model defined in huaweicloud sdk

        :param basic_info: 
        :type basic_info: :class:`huaweicloudsdkeihealth.v1.DrugJobDto`
        :param molecule_file: 
        :type molecule_file: :class:`huaweicloudsdkeihealth.v1.MoleculeFileDto`
        :param job_result: 
        :type job_result: :class:`huaweicloudsdkeihealth.v1.JobResult`
        :param part_failed_reason: 作业结果信息
        :type part_failed_reason: list[:class:`huaweicloudsdkeihealth.v1.FailedReasonRecord`]
        :param models: 模型信息
        :type models: list[:class:`huaweicloudsdkeihealth.v1.BasicDrugModel`]
        """
        
        super(ShowAdmetJobResponse, self).__init__()

        self._basic_info = None
        self._molecule_file = None
        self._job_result = None
        self._part_failed_reason = None
        self._models = None
        self.discriminator = None

        if basic_info is not None:
            self.basic_info = basic_info
        if molecule_file is not None:
            self.molecule_file = molecule_file
        if job_result is not None:
            self.job_result = job_result
        if part_failed_reason is not None:
            self.part_failed_reason = part_failed_reason
        if models is not None:
            self.models = models

    @property
    def basic_info(self):
        """Gets the basic_info of this ShowAdmetJobResponse.

        :return: The basic_info of this ShowAdmetJobResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.DrugJobDto`
        """
        return self._basic_info

    @basic_info.setter
    def basic_info(self, basic_info):
        """Sets the basic_info of this ShowAdmetJobResponse.

        :param basic_info: The basic_info of this ShowAdmetJobResponse.
        :type basic_info: :class:`huaweicloudsdkeihealth.v1.DrugJobDto`
        """
        self._basic_info = basic_info

    @property
    def molecule_file(self):
        """Gets the molecule_file of this ShowAdmetJobResponse.

        :return: The molecule_file of this ShowAdmetJobResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.MoleculeFileDto`
        """
        return self._molecule_file

    @molecule_file.setter
    def molecule_file(self, molecule_file):
        """Sets the molecule_file of this ShowAdmetJobResponse.

        :param molecule_file: The molecule_file of this ShowAdmetJobResponse.
        :type molecule_file: :class:`huaweicloudsdkeihealth.v1.MoleculeFileDto`
        """
        self._molecule_file = molecule_file

    @property
    def job_result(self):
        """Gets the job_result of this ShowAdmetJobResponse.

        :return: The job_result of this ShowAdmetJobResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.JobResult`
        """
        return self._job_result

    @job_result.setter
    def job_result(self, job_result):
        """Sets the job_result of this ShowAdmetJobResponse.

        :param job_result: The job_result of this ShowAdmetJobResponse.
        :type job_result: :class:`huaweicloudsdkeihealth.v1.JobResult`
        """
        self._job_result = job_result

    @property
    def part_failed_reason(self):
        """Gets the part_failed_reason of this ShowAdmetJobResponse.

        作业结果信息

        :return: The part_failed_reason of this ShowAdmetJobResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.FailedReasonRecord`]
        """
        return self._part_failed_reason

    @part_failed_reason.setter
    def part_failed_reason(self, part_failed_reason):
        """Sets the part_failed_reason of this ShowAdmetJobResponse.

        作业结果信息

        :param part_failed_reason: The part_failed_reason of this ShowAdmetJobResponse.
        :type part_failed_reason: list[:class:`huaweicloudsdkeihealth.v1.FailedReasonRecord`]
        """
        self._part_failed_reason = part_failed_reason

    @property
    def models(self):
        """Gets the models of this ShowAdmetJobResponse.

        模型信息

        :return: The models of this ShowAdmetJobResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.BasicDrugModel`]
        """
        return self._models

    @models.setter
    def models(self, models):
        """Sets the models of this ShowAdmetJobResponse.

        模型信息

        :param models: The models of this ShowAdmetJobResponse.
        :type models: list[:class:`huaweicloudsdkeihealth.v1.BasicDrugModel`]
        """
        self._models = models

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
