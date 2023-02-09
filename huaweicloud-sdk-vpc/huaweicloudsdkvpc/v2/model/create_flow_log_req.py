# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateFlowLogReq:

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
        'resource_type': 'str',
        'resource_id': 'str',
        'traffic_type': 'str',
        'log_group_id': 'str',
        'log_topic_id': 'str',
        'index_enabled': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'resource_type': 'resource_type',
        'resource_id': 'resource_id',
        'traffic_type': 'traffic_type',
        'log_group_id': 'log_group_id',
        'log_topic_id': 'log_topic_id',
        'index_enabled': 'index_enabled'
    }

    def __init__(self, name=None, description=None, resource_type=None, resource_id=None, traffic_type=None, log_group_id=None, log_topic_id=None, index_enabled=None):
        """CreateFlowLogReq

        The model defined in huaweicloud sdk

        :param name: 功能说明：流日志名称 取值范围：0-64个字符，支持数字、字母、中文、_（下划线）、-（中划线）、.（点）
        :type name: str
        :param description: 功能说明：流日志描述 取值范围：0-255个字符，不能包含“&lt;”和“&gt;”
        :type description: str
        :param resource_type: 功能说明：流日志所属资源类型 取值范围：支持port、network、vpc 类型。
        :type resource_type: str
        :param resource_id: resource_type对应资源的唯一ID
        :type resource_id: str
        :param traffic_type: 功能说明：流日志采集类型 取值范围：     1）all：采集指定资源的全部流量。     2）accept：采集指定资源允许传入、传出的流量。     3）reject：采集指定资源拒绝传入、传出的流量。
        :type traffic_type: str
        :param log_group_id: 日志组ID 请在云日志服务中获取，详情请参见《云日志服务用户指南》。
        :type log_group_id: str
        :param log_topic_id: 日志主题ID 请在云日志服务中获取，详情请参见《云日志服务用户指南》。
        :type log_topic_id: str
        :param index_enabled: 功能说明：是否开启日志索引 取值范围：true，false
        :type index_enabled: bool
        """
        
        

        self._name = None
        self._description = None
        self._resource_type = None
        self._resource_id = None
        self._traffic_type = None
        self._log_group_id = None
        self._log_topic_id = None
        self._index_enabled = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.traffic_type = traffic_type
        self.log_group_id = log_group_id
        self.log_topic_id = log_topic_id
        if index_enabled is not None:
            self.index_enabled = index_enabled

    @property
    def name(self):
        """Gets the name of this CreateFlowLogReq.

        功能说明：流日志名称 取值范围：0-64个字符，支持数字、字母、中文、_（下划线）、-（中划线）、.（点）

        :return: The name of this CreateFlowLogReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateFlowLogReq.

        功能说明：流日志名称 取值范围：0-64个字符，支持数字、字母、中文、_（下划线）、-（中划线）、.（点）

        :param name: The name of this CreateFlowLogReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateFlowLogReq.

        功能说明：流日志描述 取值范围：0-255个字符，不能包含“<”和“>”

        :return: The description of this CreateFlowLogReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateFlowLogReq.

        功能说明：流日志描述 取值范围：0-255个字符，不能包含“<”和“>”

        :param description: The description of this CreateFlowLogReq.
        :type description: str
        """
        self._description = description

    @property
    def resource_type(self):
        """Gets the resource_type of this CreateFlowLogReq.

        功能说明：流日志所属资源类型 取值范围：支持port、network、vpc 类型。

        :return: The resource_type of this CreateFlowLogReq.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this CreateFlowLogReq.

        功能说明：流日志所属资源类型 取值范围：支持port、network、vpc 类型。

        :param resource_type: The resource_type of this CreateFlowLogReq.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_id(self):
        """Gets the resource_id of this CreateFlowLogReq.

        resource_type对应资源的唯一ID

        :return: The resource_id of this CreateFlowLogReq.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this CreateFlowLogReq.

        resource_type对应资源的唯一ID

        :param resource_id: The resource_id of this CreateFlowLogReq.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def traffic_type(self):
        """Gets the traffic_type of this CreateFlowLogReq.

        功能说明：流日志采集类型 取值范围：     1）all：采集指定资源的全部流量。     2）accept：采集指定资源允许传入、传出的流量。     3）reject：采集指定资源拒绝传入、传出的流量。

        :return: The traffic_type of this CreateFlowLogReq.
        :rtype: str
        """
        return self._traffic_type

    @traffic_type.setter
    def traffic_type(self, traffic_type):
        """Sets the traffic_type of this CreateFlowLogReq.

        功能说明：流日志采集类型 取值范围：     1）all：采集指定资源的全部流量。     2）accept：采集指定资源允许传入、传出的流量。     3）reject：采集指定资源拒绝传入、传出的流量。

        :param traffic_type: The traffic_type of this CreateFlowLogReq.
        :type traffic_type: str
        """
        self._traffic_type = traffic_type

    @property
    def log_group_id(self):
        """Gets the log_group_id of this CreateFlowLogReq.

        日志组ID 请在云日志服务中获取，详情请参见《云日志服务用户指南》。

        :return: The log_group_id of this CreateFlowLogReq.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        """Sets the log_group_id of this CreateFlowLogReq.

        日志组ID 请在云日志服务中获取，详情请参见《云日志服务用户指南》。

        :param log_group_id: The log_group_id of this CreateFlowLogReq.
        :type log_group_id: str
        """
        self._log_group_id = log_group_id

    @property
    def log_topic_id(self):
        """Gets the log_topic_id of this CreateFlowLogReq.

        日志主题ID 请在云日志服务中获取，详情请参见《云日志服务用户指南》。

        :return: The log_topic_id of this CreateFlowLogReq.
        :rtype: str
        """
        return self._log_topic_id

    @log_topic_id.setter
    def log_topic_id(self, log_topic_id):
        """Sets the log_topic_id of this CreateFlowLogReq.

        日志主题ID 请在云日志服务中获取，详情请参见《云日志服务用户指南》。

        :param log_topic_id: The log_topic_id of this CreateFlowLogReq.
        :type log_topic_id: str
        """
        self._log_topic_id = log_topic_id

    @property
    def index_enabled(self):
        """Gets the index_enabled of this CreateFlowLogReq.

        功能说明：是否开启日志索引 取值范围：true，false

        :return: The index_enabled of this CreateFlowLogReq.
        :rtype: bool
        """
        return self._index_enabled

    @index_enabled.setter
    def index_enabled(self, index_enabled):
        """Sets the index_enabled of this CreateFlowLogReq.

        功能说明：是否开启日志索引 取值范围：true，false

        :param index_enabled: The index_enabled of this CreateFlowLogReq.
        :type index_enabled: bool
        """
        self._index_enabled = index_enabled

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
        if not isinstance(other, CreateFlowLogReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
