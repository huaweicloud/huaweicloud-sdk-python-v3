# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EndpointList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'endpoints': 'list[Endpoint]',
        'total': 'int'
    }

    attribute_map = {
        'endpoints': 'endpoints',
        'total': 'total'
    }

    def __init__(self, endpoints=None, total=None):
        r"""EndpointList

        The model defined in huaweicloud sdk

        :param endpoints: Endpoint的具体信息
        :type endpoints: list[:class:`huaweicloudsdkcodeartspipeline.v2.Endpoint`]
        :param total: 数量
        :type total: int
        """
        
        

        self._endpoints = None
        self._total = None
        self.discriminator = None

        if endpoints is not None:
            self.endpoints = endpoints
        if total is not None:
            self.total = total

    @property
    def endpoints(self):
        r"""Gets the endpoints of this EndpointList.

        Endpoint的具体信息

        :return: The endpoints of this EndpointList.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.Endpoint`]
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        r"""Sets the endpoints of this EndpointList.

        Endpoint的具体信息

        :param endpoints: The endpoints of this EndpointList.
        :type endpoints: list[:class:`huaweicloudsdkcodeartspipeline.v2.Endpoint`]
        """
        self._endpoints = endpoints

    @property
    def total(self):
        r"""Gets the total of this EndpointList.

        数量

        :return: The total of this EndpointList.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this EndpointList.

        数量

        :param total: The total of this EndpointList.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, EndpointList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
