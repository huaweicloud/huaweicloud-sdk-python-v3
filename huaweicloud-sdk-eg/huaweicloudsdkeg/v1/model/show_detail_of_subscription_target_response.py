# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDetailOfSubscriptionTargetResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'provider_type': 'str',
        'connection_id': 'str',
        'detail': 'object',
        'transform': 'TransForm',
        'dead_letter_queue': 'DeadLetterQueue',
        'created_time': 'str',
        'updated_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'provider_type': 'provider_type',
        'connection_id': 'connection_id',
        'detail': 'detail',
        'transform': 'transform',
        'dead_letter_queue': 'dead_letter_queue',
        'created_time': 'created_time',
        'updated_time': 'updated_time'
    }

    def __init__(self, id=None, name=None, provider_type=None, connection_id=None, detail=None, transform=None, dead_letter_queue=None, created_time=None, updated_time=None):
        """ShowDetailOfSubscriptionTargetResponse

        The model defined in huaweicloud sdk

        :param id: 订阅目标ID
        :type id: str
        :param name: 订阅的事件目标名称
        :type name: str
        :param provider_type: 订阅的事件目标的提供方类型
        :type provider_type: str
        :param connection_id: 订阅的事件目标使用的目标链接ID
        :type connection_id: str
        :param detail: 订阅的事件目标参数列表
        :type detail: object
        :param transform: 
        :type transform: :class:`huaweicloudsdkeg.v1.TransForm`
        :param dead_letter_queue: 
        :type dead_letter_queue: :class:`huaweicloudsdkeg.v1.DeadLetterQueue`
        :param created_time: 创建时间
        :type created_time: str
        :param updated_time: 更新时间
        :type updated_time: str
        """
        
        super(ShowDetailOfSubscriptionTargetResponse, self).__init__()

        self._id = None
        self._name = None
        self._provider_type = None
        self._connection_id = None
        self._detail = None
        self._transform = None
        self._dead_letter_queue = None
        self._created_time = None
        self._updated_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if provider_type is not None:
            self.provider_type = provider_type
        if connection_id is not None:
            self.connection_id = connection_id
        if detail is not None:
            self.detail = detail
        if transform is not None:
            self.transform = transform
        if dead_letter_queue is not None:
            self.dead_letter_queue = dead_letter_queue
        if created_time is not None:
            self.created_time = created_time
        if updated_time is not None:
            self.updated_time = updated_time

    @property
    def id(self):
        """Gets the id of this ShowDetailOfSubscriptionTargetResponse.

        订阅目标ID

        :return: The id of this ShowDetailOfSubscriptionTargetResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowDetailOfSubscriptionTargetResponse.

        订阅目标ID

        :param id: The id of this ShowDetailOfSubscriptionTargetResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ShowDetailOfSubscriptionTargetResponse.

        订阅的事件目标名称

        :return: The name of this ShowDetailOfSubscriptionTargetResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowDetailOfSubscriptionTargetResponse.

        订阅的事件目标名称

        :param name: The name of this ShowDetailOfSubscriptionTargetResponse.
        :type name: str
        """
        self._name = name

    @property
    def provider_type(self):
        """Gets the provider_type of this ShowDetailOfSubscriptionTargetResponse.

        订阅的事件目标的提供方类型

        :return: The provider_type of this ShowDetailOfSubscriptionTargetResponse.
        :rtype: str
        """
        return self._provider_type

    @provider_type.setter
    def provider_type(self, provider_type):
        """Sets the provider_type of this ShowDetailOfSubscriptionTargetResponse.

        订阅的事件目标的提供方类型

        :param provider_type: The provider_type of this ShowDetailOfSubscriptionTargetResponse.
        :type provider_type: str
        """
        self._provider_type = provider_type

    @property
    def connection_id(self):
        """Gets the connection_id of this ShowDetailOfSubscriptionTargetResponse.

        订阅的事件目标使用的目标链接ID

        :return: The connection_id of this ShowDetailOfSubscriptionTargetResponse.
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        """Sets the connection_id of this ShowDetailOfSubscriptionTargetResponse.

        订阅的事件目标使用的目标链接ID

        :param connection_id: The connection_id of this ShowDetailOfSubscriptionTargetResponse.
        :type connection_id: str
        """
        self._connection_id = connection_id

    @property
    def detail(self):
        """Gets the detail of this ShowDetailOfSubscriptionTargetResponse.

        订阅的事件目标参数列表

        :return: The detail of this ShowDetailOfSubscriptionTargetResponse.
        :rtype: object
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this ShowDetailOfSubscriptionTargetResponse.

        订阅的事件目标参数列表

        :param detail: The detail of this ShowDetailOfSubscriptionTargetResponse.
        :type detail: object
        """
        self._detail = detail

    @property
    def transform(self):
        """Gets the transform of this ShowDetailOfSubscriptionTargetResponse.

        :return: The transform of this ShowDetailOfSubscriptionTargetResponse.
        :rtype: :class:`huaweicloudsdkeg.v1.TransForm`
        """
        return self._transform

    @transform.setter
    def transform(self, transform):
        """Sets the transform of this ShowDetailOfSubscriptionTargetResponse.

        :param transform: The transform of this ShowDetailOfSubscriptionTargetResponse.
        :type transform: :class:`huaweicloudsdkeg.v1.TransForm`
        """
        self._transform = transform

    @property
    def dead_letter_queue(self):
        """Gets the dead_letter_queue of this ShowDetailOfSubscriptionTargetResponse.

        :return: The dead_letter_queue of this ShowDetailOfSubscriptionTargetResponse.
        :rtype: :class:`huaweicloudsdkeg.v1.DeadLetterQueue`
        """
        return self._dead_letter_queue

    @dead_letter_queue.setter
    def dead_letter_queue(self, dead_letter_queue):
        """Sets the dead_letter_queue of this ShowDetailOfSubscriptionTargetResponse.

        :param dead_letter_queue: The dead_letter_queue of this ShowDetailOfSubscriptionTargetResponse.
        :type dead_letter_queue: :class:`huaweicloudsdkeg.v1.DeadLetterQueue`
        """
        self._dead_letter_queue = dead_letter_queue

    @property
    def created_time(self):
        """Gets the created_time of this ShowDetailOfSubscriptionTargetResponse.

        创建时间

        :return: The created_time of this ShowDetailOfSubscriptionTargetResponse.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this ShowDetailOfSubscriptionTargetResponse.

        创建时间

        :param created_time: The created_time of this ShowDetailOfSubscriptionTargetResponse.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def updated_time(self):
        """Gets the updated_time of this ShowDetailOfSubscriptionTargetResponse.

        更新时间

        :return: The updated_time of this ShowDetailOfSubscriptionTargetResponse.
        :rtype: str
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        """Sets the updated_time of this ShowDetailOfSubscriptionTargetResponse.

        更新时间

        :param updated_time: The updated_time of this ShowDetailOfSubscriptionTargetResponse.
        :type updated_time: str
        """
        self._updated_time = updated_time

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
        if not isinstance(other, ShowDetailOfSubscriptionTargetResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
