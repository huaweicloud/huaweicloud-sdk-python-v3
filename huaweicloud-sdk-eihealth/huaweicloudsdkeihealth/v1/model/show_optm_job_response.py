# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOptmJobResponse(SdkResponse):

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
        'smiles': 'str',
        'molecule_file': 'DrugFile',
        'num_trials': 'int',
        'binding_site': 'BindSiteDto',
        'binding_sites': 'list[BindSiteDto]',
        'weak_constraints': 'list[WeakConstraintDto]',
        'strong_constraints': 'list[StrongConstraintDto]',
        'sampler_mixin_weight': 'float',
        'base_model': 'BaseModel',
        'models': 'list[BasicDrugModel]',
        'cluster_result': 'ClusterJobRsp'
    }

    attribute_map = {
        'basic_info': 'basic_info',
        'smiles': 'smiles',
        'molecule_file': 'molecule_file',
        'num_trials': 'num_trials',
        'binding_site': 'binding_site',
        'binding_sites': 'binding_sites',
        'weak_constraints': 'weak_constraints',
        'strong_constraints': 'strong_constraints',
        'sampler_mixin_weight': 'sampler_mixin_weight',
        'base_model': 'base_model',
        'models': 'models',
        'cluster_result': 'cluster_result'
    }

    def __init__(self, basic_info=None, smiles=None, molecule_file=None, num_trials=None, binding_site=None, binding_sites=None, weak_constraints=None, strong_constraints=None, sampler_mixin_weight=None, base_model=None, models=None, cluster_result=None):
        r"""ShowOptmJobResponse

        The model defined in huaweicloud sdk

        :param basic_info: 
        :type basic_info: :class:`huaweicloudsdkeihealth.v1.DrugJobDto`
        :param smiles: 分子SMILES表达式
        :type smiles: str
        :param molecule_file: 
        :type molecule_file: :class:`huaweicloudsdkeihealth.v1.DrugFile`
        :param num_trials: 生成分子数量
        :type num_trials: int
        :param binding_site: 
        :type binding_site: :class:`huaweicloudsdkeihealth.v1.BindSiteDto`
        :param binding_sites: 受体列表和受体是二选一的关系，受体列表优先级最高
        :type binding_sites: list[:class:`huaweicloudsdkeihealth.v1.BindSiteDto`]
        :param weak_constraints: 弱约束集合
        :type weak_constraints: list[:class:`huaweicloudsdkeihealth.v1.WeakConstraintDto`]
        :param strong_constraints: 强约束集合
        :type strong_constraints: list[:class:`huaweicloudsdkeihealth.v1.StrongConstraintDto`]
        :param sampler_mixin_weight: 初始化采样权重
        :type sampler_mixin_weight: float
        :param base_model: 
        :type base_model: :class:`huaweicloudsdkeihealth.v1.BaseModel`
        :param models: 模型列表
        :type models: list[:class:`huaweicloudsdkeihealth.v1.BasicDrugModel`]
        :param cluster_result: 
        :type cluster_result: :class:`huaweicloudsdkeihealth.v1.ClusterJobRsp`
        """
        
        super(ShowOptmJobResponse, self).__init__()

        self._basic_info = None
        self._smiles = None
        self._molecule_file = None
        self._num_trials = None
        self._binding_site = None
        self._binding_sites = None
        self._weak_constraints = None
        self._strong_constraints = None
        self._sampler_mixin_weight = None
        self._base_model = None
        self._models = None
        self._cluster_result = None
        self.discriminator = None

        if basic_info is not None:
            self.basic_info = basic_info
        if smiles is not None:
            self.smiles = smiles
        if molecule_file is not None:
            self.molecule_file = molecule_file
        if num_trials is not None:
            self.num_trials = num_trials
        if binding_site is not None:
            self.binding_site = binding_site
        if binding_sites is not None:
            self.binding_sites = binding_sites
        if weak_constraints is not None:
            self.weak_constraints = weak_constraints
        if strong_constraints is not None:
            self.strong_constraints = strong_constraints
        if sampler_mixin_weight is not None:
            self.sampler_mixin_weight = sampler_mixin_weight
        if base_model is not None:
            self.base_model = base_model
        if models is not None:
            self.models = models
        if cluster_result is not None:
            self.cluster_result = cluster_result

    @property
    def basic_info(self):
        r"""Gets the basic_info of this ShowOptmJobResponse.

        :return: The basic_info of this ShowOptmJobResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.DrugJobDto`
        """
        return self._basic_info

    @basic_info.setter
    def basic_info(self, basic_info):
        r"""Sets the basic_info of this ShowOptmJobResponse.

        :param basic_info: The basic_info of this ShowOptmJobResponse.
        :type basic_info: :class:`huaweicloudsdkeihealth.v1.DrugJobDto`
        """
        self._basic_info = basic_info

    @property
    def smiles(self):
        r"""Gets the smiles of this ShowOptmJobResponse.

        分子SMILES表达式

        :return: The smiles of this ShowOptmJobResponse.
        :rtype: str
        """
        return self._smiles

    @smiles.setter
    def smiles(self, smiles):
        r"""Sets the smiles of this ShowOptmJobResponse.

        分子SMILES表达式

        :param smiles: The smiles of this ShowOptmJobResponse.
        :type smiles: str
        """
        self._smiles = smiles

    @property
    def molecule_file(self):
        r"""Gets the molecule_file of this ShowOptmJobResponse.

        :return: The molecule_file of this ShowOptmJobResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.DrugFile`
        """
        return self._molecule_file

    @molecule_file.setter
    def molecule_file(self, molecule_file):
        r"""Sets the molecule_file of this ShowOptmJobResponse.

        :param molecule_file: The molecule_file of this ShowOptmJobResponse.
        :type molecule_file: :class:`huaweicloudsdkeihealth.v1.DrugFile`
        """
        self._molecule_file = molecule_file

    @property
    def num_trials(self):
        r"""Gets the num_trials of this ShowOptmJobResponse.

        生成分子数量

        :return: The num_trials of this ShowOptmJobResponse.
        :rtype: int
        """
        return self._num_trials

    @num_trials.setter
    def num_trials(self, num_trials):
        r"""Sets the num_trials of this ShowOptmJobResponse.

        生成分子数量

        :param num_trials: The num_trials of this ShowOptmJobResponse.
        :type num_trials: int
        """
        self._num_trials = num_trials

    @property
    def binding_site(self):
        r"""Gets the binding_site of this ShowOptmJobResponse.

        :return: The binding_site of this ShowOptmJobResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.BindSiteDto`
        """
        return self._binding_site

    @binding_site.setter
    def binding_site(self, binding_site):
        r"""Sets the binding_site of this ShowOptmJobResponse.

        :param binding_site: The binding_site of this ShowOptmJobResponse.
        :type binding_site: :class:`huaweicloudsdkeihealth.v1.BindSiteDto`
        """
        self._binding_site = binding_site

    @property
    def binding_sites(self):
        r"""Gets the binding_sites of this ShowOptmJobResponse.

        受体列表和受体是二选一的关系，受体列表优先级最高

        :return: The binding_sites of this ShowOptmJobResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.BindSiteDto`]
        """
        return self._binding_sites

    @binding_sites.setter
    def binding_sites(self, binding_sites):
        r"""Sets the binding_sites of this ShowOptmJobResponse.

        受体列表和受体是二选一的关系，受体列表优先级最高

        :param binding_sites: The binding_sites of this ShowOptmJobResponse.
        :type binding_sites: list[:class:`huaweicloudsdkeihealth.v1.BindSiteDto`]
        """
        self._binding_sites = binding_sites

    @property
    def weak_constraints(self):
        r"""Gets the weak_constraints of this ShowOptmJobResponse.

        弱约束集合

        :return: The weak_constraints of this ShowOptmJobResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.WeakConstraintDto`]
        """
        return self._weak_constraints

    @weak_constraints.setter
    def weak_constraints(self, weak_constraints):
        r"""Sets the weak_constraints of this ShowOptmJobResponse.

        弱约束集合

        :param weak_constraints: The weak_constraints of this ShowOptmJobResponse.
        :type weak_constraints: list[:class:`huaweicloudsdkeihealth.v1.WeakConstraintDto`]
        """
        self._weak_constraints = weak_constraints

    @property
    def strong_constraints(self):
        r"""Gets the strong_constraints of this ShowOptmJobResponse.

        强约束集合

        :return: The strong_constraints of this ShowOptmJobResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.StrongConstraintDto`]
        """
        return self._strong_constraints

    @strong_constraints.setter
    def strong_constraints(self, strong_constraints):
        r"""Sets the strong_constraints of this ShowOptmJobResponse.

        强约束集合

        :param strong_constraints: The strong_constraints of this ShowOptmJobResponse.
        :type strong_constraints: list[:class:`huaweicloudsdkeihealth.v1.StrongConstraintDto`]
        """
        self._strong_constraints = strong_constraints

    @property
    def sampler_mixin_weight(self):
        r"""Gets the sampler_mixin_weight of this ShowOptmJobResponse.

        初始化采样权重

        :return: The sampler_mixin_weight of this ShowOptmJobResponse.
        :rtype: float
        """
        return self._sampler_mixin_weight

    @sampler_mixin_weight.setter
    def sampler_mixin_weight(self, sampler_mixin_weight):
        r"""Sets the sampler_mixin_weight of this ShowOptmJobResponse.

        初始化采样权重

        :param sampler_mixin_weight: The sampler_mixin_weight of this ShowOptmJobResponse.
        :type sampler_mixin_weight: float
        """
        self._sampler_mixin_weight = sampler_mixin_weight

    @property
    def base_model(self):
        r"""Gets the base_model of this ShowOptmJobResponse.

        :return: The base_model of this ShowOptmJobResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.BaseModel`
        """
        return self._base_model

    @base_model.setter
    def base_model(self, base_model):
        r"""Sets the base_model of this ShowOptmJobResponse.

        :param base_model: The base_model of this ShowOptmJobResponse.
        :type base_model: :class:`huaweicloudsdkeihealth.v1.BaseModel`
        """
        self._base_model = base_model

    @property
    def models(self):
        r"""Gets the models of this ShowOptmJobResponse.

        模型列表

        :return: The models of this ShowOptmJobResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.BasicDrugModel`]
        """
        return self._models

    @models.setter
    def models(self, models):
        r"""Sets the models of this ShowOptmJobResponse.

        模型列表

        :param models: The models of this ShowOptmJobResponse.
        :type models: list[:class:`huaweicloudsdkeihealth.v1.BasicDrugModel`]
        """
        self._models = models

    @property
    def cluster_result(self):
        r"""Gets the cluster_result of this ShowOptmJobResponse.

        :return: The cluster_result of this ShowOptmJobResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.ClusterJobRsp`
        """
        return self._cluster_result

    @cluster_result.setter
    def cluster_result(self, cluster_result):
        r"""Sets the cluster_result of this ShowOptmJobResponse.

        :param cluster_result: The cluster_result of this ShowOptmJobResponse.
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
        if not isinstance(other, ShowOptmJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
