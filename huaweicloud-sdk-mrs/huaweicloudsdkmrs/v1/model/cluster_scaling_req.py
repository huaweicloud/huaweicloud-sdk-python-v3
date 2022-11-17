# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterScalingReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service_id': 'str',
        'plan_id': 'str',
        'parameters': 'ClusterScalingParams',
        'previous_values': 'dict(str, str)'
    }

    attribute_map = {
        'service_id': 'service_id',
        'plan_id': 'plan_id',
        'parameters': 'parameters',
        'previous_values': 'previous_values'
    }

    def __init__(self, service_id=None, plan_id=None, parameters=None, previous_values=None):
        """ClusterScalingReq

        The model defined in huaweicloud sdk

        :param service_id: 服务ID，为扩展接口，预留此参数。用户不需要配置。
        :type service_id: str
        :param plan_id: 套餐ID，为扩展接口，预留此参数。用户不需要配置。
        :type plan_id: str
        :param parameters: 
        :type parameters: :class:`huaweicloudsdkmrs.v1.ClusterScalingParams`
        :param previous_values: 扩展接口，预留此参数。用户不需要配置。
        :type previous_values: dict(str, str)
        """
        
        

        self._service_id = None
        self._plan_id = None
        self._parameters = None
        self._previous_values = None
        self.discriminator = None

        if service_id is not None:
            self.service_id = service_id
        if plan_id is not None:
            self.plan_id = plan_id
        self.parameters = parameters
        if previous_values is not None:
            self.previous_values = previous_values

    @property
    def service_id(self):
        """Gets the service_id of this ClusterScalingReq.

        服务ID，为扩展接口，预留此参数。用户不需要配置。

        :return: The service_id of this ClusterScalingReq.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this ClusterScalingReq.

        服务ID，为扩展接口，预留此参数。用户不需要配置。

        :param service_id: The service_id of this ClusterScalingReq.
        :type service_id: str
        """
        self._service_id = service_id

    @property
    def plan_id(self):
        """Gets the plan_id of this ClusterScalingReq.

        套餐ID，为扩展接口，预留此参数。用户不需要配置。

        :return: The plan_id of this ClusterScalingReq.
        :rtype: str
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        """Sets the plan_id of this ClusterScalingReq.

        套餐ID，为扩展接口，预留此参数。用户不需要配置。

        :param plan_id: The plan_id of this ClusterScalingReq.
        :type plan_id: str
        """
        self._plan_id = plan_id

    @property
    def parameters(self):
        """Gets the parameters of this ClusterScalingReq.

        :return: The parameters of this ClusterScalingReq.
        :rtype: :class:`huaweicloudsdkmrs.v1.ClusterScalingParams`
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this ClusterScalingReq.

        :param parameters: The parameters of this ClusterScalingReq.
        :type parameters: :class:`huaweicloudsdkmrs.v1.ClusterScalingParams`
        """
        self._parameters = parameters

    @property
    def previous_values(self):
        """Gets the previous_values of this ClusterScalingReq.

        扩展接口，预留此参数。用户不需要配置。

        :return: The previous_values of this ClusterScalingReq.
        :rtype: dict(str, str)
        """
        return self._previous_values

    @previous_values.setter
    def previous_values(self, previous_values):
        """Sets the previous_values of this ClusterScalingReq.

        扩展接口，预留此参数。用户不需要配置。

        :param previous_values: The previous_values of this ClusterScalingReq.
        :type previous_values: dict(str, str)
        """
        self._previous_values = previous_values

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
        if not isinstance(other, ClusterScalingReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
