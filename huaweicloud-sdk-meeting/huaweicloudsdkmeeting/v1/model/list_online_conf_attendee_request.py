# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOnlineConfAttendeeRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'conf_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'search_key': 'str'
    }

    attribute_map = {
        'conf_id': 'conf_id',
        'offset': 'offset',
        'limit': 'limit',
        'search_key': 'search_key'
    }

    def __init__(self, conf_id=None, offset=None, limit=None, search_key=None):
        r"""ListOnlineConfAttendeeRequest

        The model defined in huaweicloud sdk

        :param conf_id: 会议ID
        :type conf_id: str
        :param offset: 记录数偏移
        :type offset: int
        :param limit: 返回的与会者记录数，最大500条
        :type limit: int
        :param search_key: 查询条件,支持third-account查询返回
        :type search_key: str
        """
        
        

        self._conf_id = None
        self._offset = None
        self._limit = None
        self._search_key = None
        self.discriminator = None

        self.conf_id = conf_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if search_key is not None:
            self.search_key = search_key

    @property
    def conf_id(self):
        r"""Gets the conf_id of this ListOnlineConfAttendeeRequest.

        会议ID

        :return: The conf_id of this ListOnlineConfAttendeeRequest.
        :rtype: str
        """
        return self._conf_id

    @conf_id.setter
    def conf_id(self, conf_id):
        r"""Sets the conf_id of this ListOnlineConfAttendeeRequest.

        会议ID

        :param conf_id: The conf_id of this ListOnlineConfAttendeeRequest.
        :type conf_id: str
        """
        self._conf_id = conf_id

    @property
    def offset(self):
        r"""Gets the offset of this ListOnlineConfAttendeeRequest.

        记录数偏移

        :return: The offset of this ListOnlineConfAttendeeRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListOnlineConfAttendeeRequest.

        记录数偏移

        :param offset: The offset of this ListOnlineConfAttendeeRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListOnlineConfAttendeeRequest.

        返回的与会者记录数，最大500条

        :return: The limit of this ListOnlineConfAttendeeRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListOnlineConfAttendeeRequest.

        返回的与会者记录数，最大500条

        :param limit: The limit of this ListOnlineConfAttendeeRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def search_key(self):
        r"""Gets the search_key of this ListOnlineConfAttendeeRequest.

        查询条件,支持third-account查询返回

        :return: The search_key of this ListOnlineConfAttendeeRequest.
        :rtype: str
        """
        return self._search_key

    @search_key.setter
    def search_key(self, search_key):
        r"""Sets the search_key of this ListOnlineConfAttendeeRequest.

        查询条件,支持third-account查询返回

        :param search_key: The search_key of this ListOnlineConfAttendeeRequest.
        :type search_key: str
        """
        self._search_key = search_key

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
        if not isinstance(other, ListOnlineConfAttendeeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
