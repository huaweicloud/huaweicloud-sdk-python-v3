# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFlowLogsRequest:

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
        'tenant_id': 'str',
        'description': 'str',
        'resource_type': 'str',
        'resource_id': 'str',
        'traffic_type': 'str',
        'log_group_id': 'str',
        'log_topic_id': 'str',
        'log_store_type': 'str',
        'status': 'str',
        'limit': 'str',
        'marker': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'tenant_id': 'tenant_id',
        'description': 'description',
        'resource_type': 'resource_type',
        'resource_id': 'resource_id',
        'traffic_type': 'traffic_type',
        'log_group_id': 'log_group_id',
        'log_topic_id': 'log_topic_id',
        'log_store_type': 'log_store_type',
        'status': 'status',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, id=None, name=None, tenant_id=None, description=None, resource_type=None, resource_id=None, traffic_type=None, log_group_id=None, log_topic_id=None, log_store_type=None, status=None, limit=None, marker=None):
        """ListFlowLogsRequest

        The model defined in huaweicloud sdk

        :param id: 流日志资源唯一标识
        :type id: str
        :param name: 功能说明：流日志名称 取值范围：0-64个字符，支持数字、字母、中文、_（下划线）、-（中划线）、.（点）
        :type name: str
        :param tenant_id: 项目ID
        :type tenant_id: str
        :param description: 功能说明：流日志描述 取值范围：0-255个字符，不能包含“&lt;”和“&gt;”
        :type description: str
        :param resource_type: 功能说明：流日志所属资源类型 取值范围：支持port、network、vpc 3种类型。
        :type resource_type: str
        :param resource_id: resource_type对应资源的唯一ID
        :type resource_id: str
        :param traffic_type: 功能说明：流日志采集类型 取值范围：     1）all：采集指定资源的全部流量。     2）accept：采集指定资源允许传入、传出的流量。     3）reject：采集指定资源拒绝传入、传出的流量。
        :type traffic_type: str
        :param log_group_id: 日志组ID 请在云日志服务中获取，详情请参见《云日志服务用户指南》。
        :type log_group_id: str
        :param log_topic_id: 日志主题ID 请在云日志服务中获取，详情请参见《云日志服务用户指南》。
        :type log_topic_id: str
        :param log_store_type: 功能说明：流日志存储类型 取值范围：     lts：存储类型为云日志服务（LTS）。
        :type log_store_type: str
        :param status: 功能说明：流日志状态 取值范围：     ACTIVE：开启     DOWN：关闭     ERROR：异常故障
        :type status: str
        :param limit: 功能说明：每页返回的个数 取值范围：0 ~ intmax
        :type limit: str
        :param marker: 分页查询起始的资源ID，为空时为查询第一页
        :type marker: str
        """
        
        

        self._id = None
        self._name = None
        self._tenant_id = None
        self._description = None
        self._resource_type = None
        self._resource_id = None
        self._traffic_type = None
        self._log_group_id = None
        self._log_topic_id = None
        self._log_store_type = None
        self._status = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if description is not None:
            self.description = description
        if resource_type is not None:
            self.resource_type = resource_type
        if resource_id is not None:
            self.resource_id = resource_id
        if traffic_type is not None:
            self.traffic_type = traffic_type
        if log_group_id is not None:
            self.log_group_id = log_group_id
        if log_topic_id is not None:
            self.log_topic_id = log_topic_id
        if log_store_type is not None:
            self.log_store_type = log_store_type
        if status is not None:
            self.status = status
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def id(self):
        """Gets the id of this ListFlowLogsRequest.

        流日志资源唯一标识

        :return: The id of this ListFlowLogsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListFlowLogsRequest.

        流日志资源唯一标识

        :param id: The id of this ListFlowLogsRequest.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListFlowLogsRequest.

        功能说明：流日志名称 取值范围：0-64个字符，支持数字、字母、中文、_（下划线）、-（中划线）、.（点）

        :return: The name of this ListFlowLogsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListFlowLogsRequest.

        功能说明：流日志名称 取值范围：0-64个字符，支持数字、字母、中文、_（下划线）、-（中划线）、.（点）

        :param name: The name of this ListFlowLogsRequest.
        :type name: str
        """
        self._name = name

    @property
    def tenant_id(self):
        """Gets the tenant_id of this ListFlowLogsRequest.

        项目ID

        :return: The tenant_id of this ListFlowLogsRequest.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this ListFlowLogsRequest.

        项目ID

        :param tenant_id: The tenant_id of this ListFlowLogsRequest.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def description(self):
        """Gets the description of this ListFlowLogsRequest.

        功能说明：流日志描述 取值范围：0-255个字符，不能包含“<”和“>”

        :return: The description of this ListFlowLogsRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListFlowLogsRequest.

        功能说明：流日志描述 取值范围：0-255个字符，不能包含“<”和“>”

        :param description: The description of this ListFlowLogsRequest.
        :type description: str
        """
        self._description = description

    @property
    def resource_type(self):
        """Gets the resource_type of this ListFlowLogsRequest.

        功能说明：流日志所属资源类型 取值范围：支持port、network、vpc 3种类型。

        :return: The resource_type of this ListFlowLogsRequest.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this ListFlowLogsRequest.

        功能说明：流日志所属资源类型 取值范围：支持port、network、vpc 3种类型。

        :param resource_type: The resource_type of this ListFlowLogsRequest.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_id(self):
        """Gets the resource_id of this ListFlowLogsRequest.

        resource_type对应资源的唯一ID

        :return: The resource_id of this ListFlowLogsRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this ListFlowLogsRequest.

        resource_type对应资源的唯一ID

        :param resource_id: The resource_id of this ListFlowLogsRequest.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def traffic_type(self):
        """Gets the traffic_type of this ListFlowLogsRequest.

        功能说明：流日志采集类型 取值范围：     1）all：采集指定资源的全部流量。     2）accept：采集指定资源允许传入、传出的流量。     3）reject：采集指定资源拒绝传入、传出的流量。

        :return: The traffic_type of this ListFlowLogsRequest.
        :rtype: str
        """
        return self._traffic_type

    @traffic_type.setter
    def traffic_type(self, traffic_type):
        """Sets the traffic_type of this ListFlowLogsRequest.

        功能说明：流日志采集类型 取值范围：     1）all：采集指定资源的全部流量。     2）accept：采集指定资源允许传入、传出的流量。     3）reject：采集指定资源拒绝传入、传出的流量。

        :param traffic_type: The traffic_type of this ListFlowLogsRequest.
        :type traffic_type: str
        """
        self._traffic_type = traffic_type

    @property
    def log_group_id(self):
        """Gets the log_group_id of this ListFlowLogsRequest.

        日志组ID 请在云日志服务中获取，详情请参见《云日志服务用户指南》。

        :return: The log_group_id of this ListFlowLogsRequest.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        """Sets the log_group_id of this ListFlowLogsRequest.

        日志组ID 请在云日志服务中获取，详情请参见《云日志服务用户指南》。

        :param log_group_id: The log_group_id of this ListFlowLogsRequest.
        :type log_group_id: str
        """
        self._log_group_id = log_group_id

    @property
    def log_topic_id(self):
        """Gets the log_topic_id of this ListFlowLogsRequest.

        日志主题ID 请在云日志服务中获取，详情请参见《云日志服务用户指南》。

        :return: The log_topic_id of this ListFlowLogsRequest.
        :rtype: str
        """
        return self._log_topic_id

    @log_topic_id.setter
    def log_topic_id(self, log_topic_id):
        """Sets the log_topic_id of this ListFlowLogsRequest.

        日志主题ID 请在云日志服务中获取，详情请参见《云日志服务用户指南》。

        :param log_topic_id: The log_topic_id of this ListFlowLogsRequest.
        :type log_topic_id: str
        """
        self._log_topic_id = log_topic_id

    @property
    def log_store_type(self):
        """Gets the log_store_type of this ListFlowLogsRequest.

        功能说明：流日志存储类型 取值范围：     lts：存储类型为云日志服务（LTS）。

        :return: The log_store_type of this ListFlowLogsRequest.
        :rtype: str
        """
        return self._log_store_type

    @log_store_type.setter
    def log_store_type(self, log_store_type):
        """Sets the log_store_type of this ListFlowLogsRequest.

        功能说明：流日志存储类型 取值范围：     lts：存储类型为云日志服务（LTS）。

        :param log_store_type: The log_store_type of this ListFlowLogsRequest.
        :type log_store_type: str
        """
        self._log_store_type = log_store_type

    @property
    def status(self):
        """Gets the status of this ListFlowLogsRequest.

        功能说明：流日志状态 取值范围：     ACTIVE：开启     DOWN：关闭     ERROR：异常故障

        :return: The status of this ListFlowLogsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListFlowLogsRequest.

        功能说明：流日志状态 取值范围：     ACTIVE：开启     DOWN：关闭     ERROR：异常故障

        :param status: The status of this ListFlowLogsRequest.
        :type status: str
        """
        self._status = status

    @property
    def limit(self):
        """Gets the limit of this ListFlowLogsRequest.

        功能说明：每页返回的个数 取值范围：0 ~ intmax

        :return: The limit of this ListFlowLogsRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListFlowLogsRequest.

        功能说明：每页返回的个数 取值范围：0 ~ intmax

        :param limit: The limit of this ListFlowLogsRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListFlowLogsRequest.

        分页查询起始的资源ID，为空时为查询第一页

        :return: The marker of this ListFlowLogsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListFlowLogsRequest.

        分页查询起始的资源ID，为空时为查询第一页

        :param marker: The marker of this ListFlowLogsRequest.
        :type marker: str
        """
        self._marker = marker

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
        if not isinstance(other, ListFlowLogsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
