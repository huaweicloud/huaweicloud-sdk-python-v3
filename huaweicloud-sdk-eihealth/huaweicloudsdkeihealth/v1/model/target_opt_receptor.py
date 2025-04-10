# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TargetOptReceptor:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file': 'ReceptorDrugFile',
        'balanced_charge': 'bool',
        'water_model': 'str',
        'force_field': 'str',
        'ion_type': 'str',
        'ion_concentration': 'float'
    }

    attribute_map = {
        'file': 'file',
        'balanced_charge': 'balanced_charge',
        'water_model': 'water_model',
        'force_field': 'force_field',
        'ion_type': 'ion_type',
        'ion_concentration': 'ion_concentration'
    }

    def __init__(self, file=None, balanced_charge=None, water_model=None, force_field=None, ion_type=None, ion_concentration=None):
        r"""TargetOptReceptor

        The model defined in huaweicloud sdk

        :param file: 
        :type file: :class:`huaweicloudsdkeihealth.v1.ReceptorDrugFile`
        :param balanced_charge: 是否平衡电荷
        :type balanced_charge: bool
        :param water_model: 水模型, 支持选择spc, spce, tip3p, tip4p, tip5p
        :type water_model: str
        :param force_field: 蛋白立场，支持选择amber03, amber94, amber96, amber99, amber99sb, amber99sb-ildn, amberGS, charmm27, oplsaa, gromos43a1, gromos43a2, gromos45a3, gromos53a5, gromos53a6, gromos54a7
        :type force_field: str
        :param ion_type: 离子种类，支持选择NaCl、MgCl2、None，若设置了平衡电荷不支持选择None
        :type ion_type: str
        :param ion_concentration: 离子浓度，单位mol/L，若离子种类设置为None离子浓度不支持设置
        :type ion_concentration: float
        """
        
        

        self._file = None
        self._balanced_charge = None
        self._water_model = None
        self._force_field = None
        self._ion_type = None
        self._ion_concentration = None
        self.discriminator = None

        self.file = file
        if balanced_charge is not None:
            self.balanced_charge = balanced_charge
        if water_model is not None:
            self.water_model = water_model
        if force_field is not None:
            self.force_field = force_field
        if ion_type is not None:
            self.ion_type = ion_type
        if ion_concentration is not None:
            self.ion_concentration = ion_concentration

    @property
    def file(self):
        r"""Gets the file of this TargetOptReceptor.

        :return: The file of this TargetOptReceptor.
        :rtype: :class:`huaweicloudsdkeihealth.v1.ReceptorDrugFile`
        """
        return self._file

    @file.setter
    def file(self, file):
        r"""Sets the file of this TargetOptReceptor.

        :param file: The file of this TargetOptReceptor.
        :type file: :class:`huaweicloudsdkeihealth.v1.ReceptorDrugFile`
        """
        self._file = file

    @property
    def balanced_charge(self):
        r"""Gets the balanced_charge of this TargetOptReceptor.

        是否平衡电荷

        :return: The balanced_charge of this TargetOptReceptor.
        :rtype: bool
        """
        return self._balanced_charge

    @balanced_charge.setter
    def balanced_charge(self, balanced_charge):
        r"""Sets the balanced_charge of this TargetOptReceptor.

        是否平衡电荷

        :param balanced_charge: The balanced_charge of this TargetOptReceptor.
        :type balanced_charge: bool
        """
        self._balanced_charge = balanced_charge

    @property
    def water_model(self):
        r"""Gets the water_model of this TargetOptReceptor.

        水模型, 支持选择spc, spce, tip3p, tip4p, tip5p

        :return: The water_model of this TargetOptReceptor.
        :rtype: str
        """
        return self._water_model

    @water_model.setter
    def water_model(self, water_model):
        r"""Sets the water_model of this TargetOptReceptor.

        水模型, 支持选择spc, spce, tip3p, tip4p, tip5p

        :param water_model: The water_model of this TargetOptReceptor.
        :type water_model: str
        """
        self._water_model = water_model

    @property
    def force_field(self):
        r"""Gets the force_field of this TargetOptReceptor.

        蛋白立场，支持选择amber03, amber94, amber96, amber99, amber99sb, amber99sb-ildn, amberGS, charmm27, oplsaa, gromos43a1, gromos43a2, gromos45a3, gromos53a5, gromos53a6, gromos54a7

        :return: The force_field of this TargetOptReceptor.
        :rtype: str
        """
        return self._force_field

    @force_field.setter
    def force_field(self, force_field):
        r"""Sets the force_field of this TargetOptReceptor.

        蛋白立场，支持选择amber03, amber94, amber96, amber99, amber99sb, amber99sb-ildn, amberGS, charmm27, oplsaa, gromos43a1, gromos43a2, gromos45a3, gromos53a5, gromos53a6, gromos54a7

        :param force_field: The force_field of this TargetOptReceptor.
        :type force_field: str
        """
        self._force_field = force_field

    @property
    def ion_type(self):
        r"""Gets the ion_type of this TargetOptReceptor.

        离子种类，支持选择NaCl、MgCl2、None，若设置了平衡电荷不支持选择None

        :return: The ion_type of this TargetOptReceptor.
        :rtype: str
        """
        return self._ion_type

    @ion_type.setter
    def ion_type(self, ion_type):
        r"""Sets the ion_type of this TargetOptReceptor.

        离子种类，支持选择NaCl、MgCl2、None，若设置了平衡电荷不支持选择None

        :param ion_type: The ion_type of this TargetOptReceptor.
        :type ion_type: str
        """
        self._ion_type = ion_type

    @property
    def ion_concentration(self):
        r"""Gets the ion_concentration of this TargetOptReceptor.

        离子浓度，单位mol/L，若离子种类设置为None离子浓度不支持设置

        :return: The ion_concentration of this TargetOptReceptor.
        :rtype: float
        """
        return self._ion_concentration

    @ion_concentration.setter
    def ion_concentration(self, ion_concentration):
        r"""Sets the ion_concentration of this TargetOptReceptor.

        离子浓度，单位mol/L，若离子种类设置为None离子浓度不支持设置

        :param ion_concentration: The ion_concentration of this TargetOptReceptor.
        :type ion_concentration: float
        """
        self._ion_concentration = ion_concentration

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
        if not isinstance(other, TargetOptReceptor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
