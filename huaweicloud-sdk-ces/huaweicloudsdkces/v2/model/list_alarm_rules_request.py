# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAlarmRulesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarm_id': 'str',
        'name': 'str',
        'namespace': 'str',
        'resource_id': 'str',
        'enterprise_project_id': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'alarm_id': 'alarm_id',
        'name': 'name',
        'namespace': 'namespace',
        'resource_id': 'resource_id',
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, alarm_id=None, name=None, namespace=None, resource_id=None, enterprise_project_id=None, offset=None, limit=None):
        """ListAlarmRulesRequest

        The model defined in huaweicloud sdk

        :param alarm_id: 告警规则ID
        :type alarm_id: str
        :param name: 告警名称, 只能包含0-9/a-z/A-Z/_/-或汉字，长度1-128
        :type name: str
        :param namespace: 查询服务的命名空间，各服务命名空间请参考[服务命名空间](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)
        :type namespace: str
        :param resource_id: 告警资源ID，多维度情况按字母升序排列并使用逗号分隔
        :type resource_id: str
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        :param offset: 分页偏移量
        :type offset: int
        :param limit: 分页大小
        :type limit: int
        """
        
        

        self._alarm_id = None
        self._name = None
        self._namespace = None
        self._resource_id = None
        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if alarm_id is not None:
            self.alarm_id = alarm_id
        if name is not None:
            self.name = name
        if namespace is not None:
            self.namespace = namespace
        if resource_id is not None:
            self.resource_id = resource_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def alarm_id(self):
        """Gets the alarm_id of this ListAlarmRulesRequest.

        告警规则ID

        :return: The alarm_id of this ListAlarmRulesRequest.
        :rtype: str
        """
        return self._alarm_id

    @alarm_id.setter
    def alarm_id(self, alarm_id):
        """Sets the alarm_id of this ListAlarmRulesRequest.

        告警规则ID

        :param alarm_id: The alarm_id of this ListAlarmRulesRequest.
        :type alarm_id: str
        """
        self._alarm_id = alarm_id

    @property
    def name(self):
        """Gets the name of this ListAlarmRulesRequest.

        告警名称, 只能包含0-9/a-z/A-Z/_/-或汉字，长度1-128

        :return: The name of this ListAlarmRulesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListAlarmRulesRequest.

        告警名称, 只能包含0-9/a-z/A-Z/_/-或汉字，长度1-128

        :param name: The name of this ListAlarmRulesRequest.
        :type name: str
        """
        self._name = name

    @property
    def namespace(self):
        """Gets the namespace of this ListAlarmRulesRequest.

        查询服务的命名空间，各服务命名空间请参考[服务命名空间](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)

        :return: The namespace of this ListAlarmRulesRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this ListAlarmRulesRequest.

        查询服务的命名空间，各服务命名空间请参考[服务命名空间](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)

        :param namespace: The namespace of this ListAlarmRulesRequest.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def resource_id(self):
        """Gets the resource_id of this ListAlarmRulesRequest.

        告警资源ID，多维度情况按字母升序排列并使用逗号分隔

        :return: The resource_id of this ListAlarmRulesRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this ListAlarmRulesRequest.

        告警资源ID，多维度情况按字母升序排列并使用逗号分隔

        :param resource_id: The resource_id of this ListAlarmRulesRequest.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListAlarmRulesRequest.

        企业项目ID

        :return: The enterprise_project_id of this ListAlarmRulesRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListAlarmRulesRequest.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this ListAlarmRulesRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        """Gets the offset of this ListAlarmRulesRequest.

        分页偏移量

        :return: The offset of this ListAlarmRulesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListAlarmRulesRequest.

        分页偏移量

        :param offset: The offset of this ListAlarmRulesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListAlarmRulesRequest.

        分页大小

        :return: The limit of this ListAlarmRulesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAlarmRulesRequest.

        分页大小

        :param limit: The limit of this ListAlarmRulesRequest.
        :type limit: int
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
        if not isinstance(other, ListAlarmRulesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
