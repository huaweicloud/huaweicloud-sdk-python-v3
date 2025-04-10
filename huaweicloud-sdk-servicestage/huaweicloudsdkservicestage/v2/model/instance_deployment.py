# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceDeployment:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'variables': 'InstanceDeploymentVariables'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'variables': 'variables'
    }

    def __init__(self, instance_id=None, variables=None):
        r"""InstanceDeployment

        The model defined in huaweicloud sdk

        :param instance_id: 实例id
        :type instance_id: str
        :param variables: 
        :type variables: :class:`huaweicloudsdkservicestage.v2.InstanceDeploymentVariables`
        """
        
        

        self._instance_id = None
        self._variables = None
        self.discriminator = None

        self.instance_id = instance_id
        if variables is not None:
            self.variables = variables

    @property
    def instance_id(self):
        r"""Gets the instance_id of this InstanceDeployment.

        实例id

        :return: The instance_id of this InstanceDeployment.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this InstanceDeployment.

        实例id

        :param instance_id: The instance_id of this InstanceDeployment.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def variables(self):
        r"""Gets the variables of this InstanceDeployment.

        :return: The variables of this InstanceDeployment.
        :rtype: :class:`huaweicloudsdkservicestage.v2.InstanceDeploymentVariables`
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        r"""Sets the variables of this InstanceDeployment.

        :param variables: The variables of this InstanceDeployment.
        :type variables: :class:`huaweicloudsdkservicestage.v2.InstanceDeploymentVariables`
        """
        self._variables = variables

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
        if not isinstance(other, InstanceDeployment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
