# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlowLogRequest:

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
        'log_group_id': 'str',
        'log_stream_id': 'str',
        'log_store_type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'resource_type': 'resource_type',
        'resource_id': 'resource_id',
        'log_group_id': 'log_group_id',
        'log_stream_id': 'log_stream_id',
        'log_store_type': 'log_store_type'
    }

    def __init__(self, name=None, description=None, resource_type=None, resource_id=None, log_group_id=None, log_stream_id=None, log_store_type=None):
        """FlowLogRequest

        The model defined in huaweicloud sdk

        :param name: 流日志名称
        :type name: str
        :param description: 流日志描述
        :type description: str
        :param resource_type: 流日志采集的资源类型:   - VPC连接   - 虚拟网关连接   - 对等连接
        :type resource_type: str
        :param resource_id: 要采集的资源ID
        :type resource_id: str
        :param log_group_id: 日志组ID。请在云日志服务中获取，详情请参见《云日志服务用户指南》。
        :type log_group_id: str
        :param log_stream_id: 日志主题ID。请在云日志服务中获取，详情请参见《云日志服务用户指南》。
        :type log_stream_id: str
        :param log_store_type: 流日志的存储类型: - LTS: 云日志服务器存储
        :type log_store_type: str
        """
        
        

        self._name = None
        self._description = None
        self._resource_type = None
        self._resource_id = None
        self._log_group_id = None
        self._log_stream_id = None
        self._log_store_type = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.log_group_id = log_group_id
        self.log_stream_id = log_stream_id
        self.log_store_type = log_store_type

    @property
    def name(self):
        """Gets the name of this FlowLogRequest.

        流日志名称

        :return: The name of this FlowLogRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FlowLogRequest.

        流日志名称

        :param name: The name of this FlowLogRequest.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this FlowLogRequest.

        流日志描述

        :return: The description of this FlowLogRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FlowLogRequest.

        流日志描述

        :param description: The description of this FlowLogRequest.
        :type description: str
        """
        self._description = description

    @property
    def resource_type(self):
        """Gets the resource_type of this FlowLogRequest.

        流日志采集的资源类型:   - VPC连接   - 虚拟网关连接   - 对等连接

        :return: The resource_type of this FlowLogRequest.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this FlowLogRequest.

        流日志采集的资源类型:   - VPC连接   - 虚拟网关连接   - 对等连接

        :param resource_type: The resource_type of this FlowLogRequest.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_id(self):
        """Gets the resource_id of this FlowLogRequest.

        要采集的资源ID

        :return: The resource_id of this FlowLogRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this FlowLogRequest.

        要采集的资源ID

        :param resource_id: The resource_id of this FlowLogRequest.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def log_group_id(self):
        """Gets the log_group_id of this FlowLogRequest.

        日志组ID。请在云日志服务中获取，详情请参见《云日志服务用户指南》。

        :return: The log_group_id of this FlowLogRequest.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        """Sets the log_group_id of this FlowLogRequest.

        日志组ID。请在云日志服务中获取，详情请参见《云日志服务用户指南》。

        :param log_group_id: The log_group_id of this FlowLogRequest.
        :type log_group_id: str
        """
        self._log_group_id = log_group_id

    @property
    def log_stream_id(self):
        """Gets the log_stream_id of this FlowLogRequest.

        日志主题ID。请在云日志服务中获取，详情请参见《云日志服务用户指南》。

        :return: The log_stream_id of this FlowLogRequest.
        :rtype: str
        """
        return self._log_stream_id

    @log_stream_id.setter
    def log_stream_id(self, log_stream_id):
        """Sets the log_stream_id of this FlowLogRequest.

        日志主题ID。请在云日志服务中获取，详情请参见《云日志服务用户指南》。

        :param log_stream_id: The log_stream_id of this FlowLogRequest.
        :type log_stream_id: str
        """
        self._log_stream_id = log_stream_id

    @property
    def log_store_type(self):
        """Gets the log_store_type of this FlowLogRequest.

        流日志的存储类型: - LTS: 云日志服务器存储

        :return: The log_store_type of this FlowLogRequest.
        :rtype: str
        """
        return self._log_store_type

    @log_store_type.setter
    def log_store_type(self, log_store_type):
        """Sets the log_store_type of this FlowLogRequest.

        流日志的存储类型: - LTS: 云日志服务器存储

        :param log_store_type: The log_store_type of this FlowLogRequest.
        :type log_store_type: str
        """
        self._log_store_type = log_store_type

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
        if not isinstance(other, FlowLogRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
