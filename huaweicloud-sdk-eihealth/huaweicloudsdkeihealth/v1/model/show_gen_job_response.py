# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowGenJobResponse(SdkResponse):

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
        'smiles_list': 'list[str]',
        'molecule_file': 'DrugFile',
        'num_trials': 'int',
        'initial_dataset_size': 'int',
        'binding_sites': 'list[BindSiteDto]',
        'weak_constraints': 'list[WeakConstraintDto]',
        'strong_constraints': 'list[StrongConstraintDto]',
        'base_model': 'BaseModel',
        'models': 'list[BasicDrugModel]'
    }

    attribute_map = {
        'basic_info': 'basic_info',
        'smiles_list': 'smiles_list',
        'molecule_file': 'molecule_file',
        'num_trials': 'num_trials',
        'initial_dataset_size': 'initial_dataset_size',
        'binding_sites': 'binding_sites',
        'weak_constraints': 'weak_constraints',
        'strong_constraints': 'strong_constraints',
        'base_model': 'base_model',
        'models': 'models'
    }

    def __init__(self, basic_info=None, smiles_list=None, molecule_file=None, num_trials=None, initial_dataset_size=None, binding_sites=None, weak_constraints=None, strong_constraints=None, base_model=None, models=None):
        r"""ShowGenJobResponse

        The model defined in huaweicloud sdk

        :param basic_info: 
        :type basic_info: :class:`huaweicloudsdkeihealth.v1.DrugJobDto`
        :param smiles_list: 分子表达式列表
        :type smiles_list: list[str]
        :param molecule_file: 
        :type molecule_file: :class:`huaweicloudsdkeihealth.v1.DrugFile`
        :param num_trials: 生成分子数量
        :type num_trials: int
        :param initial_dataset_size: 初始化数据集的分子数目。当为-1时，表示分子数目未知
        :type initial_dataset_size: int
        :param binding_sites: 靶点列表
        :type binding_sites: list[:class:`huaweicloudsdkeihealth.v1.BindSiteDto`]
        :param weak_constraints: 弱约束集合
        :type weak_constraints: list[:class:`huaweicloudsdkeihealth.v1.WeakConstraintDto`]
        :param strong_constraints: 强约束集合
        :type strong_constraints: list[:class:`huaweicloudsdkeihealth.v1.StrongConstraintDto`]
        :param base_model: 
        :type base_model: :class:`huaweicloudsdkeihealth.v1.BaseModel`
        :param models: 模型列表
        :type models: list[:class:`huaweicloudsdkeihealth.v1.BasicDrugModel`]
        """
        
        super(ShowGenJobResponse, self).__init__()

        self._basic_info = None
        self._smiles_list = None
        self._molecule_file = None
        self._num_trials = None
        self._initial_dataset_size = None
        self._binding_sites = None
        self._weak_constraints = None
        self._strong_constraints = None
        self._base_model = None
        self._models = None
        self.discriminator = None

        if basic_info is not None:
            self.basic_info = basic_info
        if smiles_list is not None:
            self.smiles_list = smiles_list
        if molecule_file is not None:
            self.molecule_file = molecule_file
        if num_trials is not None:
            self.num_trials = num_trials
        if initial_dataset_size is not None:
            self.initial_dataset_size = initial_dataset_size
        if binding_sites is not None:
            self.binding_sites = binding_sites
        if weak_constraints is not None:
            self.weak_constraints = weak_constraints
        if strong_constraints is not None:
            self.strong_constraints = strong_constraints
        if base_model is not None:
            self.base_model = base_model
        if models is not None:
            self.models = models

    @property
    def basic_info(self):
        r"""Gets the basic_info of this ShowGenJobResponse.

        :return: The basic_info of this ShowGenJobResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.DrugJobDto`
        """
        return self._basic_info

    @basic_info.setter
    def basic_info(self, basic_info):
        r"""Sets the basic_info of this ShowGenJobResponse.

        :param basic_info: The basic_info of this ShowGenJobResponse.
        :type basic_info: :class:`huaweicloudsdkeihealth.v1.DrugJobDto`
        """
        self._basic_info = basic_info

    @property
    def smiles_list(self):
        r"""Gets the smiles_list of this ShowGenJobResponse.

        分子表达式列表

        :return: The smiles_list of this ShowGenJobResponse.
        :rtype: list[str]
        """
        return self._smiles_list

    @smiles_list.setter
    def smiles_list(self, smiles_list):
        r"""Sets the smiles_list of this ShowGenJobResponse.

        分子表达式列表

        :param smiles_list: The smiles_list of this ShowGenJobResponse.
        :type smiles_list: list[str]
        """
        self._smiles_list = smiles_list

    @property
    def molecule_file(self):
        r"""Gets the molecule_file of this ShowGenJobResponse.

        :return: The molecule_file of this ShowGenJobResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.DrugFile`
        """
        return self._molecule_file

    @molecule_file.setter
    def molecule_file(self, molecule_file):
        r"""Sets the molecule_file of this ShowGenJobResponse.

        :param molecule_file: The molecule_file of this ShowGenJobResponse.
        :type molecule_file: :class:`huaweicloudsdkeihealth.v1.DrugFile`
        """
        self._molecule_file = molecule_file

    @property
    def num_trials(self):
        r"""Gets the num_trials of this ShowGenJobResponse.

        生成分子数量

        :return: The num_trials of this ShowGenJobResponse.
        :rtype: int
        """
        return self._num_trials

    @num_trials.setter
    def num_trials(self, num_trials):
        r"""Sets the num_trials of this ShowGenJobResponse.

        生成分子数量

        :param num_trials: The num_trials of this ShowGenJobResponse.
        :type num_trials: int
        """
        self._num_trials = num_trials

    @property
    def initial_dataset_size(self):
        r"""Gets the initial_dataset_size of this ShowGenJobResponse.

        初始化数据集的分子数目。当为-1时，表示分子数目未知

        :return: The initial_dataset_size of this ShowGenJobResponse.
        :rtype: int
        """
        return self._initial_dataset_size

    @initial_dataset_size.setter
    def initial_dataset_size(self, initial_dataset_size):
        r"""Sets the initial_dataset_size of this ShowGenJobResponse.

        初始化数据集的分子数目。当为-1时，表示分子数目未知

        :param initial_dataset_size: The initial_dataset_size of this ShowGenJobResponse.
        :type initial_dataset_size: int
        """
        self._initial_dataset_size = initial_dataset_size

    @property
    def binding_sites(self):
        r"""Gets the binding_sites of this ShowGenJobResponse.

        靶点列表

        :return: The binding_sites of this ShowGenJobResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.BindSiteDto`]
        """
        return self._binding_sites

    @binding_sites.setter
    def binding_sites(self, binding_sites):
        r"""Sets the binding_sites of this ShowGenJobResponse.

        靶点列表

        :param binding_sites: The binding_sites of this ShowGenJobResponse.
        :type binding_sites: list[:class:`huaweicloudsdkeihealth.v1.BindSiteDto`]
        """
        self._binding_sites = binding_sites

    @property
    def weak_constraints(self):
        r"""Gets the weak_constraints of this ShowGenJobResponse.

        弱约束集合

        :return: The weak_constraints of this ShowGenJobResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.WeakConstraintDto`]
        """
        return self._weak_constraints

    @weak_constraints.setter
    def weak_constraints(self, weak_constraints):
        r"""Sets the weak_constraints of this ShowGenJobResponse.

        弱约束集合

        :param weak_constraints: The weak_constraints of this ShowGenJobResponse.
        :type weak_constraints: list[:class:`huaweicloudsdkeihealth.v1.WeakConstraintDto`]
        """
        self._weak_constraints = weak_constraints

    @property
    def strong_constraints(self):
        r"""Gets the strong_constraints of this ShowGenJobResponse.

        强约束集合

        :return: The strong_constraints of this ShowGenJobResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.StrongConstraintDto`]
        """
        return self._strong_constraints

    @strong_constraints.setter
    def strong_constraints(self, strong_constraints):
        r"""Sets the strong_constraints of this ShowGenJobResponse.

        强约束集合

        :param strong_constraints: The strong_constraints of this ShowGenJobResponse.
        :type strong_constraints: list[:class:`huaweicloudsdkeihealth.v1.StrongConstraintDto`]
        """
        self._strong_constraints = strong_constraints

    @property
    def base_model(self):
        r"""Gets the base_model of this ShowGenJobResponse.

        :return: The base_model of this ShowGenJobResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.BaseModel`
        """
        return self._base_model

    @base_model.setter
    def base_model(self, base_model):
        r"""Sets the base_model of this ShowGenJobResponse.

        :param base_model: The base_model of this ShowGenJobResponse.
        :type base_model: :class:`huaweicloudsdkeihealth.v1.BaseModel`
        """
        self._base_model = base_model

    @property
    def models(self):
        r"""Gets the models of this ShowGenJobResponse.

        模型列表

        :return: The models of this ShowGenJobResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.BasicDrugModel`]
        """
        return self._models

    @models.setter
    def models(self, models):
        r"""Sets the models of this ShowGenJobResponse.

        模型列表

        :param models: The models of this ShowGenJobResponse.
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
        if not isinstance(other, ShowGenJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
