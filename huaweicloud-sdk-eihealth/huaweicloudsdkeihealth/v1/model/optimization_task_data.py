# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OptimizationTaskData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'smiles': 'str',
        'num_trials': 'int',
        'strong_constraints': 'list[MoleculeConstraint]',
        'weak_constraints': 'list[MoleculeConstraint]',
        'num_expected': 'int',
        'binding_site': 'BindingSite',
        'custom_props': 'list[CustomProp]'
    }

    attribute_map = {
        'smiles': 'smiles',
        'num_trials': 'num_trials',
        'strong_constraints': 'strong_constraints',
        'weak_constraints': 'weak_constraints',
        'num_expected': 'num_expected',
        'binding_site': 'binding_site',
        'custom_props': 'custom_props'
    }

    def __init__(self, smiles=None, num_trials=None, strong_constraints=None, weak_constraints=None, num_expected=None, binding_site=None, custom_props=None):
        """OptimizationTaskData

        The model defined in huaweicloud sdk

        :param smiles: 分子SMILES表达式
        :type smiles: str
        :param num_trials: 生成分子数量
        :type num_trials: int
        :param strong_constraints: 强约束集合
        :type strong_constraints: list[:class:`huaweicloudsdkeihealth.v1.MoleculeConstraint`]
        :param weak_constraints: 弱约束集合
        :type weak_constraints: list[:class:`huaweicloudsdkeihealth.v1.MoleculeConstraint`]
        :param num_expected: 期望最大返回条目数（排序后取Top）
        :type num_expected: int
        :param binding_site: 
        :type binding_site: :class:`huaweicloudsdkeihealth.v1.BindingSite`
        :param custom_props: 用户已开启的自定义属性集合
        :type custom_props: list[:class:`huaweicloudsdkeihealth.v1.CustomProp`]
        """
        
        

        self._smiles = None
        self._num_trials = None
        self._strong_constraints = None
        self._weak_constraints = None
        self._num_expected = None
        self._binding_site = None
        self._custom_props = None
        self.discriminator = None

        self.smiles = smiles
        if num_trials is not None:
            self.num_trials = num_trials
        if strong_constraints is not None:
            self.strong_constraints = strong_constraints
        if weak_constraints is not None:
            self.weak_constraints = weak_constraints
        if num_expected is not None:
            self.num_expected = num_expected
        if binding_site is not None:
            self.binding_site = binding_site
        if custom_props is not None:
            self.custom_props = custom_props

    @property
    def smiles(self):
        """Gets the smiles of this OptimizationTaskData.

        分子SMILES表达式

        :return: The smiles of this OptimizationTaskData.
        :rtype: str
        """
        return self._smiles

    @smiles.setter
    def smiles(self, smiles):
        """Sets the smiles of this OptimizationTaskData.

        分子SMILES表达式

        :param smiles: The smiles of this OptimizationTaskData.
        :type smiles: str
        """
        self._smiles = smiles

    @property
    def num_trials(self):
        """Gets the num_trials of this OptimizationTaskData.

        生成分子数量

        :return: The num_trials of this OptimizationTaskData.
        :rtype: int
        """
        return self._num_trials

    @num_trials.setter
    def num_trials(self, num_trials):
        """Sets the num_trials of this OptimizationTaskData.

        生成分子数量

        :param num_trials: The num_trials of this OptimizationTaskData.
        :type num_trials: int
        """
        self._num_trials = num_trials

    @property
    def strong_constraints(self):
        """Gets the strong_constraints of this OptimizationTaskData.

        强约束集合

        :return: The strong_constraints of this OptimizationTaskData.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.MoleculeConstraint`]
        """
        return self._strong_constraints

    @strong_constraints.setter
    def strong_constraints(self, strong_constraints):
        """Sets the strong_constraints of this OptimizationTaskData.

        强约束集合

        :param strong_constraints: The strong_constraints of this OptimizationTaskData.
        :type strong_constraints: list[:class:`huaweicloudsdkeihealth.v1.MoleculeConstraint`]
        """
        self._strong_constraints = strong_constraints

    @property
    def weak_constraints(self):
        """Gets the weak_constraints of this OptimizationTaskData.

        弱约束集合

        :return: The weak_constraints of this OptimizationTaskData.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.MoleculeConstraint`]
        """
        return self._weak_constraints

    @weak_constraints.setter
    def weak_constraints(self, weak_constraints):
        """Sets the weak_constraints of this OptimizationTaskData.

        弱约束集合

        :param weak_constraints: The weak_constraints of this OptimizationTaskData.
        :type weak_constraints: list[:class:`huaweicloudsdkeihealth.v1.MoleculeConstraint`]
        """
        self._weak_constraints = weak_constraints

    @property
    def num_expected(self):
        """Gets the num_expected of this OptimizationTaskData.

        期望最大返回条目数（排序后取Top）

        :return: The num_expected of this OptimizationTaskData.
        :rtype: int
        """
        return self._num_expected

    @num_expected.setter
    def num_expected(self, num_expected):
        """Sets the num_expected of this OptimizationTaskData.

        期望最大返回条目数（排序后取Top）

        :param num_expected: The num_expected of this OptimizationTaskData.
        :type num_expected: int
        """
        self._num_expected = num_expected

    @property
    def binding_site(self):
        """Gets the binding_site of this OptimizationTaskData.

        :return: The binding_site of this OptimizationTaskData.
        :rtype: :class:`huaweicloudsdkeihealth.v1.BindingSite`
        """
        return self._binding_site

    @binding_site.setter
    def binding_site(self, binding_site):
        """Sets the binding_site of this OptimizationTaskData.

        :param binding_site: The binding_site of this OptimizationTaskData.
        :type binding_site: :class:`huaweicloudsdkeihealth.v1.BindingSite`
        """
        self._binding_site = binding_site

    @property
    def custom_props(self):
        """Gets the custom_props of this OptimizationTaskData.

        用户已开启的自定义属性集合

        :return: The custom_props of this OptimizationTaskData.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.CustomProp`]
        """
        return self._custom_props

    @custom_props.setter
    def custom_props(self, custom_props):
        """Sets the custom_props of this OptimizationTaskData.

        用户已开启的自定义属性集合

        :param custom_props: The custom_props of this OptimizationTaskData.
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
        if not isinstance(other, OptimizationTaskData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
