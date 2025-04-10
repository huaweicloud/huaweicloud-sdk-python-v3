# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InteractionConstraintDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'interactions': 'list[Interaction]',
        'exclusive': 'bool',
        'operator': 'OperatorType'
    }

    attribute_map = {
        'interactions': 'interactions',
        'exclusive': 'exclusive',
        'operator': 'operator'
    }

    def __init__(self, interactions=None, exclusive=None, operator=None):
        r"""InteractionConstraintDto

        The model defined in huaweicloud sdk

        :param interactions: 相互作用力列表
        :type interactions: list[:class:`huaweicloudsdkeihealth.v1.Interaction`]
        :param exclusive: 是否排除指定的约束作用力
        :type exclusive: bool
        :param operator: 
        :type operator: :class:`huaweicloudsdkeihealth.v1.OperatorType`
        """
        
        

        self._interactions = None
        self._exclusive = None
        self._operator = None
        self.discriminator = None

        self.interactions = interactions
        self.exclusive = exclusive
        if operator is not None:
            self.operator = operator

    @property
    def interactions(self):
        r"""Gets the interactions of this InteractionConstraintDto.

        相互作用力列表

        :return: The interactions of this InteractionConstraintDto.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.Interaction`]
        """
        return self._interactions

    @interactions.setter
    def interactions(self, interactions):
        r"""Sets the interactions of this InteractionConstraintDto.

        相互作用力列表

        :param interactions: The interactions of this InteractionConstraintDto.
        :type interactions: list[:class:`huaweicloudsdkeihealth.v1.Interaction`]
        """
        self._interactions = interactions

    @property
    def exclusive(self):
        r"""Gets the exclusive of this InteractionConstraintDto.

        是否排除指定的约束作用力

        :return: The exclusive of this InteractionConstraintDto.
        :rtype: bool
        """
        return self._exclusive

    @exclusive.setter
    def exclusive(self, exclusive):
        r"""Sets the exclusive of this InteractionConstraintDto.

        是否排除指定的约束作用力

        :param exclusive: The exclusive of this InteractionConstraintDto.
        :type exclusive: bool
        """
        self._exclusive = exclusive

    @property
    def operator(self):
        r"""Gets the operator of this InteractionConstraintDto.

        :return: The operator of this InteractionConstraintDto.
        :rtype: :class:`huaweicloudsdkeihealth.v1.OperatorType`
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        r"""Sets the operator of this InteractionConstraintDto.

        :param operator: The operator of this InteractionConstraintDto.
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
        if not isinstance(other, InteractionConstraintDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
