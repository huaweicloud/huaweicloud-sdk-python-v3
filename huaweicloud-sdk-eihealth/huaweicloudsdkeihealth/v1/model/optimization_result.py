# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OptimizationResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'smiles': 'str',
        'num_rounds': 'int',
        'num_trials_per_round': 'int',
        'num_expected': 'int',
        'num_strong_constraints': 'int',
        'num_weak_constraints': 'int',
        'prop_names': 'list[str]',
        'original': 'PlainMoleculeItem',
        'result': 'list[OptimizationResultItem]',
        'strong_constraints': 'list[MoleculeConstraint]',
        'weak_constraints': 'list[MoleculeConstraint]',
        'binding_site': 'BindingSite',
        'custom_props': 'list[CustomProp]'
    }

    attribute_map = {
        'name': 'name',
        'smiles': 'smiles',
        'num_rounds': 'num_rounds',
        'num_trials_per_round': 'num_trials_per_round',
        'num_expected': 'num_expected',
        'num_strong_constraints': 'num_strong_constraints',
        'num_weak_constraints': 'num_weak_constraints',
        'prop_names': 'prop_names',
        'original': 'original',
        'result': 'result',
        'strong_constraints': 'strong_constraints',
        'weak_constraints': 'weak_constraints',
        'binding_site': 'binding_site',
        'custom_props': 'custom_props'
    }

    def __init__(self, name=None, smiles=None, num_rounds=None, num_trials_per_round=None, num_expected=None, num_strong_constraints=None, num_weak_constraints=None, prop_names=None, original=None, result=None, strong_constraints=None, weak_constraints=None, binding_site=None, custom_props=None):
        r"""OptimizationResult

        The model defined in huaweicloud sdk

        :param name: 任务名
        :type name: str
        :param smiles: 分子SMILES表达式
        :type smiles: str
        :param num_rounds: 总生成轮数
        :type num_rounds: int
        :param num_trials_per_round: 每轮生成数量
        :type num_trials_per_round: int
        :param num_expected: 期望条目数
        :type num_expected: int
        :param num_strong_constraints: 强约束数量
        :type num_strong_constraints: int
        :param num_weak_constraints: 弱约束数量
        :type num_weak_constraints: int
        :param prop_names: 分子ADMET属性名列表
        :type prop_names: list[str]
        :param original: 
        :type original: :class:`huaweicloudsdkeihealth.v1.PlainMoleculeItem`
        :param result: 分子优化结果条目
        :type result: list[:class:`huaweicloudsdkeihealth.v1.OptimizationResultItem`]
        :param strong_constraints: 强约束集合
        :type strong_constraints: list[:class:`huaweicloudsdkeihealth.v1.MoleculeConstraint`]
        :param weak_constraints: 弱约束集合
        :type weak_constraints: list[:class:`huaweicloudsdkeihealth.v1.MoleculeConstraint`]
        :param binding_site: 
        :type binding_site: :class:`huaweicloudsdkeihealth.v1.BindingSite`
        :param custom_props: 用户已开启的自定义属性集合
        :type custom_props: list[:class:`huaweicloudsdkeihealth.v1.CustomProp`]
        """
        
        

        self._name = None
        self._smiles = None
        self._num_rounds = None
        self._num_trials_per_round = None
        self._num_expected = None
        self._num_strong_constraints = None
        self._num_weak_constraints = None
        self._prop_names = None
        self._original = None
        self._result = None
        self._strong_constraints = None
        self._weak_constraints = None
        self._binding_site = None
        self._custom_props = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if smiles is not None:
            self.smiles = smiles
        if num_rounds is not None:
            self.num_rounds = num_rounds
        if num_trials_per_round is not None:
            self.num_trials_per_round = num_trials_per_round
        if num_expected is not None:
            self.num_expected = num_expected
        if num_strong_constraints is not None:
            self.num_strong_constraints = num_strong_constraints
        if num_weak_constraints is not None:
            self.num_weak_constraints = num_weak_constraints
        if prop_names is not None:
            self.prop_names = prop_names
        if original is not None:
            self.original = original
        if result is not None:
            self.result = result
        if strong_constraints is not None:
            self.strong_constraints = strong_constraints
        if weak_constraints is not None:
            self.weak_constraints = weak_constraints
        if binding_site is not None:
            self.binding_site = binding_site
        if custom_props is not None:
            self.custom_props = custom_props

    @property
    def name(self):
        r"""Gets the name of this OptimizationResult.

        任务名

        :return: The name of this OptimizationResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this OptimizationResult.

        任务名

        :param name: The name of this OptimizationResult.
        :type name: str
        """
        self._name = name

    @property
    def smiles(self):
        r"""Gets the smiles of this OptimizationResult.

        分子SMILES表达式

        :return: The smiles of this OptimizationResult.
        :rtype: str
        """
        return self._smiles

    @smiles.setter
    def smiles(self, smiles):
        r"""Sets the smiles of this OptimizationResult.

        分子SMILES表达式

        :param smiles: The smiles of this OptimizationResult.
        :type smiles: str
        """
        self._smiles = smiles

    @property
    def num_rounds(self):
        r"""Gets the num_rounds of this OptimizationResult.

        总生成轮数

        :return: The num_rounds of this OptimizationResult.
        :rtype: int
        """
        return self._num_rounds

    @num_rounds.setter
    def num_rounds(self, num_rounds):
        r"""Sets the num_rounds of this OptimizationResult.

        总生成轮数

        :param num_rounds: The num_rounds of this OptimizationResult.
        :type num_rounds: int
        """
        self._num_rounds = num_rounds

    @property
    def num_trials_per_round(self):
        r"""Gets the num_trials_per_round of this OptimizationResult.

        每轮生成数量

        :return: The num_trials_per_round of this OptimizationResult.
        :rtype: int
        """
        return self._num_trials_per_round

    @num_trials_per_round.setter
    def num_trials_per_round(self, num_trials_per_round):
        r"""Sets the num_trials_per_round of this OptimizationResult.

        每轮生成数量

        :param num_trials_per_round: The num_trials_per_round of this OptimizationResult.
        :type num_trials_per_round: int
        """
        self._num_trials_per_round = num_trials_per_round

    @property
    def num_expected(self):
        r"""Gets the num_expected of this OptimizationResult.

        期望条目数

        :return: The num_expected of this OptimizationResult.
        :rtype: int
        """
        return self._num_expected

    @num_expected.setter
    def num_expected(self, num_expected):
        r"""Sets the num_expected of this OptimizationResult.

        期望条目数

        :param num_expected: The num_expected of this OptimizationResult.
        :type num_expected: int
        """
        self._num_expected = num_expected

    @property
    def num_strong_constraints(self):
        r"""Gets the num_strong_constraints of this OptimizationResult.

        强约束数量

        :return: The num_strong_constraints of this OptimizationResult.
        :rtype: int
        """
        return self._num_strong_constraints

    @num_strong_constraints.setter
    def num_strong_constraints(self, num_strong_constraints):
        r"""Sets the num_strong_constraints of this OptimizationResult.

        强约束数量

        :param num_strong_constraints: The num_strong_constraints of this OptimizationResult.
        :type num_strong_constraints: int
        """
        self._num_strong_constraints = num_strong_constraints

    @property
    def num_weak_constraints(self):
        r"""Gets the num_weak_constraints of this OptimizationResult.

        弱约束数量

        :return: The num_weak_constraints of this OptimizationResult.
        :rtype: int
        """
        return self._num_weak_constraints

    @num_weak_constraints.setter
    def num_weak_constraints(self, num_weak_constraints):
        r"""Sets the num_weak_constraints of this OptimizationResult.

        弱约束数量

        :param num_weak_constraints: The num_weak_constraints of this OptimizationResult.
        :type num_weak_constraints: int
        """
        self._num_weak_constraints = num_weak_constraints

    @property
    def prop_names(self):
        r"""Gets the prop_names of this OptimizationResult.

        分子ADMET属性名列表

        :return: The prop_names of this OptimizationResult.
        :rtype: list[str]
        """
        return self._prop_names

    @prop_names.setter
    def prop_names(self, prop_names):
        r"""Sets the prop_names of this OptimizationResult.

        分子ADMET属性名列表

        :param prop_names: The prop_names of this OptimizationResult.
        :type prop_names: list[str]
        """
        self._prop_names = prop_names

    @property
    def original(self):
        r"""Gets the original of this OptimizationResult.

        :return: The original of this OptimizationResult.
        :rtype: :class:`huaweicloudsdkeihealth.v1.PlainMoleculeItem`
        """
        return self._original

    @original.setter
    def original(self, original):
        r"""Sets the original of this OptimizationResult.

        :param original: The original of this OptimizationResult.
        :type original: :class:`huaweicloudsdkeihealth.v1.PlainMoleculeItem`
        """
        self._original = original

    @property
    def result(self):
        r"""Gets the result of this OptimizationResult.

        分子优化结果条目

        :return: The result of this OptimizationResult.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.OptimizationResultItem`]
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this OptimizationResult.

        分子优化结果条目

        :param result: The result of this OptimizationResult.
        :type result: list[:class:`huaweicloudsdkeihealth.v1.OptimizationResultItem`]
        """
        self._result = result

    @property
    def strong_constraints(self):
        r"""Gets the strong_constraints of this OptimizationResult.

        强约束集合

        :return: The strong_constraints of this OptimizationResult.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.MoleculeConstraint`]
        """
        return self._strong_constraints

    @strong_constraints.setter
    def strong_constraints(self, strong_constraints):
        r"""Sets the strong_constraints of this OptimizationResult.

        强约束集合

        :param strong_constraints: The strong_constraints of this OptimizationResult.
        :type strong_constraints: list[:class:`huaweicloudsdkeihealth.v1.MoleculeConstraint`]
        """
        self._strong_constraints = strong_constraints

    @property
    def weak_constraints(self):
        r"""Gets the weak_constraints of this OptimizationResult.

        弱约束集合

        :return: The weak_constraints of this OptimizationResult.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.MoleculeConstraint`]
        """
        return self._weak_constraints

    @weak_constraints.setter
    def weak_constraints(self, weak_constraints):
        r"""Sets the weak_constraints of this OptimizationResult.

        弱约束集合

        :param weak_constraints: The weak_constraints of this OptimizationResult.
        :type weak_constraints: list[:class:`huaweicloudsdkeihealth.v1.MoleculeConstraint`]
        """
        self._weak_constraints = weak_constraints

    @property
    def binding_site(self):
        r"""Gets the binding_site of this OptimizationResult.

        :return: The binding_site of this OptimizationResult.
        :rtype: :class:`huaweicloudsdkeihealth.v1.BindingSite`
        """
        return self._binding_site

    @binding_site.setter
    def binding_site(self, binding_site):
        r"""Sets the binding_site of this OptimizationResult.

        :param binding_site: The binding_site of this OptimizationResult.
        :type binding_site: :class:`huaweicloudsdkeihealth.v1.BindingSite`
        """
        self._binding_site = binding_site

    @property
    def custom_props(self):
        r"""Gets the custom_props of this OptimizationResult.

        用户已开启的自定义属性集合

        :return: The custom_props of this OptimizationResult.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.CustomProp`]
        """
        return self._custom_props

    @custom_props.setter
    def custom_props(self, custom_props):
        r"""Sets the custom_props of this OptimizationResult.

        用户已开启的自定义属性集合

        :param custom_props: The custom_props of this OptimizationResult.
        :type custom_props: list[:class:`huaweicloudsdkeihealth.v1.CustomProp`]
        """
        self._custom_props = custom_props

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
        if not isinstance(other, OptimizationResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
