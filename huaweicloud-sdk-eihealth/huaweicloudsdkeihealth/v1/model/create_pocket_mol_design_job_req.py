# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePocketMolDesignJobReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'basic_info': 'CreateDrugJobBasicInfo',
        'receptor': 'PocketMolDesignReceptorDto',
        'ligands': 'list[PocketFragment]',
        'num_trials': 'int',
        'model_ids': 'list[str]',
        'molecular_weight': 'list[int]',
        'optimization_mode': 'OptimizationMode'
    }

    attribute_map = {
        'basic_info': 'basic_info',
        'receptor': 'receptor',
        'ligands': 'ligands',
        'num_trials': 'num_trials',
        'model_ids': 'model_ids',
        'molecular_weight': 'molecular_weight',
        'optimization_mode': 'optimization_mode'
    }

    def __init__(self, basic_info=None, receptor=None, ligands=None, num_trials=None, model_ids=None, molecular_weight=None, optimization_mode=None):
        r"""CreatePocketMolDesignJobReq

        The model defined in huaweicloud sdk

        :param basic_info: 
        :type basic_info: :class:`huaweicloudsdkeihealth.v1.CreateDrugJobBasicInfo`
        :param receptor: 
        :type receptor: :class:`huaweicloudsdkeihealth.v1.PocketMolDesignReceptorDto`
        :param ligands: 配体文件列表，最多支持1个
        :type ligands: list[:class:`huaweicloudsdkeihealth.v1.PocketFragment`]
        :param num_trials: 生成分子数量
        :type num_trials: int
        :param model_ids: 模型id列表
        :type model_ids: list[str]
        :param molecular_weight: 分子量范围
        :type molecular_weight: list[int]
        :param optimization_mode: 
        :type optimization_mode: :class:`huaweicloudsdkeihealth.v1.OptimizationMode`
        """
        
        

        self._basic_info = None
        self._receptor = None
        self._ligands = None
        self._num_trials = None
        self._model_ids = None
        self._molecular_weight = None
        self._optimization_mode = None
        self.discriminator = None

        self.basic_info = basic_info
        self.receptor = receptor
        if ligands is not None:
            self.ligands = ligands
        if num_trials is not None:
            self.num_trials = num_trials
        if model_ids is not None:
            self.model_ids = model_ids
        if molecular_weight is not None:
            self.molecular_weight = molecular_weight
        if optimization_mode is not None:
            self.optimization_mode = optimization_mode

    @property
    def basic_info(self):
        r"""Gets the basic_info of this CreatePocketMolDesignJobReq.

        :return: The basic_info of this CreatePocketMolDesignJobReq.
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateDrugJobBasicInfo`
        """
        return self._basic_info

    @basic_info.setter
    def basic_info(self, basic_info):
        r"""Sets the basic_info of this CreatePocketMolDesignJobReq.

        :param basic_info: The basic_info of this CreatePocketMolDesignJobReq.
        :type basic_info: :class:`huaweicloudsdkeihealth.v1.CreateDrugJobBasicInfo`
        """
        self._basic_info = basic_info

    @property
    def receptor(self):
        r"""Gets the receptor of this CreatePocketMolDesignJobReq.

        :return: The receptor of this CreatePocketMolDesignJobReq.
        :rtype: :class:`huaweicloudsdkeihealth.v1.PocketMolDesignReceptorDto`
        """
        return self._receptor

    @receptor.setter
    def receptor(self, receptor):
        r"""Sets the receptor of this CreatePocketMolDesignJobReq.

        :param receptor: The receptor of this CreatePocketMolDesignJobReq.
        :type receptor: :class:`huaweicloudsdkeihealth.v1.PocketMolDesignReceptorDto`
        """
        self._receptor = receptor

    @property
    def ligands(self):
        r"""Gets the ligands of this CreatePocketMolDesignJobReq.

        配体文件列表，最多支持1个

        :return: The ligands of this CreatePocketMolDesignJobReq.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.PocketFragment`]
        """
        return self._ligands

    @ligands.setter
    def ligands(self, ligands):
        r"""Sets the ligands of this CreatePocketMolDesignJobReq.

        配体文件列表，最多支持1个

        :param ligands: The ligands of this CreatePocketMolDesignJobReq.
        :type ligands: list[:class:`huaweicloudsdkeihealth.v1.PocketFragment`]
        """
        self._ligands = ligands

    @property
    def num_trials(self):
        r"""Gets the num_trials of this CreatePocketMolDesignJobReq.

        生成分子数量

        :return: The num_trials of this CreatePocketMolDesignJobReq.
        :rtype: int
        """
        return self._num_trials

    @num_trials.setter
    def num_trials(self, num_trials):
        r"""Sets the num_trials of this CreatePocketMolDesignJobReq.

        生成分子数量

        :param num_trials: The num_trials of this CreatePocketMolDesignJobReq.
        :type num_trials: int
        """
        self._num_trials = num_trials

    @property
    def model_ids(self):
        r"""Gets the model_ids of this CreatePocketMolDesignJobReq.

        模型id列表

        :return: The model_ids of this CreatePocketMolDesignJobReq.
        :rtype: list[str]
        """
        return self._model_ids

    @model_ids.setter
    def model_ids(self, model_ids):
        r"""Sets the model_ids of this CreatePocketMolDesignJobReq.

        模型id列表

        :param model_ids: The model_ids of this CreatePocketMolDesignJobReq.
        :type model_ids: list[str]
        """
        self._model_ids = model_ids

    @property
    def molecular_weight(self):
        r"""Gets the molecular_weight of this CreatePocketMolDesignJobReq.

        分子量范围

        :return: The molecular_weight of this CreatePocketMolDesignJobReq.
        :rtype: list[int]
        """
        return self._molecular_weight

    @molecular_weight.setter
    def molecular_weight(self, molecular_weight):
        r"""Sets the molecular_weight of this CreatePocketMolDesignJobReq.

        分子量范围

        :param molecular_weight: The molecular_weight of this CreatePocketMolDesignJobReq.
        :type molecular_weight: list[int]
        """
        self._molecular_weight = molecular_weight

    @property
    def optimization_mode(self):
        r"""Gets the optimization_mode of this CreatePocketMolDesignJobReq.

        :return: The optimization_mode of this CreatePocketMolDesignJobReq.
        :rtype: :class:`huaweicloudsdkeihealth.v1.OptimizationMode`
        """
        return self._optimization_mode

    @optimization_mode.setter
    def optimization_mode(self, optimization_mode):
        r"""Sets the optimization_mode of this CreatePocketMolDesignJobReq.

        :param optimization_mode: The optimization_mode of this CreatePocketMolDesignJobReq.
        :type optimization_mode: :class:`huaweicloudsdkeihealth.v1.OptimizationMode`
        """
        self._optimization_mode = optimization_mode

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
        if not isinstance(other, CreatePocketMolDesignJobReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
