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
        'add_membrane': 'bool',
        'ligands': 'list[LigandPreviewDto]',
        'graph': 'FepGraphDto',
        'params': 'FepParamDto',
        'job_result': 'JobResult',
        'part_failed_reason': 'list[FailedReasonRecord]'
    }

    attribute_map = {
        'basic_info': 'basic_info',
        'receptor': 'receptor',
        'add_membrane': 'add_membrane',
        'ligands': 'ligands',
        'graph': 'graph',
        'params': 'params',
        'job_result': 'job_result',
        'part_failed_reason': 'part_failed_reason'
    }

    def __init__(self, basic_info=None, receptor=None, add_membrane=None, ligands=None, graph=None, params=None, job_result=None, part_failed_reason=None):
        r"""ShowFepJobResponse

        The model defined in huaweicloud sdk

        :param basic_info: 
        :type basic_info: :class:`huaweicloudsdkeihealth.v1.DrugJobDto`
        :param receptor: 
        :type receptor: :class:`huaweicloudsdkeihealth.v1.ReceptorDrugFile`
        :param add_membrane: 是否加膜处理
        :type add_membrane: bool
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
        self._add_membrane = None
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
        if add_membrane is not None:
            self.add_membrane = add_membrane
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
        r"""Gets the basic_info of this ShowFepJobResponse.

        :return: The basic_info of this ShowFepJobResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.DrugJobDto`
        """
        return self._basic_info

    @basic_info.setter
    def basic_info(self, basic_info):
        r"""Sets the basic_info of this ShowFepJobResponse.

        :param basic_info: The basic_info of this ShowFepJobResponse.
        :type basic_info: :class:`huaweicloudsdkeihealth.v1.DrugJobDto`
        """
        self._basic_info = basic_info

    @property
    def receptor(self):
        r"""Gets the receptor of this ShowFepJobResponse.

        :return: The receptor of this ShowFepJobResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.ReceptorDrugFile`
        """
        return self._receptor

    @receptor.setter
    def receptor(self, receptor):
        r"""Sets the receptor of this ShowFepJobResponse.

        :param receptor: The receptor of this ShowFepJobResponse.
        :type receptor: :class:`huaweicloudsdkeihealth.v1.ReceptorDrugFile`
        """
        self._receptor = receptor

    @property
    def add_membrane(self):
        r"""Gets the add_membrane of this ShowFepJobResponse.

        是否加膜处理

        :return: The add_membrane of this ShowFepJobResponse.
        :rtype: bool
        """
        return self._add_membrane

    @add_membrane.setter
    def add_membrane(self, add_membrane):
        r"""Sets the add_membrane of this ShowFepJobResponse.

        是否加膜处理

        :param add_membrane: The add_membrane of this ShowFepJobResponse.
        :type add_membrane: bool
        """
        self._add_membrane = add_membrane

    @property
    def ligands(self):
        r"""Gets the ligands of this ShowFepJobResponse.

        配体列表

        :return: The ligands of this ShowFepJobResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.LigandPreviewDto`]
        """
        return self._ligands

    @ligands.setter
    def ligands(self, ligands):
        r"""Sets the ligands of this ShowFepJobResponse.

        配体列表

        :param ligands: The ligands of this ShowFepJobResponse.
        :type ligands: list[:class:`huaweicloudsdkeihealth.v1.LigandPreviewDto`]
        """
        self._ligands = ligands

    @property
    def graph(self):
        r"""Gets the graph of this ShowFepJobResponse.

        :return: The graph of this ShowFepJobResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.FepGraphDto`
        """
        return self._graph

    @graph.setter
    def graph(self, graph):
        r"""Sets the graph of this ShowFepJobResponse.

        :param graph: The graph of this ShowFepJobResponse.
        :type graph: :class:`huaweicloudsdkeihealth.v1.FepGraphDto`
        """
        self._graph = graph

    @property
    def params(self):
        r"""Gets the params of this ShowFepJobResponse.

        :return: The params of this ShowFepJobResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.FepParamDto`
        """
        return self._params

    @params.setter
    def params(self, params):
        r"""Sets the params of this ShowFepJobResponse.

        :param params: The params of this ShowFepJobResponse.
        :type params: :class:`huaweicloudsdkeihealth.v1.FepParamDto`
        """
        self._params = params

    @property
    def job_result(self):
        r"""Gets the job_result of this ShowFepJobResponse.

        :return: The job_result of this ShowFepJobResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.JobResult`
        """
        return self._job_result

    @job_result.setter
    def job_result(self, job_result):
        r"""Sets the job_result of this ShowFepJobResponse.

        :param job_result: The job_result of this ShowFepJobResponse.
        :type job_result: :class:`huaweicloudsdkeihealth.v1.JobResult`
        """
        self._job_result = job_result

    @property
    def part_failed_reason(self):
        r"""Gets the part_failed_reason of this ShowFepJobResponse.

        部分失败原因和数量

        :return: The part_failed_reason of this ShowFepJobResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.FailedReasonRecord`]
        """
        return self._part_failed_reason

    @part_failed_reason.setter
    def part_failed_reason(self, part_failed_reason):
        r"""Sets the part_failed_reason of this ShowFepJobResponse.

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
