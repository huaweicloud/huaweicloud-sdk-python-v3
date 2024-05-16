# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHostResultsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_id': 'str',
        'scan_id': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'host_id': 'host_id',
        'scan_id': 'scan_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, host_id=None, scan_id=None, offset=None, limit=None):
        """ListHostResultsRequest

        The model defined in huaweicloud sdk

        :param host_id: 主机ID
        :type host_id: str
        :param scan_id: 扫描ID
        :type scan_id: str
        :param offset: 分页查询，偏移量，表示从此偏移量开始查询
        :type offset: int
        :param limit: 分页查询，每页显示的条目数量
        :type limit: int
        """
        
        

        self._host_id = None
        self._scan_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.host_id = host_id
        self.scan_id = scan_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def host_id(self):
        """Gets the host_id of this ListHostResultsRequest.

        主机ID

        :return: The host_id of this ListHostResultsRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this ListHostResultsRequest.

        主机ID

        :param host_id: The host_id of this ListHostResultsRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def scan_id(self):
        """Gets the scan_id of this ListHostResultsRequest.

        扫描ID

        :return: The scan_id of this ListHostResultsRequest.
        :rtype: str
        """
        return self._scan_id

    @scan_id.setter
    def scan_id(self, scan_id):
        """Sets the scan_id of this ListHostResultsRequest.

        扫描ID

        :param scan_id: The scan_id of this ListHostResultsRequest.
        :type scan_id: str
        """
        self._scan_id = scan_id

    @property
    def offset(self):
        """Gets the offset of this ListHostResultsRequest.

        分页查询，偏移量，表示从此偏移量开始查询

        :return: The offset of this ListHostResultsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListHostResultsRequest.

        分页查询，偏移量，表示从此偏移量开始查询

        :param offset: The offset of this ListHostResultsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListHostResultsRequest.

        分页查询，每页显示的条目数量

        :return: The limit of this ListHostResultsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListHostResultsRequest.

        分页查询，每页显示的条目数量

        :param limit: The limit of this ListHostResultsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListHostResultsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
