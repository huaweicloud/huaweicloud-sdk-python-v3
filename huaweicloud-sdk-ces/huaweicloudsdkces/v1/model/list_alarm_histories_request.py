# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAlarmHistoriesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'alarm_id': 'str',
        'alarm_name': 'str',
        'alarm_status': 'str',
        'alarm_level': 'str',
        'namespace': 'str',
        '_from': 'str',
        'to': 'str',
        'start': 'str',
        'limit': 'str'
    }

    attribute_map = {
        'group_id': 'group_id',
        'alarm_id': 'alarm_id',
        'alarm_name': 'alarm_name',
        'alarm_status': 'alarm_status',
        'alarm_level': 'alarm_level',
        'namespace': 'namespace',
        '_from': 'from',
        'to': 'to',
        'start': 'start',
        'limit': 'limit'
    }

    def __init__(self, group_id=None, alarm_id=None, alarm_name=None, alarm_status=None, alarm_level=None, namespace=None, _from=None, to=None, start=None, limit=None):
        """ListAlarmHistoriesRequest

        The model defined in huaweicloud sdk

        :param group_id: 服务提供的资源分组功能，创建的资源分组ID，如：rg1603107497873DK4O2pXbn。
        :type group_id: str
        :param alarm_id: 告警规则ID。如：al1603088932912v98rGl1al。
        :type alarm_id: str
        :param alarm_name: 告警规则名称，如alarm-test01。
        :type alarm_name: str
        :param alarm_status: 告警历史的状态，取值为ok，alarm，insufficient_data； ok为正常，alarm为告警，insufficient_data为数据不足。
        :type alarm_status: str
        :param alarm_level: 告警历史的告警级别，值为1,2,3,4；1为紧急，2为重要，3为次要，4为提示。
        :type alarm_level: str
        :param namespace: 告警资源对应的命名空间，如ECS服务的资源命名空间为：SYS.ECS；各服务命名空间可查看：“[服务命名空间](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。
        :type namespace: str
        :param _from: 查询告警历史的起始时间，UNIX时间戳，单位毫秒，如：1602501480905；from，to如果不进行赋值，则默认to是当前时间，from是当前时间减7天的时间戳。
        :type _from: str
        :param to: 查询告警历史的截止时间，UNIX时间戳，单位毫秒。from必须小于等于to，如：1603106280905；from，to如果不进行赋值，则默认to是当前时间，from是当前时间减7天的时间戳。
        :type to: str
        :param start: 分页起始值，类型为integer，默认值为0。
        :type start: str
        :param limit: 单次查询的条数限制，取值范围(0,100]，默认值为100， 用于限制结果数据条数。
        :type limit: str
        """
        
        

        self._group_id = None
        self._alarm_id = None
        self._alarm_name = None
        self._alarm_status = None
        self._alarm_level = None
        self._namespace = None
        self.__from = None
        self._to = None
        self._start = None
        self._limit = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if alarm_id is not None:
            self.alarm_id = alarm_id
        if alarm_name is not None:
            self.alarm_name = alarm_name
        if alarm_status is not None:
            self.alarm_status = alarm_status
        if alarm_level is not None:
            self.alarm_level = alarm_level
        if namespace is not None:
            self.namespace = namespace
        if _from is not None:
            self._from = _from
        if to is not None:
            self.to = to
        if start is not None:
            self.start = start
        if limit is not None:
            self.limit = limit

    @property
    def group_id(self):
        """Gets the group_id of this ListAlarmHistoriesRequest.

        服务提供的资源分组功能，创建的资源分组ID，如：rg1603107497873DK4O2pXbn。

        :return: The group_id of this ListAlarmHistoriesRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ListAlarmHistoriesRequest.

        服务提供的资源分组功能，创建的资源分组ID，如：rg1603107497873DK4O2pXbn。

        :param group_id: The group_id of this ListAlarmHistoriesRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def alarm_id(self):
        """Gets the alarm_id of this ListAlarmHistoriesRequest.

        告警规则ID。如：al1603088932912v98rGl1al。

        :return: The alarm_id of this ListAlarmHistoriesRequest.
        :rtype: str
        """
        return self._alarm_id

    @alarm_id.setter
    def alarm_id(self, alarm_id):
        """Sets the alarm_id of this ListAlarmHistoriesRequest.

        告警规则ID。如：al1603088932912v98rGl1al。

        :param alarm_id: The alarm_id of this ListAlarmHistoriesRequest.
        :type alarm_id: str
        """
        self._alarm_id = alarm_id

    @property
    def alarm_name(self):
        """Gets the alarm_name of this ListAlarmHistoriesRequest.

        告警规则名称，如alarm-test01。

        :return: The alarm_name of this ListAlarmHistoriesRequest.
        :rtype: str
        """
        return self._alarm_name

    @alarm_name.setter
    def alarm_name(self, alarm_name):
        """Sets the alarm_name of this ListAlarmHistoriesRequest.

        告警规则名称，如alarm-test01。

        :param alarm_name: The alarm_name of this ListAlarmHistoriesRequest.
        :type alarm_name: str
        """
        self._alarm_name = alarm_name

    @property
    def alarm_status(self):
        """Gets the alarm_status of this ListAlarmHistoriesRequest.

        告警历史的状态，取值为ok，alarm，insufficient_data； ok为正常，alarm为告警，insufficient_data为数据不足。

        :return: The alarm_status of this ListAlarmHistoriesRequest.
        :rtype: str
        """
        return self._alarm_status

    @alarm_status.setter
    def alarm_status(self, alarm_status):
        """Sets the alarm_status of this ListAlarmHistoriesRequest.

        告警历史的状态，取值为ok，alarm，insufficient_data； ok为正常，alarm为告警，insufficient_data为数据不足。

        :param alarm_status: The alarm_status of this ListAlarmHistoriesRequest.
        :type alarm_status: str
        """
        self._alarm_status = alarm_status

    @property
    def alarm_level(self):
        """Gets the alarm_level of this ListAlarmHistoriesRequest.

        告警历史的告警级别，值为1,2,3,4；1为紧急，2为重要，3为次要，4为提示。

        :return: The alarm_level of this ListAlarmHistoriesRequest.
        :rtype: str
        """
        return self._alarm_level

    @alarm_level.setter
    def alarm_level(self, alarm_level):
        """Sets the alarm_level of this ListAlarmHistoriesRequest.

        告警历史的告警级别，值为1,2,3,4；1为紧急，2为重要，3为次要，4为提示。

        :param alarm_level: The alarm_level of this ListAlarmHistoriesRequest.
        :type alarm_level: str
        """
        self._alarm_level = alarm_level

    @property
    def namespace(self):
        """Gets the namespace of this ListAlarmHistoriesRequest.

        告警资源对应的命名空间，如ECS服务的资源命名空间为：SYS.ECS；各服务命名空间可查看：“[服务命名空间](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :return: The namespace of this ListAlarmHistoriesRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this ListAlarmHistoriesRequest.

        告警资源对应的命名空间，如ECS服务的资源命名空间为：SYS.ECS；各服务命名空间可查看：“[服务命名空间](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :param namespace: The namespace of this ListAlarmHistoriesRequest.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def _from(self):
        """Gets the _from of this ListAlarmHistoriesRequest.

        查询告警历史的起始时间，UNIX时间戳，单位毫秒，如：1602501480905；from，to如果不进行赋值，则默认to是当前时间，from是当前时间减7天的时间戳。

        :return: The _from of this ListAlarmHistoriesRequest.
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this ListAlarmHistoriesRequest.

        查询告警历史的起始时间，UNIX时间戳，单位毫秒，如：1602501480905；from，to如果不进行赋值，则默认to是当前时间，from是当前时间减7天的时间戳。

        :param _from: The _from of this ListAlarmHistoriesRequest.
        :type _from: str
        """
        self.__from = _from

    @property
    def to(self):
        """Gets the to of this ListAlarmHistoriesRequest.

        查询告警历史的截止时间，UNIX时间戳，单位毫秒。from必须小于等于to，如：1603106280905；from，to如果不进行赋值，则默认to是当前时间，from是当前时间减7天的时间戳。

        :return: The to of this ListAlarmHistoriesRequest.
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this ListAlarmHistoriesRequest.

        查询告警历史的截止时间，UNIX时间戳，单位毫秒。from必须小于等于to，如：1603106280905；from，to如果不进行赋值，则默认to是当前时间，from是当前时间减7天的时间戳。

        :param to: The to of this ListAlarmHistoriesRequest.
        :type to: str
        """
        self._to = to

    @property
    def start(self):
        """Gets the start of this ListAlarmHistoriesRequest.

        分页起始值，类型为integer，默认值为0。

        :return: The start of this ListAlarmHistoriesRequest.
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this ListAlarmHistoriesRequest.

        分页起始值，类型为integer，默认值为0。

        :param start: The start of this ListAlarmHistoriesRequest.
        :type start: str
        """
        self._start = start

    @property
    def limit(self):
        """Gets the limit of this ListAlarmHistoriesRequest.

        单次查询的条数限制，取值范围(0,100]，默认值为100， 用于限制结果数据条数。

        :return: The limit of this ListAlarmHistoriesRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAlarmHistoriesRequest.

        单次查询的条数限制，取值范围(0,100]，默认值为100， 用于限制结果数据条数。

        :param limit: The limit of this ListAlarmHistoriesRequest.
        :type limit: str
        """
        self._limit = limit

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
        if not isinstance(other, ListAlarmHistoriesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
