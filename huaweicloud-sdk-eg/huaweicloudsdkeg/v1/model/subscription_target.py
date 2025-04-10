# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubscriptionTarget:

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
        'dead_letter_queue': 'DeadLetterQueue'
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
        'dead_letter_queue': 'dead_letter_queue'
    }

    def __init__(self, id=None, name=None, provider_type=None, connection_id=None, detail=None, kafka_detail=None, smn_detail=None, eg_detail=None, apigw_detail=None, retry_times=None, transform=None, dead_letter_queue=None):
        r"""SubscriptionTarget

        The model defined in huaweicloud sdk

        :param id: 订阅目标ID，需保证全局唯一，由小写字母、数字、中划线组成，必须字母或数字开头。 更新订阅场景时，指定ID的订阅目标存在时则进行更新，否则进行创建； 创建订阅目标场景时，指定ID作为待创建的订阅目标对象ID，未指定时由系统自动生成。 更新订阅目标时，此字段忽略；
        :type id: str
        :param name: 订阅的事件目标名称
        :type name: str
        :param provider_type: 订阅的事件目标的提供方类型
        :type provider_type: str
        :param connection_id: 订阅的事件目标使用的目标链接ID
        :type connection_id: str
        :param detail: 订阅的事件目标参数列表，该字段序列化后总长度不超过1024字节，函数(urn、invoke_type、agency_name)、函数流（workflow_id、agency_name）、webhook（url）订阅目标必填，其中函数、函数流委托名称必填
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
        """
        
        

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
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
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
        self.transform = transform
        if dead_letter_queue is not None:
            self.dead_letter_queue = dead_letter_queue

    @property
    def id(self):
        r"""Gets the id of this SubscriptionTarget.

        订阅目标ID，需保证全局唯一，由小写字母、数字、中划线组成，必须字母或数字开头。 更新订阅场景时，指定ID的订阅目标存在时则进行更新，否则进行创建； 创建订阅目标场景时，指定ID作为待创建的订阅目标对象ID，未指定时由系统自动生成。 更新订阅目标时，此字段忽略；

        :return: The id of this SubscriptionTarget.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SubscriptionTarget.

        订阅目标ID，需保证全局唯一，由小写字母、数字、中划线组成，必须字母或数字开头。 更新订阅场景时，指定ID的订阅目标存在时则进行更新，否则进行创建； 创建订阅目标场景时，指定ID作为待创建的订阅目标对象ID，未指定时由系统自动生成。 更新订阅目标时，此字段忽略；

        :param id: The id of this SubscriptionTarget.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this SubscriptionTarget.

        订阅的事件目标名称

        :return: The name of this SubscriptionTarget.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this SubscriptionTarget.

        订阅的事件目标名称

        :param name: The name of this SubscriptionTarget.
        :type name: str
        """
        self._name = name

    @property
    def provider_type(self):
        r"""Gets the provider_type of this SubscriptionTarget.

        订阅的事件目标的提供方类型

        :return: The provider_type of this SubscriptionTarget.
        :rtype: str
        """
        return self._provider_type

    @provider_type.setter
    def provider_type(self, provider_type):
        r"""Sets the provider_type of this SubscriptionTarget.

        订阅的事件目标的提供方类型

        :param provider_type: The provider_type of this SubscriptionTarget.
        :type provider_type: str
        """
        self._provider_type = provider_type

    @property
    def connection_id(self):
        r"""Gets the connection_id of this SubscriptionTarget.

        订阅的事件目标使用的目标链接ID

        :return: The connection_id of this SubscriptionTarget.
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        r"""Sets the connection_id of this SubscriptionTarget.

        订阅的事件目标使用的目标链接ID

        :param connection_id: The connection_id of this SubscriptionTarget.
        :type connection_id: str
        """
        self._connection_id = connection_id

    @property
    def detail(self):
        r"""Gets the detail of this SubscriptionTarget.

        订阅的事件目标参数列表，该字段序列化后总长度不超过1024字节，函数(urn、invoke_type、agency_name)、函数流（workflow_id、agency_name）、webhook（url）订阅目标必填，其中函数、函数流委托名称必填

        :return: The detail of this SubscriptionTarget.
        :rtype: object
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        r"""Sets the detail of this SubscriptionTarget.

        订阅的事件目标参数列表，该字段序列化后总长度不超过1024字节，函数(urn、invoke_type、agency_name)、函数流（workflow_id、agency_name）、webhook（url）订阅目标必填，其中函数、函数流委托名称必填

        :param detail: The detail of this SubscriptionTarget.
        :type detail: object
        """
        self._detail = detail

    @property
    def kafka_detail(self):
        r"""Gets the kafka_detail of this SubscriptionTarget.

        :return: The kafka_detail of this SubscriptionTarget.
        :rtype: :class:`huaweicloudsdkeg.v1.KafkaTargetDetail`
        """
        return self._kafka_detail

    @kafka_detail.setter
    def kafka_detail(self, kafka_detail):
        r"""Sets the kafka_detail of this SubscriptionTarget.

        :param kafka_detail: The kafka_detail of this SubscriptionTarget.
        :type kafka_detail: :class:`huaweicloudsdkeg.v1.KafkaTargetDetail`
        """
        self._kafka_detail = kafka_detail

    @property
    def smn_detail(self):
        r"""Gets the smn_detail of this SubscriptionTarget.

        :return: The smn_detail of this SubscriptionTarget.
        :rtype: :class:`huaweicloudsdkeg.v1.SmnTargetDetail`
        """
        return self._smn_detail

    @smn_detail.setter
    def smn_detail(self, smn_detail):
        r"""Sets the smn_detail of this SubscriptionTarget.

        :param smn_detail: The smn_detail of this SubscriptionTarget.
        :type smn_detail: :class:`huaweicloudsdkeg.v1.SmnTargetDetail`
        """
        self._smn_detail = smn_detail

    @property
    def eg_detail(self):
        r"""Gets the eg_detail of this SubscriptionTarget.

        :return: The eg_detail of this SubscriptionTarget.
        :rtype: :class:`huaweicloudsdkeg.v1.EgTargetDetail`
        """
        return self._eg_detail

    @eg_detail.setter
    def eg_detail(self, eg_detail):
        r"""Sets the eg_detail of this SubscriptionTarget.

        :param eg_detail: The eg_detail of this SubscriptionTarget.
        :type eg_detail: :class:`huaweicloudsdkeg.v1.EgTargetDetail`
        """
        self._eg_detail = eg_detail

    @property
    def apigw_detail(self):
        r"""Gets the apigw_detail of this SubscriptionTarget.

        :return: The apigw_detail of this SubscriptionTarget.
        :rtype: :class:`huaweicloudsdkeg.v1.ApigwTargetDetail`
        """
        return self._apigw_detail

    @apigw_detail.setter
    def apigw_detail(self, apigw_detail):
        r"""Sets the apigw_detail of this SubscriptionTarget.

        :param apigw_detail: The apigw_detail of this SubscriptionTarget.
        :type apigw_detail: :class:`huaweicloudsdkeg.v1.ApigwTargetDetail`
        """
        self._apigw_detail = apigw_detail

    @property
    def retry_times(self):
        r"""Gets the retry_times of this SubscriptionTarget.

        重试次数

        :return: The retry_times of this SubscriptionTarget.
        :rtype: int
        """
        return self._retry_times

    @retry_times.setter
    def retry_times(self, retry_times):
        r"""Sets the retry_times of this SubscriptionTarget.

        重试次数

        :param retry_times: The retry_times of this SubscriptionTarget.
        :type retry_times: int
        """
        self._retry_times = retry_times

    @property
    def transform(self):
        r"""Gets the transform of this SubscriptionTarget.

        :return: The transform of this SubscriptionTarget.
        :rtype: :class:`huaweicloudsdkeg.v1.TransForm`
        """
        return self._transform

    @transform.setter
    def transform(self, transform):
        r"""Sets the transform of this SubscriptionTarget.

        :param transform: The transform of this SubscriptionTarget.
        :type transform: :class:`huaweicloudsdkeg.v1.TransForm`
        """
        self._transform = transform

    @property
    def dead_letter_queue(self):
        r"""Gets the dead_letter_queue of this SubscriptionTarget.

        :return: The dead_letter_queue of this SubscriptionTarget.
        :rtype: :class:`huaweicloudsdkeg.v1.DeadLetterQueue`
        """
        return self._dead_letter_queue

    @dead_letter_queue.setter
    def dead_letter_queue(self, dead_letter_queue):
        r"""Sets the dead_letter_queue of this SubscriptionTarget.

        :param dead_letter_queue: The dead_letter_queue of this SubscriptionTarget.
        :type dead_letter_queue: :class:`huaweicloudsdkeg.v1.DeadLetterQueue`
        """
        self._dead_letter_queue = dead_letter_queue

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
        if not isinstance(other, SubscriptionTarget):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
