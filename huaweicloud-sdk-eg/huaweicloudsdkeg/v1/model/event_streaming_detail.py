# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventStreamingDetail:

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
        'updated_time': 'str'
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
        'updated_time': 'updated_time'
    }

    def __init__(self, name=None, description=None, source=None, sink=None, rule_config=None, option=None, status=None, id=None, created_time=None, updated_time=None):
        """EventStreamingDetail

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
        """
        
        

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

    @property
    def name(self):
        """Gets the name of this EventStreamingDetail.

        事件流名称，租户下唯一，由字母、数字、点、下划线和中划线组成，必须字母或数字开头

        :return: The name of this EventStreamingDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EventStreamingDetail.

        事件流名称，租户下唯一，由字母、数字、点、下划线和中划线组成，必须字母或数字开头

        :param name: The name of this EventStreamingDetail.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this EventStreamingDetail.

        事件流描述

        :return: The description of this EventStreamingDetail.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EventStreamingDetail.

        事件流描述

        :param description: The description of this EventStreamingDetail.
        :type description: str
        """
        self._description = description

    @property
    def source(self):
        """Gets the source of this EventStreamingDetail.

        :return: The source of this EventStreamingDetail.
        :rtype: :class:`huaweicloudsdkeg.v1.EventStreamingSource`
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this EventStreamingDetail.

        :param source: The source of this EventStreamingDetail.
        :type source: :class:`huaweicloudsdkeg.v1.EventStreamingSource`
        """
        self._source = source

    @property
    def sink(self):
        """Gets the sink of this EventStreamingDetail.

        :return: The sink of this EventStreamingDetail.
        :rtype: :class:`huaweicloudsdkeg.v1.EventStreamingSink`
        """
        return self._sink

    @sink.setter
    def sink(self, sink):
        """Sets the sink of this EventStreamingDetail.

        :param sink: The sink of this EventStreamingDetail.
        :type sink: :class:`huaweicloudsdkeg.v1.EventStreamingSink`
        """
        self._sink = sink

    @property
    def rule_config(self):
        """Gets the rule_config of this EventStreamingDetail.

        :return: The rule_config of this EventStreamingDetail.
        :rtype: :class:`huaweicloudsdkeg.v1.EventStreamingCreateReqRuleConfig`
        """
        return self._rule_config

    @rule_config.setter
    def rule_config(self, rule_config):
        """Sets the rule_config of this EventStreamingDetail.

        :param rule_config: The rule_config of this EventStreamingDetail.
        :type rule_config: :class:`huaweicloudsdkeg.v1.EventStreamingCreateReqRuleConfig`
        """
        self._rule_config = rule_config

    @property
    def option(self):
        """Gets the option of this EventStreamingDetail.

        :return: The option of this EventStreamingDetail.
        :rtype: :class:`huaweicloudsdkeg.v1.RunOption`
        """
        return self._option

    @option.setter
    def option(self, option):
        """Sets the option of this EventStreamingDetail.

        :param option: The option of this EventStreamingDetail.
        :type option: :class:`huaweicloudsdkeg.v1.RunOption`
        """
        self._option = option

    @property
    def status(self):
        """Gets the status of this EventStreamingDetail.

        事件流状态

        :return: The status of this EventStreamingDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this EventStreamingDetail.

        事件流状态

        :param status: The status of this EventStreamingDetail.
        :type status: str
        """
        self._status = status

    @property
    def id(self):
        """Gets the id of this EventStreamingDetail.

        事件流ID

        :return: The id of this EventStreamingDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EventStreamingDetail.

        事件流ID

        :param id: The id of this EventStreamingDetail.
        :type id: str
        """
        self._id = id

    @property
    def created_time(self):
        """Gets the created_time of this EventStreamingDetail.

        创建时间

        :return: The created_time of this EventStreamingDetail.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this EventStreamingDetail.

        创建时间

        :param created_time: The created_time of this EventStreamingDetail.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def updated_time(self):
        """Gets the updated_time of this EventStreamingDetail.

        更新时间

        :return: The updated_time of this EventStreamingDetail.
        :rtype: str
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        """Sets the updated_time of this EventStreamingDetail.

        更新时间

        :param updated_time: The updated_time of this EventStreamingDetail.
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
        if not isinstance(other, EventStreamingDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
