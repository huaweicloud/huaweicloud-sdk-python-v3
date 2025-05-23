# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VarOverridesPrimitiveTypeHolder:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'var_overrides': 'VarOverridesPrimitiveTypeHolderVarOverrides'
    }

    attribute_map = {
        'var_overrides': 'var_overrides'
    }

    def __init__(self, var_overrides=None):
        r"""VarOverridesPrimitiveTypeHolder

        The model defined in huaweicloud sdk

        :param var_overrides: 
        :type var_overrides: :class:`huaweicloudsdkaos.v1.VarOverridesPrimitiveTypeHolderVarOverrides`
        """
        
        

        self._var_overrides = None
        self.discriminator = None

        if var_overrides is not None:
            self.var_overrides = var_overrides

    @property
    def var_overrides(self):
        r"""Gets the var_overrides of this VarOverridesPrimitiveTypeHolder.

        :return: The var_overrides of this VarOverridesPrimitiveTypeHolder.
        :rtype: :class:`huaweicloudsdkaos.v1.VarOverridesPrimitiveTypeHolderVarOverrides`
        """
        return self._var_overrides

    @var_overrides.setter
    def var_overrides(self, var_overrides):
        r"""Sets the var_overrides of this VarOverridesPrimitiveTypeHolder.

        :param var_overrides: The var_overrides of this VarOverridesPrimitiveTypeHolder.
        :type var_overrides: :class:`huaweicloudsdkaos.v1.VarOverridesPrimitiveTypeHolderVarOverrides`
        """
        self._var_overrides = var_overrides

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
        if not isinstance(other, VarOverridesPrimitiveTypeHolder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
