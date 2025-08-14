# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListServerHdaDetailsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'server_group_id': 'str',
        'server_name': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'server_group_id': 'server_group_id',
        'server_name': 'server_name'
    }

    def __init__(self, offset=None, limit=None, server_group_id=None, server_name=None):
        r"""ListServerHdaDetailsRequest

        The model defined in huaweicloud sdk

        :param offset: 查询的偏移量，默认值0。
        :type offset: int
        :param limit: 查询的数量，值区间[1-100]，默认值10。
        :type limit: int
        :param server_group_id: 服务器组id。
        :type server_group_id: str
        :param server_name: 服务器名称。
        :type server_name: str
        """
        
        

        self._offset = None
        self._limit = None
        self._server_group_id = None
        self._server_name = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if server_group_id is not None:
            self.server_group_id = server_group_id
        if server_name is not None:
            self.server_name = server_name

    @property
    def offset(self):
        r"""Gets the offset of this ListServerHdaDetailsRequest.

        查询的偏移量，默认值0。

        :return: The offset of this ListServerHdaDetailsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListServerHdaDetailsRequest.

        查询的偏移量，默认值0。

        :param offset: The offset of this ListServerHdaDetailsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListServerHdaDetailsRequest.

        查询的数量，值区间[1-100]，默认值10。

        :return: The limit of this ListServerHdaDetailsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListServerHdaDetailsRequest.

        查询的数量，值区间[1-100]，默认值10。

        :param limit: The limit of this ListServerHdaDetailsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def server_group_id(self):
        r"""Gets the server_group_id of this ListServerHdaDetailsRequest.

        服务器组id。

        :return: The server_group_id of this ListServerHdaDetailsRequest.
        :rtype: str
        """
        return self._server_group_id

    @server_group_id.setter
    def server_group_id(self, server_group_id):
        r"""Sets the server_group_id of this ListServerHdaDetailsRequest.

        服务器组id。

        :param server_group_id: The server_group_id of this ListServerHdaDetailsRequest.
        :type server_group_id: str
        """
        self._server_group_id = server_group_id

    @property
    def server_name(self):
        r"""Gets the server_name of this ListServerHdaDetailsRequest.

        服务器名称。

        :return: The server_name of this ListServerHdaDetailsRequest.
        :rtype: str
        """
        return self._server_name

    @server_name.setter
    def server_name(self, server_name):
        r"""Sets the server_name of this ListServerHdaDetailsRequest.

        服务器名称。

        :param server_name: The server_name of this ListServerHdaDetailsRequest.
        :type server_name: str
        """
        self._server_name = server_name

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
        if not isinstance(other, ListServerHdaDetailsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
