# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCoreGatewaysRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'status': 'str',
        'gateway_id': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'name': 'name',
        'status': 'status',
        'gateway_id': 'gateway_id',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, name=None, status=None, gateway_id=None, limit=None, offset=None):
        r"""ListCoreGatewaysRequest

        The model defined in huaweicloud sdk

        :param name: 按名称过滤网关，支持模糊匹配。
        :type name: str
        :param status: 按状态过滤网关。
        :type status: str
        :param gateway_id: 按网关ID过滤，支持多个ID（最多支持20个ID）。
        :type gateway_id: str
        :param limit: 返回的最大结果数。
        :type limit: int
        :param offset: 返回结果偏移量。
        :type offset: int
        """
        
        

        self._name = None
        self._status = None
        self._gateway_id = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if gateway_id is not None:
            self.gateway_id = gateway_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def name(self):
        r"""Gets the name of this ListCoreGatewaysRequest.

        按名称过滤网关，支持模糊匹配。

        :return: The name of this ListCoreGatewaysRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListCoreGatewaysRequest.

        按名称过滤网关，支持模糊匹配。

        :param name: The name of this ListCoreGatewaysRequest.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this ListCoreGatewaysRequest.

        按状态过滤网关。

        :return: The status of this ListCoreGatewaysRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListCoreGatewaysRequest.

        按状态过滤网关。

        :param status: The status of this ListCoreGatewaysRequest.
        :type status: str
        """
        self._status = status

    @property
    def gateway_id(self):
        r"""Gets the gateway_id of this ListCoreGatewaysRequest.

        按网关ID过滤，支持多个ID（最多支持20个ID）。

        :return: The gateway_id of this ListCoreGatewaysRequest.
        :rtype: str
        """
        return self._gateway_id

    @gateway_id.setter
    def gateway_id(self, gateway_id):
        r"""Sets the gateway_id of this ListCoreGatewaysRequest.

        按网关ID过滤，支持多个ID（最多支持20个ID）。

        :param gateway_id: The gateway_id of this ListCoreGatewaysRequest.
        :type gateway_id: str
        """
        self._gateway_id = gateway_id

    @property
    def limit(self):
        r"""Gets the limit of this ListCoreGatewaysRequest.

        返回的最大结果数。

        :return: The limit of this ListCoreGatewaysRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListCoreGatewaysRequest.

        返回的最大结果数。

        :param limit: The limit of this ListCoreGatewaysRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListCoreGatewaysRequest.

        返回结果偏移量。

        :return: The offset of this ListCoreGatewaysRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListCoreGatewaysRequest.

        返回结果偏移量。

        :param offset: The offset of this ListCoreGatewaysRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListCoreGatewaysRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
