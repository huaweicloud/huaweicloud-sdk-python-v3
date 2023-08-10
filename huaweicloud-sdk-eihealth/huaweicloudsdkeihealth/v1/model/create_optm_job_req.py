# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateOptmJobReq:

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
        'smiles': 'str',
        'binding_site': 'BindSiteDto',
        'weak_constraints': 'list[WeakConstraintDto]',
        'strong_constraints': 'list[StrongConstraintDto]',
        'num_trials': 'int'
    }

    attribute_map = {
        'basic_info': 'basic_info',
        'smiles': 'smiles',
        'binding_site': 'binding_site',
        'weak_constraints': 'weak_constraints',
        'strong_constraints': 'strong_constraints',
        'num_trials': 'num_trials'
    }

    def __init__(self, basic_info=None, smiles=None, binding_site=None, weak_constraints=None, strong_constraints=None, num_trials=None):
        """CreateOptmJobReq

        The model defined in huaweicloud sdk

        :param basic_info: 
        :type basic_info: :class:`huaweicloudsdkeihealth.v1.CreateDrugJobBasicInfo`
        :param smiles: 分子SMILES表达式
        :type smiles: str
        :param binding_site: 
        :type binding_site: :class:`huaweicloudsdkeihealth.v1.BindSiteDto`
        :param weak_constraints: 弱约束集合
        :type weak_constraints: list[:class:`huaweicloudsdkeihealth.v1.WeakConstraintDto`]
        :param strong_constraints: 强约束集合
        :type strong_constraints: list[:class:`huaweicloudsdkeihealth.v1.StrongConstraintDto`]
        :param num_trials: 生成分子数量
        :type num_trials: int
        """
        
        

        self._basic_info = None
        self._smiles = None
        self._binding_site = None
        self._weak_constraints = None
        self._strong_constraints = None
        self._num_trials = None
        self.discriminator = None

        self.basic_info = basic_info
        self.smiles = smiles
        if binding_site is not None:
            self.binding_site = binding_site
        if weak_constraints is not None:
            self.weak_constraints = weak_constraints
        if strong_constraints is not None:
            self.strong_constraints = strong_constraints
        if num_trials is not None:
            self.num_trials = num_trials

    @property
    def basic_info(self):
        """Gets the basic_info of this CreateOptmJobReq.

        :return: The basic_info of this CreateOptmJobReq.
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateDrugJobBasicInfo`
        """
        return self._basic_info

    @basic_info.setter
    def basic_info(self, basic_info):
        """Sets the basic_info of this CreateOptmJobReq.

        :param basic_info: The basic_info of this CreateOptmJobReq.
        :type basic_info: :class:`huaweicloudsdkeihealth.v1.CreateDrugJobBasicInfo`
        """
        self._basic_info = basic_info

    @property
    def smiles(self):
        """Gets the smiles of this CreateOptmJobReq.

        分子SMILES表达式

        :return: The smiles of this CreateOptmJobReq.
        :rtype: str
        """
        return self._smiles

    @smiles.setter
    def smiles(self, smiles):
        """Sets the smiles of this CreateOptmJobReq.

        分子SMILES表达式

        :param smiles: The smiles of this CreateOptmJobReq.
        :type smiles: str
        """
        self._smiles = smiles

    @property
    def binding_site(self):
        """Gets the binding_site of this CreateOptmJobReq.

        :return: The binding_site of this CreateOptmJobReq.
        :rtype: :class:`huaweicloudsdkeihealth.v1.BindSiteDto`
        """
        return self._binding_site

    @binding_site.setter
    def binding_site(self, binding_site):
        """Sets the binding_site of this CreateOptmJobReq.

        :param binding_site: The binding_site of this CreateOptmJobReq.
        :type binding_site: :class:`huaweicloudsdkeihealth.v1.BindSiteDto`
        """
        self._binding_site = binding_site

    @property
    def weak_constraints(self):
        """Gets the weak_constraints of this CreateOptmJobReq.

        弱约束集合

        :return: The weak_constraints of this CreateOptmJobReq.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.WeakConstraintDto`]
        """
        return self._weak_constraints

    @weak_constraints.setter
    def weak_constraints(self, weak_constraints):
        """Sets the weak_constraints of this CreateOptmJobReq.

        弱约束集合

        :param weak_constraints: The weak_constraints of this CreateOptmJobReq.
        :type weak_constraints: list[:class:`huaweicloudsdkeihealth.v1.WeakConstraintDto`]
        """
        self._weak_constraints = weak_constraints

    @property
    def strong_constraints(self):
        """Gets the strong_constraints of this CreateOptmJobReq.

        强约束集合

        :return: The strong_constraints of this CreateOptmJobReq.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.StrongConstraintDto`]
        """
        return self._strong_constraints

    @strong_constraints.setter
    def strong_constraints(self, strong_constraints):
        """Sets the strong_constraints of this CreateOptmJobReq.

        强约束集合

        :param strong_constraints: The strong_constraints of this CreateOptmJobReq.
        :type strong_constraints: list[:class:`huaweicloudsdkeihealth.v1.StrongConstraintDto`]
        """
        self._strong_constraints = strong_constraints

    @property
    def num_trials(self):
        """Gets the num_trials of this CreateOptmJobReq.

        生成分子数量

        :return: The num_trials of this CreateOptmJobReq.
        :rtype: int
        """
        return self._num_trials

    @num_trials.setter
    def num_trials(self, num_trials):
        """Sets the num_trials of this CreateOptmJobReq.

        生成分子数量

        :param num_trials: The num_trials of this CreateOptmJobReq.
        :type num_trials: int
        """
        self._num_trials = num_trials

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
        if not isinstance(other, CreateOptmJobReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
