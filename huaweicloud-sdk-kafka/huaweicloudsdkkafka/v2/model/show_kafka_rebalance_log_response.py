# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowKafkaRebalanceLogResponse(SdkResponse):

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
        'instance_id': 'str',
        'status': 'str',
        'log_stream_id': 'str',
        'log_group_id': 'str',
        'dashboard_id': 'str',
        'create_at': 'str',
        'update_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'instance_id': 'instanceId',
        'status': 'status',
        'log_stream_id': 'logStreamId',
        'log_group_id': 'logGroupId',
        'dashboard_id': 'dashboardId',
        'create_at': 'createAt',
        'update_at': 'updateAt'
    }

    def __init__(self, id=None, instance_id=None, status=None, log_stream_id=None, log_group_id=None, dashboard_id=None, create_at=None, update_at=None):
        r"""ShowKafkaRebalanceLogResponse

        The model defined in huaweicloud sdk

        :param id: 日志ID。
        :type id: str
        :param instance_id: 实例ID。
        :type instance_id: str
        :param status: 状态。
        :type status: str
        :param log_stream_id: 日志流ID。
        :type log_stream_id: str
        :param log_group_id: 日志组ID。
        :type log_group_id: str
        :param dashboard_id: 看板ID。
        :type dashboard_id: str
        :param create_at: 创建时间。
        :type create_at: str
        :param update_at: 更新时间。
        :type update_at: str
        """
        
        super(ShowKafkaRebalanceLogResponse, self).__init__()

        self._id = None
        self._instance_id = None
        self._status = None
        self._log_stream_id = None
        self._log_group_id = None
        self._dashboard_id = None
        self._create_at = None
        self._update_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if instance_id is not None:
            self.instance_id = instance_id
        if status is not None:
            self.status = status
        if log_stream_id is not None:
            self.log_stream_id = log_stream_id
        if log_group_id is not None:
            self.log_group_id = log_group_id
        if dashboard_id is not None:
            self.dashboard_id = dashboard_id
        if create_at is not None:
            self.create_at = create_at
        if update_at is not None:
            self.update_at = update_at

    @property
    def id(self):
        r"""Gets the id of this ShowKafkaRebalanceLogResponse.

        日志ID。

        :return: The id of this ShowKafkaRebalanceLogResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowKafkaRebalanceLogResponse.

        日志ID。

        :param id: The id of this ShowKafkaRebalanceLogResponse.
        :type id: str
        """
        self._id = id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowKafkaRebalanceLogResponse.

        实例ID。

        :return: The instance_id of this ShowKafkaRebalanceLogResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowKafkaRebalanceLogResponse.

        实例ID。

        :param instance_id: The instance_id of this ShowKafkaRebalanceLogResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def status(self):
        r"""Gets the status of this ShowKafkaRebalanceLogResponse.

        状态。

        :return: The status of this ShowKafkaRebalanceLogResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowKafkaRebalanceLogResponse.

        状态。

        :param status: The status of this ShowKafkaRebalanceLogResponse.
        :type status: str
        """
        self._status = status

    @property
    def log_stream_id(self):
        r"""Gets the log_stream_id of this ShowKafkaRebalanceLogResponse.

        日志流ID。

        :return: The log_stream_id of this ShowKafkaRebalanceLogResponse.
        :rtype: str
        """
        return self._log_stream_id

    @log_stream_id.setter
    def log_stream_id(self, log_stream_id):
        r"""Sets the log_stream_id of this ShowKafkaRebalanceLogResponse.

        日志流ID。

        :param log_stream_id: The log_stream_id of this ShowKafkaRebalanceLogResponse.
        :type log_stream_id: str
        """
        self._log_stream_id = log_stream_id

    @property
    def log_group_id(self):
        r"""Gets the log_group_id of this ShowKafkaRebalanceLogResponse.

        日志组ID。

        :return: The log_group_id of this ShowKafkaRebalanceLogResponse.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        r"""Sets the log_group_id of this ShowKafkaRebalanceLogResponse.

        日志组ID。

        :param log_group_id: The log_group_id of this ShowKafkaRebalanceLogResponse.
        :type log_group_id: str
        """
        self._log_group_id = log_group_id

    @property
    def dashboard_id(self):
        r"""Gets the dashboard_id of this ShowKafkaRebalanceLogResponse.

        看板ID。

        :return: The dashboard_id of this ShowKafkaRebalanceLogResponse.
        :rtype: str
        """
        return self._dashboard_id

    @dashboard_id.setter
    def dashboard_id(self, dashboard_id):
        r"""Sets the dashboard_id of this ShowKafkaRebalanceLogResponse.

        看板ID。

        :param dashboard_id: The dashboard_id of this ShowKafkaRebalanceLogResponse.
        :type dashboard_id: str
        """
        self._dashboard_id = dashboard_id

    @property
    def create_at(self):
        r"""Gets the create_at of this ShowKafkaRebalanceLogResponse.

        创建时间。

        :return: The create_at of this ShowKafkaRebalanceLogResponse.
        :rtype: str
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this ShowKafkaRebalanceLogResponse.

        创建时间。

        :param create_at: The create_at of this ShowKafkaRebalanceLogResponse.
        :type create_at: str
        """
        self._create_at = create_at

    @property
    def update_at(self):
        r"""Gets the update_at of this ShowKafkaRebalanceLogResponse.

        更新时间。

        :return: The update_at of this ShowKafkaRebalanceLogResponse.
        :rtype: str
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        r"""Sets the update_at of this ShowKafkaRebalanceLogResponse.

        更新时间。

        :param update_at: The update_at of this ShowKafkaRebalanceLogResponse.
        :type update_at: str
        """
        self._update_at = update_at

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
        if not isinstance(other, ShowKafkaRebalanceLogResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
