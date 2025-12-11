# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowResourceClustersRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service_type': 'str'
    }

    attribute_map = {
        'service_type': 'service_type'
    }

    def __init__(self, service_type=None):
        r"""ShowResourceClustersRequest

        The model defined in huaweicloud sdk

        :param service_type: 集群服务类型，取值范围：“ecs”或“bms”。
        :type service_type: str
        """
        
        

        self._service_type = None
        self.discriminator = None

        if service_type is not None:
            self.service_type = service_type

    @property
    def service_type(self):
        r"""Gets the service_type of this ShowResourceClustersRequest.

        集群服务类型，取值范围：“ecs”或“bms”。

        :return: The service_type of this ShowResourceClustersRequest.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        r"""Sets the service_type of this ShowResourceClustersRequest.

        集群服务类型，取值范围：“ecs”或“bms”。

        :param service_type: The service_type of this ShowResourceClustersRequest.
        :type service_type: str
        """
        self._service_type = service_type

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
        if not isinstance(other, ShowResourceClustersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
