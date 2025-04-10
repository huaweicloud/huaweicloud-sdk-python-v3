# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSubscriptionTargetResponse(SdkResponse):

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
        'kafka_detail': 'KafkaTargetDetail',
        'smn_detail': 'SmnTargetDetail',
        'eg_detail': 'EgTargetDetail',
        'apigw_detail': 'ApigwTargetDetail',
        'retry_times': 'int',
        'transform': 'TransForm',
        'dead_letter_queue': 'DeadLetterQueue',
        'created_time': 'str',
        'updated_time': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'provider_type': 'provider_type',
        'connection_id': 'connection_id',
        'detail': 'detail',
        'kafka_detail': 'kafka_detail',
        'smn_detail': 'smn_detail',
        'eg_detail': 'eg_detail',
        'apigw_detail': 'apigw_detail',
        'retry_times': 'retry_times',
        'transform': 'transform',
        'dead_letter_queue': 'dead_letter_queue',
        'created_time': 'created_time',
        'updated_time': 'updated_time',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, id=None, name=None, provider_type=None, connection_id=None, detail=None, kafka_detail=None, smn_detail=None, eg_detail=None, apigw_detail=None, retry_times=None, transform=None, dead_letter_queue=None, created_time=None, updated_time=None, x_request_id=None):
        r"""UpdateSubscriptionTargetResponse

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
        :param kafka_detail: 
        :type kafka_detail: :class:`huaweicloudsdkeg.v1.KafkaTargetDetail`
        :param smn_detail: 
        :type smn_detail: :class:`huaweicloudsdkeg.v1.SmnTargetDetail`
        :param eg_detail: 
        :type eg_detail: :class:`huaweicloudsdkeg.v1.EgTargetDetail`
        :param apigw_detail: 
        :type apigw_detail: :class:`huaweicloudsdkeg.v1.ApigwTargetDetail`
        :param retry_times: 重试次数
        :type retry_times: int
        :param transform: 
        :type transform: :class:`huaweicloudsdkeg.v1.TransForm`
        :param dead_letter_queue: 
        :type dead_letter_queue: :class:`huaweicloudsdkeg.v1.DeadLetterQueue`
        :param created_time: 创建时间
        :type created_time: str
        :param updated_time: 更新时间
        :type updated_time: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(UpdateSubscriptionTargetResponse, self).__init__()

        self._id = None
        self._name = None
        self._provider_type = None
        self._connection_id = None
        self._detail = None
        self._kafka_detail = None
        self._smn_detail = None
        self._eg_detail = None
        self._apigw_detail = None
        self._retry_times = None
        self._transform = None
        self._dead_letter_queue = None
        self._created_time = None
        self._updated_time = None
        self._x_request_id = None
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
        if kafka_detail is not None:
            self.kafka_detail = kafka_detail
        if smn_detail is not None:
            self.smn_detail = smn_detail
        if eg_detail is not None:
            self.eg_detail = eg_detail
        if apigw_detail is not None:
            self.apigw_detail = apigw_detail
        if retry_times is not None:
            self.retry_times = retry_times
        if transform is not None:
            self.transform = transform
        if dead_letter_queue is not None:
            self.dead_letter_queue = dead_letter_queue
        if created_time is not None:
            self.created_time = created_time
        if updated_time is not None:
            self.updated_time = updated_time
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def id(self):
        r"""Gets the id of this UpdateSubscriptionTargetResponse.

        订阅目标ID

        :return: The id of this UpdateSubscriptionTargetResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UpdateSubscriptionTargetResponse.

        订阅目标ID

        :param id: The id of this UpdateSubscriptionTargetResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this UpdateSubscriptionTargetResponse.

        订阅的事件目标名称

        :return: The name of this UpdateSubscriptionTargetResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateSubscriptionTargetResponse.

        订阅的事件目标名称

        :param name: The name of this UpdateSubscriptionTargetResponse.
        :type name: str
        """
        self._name = name

    @property
    def provider_type(self):
        r"""Gets the provider_type of this UpdateSubscriptionTargetResponse.

        订阅的事件目标的提供方类型

        :return: The provider_type of this UpdateSubscriptionTargetResponse.
        :rtype: str
        """
        return self._provider_type

    @provider_type.setter
    def provider_type(self, provider_type):
        r"""Sets the provider_type of this UpdateSubscriptionTargetResponse.

        订阅的事件目标的提供方类型

        :param provider_type: The provider_type of this UpdateSubscriptionTargetResponse.
        :type provider_type: str
        """
        self._provider_type = provider_type

    @property
    def connection_id(self):
        r"""Gets the connection_id of this UpdateSubscriptionTargetResponse.

        订阅的事件目标使用的目标链接ID

        :return: The connection_id of this UpdateSubscriptionTargetResponse.
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        r"""Sets the connection_id of this UpdateSubscriptionTargetResponse.

        订阅的事件目标使用的目标链接ID

        :param connection_id: The connection_id of this UpdateSubscriptionTargetResponse.
        :type connection_id: str
        """
        self._connection_id = connection_id

    @property
    def detail(self):
        r"""Gets the detail of this UpdateSubscriptionTargetResponse.

        订阅的事件目标参数列表

        :return: The detail of this UpdateSubscriptionTargetResponse.
        :rtype: object
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        r"""Sets the detail of this UpdateSubscriptionTargetResponse.

        订阅的事件目标参数列表

        :param detail: The detail of this UpdateSubscriptionTargetResponse.
        :type detail: object
        """
        self._detail = detail

    @property
    def kafka_detail(self):
        r"""Gets the kafka_detail of this UpdateSubscriptionTargetResponse.

        :return: The kafka_detail of this UpdateSubscriptionTargetResponse.
        :rtype: :class:`huaweicloudsdkeg.v1.KafkaTargetDetail`
        """
        return self._kafka_detail

    @kafka_detail.setter
    def kafka_detail(self, kafka_detail):
        r"""Sets the kafka_detail of this UpdateSubscriptionTargetResponse.

        :param kafka_detail: The kafka_detail of this UpdateSubscriptionTargetResponse.
        :type kafka_detail: :class:`huaweicloudsdkeg.v1.KafkaTargetDetail`
        """
        self._kafka_detail = kafka_detail

    @property
    def smn_detail(self):
        r"""Gets the smn_detail of this UpdateSubscriptionTargetResponse.

        :return: The smn_detail of this UpdateSubscriptionTargetResponse.
        :rtype: :class:`huaweicloudsdkeg.v1.SmnTargetDetail`
        """
        return self._smn_detail

    @smn_detail.setter
    def smn_detail(self, smn_detail):
        r"""Sets the smn_detail of this UpdateSubscriptionTargetResponse.

        :param smn_detail: The smn_detail of this UpdateSubscriptionTargetResponse.
        :type smn_detail: :class:`huaweicloudsdkeg.v1.SmnTargetDetail`
        """
        self._smn_detail = smn_detail

    @property
    def eg_detail(self):
        r"""Gets the eg_detail of this UpdateSubscriptionTargetResponse.

        :return: The eg_detail of this UpdateSubscriptionTargetResponse.
        :rtype: :class:`huaweicloudsdkeg.v1.EgTargetDetail`
        """
        return self._eg_detail

    @eg_detail.setter
    def eg_detail(self, eg_detail):
        r"""Sets the eg_detail of this UpdateSubscriptionTargetResponse.

        :param eg_detail: The eg_detail of this UpdateSubscriptionTargetResponse.
        :type eg_detail: :class:`huaweicloudsdkeg.v1.EgTargetDetail`
        """
        self._eg_detail = eg_detail

    @property
    def apigw_detail(self):
        r"""Gets the apigw_detail of this UpdateSubscriptionTargetResponse.

        :return: The apigw_detail of this UpdateSubscriptionTargetResponse.
        :rtype: :class:`huaweicloudsdkeg.v1.ApigwTargetDetail`
        """
        return self._apigw_detail

    @apigw_detail.setter
    def apigw_detail(self, apigw_detail):
        r"""Sets the apigw_detail of this UpdateSubscriptionTargetResponse.

        :param apigw_detail: The apigw_detail of this UpdateSubscriptionTargetResponse.
        :type apigw_detail: :class:`huaweicloudsdkeg.v1.ApigwTargetDetail`
        """
        self._apigw_detail = apigw_detail

    @property
    def retry_times(self):
        r"""Gets the retry_times of this UpdateSubscriptionTargetResponse.

        重试次数

        :return: The retry_times of this UpdateSubscriptionTargetResponse.
        :rtype: int
        """
        return self._retry_times

    @retry_times.setter
    def retry_times(self, retry_times):
        r"""Sets the retry_times of this UpdateSubscriptionTargetResponse.

        重试次数

        :param retry_times: The retry_times of this UpdateSubscriptionTargetResponse.
        :type retry_times: int
        """
        self._retry_times = retry_times

    @property
    def transform(self):
        r"""Gets the transform of this UpdateSubscriptionTargetResponse.

        :return: The transform of this UpdateSubscriptionTargetResponse.
        :rtype: :class:`huaweicloudsdkeg.v1.TransForm`
        """
        return self._transform

    @transform.setter
    def transform(self, transform):
        r"""Sets the transform of this UpdateSubscriptionTargetResponse.

        :param transform: The transform of this UpdateSubscriptionTargetResponse.
        :type transform: :class:`huaweicloudsdkeg.v1.TransForm`
        """
        self._transform = transform

    @property
    def dead_letter_queue(self):
        r"""Gets the dead_letter_queue of this UpdateSubscriptionTargetResponse.

        :return: The dead_letter_queue of this UpdateSubscriptionTargetResponse.
        :rtype: :class:`huaweicloudsdkeg.v1.DeadLetterQueue`
        """
        return self._dead_letter_queue

    @dead_letter_queue.setter
    def dead_letter_queue(self, dead_letter_queue):
        r"""Sets the dead_letter_queue of this UpdateSubscriptionTargetResponse.

        :param dead_letter_queue: The dead_letter_queue of this UpdateSubscriptionTargetResponse.
        :type dead_letter_queue: :class:`huaweicloudsdkeg.v1.DeadLetterQueue`
        """
        self._dead_letter_queue = dead_letter_queue

    @property
    def created_time(self):
        r"""Gets the created_time of this UpdateSubscriptionTargetResponse.

        创建时间

        :return: The created_time of this UpdateSubscriptionTargetResponse.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this UpdateSubscriptionTargetResponse.

        创建时间

        :param created_time: The created_time of this UpdateSubscriptionTargetResponse.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def updated_time(self):
        r"""Gets the updated_time of this UpdateSubscriptionTargetResponse.

        更新时间

        :return: The updated_time of this UpdateSubscriptionTargetResponse.
        :rtype: str
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        r"""Sets the updated_time of this UpdateSubscriptionTargetResponse.

        更新时间

        :param updated_time: The updated_time of this UpdateSubscriptionTargetResponse.
        :type updated_time: str
        """
        self._updated_time = updated_time

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this UpdateSubscriptionTargetResponse.

        :return: The x_request_id of this UpdateSubscriptionTargetResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this UpdateSubscriptionTargetResponse.

        :param x_request_id: The x_request_id of this UpdateSubscriptionTargetResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, UpdateSubscriptionTargetResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
