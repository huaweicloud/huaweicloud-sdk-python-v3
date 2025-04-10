# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateGovPolicy:

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
        'selector': 'GovSelector',
        'spec': 'object'
    }

    attribute_map = {
        'name': 'name',
        'selector': 'selector',
        'spec': 'spec'
    }

    def __init__(self, name=None, selector=None, spec=None):
        r"""CreateGovPolicy

        The model defined in huaweicloud sdk

        :param name: 治理策略名称
        :type name: str
        :param selector: 
        :type selector: :class:`huaweicloudsdkcse.v1.GovSelector`
        :param spec: 治理策略定义内容
        :type spec: object
        """
        
        

        self._name = None
        self._selector = None
        self._spec = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if selector is not None:
            self.selector = selector
        if spec is not None:
            self.spec = spec

    @property
    def name(self):
        r"""Gets the name of this CreateGovPolicy.

        治理策略名称

        :return: The name of this CreateGovPolicy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateGovPolicy.

        治理策略名称

        :param name: The name of this CreateGovPolicy.
        :type name: str
        """
        self._name = name

    @property
    def selector(self):
        r"""Gets the selector of this CreateGovPolicy.

        :return: The selector of this CreateGovPolicy.
        :rtype: :class:`huaweicloudsdkcse.v1.GovSelector`
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        r"""Sets the selector of this CreateGovPolicy.

        :param selector: The selector of this CreateGovPolicy.
        :type selector: :class:`huaweicloudsdkcse.v1.GovSelector`
        """
        self._selector = selector

    @property
    def spec(self):
        r"""Gets the spec of this CreateGovPolicy.

        治理策略定义内容

        :return: The spec of this CreateGovPolicy.
        :rtype: object
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        r"""Sets the spec of this CreateGovPolicy.

        治理策略定义内容

        :param spec: The spec of this CreateGovPolicy.
        :type spec: object
        """
        self._spec = spec

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
        if not isinstance(other, CreateGovPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
