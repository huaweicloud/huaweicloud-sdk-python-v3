# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceNotifyBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'event_id': 'str',
        'capture_time': 'str',
        'domain_id': 'str',
        'resource_id': 'str',
        'resource_type': 'str',
        'event_type': 'str',
        'checksum': 'str',
        'sync_type': 'str',
        'resource': 'ResourceNotifyEntity'
    }

    attribute_map = {
        'event_id': 'event_id',
        'capture_time': 'capture_time',
        'domain_id': 'domain_id',
        'resource_id': 'resource_id',
        'resource_type': 'resource_type',
        'event_type': 'event_type',
        'checksum': 'checksum',
        'sync_type': 'sync_type',
        'resource': 'resource'
    }

    def __init__(self, event_id=None, capture_time=None, domain_id=None, resource_id=None, resource_type=None, event_type=None, checksum=None, sync_type=None, resource=None):
        r"""ResourceNotifyBody

        The model defined in huaweicloud sdk

        :param event_id: 事件ID
        :type event_id: str
        :param capture_time: 捕获时间
        :type capture_time: str
        :param domain_id: 账户ID
        :type domain_id: str
        :param resource_id: 资源ID
        :type resource_id: str
        :param resource_type: 资源类型
        :type resource_type: str
        :param event_type: 事件类型：CREATE-创建，UPDATE-更新，DELETE-删除
        :type event_type: str
        :param checksum: 检验码
        :type checksum: str
        :param sync_type: 同步类型
        :type sync_type: str
        :param resource: 
        :type resource: :class:`huaweicloudsdkbcc.v1.ResourceNotifyEntity`
        """
        
        

        self._event_id = None
        self._capture_time = None
        self._domain_id = None
        self._resource_id = None
        self._resource_type = None
        self._event_type = None
        self._checksum = None
        self._sync_type = None
        self._resource = None
        self.discriminator = None

        self.event_id = event_id
        if capture_time is not None:
            self.capture_time = capture_time
        self.domain_id = domain_id
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.event_type = event_type
        if checksum is not None:
            self.checksum = checksum
        if sync_type is not None:
            self.sync_type = sync_type
        if resource is not None:
            self.resource = resource

    @property
    def event_id(self):
        r"""Gets the event_id of this ResourceNotifyBody.

        事件ID

        :return: The event_id of this ResourceNotifyBody.
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        r"""Sets the event_id of this ResourceNotifyBody.

        事件ID

        :param event_id: The event_id of this ResourceNotifyBody.
        :type event_id: str
        """
        self._event_id = event_id

    @property
    def capture_time(self):
        r"""Gets the capture_time of this ResourceNotifyBody.

        捕获时间

        :return: The capture_time of this ResourceNotifyBody.
        :rtype: str
        """
        return self._capture_time

    @capture_time.setter
    def capture_time(self, capture_time):
        r"""Sets the capture_time of this ResourceNotifyBody.

        捕获时间

        :param capture_time: The capture_time of this ResourceNotifyBody.
        :type capture_time: str
        """
        self._capture_time = capture_time

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ResourceNotifyBody.

        账户ID

        :return: The domain_id of this ResourceNotifyBody.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ResourceNotifyBody.

        账户ID

        :param domain_id: The domain_id of this ResourceNotifyBody.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ResourceNotifyBody.

        资源ID

        :return: The resource_id of this ResourceNotifyBody.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ResourceNotifyBody.

        资源ID

        :param resource_id: The resource_id of this ResourceNotifyBody.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ResourceNotifyBody.

        资源类型

        :return: The resource_type of this ResourceNotifyBody.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ResourceNotifyBody.

        资源类型

        :param resource_type: The resource_type of this ResourceNotifyBody.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def event_type(self):
        r"""Gets the event_type of this ResourceNotifyBody.

        事件类型：CREATE-创建，UPDATE-更新，DELETE-删除

        :return: The event_type of this ResourceNotifyBody.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        r"""Sets the event_type of this ResourceNotifyBody.

        事件类型：CREATE-创建，UPDATE-更新，DELETE-删除

        :param event_type: The event_type of this ResourceNotifyBody.
        :type event_type: str
        """
        self._event_type = event_type

    @property
    def checksum(self):
        r"""Gets the checksum of this ResourceNotifyBody.

        检验码

        :return: The checksum of this ResourceNotifyBody.
        :rtype: str
        """
        return self._checksum

    @checksum.setter
    def checksum(self, checksum):
        r"""Sets the checksum of this ResourceNotifyBody.

        检验码

        :param checksum: The checksum of this ResourceNotifyBody.
        :type checksum: str
        """
        self._checksum = checksum

    @property
    def sync_type(self):
        r"""Gets the sync_type of this ResourceNotifyBody.

        同步类型

        :return: The sync_type of this ResourceNotifyBody.
        :rtype: str
        """
        return self._sync_type

    @sync_type.setter
    def sync_type(self, sync_type):
        r"""Sets the sync_type of this ResourceNotifyBody.

        同步类型

        :param sync_type: The sync_type of this ResourceNotifyBody.
        :type sync_type: str
        """
        self._sync_type = sync_type

    @property
    def resource(self):
        r"""Gets the resource of this ResourceNotifyBody.

        :return: The resource of this ResourceNotifyBody.
        :rtype: :class:`huaweicloudsdkbcc.v1.ResourceNotifyEntity`
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        r"""Sets the resource of this ResourceNotifyBody.

        :param resource: The resource of this ResourceNotifyBody.
        :type resource: :class:`huaweicloudsdkbcc.v1.ResourceNotifyEntity`
        """
        self._resource = resource

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ResourceNotifyBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
