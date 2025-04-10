# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateCheckPointRequest:

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
        'stream_id': 'str',
        'consumer_group_name': 'str',
        'consumer_name': 'str',
        'body': 'list[ConsumerShardCheckpointInfo]'
    }

    attribute_map = {
        'group_id': 'group_id',
        'stream_id': 'stream_id',
        'consumer_group_name': 'consumer_group_name',
        'consumer_name': 'consumer_name',
        'body': 'body'
    }

    def __init__(self, group_id=None, stream_id=None, consumer_group_name=None, consumer_name=None, body=None):
        r"""UpdateCheckPointRequest

        The model defined in huaweicloud sdk

        :param group_id: 日志组ID，获取方式请参见：获取项目ID，获取账号ID，日志组ID、日志流ID。 缺省值：None 最小长度：36 最大长度：36
        :type group_id: str
        :param stream_id: 日志流ID，获取方式请参见：获取项目ID，获取账号ID，日志组ID、日志流ID 缺省值：None 最小长度：36 最大长度：36
        :type stream_id: str
        :param consumer_group_name: 消费组名
        :type consumer_group_name: str
        :param consumer_name: 消费者名
        :type consumer_name: str
        :param body: Body of the UpdateCheckPointRequest
        :type body: list[:class:`huaweicloudsdklts.v2.ConsumerShardCheckpointInfo`]
        """
        
        

        self._group_id = None
        self._stream_id = None
        self._consumer_group_name = None
        self._consumer_name = None
        self._body = None
        self.discriminator = None

        self.group_id = group_id
        self.stream_id = stream_id
        self.consumer_group_name = consumer_group_name
        self.consumer_name = consumer_name
        if body is not None:
            self.body = body

    @property
    def group_id(self):
        r"""Gets the group_id of this UpdateCheckPointRequest.

        日志组ID，获取方式请参见：获取项目ID，获取账号ID，日志组ID、日志流ID。 缺省值：None 最小长度：36 最大长度：36

        :return: The group_id of this UpdateCheckPointRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this UpdateCheckPointRequest.

        日志组ID，获取方式请参见：获取项目ID，获取账号ID，日志组ID、日志流ID。 缺省值：None 最小长度：36 最大长度：36

        :param group_id: The group_id of this UpdateCheckPointRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def stream_id(self):
        r"""Gets the stream_id of this UpdateCheckPointRequest.

        日志流ID，获取方式请参见：获取项目ID，获取账号ID，日志组ID、日志流ID 缺省值：None 最小长度：36 最大长度：36

        :return: The stream_id of this UpdateCheckPointRequest.
        :rtype: str
        """
        return self._stream_id

    @stream_id.setter
    def stream_id(self, stream_id):
        r"""Sets the stream_id of this UpdateCheckPointRequest.

        日志流ID，获取方式请参见：获取项目ID，获取账号ID，日志组ID、日志流ID 缺省值：None 最小长度：36 最大长度：36

        :param stream_id: The stream_id of this UpdateCheckPointRequest.
        :type stream_id: str
        """
        self._stream_id = stream_id

    @property
    def consumer_group_name(self):
        r"""Gets the consumer_group_name of this UpdateCheckPointRequest.

        消费组名

        :return: The consumer_group_name of this UpdateCheckPointRequest.
        :rtype: str
        """
        return self._consumer_group_name

    @consumer_group_name.setter
    def consumer_group_name(self, consumer_group_name):
        r"""Sets the consumer_group_name of this UpdateCheckPointRequest.

        消费组名

        :param consumer_group_name: The consumer_group_name of this UpdateCheckPointRequest.
        :type consumer_group_name: str
        """
        self._consumer_group_name = consumer_group_name

    @property
    def consumer_name(self):
        r"""Gets the consumer_name of this UpdateCheckPointRequest.

        消费者名

        :return: The consumer_name of this UpdateCheckPointRequest.
        :rtype: str
        """
        return self._consumer_name

    @consumer_name.setter
    def consumer_name(self, consumer_name):
        r"""Sets the consumer_name of this UpdateCheckPointRequest.

        消费者名

        :param consumer_name: The consumer_name of this UpdateCheckPointRequest.
        :type consumer_name: str
        """
        self._consumer_name = consumer_name

    @property
    def body(self):
        r"""Gets the body of this UpdateCheckPointRequest.

        :return: The body of this UpdateCheckPointRequest.
        :rtype: list[:class:`huaweicloudsdklts.v2.ConsumerShardCheckpointInfo`]
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateCheckPointRequest.

        :param body: The body of this UpdateCheckPointRequest.
        :type body: list[:class:`huaweicloudsdklts.v2.ConsumerShardCheckpointInfo`]
        """
        self._body = body

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
        if not isinstance(other, UpdateCheckPointRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
