# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListServersDedicatedHostRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dedicated_host_id': 'str',
        'limit': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'dedicated_host_id': 'dedicated_host_id',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, dedicated_host_id=None, limit=None, marker=None):
        """ListServersDedicatedHostRequest

        The model defined in huaweicloud sdk

        :param dedicated_host_id: 专属主机ID。  可以从专属主机控制台查询，或者通过调用查询专属主机列表API获取。
        :type dedicated_host_id: str
        :param limit: 每个页面上显示的条目数。
        :type limit: int
        :param marker: 该值是上一页最后一条记录的ID。  如果“marker”取值无效，将会返回“400”错误码。
        :type marker: str
        """
        
        

        self._dedicated_host_id = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        self.dedicated_host_id = dedicated_host_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def dedicated_host_id(self):
        """Gets the dedicated_host_id of this ListServersDedicatedHostRequest.

        专属主机ID。  可以从专属主机控制台查询，或者通过调用查询专属主机列表API获取。

        :return: The dedicated_host_id of this ListServersDedicatedHostRequest.
        :rtype: str
        """
        return self._dedicated_host_id

    @dedicated_host_id.setter
    def dedicated_host_id(self, dedicated_host_id):
        """Sets the dedicated_host_id of this ListServersDedicatedHostRequest.

        专属主机ID。  可以从专属主机控制台查询，或者通过调用查询专属主机列表API获取。

        :param dedicated_host_id: The dedicated_host_id of this ListServersDedicatedHostRequest.
        :type dedicated_host_id: str
        """
        self._dedicated_host_id = dedicated_host_id

    @property
    def limit(self):
        """Gets the limit of this ListServersDedicatedHostRequest.

        每个页面上显示的条目数。

        :return: The limit of this ListServersDedicatedHostRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListServersDedicatedHostRequest.

        每个页面上显示的条目数。

        :param limit: The limit of this ListServersDedicatedHostRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListServersDedicatedHostRequest.

        该值是上一页最后一条记录的ID。  如果“marker”取值无效，将会返回“400”错误码。

        :return: The marker of this ListServersDedicatedHostRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListServersDedicatedHostRequest.

        该值是上一页最后一条记录的ID。  如果“marker”取值无效，将会返回“400”错误码。

        :param marker: The marker of this ListServersDedicatedHostRequest.
        :type marker: str
        """
        self._marker = marker

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
        if not isinstance(other, ListServersDedicatedHostRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
