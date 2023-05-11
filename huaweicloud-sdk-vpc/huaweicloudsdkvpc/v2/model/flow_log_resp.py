# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlowLogResp:

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
        'created_at': 'str',
        'updated_at': 'str',
        'admin_state': 'bool',
        'status': 'str'
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
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'admin_state': 'admin_state',
        'status': 'status'
    }

    def __init__(self, id=None, name=None, tenant_id=None, description=None, resource_type=None, resource_id=None, traffic_type=None, log_group_id=None, log_topic_id=None, log_store_type=None, created_at=None, updated_at=None, admin_state=None, status=None):
        """FlowLogResp

        The model defined in huaweicloud sdk

        :param id: 流日志资源唯一标识
        :type id: str
        :param name: 功能说明：流日志名称 取值范围：0-64个字符，支持数字、字母、中文、_（下划线）、-（中划线）、.（点）
        :type name: str
        :param tenant_id: 项目ID
        :type tenant_id: str
        :param description: 功能说明：流日志描述 取值范围：0-255个字符，不能包含“&lt;”和“&gt;”
        :type description: str
        :param resource_type: 功能说明：流日志所属资源类型 取值范围：支持Port、Network、VPC 类型。 约束：当resource_type为Port时，Port资源必须是C3、S3、M3三种虚拟机的网卡。
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
        :param created_at: 资源创建时间
        :type created_at: str
        :param updated_at: 最近一次更新资源的时间
        :type updated_at: str
        :param admin_state: 功能说明：流日志管理 取值范围：若为true，表明开启流日志。若为false，则关闭流日志
        :type admin_state: bool
        :param status: 功能说明：流日志状态 取值范围：ACTIVE、DOWN、ERROR
        :type status: str
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
        self._created_at = None
        self._updated_at = None
        self._admin_state = None
        self._status = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.tenant_id = tenant_id
        self.description = description
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.traffic_type = traffic_type
        self.log_group_id = log_group_id
        self.log_topic_id = log_topic_id
        self.log_store_type = log_store_type
        self.created_at = created_at
        self.updated_at = updated_at
        self.admin_state = admin_state
        self.status = status

    @property
    def id(self):
        """Gets the id of this FlowLogResp.

        流日志资源唯一标识

        :return: The id of this FlowLogResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FlowLogResp.

        流日志资源唯一标识

        :param id: The id of this FlowLogResp.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this FlowLogResp.

        功能说明：流日志名称 取值范围：0-64个字符，支持数字、字母、中文、_（下划线）、-（中划线）、.（点）

        :return: The name of this FlowLogResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FlowLogResp.

        功能说明：流日志名称 取值范围：0-64个字符，支持数字、字母、中文、_（下划线）、-（中划线）、.（点）

        :param name: The name of this FlowLogResp.
        :type name: str
        """
        self._name = name

    @property
    def tenant_id(self):
        """Gets the tenant_id of this FlowLogResp.

        项目ID

        :return: The tenant_id of this FlowLogResp.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this FlowLogResp.

        项目ID

        :param tenant_id: The tenant_id of this FlowLogResp.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def description(self):
        """Gets the description of this FlowLogResp.

        功能说明：流日志描述 取值范围：0-255个字符，不能包含“<”和“>”

        :return: The description of this FlowLogResp.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FlowLogResp.

        功能说明：流日志描述 取值范围：0-255个字符，不能包含“<”和“>”

        :param description: The description of this FlowLogResp.
        :type description: str
        """
        self._description = description

    @property
    def resource_type(self):
        """Gets the resource_type of this FlowLogResp.

        功能说明：流日志所属资源类型 取值范围：支持Port、Network、VPC 类型。 约束：当resource_type为Port时，Port资源必须是C3、S3、M3三种虚拟机的网卡。

        :return: The resource_type of this FlowLogResp.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this FlowLogResp.

        功能说明：流日志所属资源类型 取值范围：支持Port、Network、VPC 类型。 约束：当resource_type为Port时，Port资源必须是C3、S3、M3三种虚拟机的网卡。

        :param resource_type: The resource_type of this FlowLogResp.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_id(self):
        """Gets the resource_id of this FlowLogResp.

        resource_type对应资源的唯一ID

        :return: The resource_id of this FlowLogResp.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this FlowLogResp.

        resource_type对应资源的唯一ID

        :param resource_id: The resource_id of this FlowLogResp.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def traffic_type(self):
        """Gets the traffic_type of this FlowLogResp.

        功能说明：流日志采集类型 取值范围：     1）all：采集指定资源的全部流量。     2）accept：采集指定资源允许传入、传出的流量。     3）reject：采集指定资源拒绝传入、传出的流量。

        :return: The traffic_type of this FlowLogResp.
        :rtype: str
        """
        return self._traffic_type

    @traffic_type.setter
    def traffic_type(self, traffic_type):
        """Sets the traffic_type of this FlowLogResp.

        功能说明：流日志采集类型 取值范围：     1）all：采集指定资源的全部流量。     2）accept：采集指定资源允许传入、传出的流量。     3）reject：采集指定资源拒绝传入、传出的流量。

        :param traffic_type: The traffic_type of this FlowLogResp.
        :type traffic_type: str
        """
        self._traffic_type = traffic_type

    @property
    def log_group_id(self):
        """Gets the log_group_id of this FlowLogResp.

        日志组ID 请在云日志服务中获取，详情请参见《云日志服务用户指南》。

        :return: The log_group_id of this FlowLogResp.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        """Sets the log_group_id of this FlowLogResp.

        日志组ID 请在云日志服务中获取，详情请参见《云日志服务用户指南》。

        :param log_group_id: The log_group_id of this FlowLogResp.
        :type log_group_id: str
        """
        self._log_group_id = log_group_id

    @property
    def log_topic_id(self):
        """Gets the log_topic_id of this FlowLogResp.

        日志主题ID 请在云日志服务中获取，详情请参见《云日志服务用户指南》。

        :return: The log_topic_id of this FlowLogResp.
        :rtype: str
        """
        return self._log_topic_id

    @log_topic_id.setter
    def log_topic_id(self, log_topic_id):
        """Sets the log_topic_id of this FlowLogResp.

        日志主题ID 请在云日志服务中获取，详情请参见《云日志服务用户指南》。

        :param log_topic_id: The log_topic_id of this FlowLogResp.
        :type log_topic_id: str
        """
        self._log_topic_id = log_topic_id

    @property
    def log_store_type(self):
        """Gets the log_store_type of this FlowLogResp.

        功能说明：流日志存储类型 取值范围：     lts：存储类型为云日志服务（LTS）。

        :return: The log_store_type of this FlowLogResp.
        :rtype: str
        """
        return self._log_store_type

    @log_store_type.setter
    def log_store_type(self, log_store_type):
        """Sets the log_store_type of this FlowLogResp.

        功能说明：流日志存储类型 取值范围：     lts：存储类型为云日志服务（LTS）。

        :param log_store_type: The log_store_type of this FlowLogResp.
        :type log_store_type: str
        """
        self._log_store_type = log_store_type

    @property
    def created_at(self):
        """Gets the created_at of this FlowLogResp.

        资源创建时间

        :return: The created_at of this FlowLogResp.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this FlowLogResp.

        资源创建时间

        :param created_at: The created_at of this FlowLogResp.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this FlowLogResp.

        最近一次更新资源的时间

        :return: The updated_at of this FlowLogResp.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this FlowLogResp.

        最近一次更新资源的时间

        :param updated_at: The updated_at of this FlowLogResp.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def admin_state(self):
        """Gets the admin_state of this FlowLogResp.

        功能说明：流日志管理 取值范围：若为true，表明开启流日志。若为false，则关闭流日志

        :return: The admin_state of this FlowLogResp.
        :rtype: bool
        """
        return self._admin_state

    @admin_state.setter
    def admin_state(self, admin_state):
        """Sets the admin_state of this FlowLogResp.

        功能说明：流日志管理 取值范围：若为true，表明开启流日志。若为false，则关闭流日志

        :param admin_state: The admin_state of this FlowLogResp.
        :type admin_state: bool
        """
        self._admin_state = admin_state

    @property
    def status(self):
        """Gets the status of this FlowLogResp.

        功能说明：流日志状态 取值范围：ACTIVE、DOWN、ERROR

        :return: The status of this FlowLogResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this FlowLogResp.

        功能说明：流日志状态 取值范围：ACTIVE、DOWN、ERROR

        :param status: The status of this FlowLogResp.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, FlowLogResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
