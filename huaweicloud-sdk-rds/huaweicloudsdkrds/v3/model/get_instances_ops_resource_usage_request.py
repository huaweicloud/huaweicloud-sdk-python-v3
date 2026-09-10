# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetInstancesOpsResourceUsageRequest:

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
        'x_language': 'str',
        'resource_type': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'x_language': 'X-Language',
        'resource_type': 'resource_type'
    }

    def __init__(self, instance_id=None, x_language=None, resource_type=None):
        r"""GetInstancesOpsResourceUsageRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param x_language: 语言。默认en-us。
        :type x_language: str
        :param resource_type: 资源类型。取值范围：cpu、mem、disk、disk_week、io。
        :type resource_type: str
        """
        
        

        self._instance_id = None
        self._x_language = None
        self._resource_type = None
        self.discriminator = None

        self.instance_id = instance_id
        if x_language is not None:
            self.x_language = x_language
        if resource_type is not None:
            self.resource_type = resource_type

    @property
    def instance_id(self):
        r"""Gets the instance_id of this GetInstancesOpsResourceUsageRequest.

        实例ID

        :return: The instance_id of this GetInstancesOpsResourceUsageRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this GetInstancesOpsResourceUsageRequest.

        实例ID

        :param instance_id: The instance_id of this GetInstancesOpsResourceUsageRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def x_language(self):
        r"""Gets the x_language of this GetInstancesOpsResourceUsageRequest.

        语言。默认en-us。

        :return: The x_language of this GetInstancesOpsResourceUsageRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this GetInstancesOpsResourceUsageRequest.

        语言。默认en-us。

        :param x_language: The x_language of this GetInstancesOpsResourceUsageRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def resource_type(self):
        r"""Gets the resource_type of this GetInstancesOpsResourceUsageRequest.

        资源类型。取值范围：cpu、mem、disk、disk_week、io。

        :return: The resource_type of this GetInstancesOpsResourceUsageRequest.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this GetInstancesOpsResourceUsageRequest.

        资源类型。取值范围：cpu、mem、disk、disk_week、io。

        :param resource_type: The resource_type of this GetInstancesOpsResourceUsageRequest.
        :type resource_type: str
        """
        self._resource_type = resource_type

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GetInstancesOpsResourceUsageRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
