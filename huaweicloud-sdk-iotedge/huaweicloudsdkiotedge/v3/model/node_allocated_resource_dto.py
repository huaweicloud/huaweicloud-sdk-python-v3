# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeAllocatedResourceDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'request': 'NodeResourceDTO',
        'limit': 'NodeResourceDTO'
    }

    attribute_map = {
        'request': 'request',
        'limit': 'limit'
    }

    def __init__(self, request=None, limit=None):
        r"""NodeAllocatedResourceDTO

        The model defined in huaweicloud sdk

        :param request: 
        :type request: :class:`huaweicloudsdkiotedge.v3.NodeResourceDTO`
        :param limit: 
        :type limit: :class:`huaweicloudsdkiotedge.v3.NodeResourceDTO`
        """
        
        

        self._request = None
        self._limit = None
        self.discriminator = None

        if request is not None:
            self.request = request
        if limit is not None:
            self.limit = limit

    @property
    def request(self):
        r"""Gets the request of this NodeAllocatedResourceDTO.

        :return: The request of this NodeAllocatedResourceDTO.
        :rtype: :class:`huaweicloudsdkiotedge.v3.NodeResourceDTO`
        """
        return self._request

    @request.setter
    def request(self, request):
        r"""Sets the request of this NodeAllocatedResourceDTO.

        :param request: The request of this NodeAllocatedResourceDTO.
        :type request: :class:`huaweicloudsdkiotedge.v3.NodeResourceDTO`
        """
        self._request = request

    @property
    def limit(self):
        r"""Gets the limit of this NodeAllocatedResourceDTO.

        :return: The limit of this NodeAllocatedResourceDTO.
        :rtype: :class:`huaweicloudsdkiotedge.v3.NodeResourceDTO`
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this NodeAllocatedResourceDTO.

        :param limit: The limit of this NodeAllocatedResourceDTO.
        :type limit: :class:`huaweicloudsdkiotedge.v3.NodeResourceDTO`
        """
        self._limit = limit

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
        if not isinstance(other, NodeAllocatedResourceDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
