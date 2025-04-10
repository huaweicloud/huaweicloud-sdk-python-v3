# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StructureConstraintParamsDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'structs': 'list[str]',
        'exclusive': 'bool',
        'operator': 'OperatorType'
    }

    attribute_map = {
        'structs': 'structs',
        'exclusive': 'exclusive',
        'operator': 'operator'
    }

    def __init__(self, structs=None, exclusive=None, operator=None):
        r"""StructureConstraintParamsDto

        The model defined in huaweicloud sdk

        :param structs: 子结构SMILES
        :type structs: list[str]
        :param exclusive: 是否排除子结构
        :type exclusive: bool
        :param operator: 
        :type operator: :class:`huaweicloudsdkeihealth.v1.OperatorType`
        """
        
        

        self._structs = None
        self._exclusive = None
        self._operator = None
        self.discriminator = None

        self.structs = structs
        self.exclusive = exclusive
        if operator is not None:
            self.operator = operator

    @property
    def structs(self):
        r"""Gets the structs of this StructureConstraintParamsDto.

        子结构SMILES

        :return: The structs of this StructureConstraintParamsDto.
        :rtype: list[str]
        """
        return self._structs

    @structs.setter
    def structs(self, structs):
        r"""Sets the structs of this StructureConstraintParamsDto.

        子结构SMILES

        :param structs: The structs of this StructureConstraintParamsDto.
        :type structs: list[str]
        """
        self._structs = structs

    @property
    def exclusive(self):
        r"""Gets the exclusive of this StructureConstraintParamsDto.

        是否排除子结构

        :return: The exclusive of this StructureConstraintParamsDto.
        :rtype: bool
        """
        return self._exclusive

    @exclusive.setter
    def exclusive(self, exclusive):
        r"""Sets the exclusive of this StructureConstraintParamsDto.

        是否排除子结构

        :param exclusive: The exclusive of this StructureConstraintParamsDto.
        :type exclusive: bool
        """
        self._exclusive = exclusive

    @property
    def operator(self):
        r"""Gets the operator of this StructureConstraintParamsDto.

        :return: The operator of this StructureConstraintParamsDto.
        :rtype: :class:`huaweicloudsdkeihealth.v1.OperatorType`
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        r"""Sets the operator of this StructureConstraintParamsDto.

        :param operator: The operator of this StructureConstraintParamsDto.
        :type operator: :class:`huaweicloudsdkeihealth.v1.OperatorType`
        """
        self._operator = operator

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
        if not isinstance(other, StructureConstraintParamsDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
