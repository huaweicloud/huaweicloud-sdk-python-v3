# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFepJobResponse(SdkResponse):

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
        'receptor': 'ReceptorDrugFile',
        'ligands': 'list[LigandPreviewDto]',
        'graph': 'FepGraphDto',
        'params': 'FepParamDto',
        'job_result': 'JobResult',
        'part_failed_reason': 'list[FailedReasonRecord]'
    }

    attribute_map = {
        'basic_info': 'basic_info',
        'receptor': 'receptor',
        'ligands': 'ligands',
        'graph': 'graph',
        'params': 'params',
        'job_result': 'job_result',
        'part_failed_reason': 'part_failed_reason'
    }

    def __init__(self, basic_info=None, receptor=None, ligands=None, graph=None, params=None, job_result=None, part_failed_reason=None):
        """ShowFepJobResponse

        The model defined in huaweicloud sdk

        :param basic_info: 
        :type basic_info: :class:`huaweicloudsdkeihealth.v1.DrugJobDto`
        :param receptor: 
        :type receptor: :class:`huaweicloudsdkeihealth.v1.ReceptorDrugFile`
        :param ligands: 配体列表
        :type ligands: list[:class:`huaweicloudsdkeihealth.v1.LigandPreviewDto`]
        :param graph: 
        :type graph: :class:`huaweicloudsdkeihealth.v1.FepGraphDto`
        :param params: 
        :type params: :class:`huaweicloudsdkeihealth.v1.FepParamDto`
        :param job_result: 
        :type job_result: :class:`huaweicloudsdkeihealth.v1.JobResult`
        :param part_failed_reason: 部分失败原因和数量
        :type part_failed_reason: list[:class:`huaweicloudsdkeihealth.v1.FailedReasonRecord`]
        """
        
        super(ShowFepJobResponse, self).__init__()

        self._basic_info = None
        self._receptor = None
        self._ligands = None
        self._graph = None
        self._params = None
        self._job_result = None
        self._part_failed_reason = None
        self.discriminator = None

        if basic_info is not None:
            self.basic_info = basic_info
        if receptor is not None:
            self.receptor = receptor
        if ligands is not None:
            self.ligands = ligands
        if graph is not None:
            self.graph = graph
        if params is not None:
            self.params = params
        if job_result is not None:
            self.job_result = job_result
        if part_failed_reason is not None:
            self.part_failed_reason = part_failed_reason

    @property
    def basic_info(self):
        """Gets the basic_info of this ShowFepJobResponse.

        :return: The basic_info of this ShowFepJobResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.DrugJobDto`
        """
        return self._basic_info

    @basic_info.setter
    def basic_info(self, basic_info):
        """Sets the basic_info of this ShowFepJobResponse.

        :param basic_info: The basic_info of this ShowFepJobResponse.
        :type basic_info: :class:`huaweicloudsdkeihealth.v1.DrugJobDto`
        """
        self._basic_info = basic_info

    @property
    def receptor(self):
        """Gets the receptor of this ShowFepJobResponse.

        :return: The receptor of this ShowFepJobResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.ReceptorDrugFile`
        """
        return self._receptor

    @receptor.setter
    def receptor(self, receptor):
        """Sets the receptor of this ShowFepJobResponse.

        :param receptor: The receptor of this ShowFepJobResponse.
        :type receptor: :class:`huaweicloudsdkeihealth.v1.ReceptorDrugFile`
        """
        self._receptor = receptor

    @property
    def ligands(self):
        """Gets the ligands of this ShowFepJobResponse.

        配体列表

        :return: The ligands of this ShowFepJobResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.LigandPreviewDto`]
        """
        return self._ligands

    @ligands.setter
    def ligands(self, ligands):
        """Sets the ligands of this ShowFepJobResponse.

        配体列表

        :param ligands: The ligands of this ShowFepJobResponse.
        :type ligands: list[:class:`huaweicloudsdkeihealth.v1.LigandPreviewDto`]
        """
        self._ligands = ligands

    @property
    def graph(self):
        """Gets the graph of this ShowFepJobResponse.

        :return: The graph of this ShowFepJobResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.FepGraphDto`
        """
        return self._graph

    @graph.setter
    def graph(self, graph):
        """Sets the graph of this ShowFepJobResponse.

        :param graph: The graph of this ShowFepJobResponse.
        :type graph: :class:`huaweicloudsdkeihealth.v1.FepGraphDto`
        """
        self._graph = graph

    @property
    def params(self):
        """Gets the params of this ShowFepJobResponse.

        :return: The params of this ShowFepJobResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.FepParamDto`
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this ShowFepJobResponse.

        :param params: The params of this ShowFepJobResponse.
        :type params: :class:`huaweicloudsdkeihealth.v1.FepParamDto`
        """
        self._params = params

    @property
    def job_result(self):
        """Gets the job_result of this ShowFepJobResponse.

        :return: The job_result of this ShowFepJobResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.JobResult`
        """
        return self._job_result

    @job_result.setter
    def job_result(self, job_result):
        """Sets the job_result of this ShowFepJobResponse.

        :param job_result: The job_result of this ShowFepJobResponse.
        :type job_result: :class:`huaweicloudsdkeihealth.v1.JobResult`
        """
        self._job_result = job_result

    @property
    def part_failed_reason(self):
        """Gets the part_failed_reason of this ShowFepJobResponse.

        部分失败原因和数量

        :return: The part_failed_reason of this ShowFepJobResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.FailedReasonRecord`]
        """
        return self._part_failed_reason

    @part_failed_reason.setter
    def part_failed_reason(self, part_failed_reason):
        """Sets the part_failed_reason of this ShowFepJobResponse.

        部分失败原因和数量

        :param part_failed_reason: The part_failed_reason of this ShowFepJobResponse.
        :type part_failed_reason: list[:class:`huaweicloudsdkeihealth.v1.FailedReasonRecord`]
        """
        self._part_failed_reason = part_failed_reason

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
        if not isinstance(other, ShowFepJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
