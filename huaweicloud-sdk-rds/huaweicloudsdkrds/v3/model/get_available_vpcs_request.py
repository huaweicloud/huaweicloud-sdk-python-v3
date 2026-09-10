# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetAvailableVpcsRequest:

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
        'vpc_id': 'str',
        'vpc_name': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'vpc_id': 'vpc_id',
        'vpc_name': 'vpc_name'
    }

    def __init__(self, instance_id=None, vpc_id=None, vpc_name=None):
        r"""GetAvailableVpcsRequest

        The model defined in huaweicloud sdk

        :param instance_id: 主实例ID
        :type instance_id: str
        :param vpc_id: 如果传入vpc_id, 则只返回该VPC下的可用子网
        :type vpc_id: str
        :param vpc_name: 如果传入vpc_name, 则只返回该name对应的VPC下的可用子网
        :type vpc_name: str
        """
        
        

        self._instance_id = None
        self._vpc_id = None
        self._vpc_name = None
        self.discriminator = None

        self.instance_id = instance_id
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if vpc_name is not None:
            self.vpc_name = vpc_name

    @property
    def instance_id(self):
        r"""Gets the instance_id of this GetAvailableVpcsRequest.

        主实例ID

        :return: The instance_id of this GetAvailableVpcsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this GetAvailableVpcsRequest.

        主实例ID

        :param instance_id: The instance_id of this GetAvailableVpcsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this GetAvailableVpcsRequest.

        如果传入vpc_id, 则只返回该VPC下的可用子网

        :return: The vpc_id of this GetAvailableVpcsRequest.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this GetAvailableVpcsRequest.

        如果传入vpc_id, 则只返回该VPC下的可用子网

        :param vpc_id: The vpc_id of this GetAvailableVpcsRequest.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def vpc_name(self):
        r"""Gets the vpc_name of this GetAvailableVpcsRequest.

        如果传入vpc_name, 则只返回该name对应的VPC下的可用子网

        :return: The vpc_name of this GetAvailableVpcsRequest.
        :rtype: str
        """
        return self._vpc_name

    @vpc_name.setter
    def vpc_name(self, vpc_name):
        r"""Sets the vpc_name of this GetAvailableVpcsRequest.

        如果传入vpc_name, 则只返回该name对应的VPC下的可用子网

        :param vpc_name: The vpc_name of this GetAvailableVpcsRequest.
        :type vpc_name: str
        """
        self._vpc_name = vpc_name

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
        if not isinstance(other, GetAvailableVpcsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
