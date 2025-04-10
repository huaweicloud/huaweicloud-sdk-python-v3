# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateConsumerGroupResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'consumer_group_name': 'str',
        'create_time': 'int',
        'log_group_id': 'str',
        'log_stream_id': 'str',
        'project_id': 'str',
        'timeout': 'int'
    }

    attribute_map = {
        'consumer_group_name': 'consumer_group_name',
        'create_time': 'create_time',
        'log_group_id': 'log_group_id',
        'log_stream_id': 'log_stream_id',
        'project_id': 'project_id',
        'timeout': 'timeout'
    }

    def __init__(self, consumer_group_name=None, create_time=None, log_group_id=None, log_stream_id=None, project_id=None, timeout=None):
        r"""CreateConsumerGroupResponse

        The model defined in huaweicloud sdk

        :param consumer_group_name: 创建的消费组名
        :type consumer_group_name: str
        :param create_time: 创建时间
        :type create_time: int
        :param log_group_id: 日志组ID
        :type log_group_id: str
        :param log_stream_id: 日志流ID
        :type log_stream_id: str
        :param project_id: 项目ID
        :type project_id: str
        :param timeout: 超时时间，单位秒
        :type timeout: int
        """
        
        super(CreateConsumerGroupResponse, self).__init__()

        self._consumer_group_name = None
        self._create_time = None
        self._log_group_id = None
        self._log_stream_id = None
        self._project_id = None
        self._timeout = None
        self.discriminator = None

        if consumer_group_name is not None:
            self.consumer_group_name = consumer_group_name
        if create_time is not None:
            self.create_time = create_time
        if log_group_id is not None:
            self.log_group_id = log_group_id
        if log_stream_id is not None:
            self.log_stream_id = log_stream_id
        if project_id is not None:
            self.project_id = project_id
        if timeout is not None:
            self.timeout = timeout

    @property
    def consumer_group_name(self):
        r"""Gets the consumer_group_name of this CreateConsumerGroupResponse.

        创建的消费组名

        :return: The consumer_group_name of this CreateConsumerGroupResponse.
        :rtype: str
        """
        return self._consumer_group_name

    @consumer_group_name.setter
    def consumer_group_name(self, consumer_group_name):
        r"""Sets the consumer_group_name of this CreateConsumerGroupResponse.

        创建的消费组名

        :param consumer_group_name: The consumer_group_name of this CreateConsumerGroupResponse.
        :type consumer_group_name: str
        """
        self._consumer_group_name = consumer_group_name

    @property
    def create_time(self):
        r"""Gets the create_time of this CreateConsumerGroupResponse.

        创建时间

        :return: The create_time of this CreateConsumerGroupResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this CreateConsumerGroupResponse.

        创建时间

        :param create_time: The create_time of this CreateConsumerGroupResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def log_group_id(self):
        r"""Gets the log_group_id of this CreateConsumerGroupResponse.

        日志组ID

        :return: The log_group_id of this CreateConsumerGroupResponse.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        r"""Sets the log_group_id of this CreateConsumerGroupResponse.

        日志组ID

        :param log_group_id: The log_group_id of this CreateConsumerGroupResponse.
        :type log_group_id: str
        """
        self._log_group_id = log_group_id

    @property
    def log_stream_id(self):
        r"""Gets the log_stream_id of this CreateConsumerGroupResponse.

        日志流ID

        :return: The log_stream_id of this CreateConsumerGroupResponse.
        :rtype: str
        """
        return self._log_stream_id

    @log_stream_id.setter
    def log_stream_id(self, log_stream_id):
        r"""Sets the log_stream_id of this CreateConsumerGroupResponse.

        日志流ID

        :param log_stream_id: The log_stream_id of this CreateConsumerGroupResponse.
        :type log_stream_id: str
        """
        self._log_stream_id = log_stream_id

    @property
    def project_id(self):
        r"""Gets the project_id of this CreateConsumerGroupResponse.

        项目ID

        :return: The project_id of this CreateConsumerGroupResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this CreateConsumerGroupResponse.

        项目ID

        :param project_id: The project_id of this CreateConsumerGroupResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def timeout(self):
        r"""Gets the timeout of this CreateConsumerGroupResponse.

        超时时间，单位秒

        :return: The timeout of this CreateConsumerGroupResponse.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        r"""Sets the timeout of this CreateConsumerGroupResponse.

        超时时间，单位秒

        :param timeout: The timeout of this CreateConsumerGroupResponse.
        :type timeout: int
        """
        self._timeout = timeout

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
        if not isinstance(other, CreateConsumerGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
