# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowEventStreamingResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'source': 'EventStreamingSource',
        'sink': 'EventStreamingSink',
        'rule_config': 'EventStreamingCreateReqRuleConfig',
        'option': 'RunOption',
        'status': 'str',
        'id': 'str',
        'created_time': 'str',
        'updated_time': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'source': 'source',
        'sink': 'sink',
        'rule_config': 'rule_config',
        'option': 'option',
        'status': 'status',
        'id': 'id',
        'created_time': 'created_time',
        'updated_time': 'updated_time',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, name=None, description=None, source=None, sink=None, rule_config=None, option=None, status=None, id=None, created_time=None, updated_time=None, x_request_id=None):
        """ShowEventStreamingResponse

        The model defined in huaweicloud sdk

        :param name: 事件流名称，租户下唯一，由字母、数字、点、下划线和中划线组成，必须字母或数字开头
        :type name: str
        :param description: 事件流描述
        :type description: str
        :param source: 
        :type source: :class:`huaweicloudsdkeg.v1.EventStreamingSource`
        :param sink: 
        :type sink: :class:`huaweicloudsdkeg.v1.EventStreamingSink`
        :param rule_config: 
        :type rule_config: :class:`huaweicloudsdkeg.v1.EventStreamingCreateReqRuleConfig`
        :param option: 
        :type option: :class:`huaweicloudsdkeg.v1.RunOption`
        :param status: 事件流状态
        :type status: str
        :param id: 事件流ID
        :type id: str
        :param created_time: 创建时间
        :type created_time: str
        :param updated_time: 更新时间
        :type updated_time: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ShowEventStreamingResponse, self).__init__()

        self._name = None
        self._description = None
        self._source = None
        self._sink = None
        self._rule_config = None
        self._option = None
        self._status = None
        self._id = None
        self._created_time = None
        self._updated_time = None
        self._x_request_id = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.source = source
        self.sink = sink
        if rule_config is not None:
            self.rule_config = rule_config
        if option is not None:
            self.option = option
        if status is not None:
            self.status = status
        if id is not None:
            self.id = id
        if created_time is not None:
            self.created_time = created_time
        if updated_time is not None:
            self.updated_time = updated_time
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def name(self):
        """Gets the name of this ShowEventStreamingResponse.

        事件流名称，租户下唯一，由字母、数字、点、下划线和中划线组成，必须字母或数字开头

        :return: The name of this ShowEventStreamingResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowEventStreamingResponse.

        事件流名称，租户下唯一，由字母、数字、点、下划线和中划线组成，必须字母或数字开头

        :param name: The name of this ShowEventStreamingResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ShowEventStreamingResponse.

        事件流描述

        :return: The description of this ShowEventStreamingResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowEventStreamingResponse.

        事件流描述

        :param description: The description of this ShowEventStreamingResponse.
        :type description: str
        """
        self._description = description

    @property
    def source(self):
        """Gets the source of this ShowEventStreamingResponse.

        :return: The source of this ShowEventStreamingResponse.
        :rtype: :class:`huaweicloudsdkeg.v1.EventStreamingSource`
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this ShowEventStreamingResponse.

        :param source: The source of this ShowEventStreamingResponse.
        :type source: :class:`huaweicloudsdkeg.v1.EventStreamingSource`
        """
        self._source = source

    @property
    def sink(self):
        """Gets the sink of this ShowEventStreamingResponse.

        :return: The sink of this ShowEventStreamingResponse.
        :rtype: :class:`huaweicloudsdkeg.v1.EventStreamingSink`
        """
        return self._sink

    @sink.setter
    def sink(self, sink):
        """Sets the sink of this ShowEventStreamingResponse.

        :param sink: The sink of this ShowEventStreamingResponse.
        :type sink: :class:`huaweicloudsdkeg.v1.EventStreamingSink`
        """
        self._sink = sink

    @property
    def rule_config(self):
        """Gets the rule_config of this ShowEventStreamingResponse.

        :return: The rule_config of this ShowEventStreamingResponse.
        :rtype: :class:`huaweicloudsdkeg.v1.EventStreamingCreateReqRuleConfig`
        """
        return self._rule_config

    @rule_config.setter
    def rule_config(self, rule_config):
        """Sets the rule_config of this ShowEventStreamingResponse.

        :param rule_config: The rule_config of this ShowEventStreamingResponse.
        :type rule_config: :class:`huaweicloudsdkeg.v1.EventStreamingCreateReqRuleConfig`
        """
        self._rule_config = rule_config

    @property
    def option(self):
        """Gets the option of this ShowEventStreamingResponse.

        :return: The option of this ShowEventStreamingResponse.
        :rtype: :class:`huaweicloudsdkeg.v1.RunOption`
        """
        return self._option

    @option.setter
    def option(self, option):
        """Sets the option of this ShowEventStreamingResponse.

        :param option: The option of this ShowEventStreamingResponse.
        :type option: :class:`huaweicloudsdkeg.v1.RunOption`
        """
        self._option = option

    @property
    def status(self):
        """Gets the status of this ShowEventStreamingResponse.

        事件流状态

        :return: The status of this ShowEventStreamingResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowEventStreamingResponse.

        事件流状态

        :param status: The status of this ShowEventStreamingResponse.
        :type status: str
        """
        self._status = status

    @property
    def id(self):
        """Gets the id of this ShowEventStreamingResponse.

        事件流ID

        :return: The id of this ShowEventStreamingResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowEventStreamingResponse.

        事件流ID

        :param id: The id of this ShowEventStreamingResponse.
        :type id: str
        """
        self._id = id

    @property
    def created_time(self):
        """Gets the created_time of this ShowEventStreamingResponse.

        创建时间

        :return: The created_time of this ShowEventStreamingResponse.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this ShowEventStreamingResponse.

        创建时间

        :param created_time: The created_time of this ShowEventStreamingResponse.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def updated_time(self):
        """Gets the updated_time of this ShowEventStreamingResponse.

        更新时间

        :return: The updated_time of this ShowEventStreamingResponse.
        :rtype: str
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        """Sets the updated_time of this ShowEventStreamingResponse.

        更新时间

        :param updated_time: The updated_time of this ShowEventStreamingResponse.
        :type updated_time: str
        """
        self._updated_time = updated_time

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ShowEventStreamingResponse.

        :return: The x_request_id of this ShowEventStreamingResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ShowEventStreamingResponse.

        :param x_request_id: The x_request_id of this ShowEventStreamingResponse.
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
        if not isinstance(other, ShowEventStreamingResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
