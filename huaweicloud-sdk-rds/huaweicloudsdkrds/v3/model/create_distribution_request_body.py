# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDistributionRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'distributor_instance_id': 'str'
    }

    attribute_map = {
        'distributor_instance_id': 'distributor_instance_id'
    }

    def __init__(self, distributor_instance_id=None):
        r"""CreateDistributionRequestBody

        The model defined in huaweicloud sdk

        :param distributor_instance_id: 配置为分发服务器的实例id。
        :type distributor_instance_id: str
        """
        
        

        self._distributor_instance_id = None
        self.discriminator = None

        self.distributor_instance_id = distributor_instance_id

    @property
    def distributor_instance_id(self):
        r"""Gets the distributor_instance_id of this CreateDistributionRequestBody.

        配置为分发服务器的实例id。

        :return: The distributor_instance_id of this CreateDistributionRequestBody.
        :rtype: str
        """
        return self._distributor_instance_id

    @distributor_instance_id.setter
    def distributor_instance_id(self, distributor_instance_id):
        r"""Sets the distributor_instance_id of this CreateDistributionRequestBody.

        配置为分发服务器的实例id。

        :param distributor_instance_id: The distributor_instance_id of this CreateDistributionRequestBody.
        :type distributor_instance_id: str
        """
        self._distributor_instance_id = distributor_instance_id

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
        if not isinstance(other, CreateDistributionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
