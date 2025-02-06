# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTaskRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service_type': 'str',
        'body': 'TaskDto'
    }

    attribute_map = {
        'service_type': 'service_type',
        'body': 'body'
    }

    def __init__(self, service_type=None, body=None):
        """CreateTaskRequest

        The model defined in huaweicloud sdk

        :param service_type: 服务类型，针对不同服务，为用户提前填充对应值，用户侧不需单独赋值；二维切割-方形件固定为 regular-plate，二维切割-异形件固定为 irregular-textile， 数学规划求解器固定为 optverse-mpsolver
        :type service_type: str
        :param body: Body of the CreateTaskRequest
        :type body: :class:`huaweicloudsdkoptverse.v2.TaskDto`
        """
        
        

        self._service_type = None
        self._body = None
        self.discriminator = None

        self.service_type = service_type
        if body is not None:
            self.body = body

    @property
    def service_type(self):
        """Gets the service_type of this CreateTaskRequest.

        服务类型，针对不同服务，为用户提前填充对应值，用户侧不需单独赋值；二维切割-方形件固定为 regular-plate，二维切割-异形件固定为 irregular-textile， 数学规划求解器固定为 optverse-mpsolver

        :return: The service_type of this CreateTaskRequest.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this CreateTaskRequest.

        服务类型，针对不同服务，为用户提前填充对应值，用户侧不需单独赋值；二维切割-方形件固定为 regular-plate，二维切割-异形件固定为 irregular-textile， 数学规划求解器固定为 optverse-mpsolver

        :param service_type: The service_type of this CreateTaskRequest.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def body(self):
        """Gets the body of this CreateTaskRequest.

        :return: The body of this CreateTaskRequest.
        :rtype: :class:`huaweicloudsdkoptverse.v2.TaskDto`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateTaskRequest.

        :param body: The body of this CreateTaskRequest.
        :type body: :class:`huaweicloudsdkoptverse.v2.TaskDto`
        """
        self._body = body

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
        if not isinstance(other, CreateTaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
