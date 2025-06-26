# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunCatalogActionRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'name': 'str',
        'parameters': 'dict(str, str)',
        'description': 'str'
    }

    attribute_map = {
        'action': 'action',
        'name': 'name',
        'parameters': 'parameters',
        'description': 'description'
    }

    def __init__(self, action=None, name=None, parameters=None, description=None):
        r"""RunCatalogActionRequestBody

        The model defined in huaweicloud sdk

        :param action: catalog操作:bind或者unbind。
        :type action: str
        :param name: DLI侧catalog映射名称.
        :type name: str
        :param parameters: 
        :type parameters: dict(str, str)
        :param description: Catalog的描述信息。
        :type description: str
        """
        
        

        self._action = None
        self._name = None
        self._parameters = None
        self._description = None
        self.discriminator = None

        self.action = action
        self.name = name
        self.parameters = parameters
        if description is not None:
            self.description = description

    @property
    def action(self):
        r"""Gets the action of this RunCatalogActionRequestBody.

        catalog操作:bind或者unbind。

        :return: The action of this RunCatalogActionRequestBody.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this RunCatalogActionRequestBody.

        catalog操作:bind或者unbind。

        :param action: The action of this RunCatalogActionRequestBody.
        :type action: str
        """
        self._action = action

    @property
    def name(self):
        r"""Gets the name of this RunCatalogActionRequestBody.

        DLI侧catalog映射名称.

        :return: The name of this RunCatalogActionRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RunCatalogActionRequestBody.

        DLI侧catalog映射名称.

        :param name: The name of this RunCatalogActionRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def parameters(self):
        r"""Gets the parameters of this RunCatalogActionRequestBody.

        :return: The parameters of this RunCatalogActionRequestBody.
        :rtype: dict(str, str)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        r"""Sets the parameters of this RunCatalogActionRequestBody.

        :param parameters: The parameters of this RunCatalogActionRequestBody.
        :type parameters: dict(str, str)
        """
        self._parameters = parameters

    @property
    def description(self):
        r"""Gets the description of this RunCatalogActionRequestBody.

        Catalog的描述信息。

        :return: The description of this RunCatalogActionRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this RunCatalogActionRequestBody.

        Catalog的描述信息。

        :param description: The description of this RunCatalogActionRequestBody.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, RunCatalogActionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
