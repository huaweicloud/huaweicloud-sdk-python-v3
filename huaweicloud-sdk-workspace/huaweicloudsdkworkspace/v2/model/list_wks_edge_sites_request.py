# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWksEdgeSitesRequest:

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
        'availability_zone_id': 'str',
        'status': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'name': 'name',
        'availability_zone_id': 'availability_zone_id',
        'status': 'status',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, name=None, availability_zone_id=None, status=None, limit=None, offset=None):
        r"""ListWksEdgeSitesRequest

        The model defined in huaweicloud sdk

        :param name: 根据边缘小站名称查询。
        :type name: str
        :param availability_zone_id: 根据边缘可用区ID查询。
        :type availability_zone_id: str
        :param status: 根据边缘小站部署状态查询。
        :type status: str
        :param limit: 每页数量，范围0-1000，默认1000。
        :type limit: int
        :param offset: 偏移量，默认0。
        :type offset: int
        """
        
        

        self._name = None
        self._availability_zone_id = None
        self._status = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if availability_zone_id is not None:
            self.availability_zone_id = availability_zone_id
        if status is not None:
            self.status = status
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def name(self):
        r"""Gets the name of this ListWksEdgeSitesRequest.

        根据边缘小站名称查询。

        :return: The name of this ListWksEdgeSitesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListWksEdgeSitesRequest.

        根据边缘小站名称查询。

        :param name: The name of this ListWksEdgeSitesRequest.
        :type name: str
        """
        self._name = name

    @property
    def availability_zone_id(self):
        r"""Gets the availability_zone_id of this ListWksEdgeSitesRequest.

        根据边缘可用区ID查询。

        :return: The availability_zone_id of this ListWksEdgeSitesRequest.
        :rtype: str
        """
        return self._availability_zone_id

    @availability_zone_id.setter
    def availability_zone_id(self, availability_zone_id):
        r"""Sets the availability_zone_id of this ListWksEdgeSitesRequest.

        根据边缘可用区ID查询。

        :param availability_zone_id: The availability_zone_id of this ListWksEdgeSitesRequest.
        :type availability_zone_id: str
        """
        self._availability_zone_id = availability_zone_id

    @property
    def status(self):
        r"""Gets the status of this ListWksEdgeSitesRequest.

        根据边缘小站部署状态查询。

        :return: The status of this ListWksEdgeSitesRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListWksEdgeSitesRequest.

        根据边缘小站部署状态查询。

        :param status: The status of this ListWksEdgeSitesRequest.
        :type status: str
        """
        self._status = status

    @property
    def limit(self):
        r"""Gets the limit of this ListWksEdgeSitesRequest.

        每页数量，范围0-1000，默认1000。

        :return: The limit of this ListWksEdgeSitesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListWksEdgeSitesRequest.

        每页数量，范围0-1000，默认1000。

        :param limit: The limit of this ListWksEdgeSitesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListWksEdgeSitesRequest.

        偏移量，默认0。

        :return: The offset of this ListWksEdgeSitesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListWksEdgeSitesRequest.

        偏移量，默认0。

        :param offset: The offset of this ListWksEdgeSitesRequest.
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
        if not isinstance(other, ListWksEdgeSitesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
