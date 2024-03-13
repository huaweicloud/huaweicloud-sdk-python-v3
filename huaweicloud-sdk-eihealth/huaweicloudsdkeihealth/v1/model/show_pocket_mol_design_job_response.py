# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPocketMolDesignJobResponse(SdkResponse):

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
        'receptor': 'PocketMolDesignReceptorDto',
        'ligands': 'list[PocketFragment]',
        'num_trials': 'int',
        'model_list': 'list[BasicDrugModel]',
        'molecular_weight': 'list[int]',
        'optimization_mode': 'OptimizationMode',
        'cluster_result': 'ClusterJobRsp'
    }

    attribute_map = {
        'basic_info': 'basic_info',
        'receptor': 'receptor',
        'ligands': 'ligands',
        'num_trials': 'num_trials',
        'model_list': 'model_list',
        'molecular_weight': 'molecular_weight',
        'optimization_mode': 'optimization_mode',
        'cluster_result': 'cluster_result'
    }

    def __init__(self, basic_info=None, receptor=None, ligands=None, num_trials=None, model_list=None, molecular_weight=None, optimization_mode=None, cluster_result=None):
        """ShowPocketMolDesignJobResponse

        The model defined in huaweicloud sdk

        :param basic_info: 
        :type basic_info: :class:`huaweicloudsdkeihealth.v1.DrugJobDto`
        :param receptor: 
        :type receptor: :class:`huaweicloudsdkeihealth.v1.PocketMolDesignReceptorDto`
        :param ligands: 配体文件列表
        :type ligands: list[:class:`huaweicloudsdkeihealth.v1.PocketFragment`]
        :param num_trials: 生成分子数量
        :type num_trials: int
        :param model_list: 模型列表
        :type model_list: list[:class:`huaweicloudsdkeihealth.v1.BasicDrugModel`]
        :param molecular_weight: 分子量范围
        :type molecular_weight: list[int]
        :param optimization_mode: 
        :type optimization_mode: :class:`huaweicloudsdkeihealth.v1.OptimizationMode`
        :param cluster_result: 
        :type cluster_result: :class:`huaweicloudsdkeihealth.v1.ClusterJobRsp`
        """
        
        super(ShowPocketMolDesignJobResponse, self).__init__()

        self._basic_info = None
        self._receptor = None
        self._ligands = None
        self._num_trials = None
        self._model_list = None
        self._molecular_weight = None
        self._optimization_mode = None
        self._cluster_result = None
        self.discriminator = None

        if basic_info is not None:
            self.basic_info = basic_info
        if receptor is not None:
            self.receptor = receptor
        if ligands is not None:
            self.ligands = ligands
        if num_trials is not None:
            self.num_trials = num_trials
        if model_list is not None:
            self.model_list = model_list
        if molecular_weight is not None:
            self.molecular_weight = molecular_weight
        if optimization_mode is not None:
            self.optimization_mode = optimization_mode
        if cluster_result is not None:
            self.cluster_result = cluster_result

    @property
    def basic_info(self):
        """Gets the basic_info of this ShowPocketMolDesignJobResponse.

        :return: The basic_info of this ShowPocketMolDesignJobResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.DrugJobDto`
        """
        return self._basic_info

    @basic_info.setter
    def basic_info(self, basic_info):
        """Sets the basic_info of this ShowPocketMolDesignJobResponse.

        :param basic_info: The basic_info of this ShowPocketMolDesignJobResponse.
        :type basic_info: :class:`huaweicloudsdkeihealth.v1.DrugJobDto`
        """
        self._basic_info = basic_info

    @property
    def receptor(self):
        """Gets the receptor of this ShowPocketMolDesignJobResponse.

        :return: The receptor of this ShowPocketMolDesignJobResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.PocketMolDesignReceptorDto`
        """
        return self._receptor

    @receptor.setter
    def receptor(self, receptor):
        """Sets the receptor of this ShowPocketMolDesignJobResponse.

        :param receptor: The receptor of this ShowPocketMolDesignJobResponse.
        :type receptor: :class:`huaweicloudsdkeihealth.v1.PocketMolDesignReceptorDto`
        """
        self._receptor = receptor

    @property
    def ligands(self):
        """Gets the ligands of this ShowPocketMolDesignJobResponse.

        配体文件列表

        :return: The ligands of this ShowPocketMolDesignJobResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.PocketFragment`]
        """
        return self._ligands

    @ligands.setter
    def ligands(self, ligands):
        """Sets the ligands of this ShowPocketMolDesignJobResponse.

        配体文件列表

        :param ligands: The ligands of this ShowPocketMolDesignJobResponse.
        :type ligands: list[:class:`huaweicloudsdkeihealth.v1.PocketFragment`]
        """
        self._ligands = ligands

    @property
    def num_trials(self):
        """Gets the num_trials of this ShowPocketMolDesignJobResponse.

        生成分子数量

        :return: The num_trials of this ShowPocketMolDesignJobResponse.
        :rtype: int
        """
        return self._num_trials

    @num_trials.setter
    def num_trials(self, num_trials):
        """Sets the num_trials of this ShowPocketMolDesignJobResponse.

        生成分子数量

        :param num_trials: The num_trials of this ShowPocketMolDesignJobResponse.
        :type num_trials: int
        """
        self._num_trials = num_trials

    @property
    def model_list(self):
        """Gets the model_list of this ShowPocketMolDesignJobResponse.

        模型列表

        :return: The model_list of this ShowPocketMolDesignJobResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.BasicDrugModel`]
        """
        return self._model_list

    @model_list.setter
    def model_list(self, model_list):
        """Sets the model_list of this ShowPocketMolDesignJobResponse.

        模型列表

        :param model_list: The model_list of this ShowPocketMolDesignJobResponse.
        :type model_list: list[:class:`huaweicloudsdkeihealth.v1.BasicDrugModel`]
        """
        self._model_list = model_list

    @property
    def molecular_weight(self):
        """Gets the molecular_weight of this ShowPocketMolDesignJobResponse.

        分子量范围

        :return: The molecular_weight of this ShowPocketMolDesignJobResponse.
        :rtype: list[int]
        """
        return self._molecular_weight

    @molecular_weight.setter
    def molecular_weight(self, molecular_weight):
        """Sets the molecular_weight of this ShowPocketMolDesignJobResponse.

        分子量范围

        :param molecular_weight: The molecular_weight of this ShowPocketMolDesignJobResponse.
        :type molecular_weight: list[int]
        """
        self._molecular_weight = molecular_weight

    @property
    def optimization_mode(self):
        """Gets the optimization_mode of this ShowPocketMolDesignJobResponse.

        :return: The optimization_mode of this ShowPocketMolDesignJobResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.OptimizationMode`
        """
        return self._optimization_mode

    @optimization_mode.setter
    def optimization_mode(self, optimization_mode):
        """Sets the optimization_mode of this ShowPocketMolDesignJobResponse.

        :param optimization_mode: The optimization_mode of this ShowPocketMolDesignJobResponse.
        :type optimization_mode: :class:`huaweicloudsdkeihealth.v1.OptimizationMode`
        """
        self._optimization_mode = optimization_mode

    @property
    def cluster_result(self):
        """Gets the cluster_result of this ShowPocketMolDesignJobResponse.

        :return: The cluster_result of this ShowPocketMolDesignJobResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.ClusterJobRsp`
        """
        return self._cluster_result

    @cluster_result.setter
    def cluster_result(self, cluster_result):
        """Sets the cluster_result of this ShowPocketMolDesignJobResponse.

        :param cluster_result: The cluster_result of this ShowPocketMolDesignJobResponse.
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
        if not isinstance(other, ShowPocketMolDesignJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
