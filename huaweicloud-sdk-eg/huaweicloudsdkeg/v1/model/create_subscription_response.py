# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSubscriptionResponse(SdkResponse):

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
        'description': 'str',
        'type': 'str',
        'status': 'str',
        'channel_id': 'str',
        'channel_name': 'str',
        'used': 'list[SubscriptionUsedInfo]',
        'sources': 'list[SubscriptionSourceInfo]',
        'targets': 'list[SubscriptionTargetInfo]',
        'created_time': 'str',
        'updated_time': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'type': 'type',
        'status': 'status',
        'channel_id': 'channel_id',
        'channel_name': 'channel_name',
        'used': 'used',
        'sources': 'sources',
        'targets': 'targets',
        'created_time': 'created_time',
        'updated_time': 'updated_time',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, id=None, name=None, description=None, type=None, status=None, channel_id=None, channel_name=None, used=None, sources=None, targets=None, created_time=None, updated_time=None, x_request_id=None):
        r"""CreateSubscriptionResponse

        The model defined in huaweicloud sdk

        :param id: 订阅ID
        :type id: str
        :param name: 订阅名称
        :type name: str
        :param description: 订阅描述
        :type description: str
        :param type: 类型
        :type type: str
        :param status: 状态
        :type status: str
        :param channel_id: 通道ID
        :type channel_id: str
        :param channel_name: 通道名称
        :type channel_name: str
        :param used: 标签信息
        :type used: list[:class:`huaweicloudsdkeg.v1.SubscriptionUsedInfo`]
        :param sources: 订阅源列表
        :type sources: list[:class:`huaweicloudsdkeg.v1.SubscriptionSourceInfo`]
        :param targets: 订阅目标列表
        :type targets: list[:class:`huaweicloudsdkeg.v1.SubscriptionTargetInfo`]
        :param created_time: 创建时间
        :type created_time: str
        :param updated_time: 更新时间
        :type updated_time: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(CreateSubscriptionResponse, self).__init__()

        self._id = None
        self._name = None
        self._description = None
        self._type = None
        self._status = None
        self._channel_id = None
        self._channel_name = None
        self._used = None
        self._sources = None
        self._targets = None
        self._created_time = None
        self._updated_time = None
        self._x_request_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if channel_id is not None:
            self.channel_id = channel_id
        if channel_name is not None:
            self.channel_name = channel_name
        if used is not None:
            self.used = used
        if sources is not None:
            self.sources = sources
        if targets is not None:
            self.targets = targets
        if created_time is not None:
            self.created_time = created_time
        if updated_time is not None:
            self.updated_time = updated_time
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def id(self):
        r"""Gets the id of this CreateSubscriptionResponse.

        订阅ID

        :return: The id of this CreateSubscriptionResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateSubscriptionResponse.

        订阅ID

        :param id: The id of this CreateSubscriptionResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this CreateSubscriptionResponse.

        订阅名称

        :return: The name of this CreateSubscriptionResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateSubscriptionResponse.

        订阅名称

        :param name: The name of this CreateSubscriptionResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateSubscriptionResponse.

        订阅描述

        :return: The description of this CreateSubscriptionResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateSubscriptionResponse.

        订阅描述

        :param description: The description of this CreateSubscriptionResponse.
        :type description: str
        """
        self._description = description

    @property
    def type(self):
        r"""Gets the type of this CreateSubscriptionResponse.

        类型

        :return: The type of this CreateSubscriptionResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateSubscriptionResponse.

        类型

        :param type: The type of this CreateSubscriptionResponse.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        r"""Gets the status of this CreateSubscriptionResponse.

        状态

        :return: The status of this CreateSubscriptionResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreateSubscriptionResponse.

        状态

        :param status: The status of this CreateSubscriptionResponse.
        :type status: str
        """
        self._status = status

    @property
    def channel_id(self):
        r"""Gets the channel_id of this CreateSubscriptionResponse.

        通道ID

        :return: The channel_id of this CreateSubscriptionResponse.
        :rtype: str
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        r"""Sets the channel_id of this CreateSubscriptionResponse.

        通道ID

        :param channel_id: The channel_id of this CreateSubscriptionResponse.
        :type channel_id: str
        """
        self._channel_id = channel_id

    @property
    def channel_name(self):
        r"""Gets the channel_name of this CreateSubscriptionResponse.

        通道名称

        :return: The channel_name of this CreateSubscriptionResponse.
        :rtype: str
        """
        return self._channel_name

    @channel_name.setter
    def channel_name(self, channel_name):
        r"""Sets the channel_name of this CreateSubscriptionResponse.

        通道名称

        :param channel_name: The channel_name of this CreateSubscriptionResponse.
        :type channel_name: str
        """
        self._channel_name = channel_name

    @property
    def used(self):
        r"""Gets the used of this CreateSubscriptionResponse.

        标签信息

        :return: The used of this CreateSubscriptionResponse.
        :rtype: list[:class:`huaweicloudsdkeg.v1.SubscriptionUsedInfo`]
        """
        return self._used

    @used.setter
    def used(self, used):
        r"""Sets the used of this CreateSubscriptionResponse.

        标签信息

        :param used: The used of this CreateSubscriptionResponse.
        :type used: list[:class:`huaweicloudsdkeg.v1.SubscriptionUsedInfo`]
        """
        self._used = used

    @property
    def sources(self):
        r"""Gets the sources of this CreateSubscriptionResponse.

        订阅源列表

        :return: The sources of this CreateSubscriptionResponse.
        :rtype: list[:class:`huaweicloudsdkeg.v1.SubscriptionSourceInfo`]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        r"""Sets the sources of this CreateSubscriptionResponse.

        订阅源列表

        :param sources: The sources of this CreateSubscriptionResponse.
        :type sources: list[:class:`huaweicloudsdkeg.v1.SubscriptionSourceInfo`]
        """
        self._sources = sources

    @property
    def targets(self):
        r"""Gets the targets of this CreateSubscriptionResponse.

        订阅目标列表

        :return: The targets of this CreateSubscriptionResponse.
        :rtype: list[:class:`huaweicloudsdkeg.v1.SubscriptionTargetInfo`]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        r"""Sets the targets of this CreateSubscriptionResponse.

        订阅目标列表

        :param targets: The targets of this CreateSubscriptionResponse.
        :type targets: list[:class:`huaweicloudsdkeg.v1.SubscriptionTargetInfo`]
        """
        self._targets = targets

    @property
    def created_time(self):
        r"""Gets the created_time of this CreateSubscriptionResponse.

        创建时间

        :return: The created_time of this CreateSubscriptionResponse.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this CreateSubscriptionResponse.

        创建时间

        :param created_time: The created_time of this CreateSubscriptionResponse.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def updated_time(self):
        r"""Gets the updated_time of this CreateSubscriptionResponse.

        更新时间

        :return: The updated_time of this CreateSubscriptionResponse.
        :rtype: str
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        r"""Sets the updated_time of this CreateSubscriptionResponse.

        更新时间

        :param updated_time: The updated_time of this CreateSubscriptionResponse.
        :type updated_time: str
        """
        self._updated_time = updated_time

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this CreateSubscriptionResponse.

        :return: The x_request_id of this CreateSubscriptionResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this CreateSubscriptionResponse.

        :param x_request_id: The x_request_id of this CreateSubscriptionResponse.
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
        if not isinstance(other, CreateSubscriptionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
