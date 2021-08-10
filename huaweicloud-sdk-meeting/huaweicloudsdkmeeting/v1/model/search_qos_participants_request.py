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
        """SearchQosParticipantsRequest - a model defined in huaweicloud sdk"""
        
        

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

        会议UUID。最大不超过64个字节。

        :return: The conf_uuid of this SearchQosParticipantsRequest.
        :rtype: str
        """
        return self._conf_uuid

    @conf_uuid.setter
    def conf_uuid(self, conf_uuid):
        """Sets the conf_uuid of this SearchQosParticipantsRequest.

        会议UUID。最大不超过64个字节。

        :param conf_uuid: The conf_uuid of this SearchQosParticipantsRequest.
        :type: str
        """
        self._conf_uuid = conf_uuid

    @property
    def conf_type(self):
        """Gets the conf_type of this SearchQosParticipantsRequest.

        会议类别。 * online：在线会议，在召开的会议。 * history：历史会议，已召开的会议。

        :return: The conf_type of this SearchQosParticipantsRequest.
        :rtype: str
        """
        return self._conf_type

    @conf_type.setter
    def conf_type(self, conf_type):
        """Sets the conf_type of this SearchQosParticipantsRequest.

        会议类别。 * online：在线会议，在召开的会议。 * history：历史会议，已召开的会议。

        :param conf_type: The conf_type of this SearchQosParticipantsRequest.
        :type: str
        """
        self._conf_type = conf_type

    @property
    def offset(self):
        """Gets the offset of this SearchQosParticipantsRequest.

        查询偏移量。 * 取值：大于等于0，默认值为0。 * 小于最小值0时，系统设置为0。 * 大于等于最大条目数量，则返回最后一页的数据。

        :return: The offset of this SearchQosParticipantsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this SearchQosParticipantsRequest.

        查询偏移量。 * 取值：大于等于0，默认值为0。 * 小于最小值0时，系统设置为0。 * 大于等于最大条目数量，则返回最后一页的数据。

        :param offset: The offset of this SearchQosParticipantsRequest.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this SearchQosParticipantsRequest.

        查询的条目数量。 * 取值：1-500，默认值为20。 * 小于最小值1时，系统设置为1。 * 大于最大值500时，系统设置为500。

        :return: The limit of this SearchQosParticipantsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this SearchQosParticipantsRequest.

        查询的条目数量。 * 取值：1-500，默认值为20。 * 小于最小值1时，系统设置为1。 * 大于最大值500时，系统设置为500。

        :param limit: The limit of this SearchQosParticipantsRequest.
        :type: int
        """
        self._limit = limit

    @property
    def search_key(self):
        """Gets the search_key of this SearchQosParticipantsRequest.

        根据与会人名称作为关键词，模糊查询与会者列表

        :return: The search_key of this SearchQosParticipantsRequest.
        :rtype: str
        """
        return self._search_key

    @search_key.setter
    def search_key(self, search_key):
        """Sets the search_key of this SearchQosParticipantsRequest.

        根据与会人名称作为关键词，模糊查询与会者列表

        :param search_key: The search_key of this SearchQosParticipantsRequest.
        :type: str
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
