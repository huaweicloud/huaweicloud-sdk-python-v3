# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Blueprint:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'blueprint_product_id': 'str',
        'blueprint_product_version': 'str',
        'variables': 'str',
        'is_blueprint_has_multi_account_resource': 'bool'
    }

    attribute_map = {
        'blueprint_product_id': 'blueprint_product_id',
        'blueprint_product_version': 'blueprint_product_version',
        'variables': 'variables',
        'is_blueprint_has_multi_account_resource': 'is_blueprint_has_multi_account_resource'
    }

    def __init__(self, blueprint_product_id=None, blueprint_product_version=None, variables=None, is_blueprint_has_multi_account_resource=None):
        r"""Blueprint

        The model defined in huaweicloud sdk

        :param blueprint_product_id: 模板ID。
        :type blueprint_product_id: str
        :param blueprint_product_version: 模板版本。
        :type blueprint_product_version: str
        :param variables: 模板部署参数。
        :type variables: str
        :param is_blueprint_has_multi_account_resource: 模板是否包含多账号资源。
        :type is_blueprint_has_multi_account_resource: bool
        """
        
        

        self._blueprint_product_id = None
        self._blueprint_product_version = None
        self._variables = None
        self._is_blueprint_has_multi_account_resource = None
        self.discriminator = None

        if blueprint_product_id is not None:
            self.blueprint_product_id = blueprint_product_id
        if blueprint_product_version is not None:
            self.blueprint_product_version = blueprint_product_version
        if variables is not None:
            self.variables = variables
        if is_blueprint_has_multi_account_resource is not None:
            self.is_blueprint_has_multi_account_resource = is_blueprint_has_multi_account_resource

    @property
    def blueprint_product_id(self):
        r"""Gets the blueprint_product_id of this Blueprint.

        模板ID。

        :return: The blueprint_product_id of this Blueprint.
        :rtype: str
        """
        return self._blueprint_product_id

    @blueprint_product_id.setter
    def blueprint_product_id(self, blueprint_product_id):
        r"""Sets the blueprint_product_id of this Blueprint.

        模板ID。

        :param blueprint_product_id: The blueprint_product_id of this Blueprint.
        :type blueprint_product_id: str
        """
        self._blueprint_product_id = blueprint_product_id

    @property
    def blueprint_product_version(self):
        r"""Gets the blueprint_product_version of this Blueprint.

        模板版本。

        :return: The blueprint_product_version of this Blueprint.
        :rtype: str
        """
        return self._blueprint_product_version

    @blueprint_product_version.setter
    def blueprint_product_version(self, blueprint_product_version):
        r"""Sets the blueprint_product_version of this Blueprint.

        模板版本。

        :param blueprint_product_version: The blueprint_product_version of this Blueprint.
        :type blueprint_product_version: str
        """
        self._blueprint_product_version = blueprint_product_version

    @property
    def variables(self):
        r"""Gets the variables of this Blueprint.

        模板部署参数。

        :return: The variables of this Blueprint.
        :rtype: str
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        r"""Sets the variables of this Blueprint.

        模板部署参数。

        :param variables: The variables of this Blueprint.
        :type variables: str
        """
        self._variables = variables

    @property
    def is_blueprint_has_multi_account_resource(self):
        r"""Gets the is_blueprint_has_multi_account_resource of this Blueprint.

        模板是否包含多账号资源。

        :return: The is_blueprint_has_multi_account_resource of this Blueprint.
        :rtype: bool
        """
        return self._is_blueprint_has_multi_account_resource

    @is_blueprint_has_multi_account_resource.setter
    def is_blueprint_has_multi_account_resource(self, is_blueprint_has_multi_account_resource):
        r"""Sets the is_blueprint_has_multi_account_resource of this Blueprint.

        模板是否包含多账号资源。

        :param is_blueprint_has_multi_account_resource: The is_blueprint_has_multi_account_resource of this Blueprint.
        :type is_blueprint_has_multi_account_resource: bool
        """
        self._is_blueprint_has_multi_account_resource = is_blueprint_has_multi_account_resource

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
        if not isinstance(other, Blueprint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
