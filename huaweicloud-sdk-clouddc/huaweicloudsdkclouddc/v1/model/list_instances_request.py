# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstancesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'str',
        'marker': 'str',
        'instance_state': 'str',
        'instance_id': 'str',
        'server_id': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'instance_state': 'instance_state',
        'instance_id': 'instance_id',
        'server_id': 'server_id'
    }

    def __init__(self, limit=None, marker=None, instance_state=None, instance_id=None, server_id=None):
        r"""ListInstancesRequest

        The model defined in huaweicloud sdk

        :param limit: 分页查询时每页行数。最大值为 1000。  默认值： 当不设置值或设置的值小于 10 时，默认值为 10。 当设置的值大于 1000 时，默认值为 1000。
        :type limit: str
        :param marker: 分页游标
        :type marker: str
        :param instance_state: 实例状态
        :type instance_state: str
        :param instance_id: 实例 ID。取值可以由多个实例 ID 组成数组，最多支持 100 个 ID，ID 之间用半角逗号（,）隔开，示例：uuid1,uuid2,uuid3。
        :type instance_id: str
        :param server_id: 实例 ID。取值可以由多个服务器 ID 组成数组，最多支持 100 个 ID，ID 之间用半角逗号（,）隔开，示例：uuid1,uuid2,uuid3。与instance_id_set查询条件互斥。
        :type server_id: str
        """
        
        

        self._limit = None
        self._marker = None
        self._instance_state = None
        self._instance_id = None
        self._server_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if instance_state is not None:
            self.instance_state = instance_state
        if instance_id is not None:
            self.instance_id = instance_id
        if server_id is not None:
            self.server_id = server_id

    @property
    def limit(self):
        r"""Gets the limit of this ListInstancesRequest.

        分页查询时每页行数。最大值为 1000。  默认值： 当不设置值或设置的值小于 10 时，默认值为 10。 当设置的值大于 1000 时，默认值为 1000。

        :return: The limit of this ListInstancesRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListInstancesRequest.

        分页查询时每页行数。最大值为 1000。  默认值： 当不设置值或设置的值小于 10 时，默认值为 10。 当设置的值大于 1000 时，默认值为 1000。

        :param limit: The limit of this ListInstancesRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListInstancesRequest.

        分页游标

        :return: The marker of this ListInstancesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListInstancesRequest.

        分页游标

        :param marker: The marker of this ListInstancesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def instance_state(self):
        r"""Gets the instance_state of this ListInstancesRequest.

        实例状态

        :return: The instance_state of this ListInstancesRequest.
        :rtype: str
        """
        return self._instance_state

    @instance_state.setter
    def instance_state(self, instance_state):
        r"""Sets the instance_state of this ListInstancesRequest.

        实例状态

        :param instance_state: The instance_state of this ListInstancesRequest.
        :type instance_state: str
        """
        self._instance_state = instance_state

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListInstancesRequest.

        实例 ID。取值可以由多个实例 ID 组成数组，最多支持 100 个 ID，ID 之间用半角逗号（,）隔开，示例：uuid1,uuid2,uuid3。

        :return: The instance_id of this ListInstancesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListInstancesRequest.

        实例 ID。取值可以由多个实例 ID 组成数组，最多支持 100 个 ID，ID 之间用半角逗号（,）隔开，示例：uuid1,uuid2,uuid3。

        :param instance_id: The instance_id of this ListInstancesRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def server_id(self):
        r"""Gets the server_id of this ListInstancesRequest.

        实例 ID。取值可以由多个服务器 ID 组成数组，最多支持 100 个 ID，ID 之间用半角逗号（,）隔开，示例：uuid1,uuid2,uuid3。与instance_id_set查询条件互斥。

        :return: The server_id of this ListInstancesRequest.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        r"""Sets the server_id of this ListInstancesRequest.

        实例 ID。取值可以由多个服务器 ID 组成数组，最多支持 100 个 ID，ID 之间用半角逗号（,）隔开，示例：uuid1,uuid2,uuid3。与instance_id_set查询条件互斥。

        :param server_id: The server_id of this ListInstancesRequest.
        :type server_id: str
        """
        self._server_id = server_id

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
        if not isinstance(other, ListInstancesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
