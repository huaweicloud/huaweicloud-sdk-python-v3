# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EngineModifyReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flavor': 'str',
        'inputs': 'dict(str, str)'
    }

    attribute_map = {
        'flavor': 'flavor',
        'inputs': 'inputs'
    }

    def __init__(self, flavor=None, inputs=None):
        r"""EngineModifyReq

        The model defined in huaweicloud sdk

        :param flavor: 变更的规格
        :type flavor: str
        :param inputs: 变更的配置，覆盖组件bp的input参数
        :type inputs: dict(str, str)
        """
        
        

        self._flavor = None
        self._inputs = None
        self.discriminator = None

        self.flavor = flavor
        if inputs is not None:
            self.inputs = inputs

    @property
    def flavor(self):
        r"""Gets the flavor of this EngineModifyReq.

        变更的规格

        :return: The flavor of this EngineModifyReq.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this EngineModifyReq.

        变更的规格

        :param flavor: The flavor of this EngineModifyReq.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def inputs(self):
        r"""Gets the inputs of this EngineModifyReq.

        变更的配置，覆盖组件bp的input参数

        :return: The inputs of this EngineModifyReq.
        :rtype: dict(str, str)
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        r"""Sets the inputs of this EngineModifyReq.

        变更的配置，覆盖组件bp的input参数

        :param inputs: The inputs of this EngineModifyReq.
        :type inputs: dict(str, str)
        """
        self._inputs = inputs

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
        if not isinstance(other, EngineModifyReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
