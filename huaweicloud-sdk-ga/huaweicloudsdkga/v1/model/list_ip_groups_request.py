# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListIpGroupsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'marker': 'str',
        'listener_id': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'listener_id': 'listener_id'
    }

    def __init__(self, limit=None, marker=None, listener_id=None):
        r"""ListIpGroupsRequest

        The model defined in huaweicloud sdk

        :param limit: 分页查询每页的资源个数。如果不设置，则默认为500。
        :type limit: int
        :param marker: 分页查询的起始的资源ID，表示上一页最后一条查询资源记录的ID。不指定时表示查询第一页。 必须与limit一起使用。
        :type marker: str
        :param listener_id: 监听器id,查询监听器绑定的IP地址组时使用该条件,当查询条件带listener_id时，结果中的associated_listeners也只包含该listener的记录
        :type listener_id: str
        """
        
        

        self._limit = None
        self._marker = None
        self._listener_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if listener_id is not None:
            self.listener_id = listener_id

    @property
    def limit(self):
        r"""Gets the limit of this ListIpGroupsRequest.

        分页查询每页的资源个数。如果不设置，则默认为500。

        :return: The limit of this ListIpGroupsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListIpGroupsRequest.

        分页查询每页的资源个数。如果不设置，则默认为500。

        :param limit: The limit of this ListIpGroupsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListIpGroupsRequest.

        分页查询的起始的资源ID，表示上一页最后一条查询资源记录的ID。不指定时表示查询第一页。 必须与limit一起使用。

        :return: The marker of this ListIpGroupsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListIpGroupsRequest.

        分页查询的起始的资源ID，表示上一页最后一条查询资源记录的ID。不指定时表示查询第一页。 必须与limit一起使用。

        :param marker: The marker of this ListIpGroupsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def listener_id(self):
        r"""Gets the listener_id of this ListIpGroupsRequest.

        监听器id,查询监听器绑定的IP地址组时使用该条件,当查询条件带listener_id时，结果中的associated_listeners也只包含该listener的记录

        :return: The listener_id of this ListIpGroupsRequest.
        :rtype: str
        """
        return self._listener_id

    @listener_id.setter
    def listener_id(self, listener_id):
        r"""Sets the listener_id of this ListIpGroupsRequest.

        监听器id,查询监听器绑定的IP地址组时使用该条件,当查询条件带listener_id时，结果中的associated_listeners也只包含该listener的记录

        :param listener_id: The listener_id of this ListIpGroupsRequest.
        :type listener_id: str
        """
        self._listener_id = listener_id

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
        if not isinstance(other, ListIpGroupsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
