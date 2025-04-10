# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TunnelInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tunnel_id': 'str',
        'device_id': 'str',
        'create_time': 'str',
        'closed_time': 'str',
        'status': 'str',
        'source_connect_state': 'ConnectState',
        'device_connect_state': 'ConnectState'
    }

    attribute_map = {
        'tunnel_id': 'tunnel_id',
        'device_id': 'device_id',
        'create_time': 'create_time',
        'closed_time': 'closed_time',
        'status': 'status',
        'source_connect_state': 'source_connect_state',
        'device_connect_state': 'device_connect_state'
    }

    def __init__(self, tunnel_id=None, device_id=None, create_time=None, closed_time=None, status=None, source_connect_state=None, device_connect_state=None):
        r"""TunnelInfo

        The model defined in huaweicloud sdk

        :param tunnel_id: 隧道ID
        :type tunnel_id: str
        :param device_id: 设备ID
        :type device_id: str
        :param create_time: 隧道创建时间。格式：yyyyMMdd&#39;T&#39;HHmmss&#39;Z&#39;，如20151212T121212Z。
        :type create_time: str
        :param closed_time: 隧道更新时间。格式：yyyyMMdd&#39;T&#39;HHmmss&#39;Z&#39;，如20151212T121212Z。
        :type closed_time: str
        :param status: 隧道状态 CLOSED | OPEN
        :type status: str
        :param source_connect_state: 
        :type source_connect_state: :class:`huaweicloudsdkiotda.v5.ConnectState`
        :param device_connect_state: 
        :type device_connect_state: :class:`huaweicloudsdkiotda.v5.ConnectState`
        """
        
        

        self._tunnel_id = None
        self._device_id = None
        self._create_time = None
        self._closed_time = None
        self._status = None
        self._source_connect_state = None
        self._device_connect_state = None
        self.discriminator = None

        if tunnel_id is not None:
            self.tunnel_id = tunnel_id
        if device_id is not None:
            self.device_id = device_id
        if create_time is not None:
            self.create_time = create_time
        if closed_time is not None:
            self.closed_time = closed_time
        if status is not None:
            self.status = status
        if source_connect_state is not None:
            self.source_connect_state = source_connect_state
        if device_connect_state is not None:
            self.device_connect_state = device_connect_state

    @property
    def tunnel_id(self):
        r"""Gets the tunnel_id of this TunnelInfo.

        隧道ID

        :return: The tunnel_id of this TunnelInfo.
        :rtype: str
        """
        return self._tunnel_id

    @tunnel_id.setter
    def tunnel_id(self, tunnel_id):
        r"""Sets the tunnel_id of this TunnelInfo.

        隧道ID

        :param tunnel_id: The tunnel_id of this TunnelInfo.
        :type tunnel_id: str
        """
        self._tunnel_id = tunnel_id

    @property
    def device_id(self):
        r"""Gets the device_id of this TunnelInfo.

        设备ID

        :return: The device_id of this TunnelInfo.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        r"""Sets the device_id of this TunnelInfo.

        设备ID

        :param device_id: The device_id of this TunnelInfo.
        :type device_id: str
        """
        self._device_id = device_id

    @property
    def create_time(self):
        r"""Gets the create_time of this TunnelInfo.

        隧道创建时间。格式：yyyyMMdd'T'HHmmss'Z'，如20151212T121212Z。

        :return: The create_time of this TunnelInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this TunnelInfo.

        隧道创建时间。格式：yyyyMMdd'T'HHmmss'Z'，如20151212T121212Z。

        :param create_time: The create_time of this TunnelInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def closed_time(self):
        r"""Gets the closed_time of this TunnelInfo.

        隧道更新时间。格式：yyyyMMdd'T'HHmmss'Z'，如20151212T121212Z。

        :return: The closed_time of this TunnelInfo.
        :rtype: str
        """
        return self._closed_time

    @closed_time.setter
    def closed_time(self, closed_time):
        r"""Sets the closed_time of this TunnelInfo.

        隧道更新时间。格式：yyyyMMdd'T'HHmmss'Z'，如20151212T121212Z。

        :param closed_time: The closed_time of this TunnelInfo.
        :type closed_time: str
        """
        self._closed_time = closed_time

    @property
    def status(self):
        r"""Gets the status of this TunnelInfo.

        隧道状态 CLOSED | OPEN

        :return: The status of this TunnelInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this TunnelInfo.

        隧道状态 CLOSED | OPEN

        :param status: The status of this TunnelInfo.
        :type status: str
        """
        self._status = status

    @property
    def source_connect_state(self):
        r"""Gets the source_connect_state of this TunnelInfo.

        :return: The source_connect_state of this TunnelInfo.
        :rtype: :class:`huaweicloudsdkiotda.v5.ConnectState`
        """
        return self._source_connect_state

    @source_connect_state.setter
    def source_connect_state(self, source_connect_state):
        r"""Sets the source_connect_state of this TunnelInfo.

        :param source_connect_state: The source_connect_state of this TunnelInfo.
        :type source_connect_state: :class:`huaweicloudsdkiotda.v5.ConnectState`
        """
        self._source_connect_state = source_connect_state

    @property
    def device_connect_state(self):
        r"""Gets the device_connect_state of this TunnelInfo.

        :return: The device_connect_state of this TunnelInfo.
        :rtype: :class:`huaweicloudsdkiotda.v5.ConnectState`
        """
        return self._device_connect_state

    @device_connect_state.setter
    def device_connect_state(self, device_connect_state):
        r"""Sets the device_connect_state of this TunnelInfo.

        :param device_connect_state: The device_connect_state of this TunnelInfo.
        :type device_connect_state: :class:`huaweicloudsdkiotda.v5.ConnectState`
        """
        self._device_connect_state = device_connect_state

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
        if not isinstance(other, TunnelInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
