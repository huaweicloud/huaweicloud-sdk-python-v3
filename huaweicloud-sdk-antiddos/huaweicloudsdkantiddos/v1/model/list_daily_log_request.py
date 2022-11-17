# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDailyLogRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'floating_ip_id': 'str',
        'sort_dir': 'str',
        'limit': 'str',
        'offset': 'str',
        'ip': 'str'
    }

    attribute_map = {
        'floating_ip_id': 'floating_ip_id',
        'sort_dir': 'sort_dir',
        'limit': 'limit',
        'offset': 'offset',
        'ip': 'ip'
    }

    def __init__(self, floating_ip_id=None, sort_dir=None, limit=None, offset=None, ip=None):
        """ListDailyLogRequest

        The model defined in huaweicloud sdk

        :param floating_ip_id: 用户EIP对应的ID
        :type floating_ip_id: str
        :param sort_dir: 可选范围： - desc：表示时间降序 - asc：表示时间升序 默认值为“desc”。
        :type sort_dir: str
        :param limit: 返回结果个数限制，此次查询返回数量最大值，取值范围：1～100，与offset配合使用。 若“limit”与“offset”均不携带则返回所有主机列表。
        :type limit: str
        :param offset: 偏移量，“limit”携带时此字段有效。
        :type offset: str
        :param ip: 用户EIP
        :type ip: str
        """
        
        

        self._floating_ip_id = None
        self._sort_dir = None
        self._limit = None
        self._offset = None
        self._ip = None
        self.discriminator = None

        self.floating_ip_id = floating_ip_id
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if ip is not None:
            self.ip = ip

    @property
    def floating_ip_id(self):
        """Gets the floating_ip_id of this ListDailyLogRequest.

        用户EIP对应的ID

        :return: The floating_ip_id of this ListDailyLogRequest.
        :rtype: str
        """
        return self._floating_ip_id

    @floating_ip_id.setter
    def floating_ip_id(self, floating_ip_id):
        """Sets the floating_ip_id of this ListDailyLogRequest.

        用户EIP对应的ID

        :param floating_ip_id: The floating_ip_id of this ListDailyLogRequest.
        :type floating_ip_id: str
        """
        self._floating_ip_id = floating_ip_id

    @property
    def sort_dir(self):
        """Gets the sort_dir of this ListDailyLogRequest.

        可选范围： - desc：表示时间降序 - asc：表示时间升序 默认值为“desc”。

        :return: The sort_dir of this ListDailyLogRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this ListDailyLogRequest.

        可选范围： - desc：表示时间降序 - asc：表示时间升序 默认值为“desc”。

        :param sort_dir: The sort_dir of this ListDailyLogRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def limit(self):
        """Gets the limit of this ListDailyLogRequest.

        返回结果个数限制，此次查询返回数量最大值，取值范围：1～100，与offset配合使用。 若“limit”与“offset”均不携带则返回所有主机列表。

        :return: The limit of this ListDailyLogRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListDailyLogRequest.

        返回结果个数限制，此次查询返回数量最大值，取值范围：1～100，与offset配合使用。 若“limit”与“offset”均不携带则返回所有主机列表。

        :param limit: The limit of this ListDailyLogRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListDailyLogRequest.

        偏移量，“limit”携带时此字段有效。

        :return: The offset of this ListDailyLogRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListDailyLogRequest.

        偏移量，“limit”携带时此字段有效。

        :param offset: The offset of this ListDailyLogRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def ip(self):
        """Gets the ip of this ListDailyLogRequest.

        用户EIP

        :return: The ip of this ListDailyLogRequest.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this ListDailyLogRequest.

        用户EIP

        :param ip: The ip of this ListDailyLogRequest.
        :type ip: str
        """
        self._ip = ip

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
        if not isinstance(other, ListDailyLogRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
