# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchQosParticipantsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'conf_uuid': 'str',
        'conf_type': 'str',
        'offset': 'int',
        'limit': 'int',
        'search_key': 'str'
    }

    attribute_map = {
        'conf_uuid': 'confUUID',
        'conf_type': 'confType',
        'offset': 'offset',
        'limit': 'limit',
        'search_key': 'searchKey'
    }

    def __init__(self, conf_uuid=None, conf_type=None, offset=None, limit=None, search_key=None):
        """SearchQosParticipantsRequest

        The model defined in huaweicloud sdk

        :param conf_uuid: 会议UUID。
        :type conf_uuid: str
        :param conf_type: 会议类别。 * online：在线会议，正在召开的会议 * history：历史会议，已结束的会议
        :type conf_type: str
        :param offset: 查询偏移量。 * 取值：大于等于0，默认值为0。 * 大于等于最大条目数量，则返回最后一页的数据。
        :type offset: int
        :param limit: 查询的条目数量。 * 取值：1-500，默认值为20。
        :type limit: int
        :param search_key: 查询条件。与会者名称可作为搜索内容。长度限制为1-512个字符。
        :type search_key: str
        """
        
        

        self._conf_uuid = None
        self._conf_type = None
        self._offset = None
        self._limit = None
        self._search_key = None
        self.discriminator = None

        self.conf_uuid = conf_uuid
        self.conf_type = conf_type
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if search_key is not None:
            self.search_key = search_key

    @property
    def conf_uuid(self):
        """Gets the conf_uuid of this SearchQosParticipantsRequest.

        会议UUID。

        :return: The conf_uuid of this SearchQosParticipantsRequest.
        :rtype: str
        """
        return self._conf_uuid

    @conf_uuid.setter
    def conf_uuid(self, conf_uuid):
        """Sets the conf_uuid of this SearchQosParticipantsRequest.

        会议UUID。

        :param conf_uuid: The conf_uuid of this SearchQosParticipantsRequest.
        :type conf_uuid: str
        """
        self._conf_uuid = conf_uuid

    @property
    def conf_type(self):
        """Gets the conf_type of this SearchQosParticipantsRequest.

        会议类别。 * online：在线会议，正在召开的会议 * history：历史会议，已结束的会议

        :return: The conf_type of this SearchQosParticipantsRequest.
        :rtype: str
        """
        return self._conf_type

    @conf_type.setter
    def conf_type(self, conf_type):
        """Sets the conf_type of this SearchQosParticipantsRequest.

        会议类别。 * online：在线会议，正在召开的会议 * history：历史会议，已结束的会议

        :param conf_type: The conf_type of this SearchQosParticipantsRequest.
        :type conf_type: str
        """
        self._conf_type = conf_type

    @property
    def offset(self):
        """Gets the offset of this SearchQosParticipantsRequest.

        查询偏移量。 * 取值：大于等于0，默认值为0。 * 大于等于最大条目数量，则返回最后一页的数据。

        :return: The offset of this SearchQosParticipantsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this SearchQosParticipantsRequest.

        查询偏移量。 * 取值：大于等于0，默认值为0。 * 大于等于最大条目数量，则返回最后一页的数据。

        :param offset: The offset of this SearchQosParticipantsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this SearchQosParticipantsRequest.

        查询的条目数量。 * 取值：1-500，默认值为20。

        :return: The limit of this SearchQosParticipantsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this SearchQosParticipantsRequest.

        查询的条目数量。 * 取值：1-500，默认值为20。

        :param limit: The limit of this SearchQosParticipantsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def search_key(self):
        """Gets the search_key of this SearchQosParticipantsRequest.

        查询条件。与会者名称可作为搜索内容。长度限制为1-512个字符。

        :return: The search_key of this SearchQosParticipantsRequest.
        :rtype: str
        """
        return self._search_key

    @search_key.setter
    def search_key(self, search_key):
        """Sets the search_key of this SearchQosParticipantsRequest.

        查询条件。与会者名称可作为搜索内容。长度限制为1-512个字符。

        :param search_key: The search_key of this SearchQosParticipantsRequest.
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
        if not isinstance(other, SearchQosParticipantsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
