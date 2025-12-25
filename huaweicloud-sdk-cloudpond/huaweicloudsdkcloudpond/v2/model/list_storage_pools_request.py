# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListStoragePoolsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'edge_site_id': 'str',
        'limit': 'int',
        'marker': 'str',
        'status': 'list[str]'
    }

    attribute_map = {
        'edge_site_id': 'edge_site_id',
        'limit': 'limit',
        'marker': 'marker',
        'status': 'status'
    }

    def __init__(self, edge_site_id=None, limit=None, marker=None, status=None):
        r"""ListStoragePoolsRequest

        The model defined in huaweicloud sdk

        :param edge_site_id: 边缘小站ID
        :type edge_site_id: str
        :param limit: 每页的数量
        :type limit: int
        :param marker: 分页标识
        :type marker: str
        :param status: 根据存储池状态查询，支持多值查询
        :type status: list[str]
        """
        
        

        self._edge_site_id = None
        self._limit = None
        self._marker = None
        self._status = None
        self.discriminator = None

        if edge_site_id is not None:
            self.edge_site_id = edge_site_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if status is not None:
            self.status = status

    @property
    def edge_site_id(self):
        r"""Gets the edge_site_id of this ListStoragePoolsRequest.

        边缘小站ID

        :return: The edge_site_id of this ListStoragePoolsRequest.
        :rtype: str
        """
        return self._edge_site_id

    @edge_site_id.setter
    def edge_site_id(self, edge_site_id):
        r"""Sets the edge_site_id of this ListStoragePoolsRequest.

        边缘小站ID

        :param edge_site_id: The edge_site_id of this ListStoragePoolsRequest.
        :type edge_site_id: str
        """
        self._edge_site_id = edge_site_id

    @property
    def limit(self):
        r"""Gets the limit of this ListStoragePoolsRequest.

        每页的数量

        :return: The limit of this ListStoragePoolsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListStoragePoolsRequest.

        每页的数量

        :param limit: The limit of this ListStoragePoolsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListStoragePoolsRequest.

        分页标识

        :return: The marker of this ListStoragePoolsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListStoragePoolsRequest.

        分页标识

        :param marker: The marker of this ListStoragePoolsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def status(self):
        r"""Gets the status of this ListStoragePoolsRequest.

        根据存储池状态查询，支持多值查询

        :return: The status of this ListStoragePoolsRequest.
        :rtype: list[str]
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListStoragePoolsRequest.

        根据存储池状态查询，支持多值查询

        :param status: The status of this ListStoragePoolsRequest.
        :type status: list[str]
        """
        self._status = status

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
        if not isinstance(other, ListStoragePoolsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
