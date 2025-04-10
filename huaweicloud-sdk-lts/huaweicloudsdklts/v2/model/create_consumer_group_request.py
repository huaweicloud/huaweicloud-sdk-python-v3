# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateConsumerGroupRequest:

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
        'body': 'ConsumerGroupInfo'
    }

    attribute_map = {
        'group_id': 'group_id',
        'stream_id': 'stream_id',
        'body': 'body'
    }

    def __init__(self, group_id=None, stream_id=None, body=None):
        r"""CreateConsumerGroupRequest

        The model defined in huaweicloud sdk

        :param group_id: 日志组ID，获取方式请参见：获取项目ID，获取账号ID，日志组ID、日志流ID。 缺省值：None 最小长度：36 最大长度：36
        :type group_id: str
        :param stream_id: 日志流ID，获取方式请参见：获取项目ID，获取账号ID，日志组ID、日志流ID 缺省值：None 最小长度：36 最大长度：36
        :type stream_id: str
        :param body: Body of the CreateConsumerGroupRequest
        :type body: :class:`huaweicloudsdklts.v2.ConsumerGroupInfo`
        """
        
        

        self._group_id = None
        self._stream_id = None
        self._body = None
        self.discriminator = None

        self.group_id = group_id
        self.stream_id = stream_id
        if body is not None:
            self.body = body

    @property
    def group_id(self):
        r"""Gets the group_id of this CreateConsumerGroupRequest.

        日志组ID，获取方式请参见：获取项目ID，获取账号ID，日志组ID、日志流ID。 缺省值：None 最小长度：36 最大长度：36

        :return: The group_id of this CreateConsumerGroupRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this CreateConsumerGroupRequest.

        日志组ID，获取方式请参见：获取项目ID，获取账号ID，日志组ID、日志流ID。 缺省值：None 最小长度：36 最大长度：36

        :param group_id: The group_id of this CreateConsumerGroupRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def stream_id(self):
        r"""Gets the stream_id of this CreateConsumerGroupRequest.

        日志流ID，获取方式请参见：获取项目ID，获取账号ID，日志组ID、日志流ID 缺省值：None 最小长度：36 最大长度：36

        :return: The stream_id of this CreateConsumerGroupRequest.
        :rtype: str
        """
        return self._stream_id

    @stream_id.setter
    def stream_id(self, stream_id):
        r"""Sets the stream_id of this CreateConsumerGroupRequest.

        日志流ID，获取方式请参见：获取项目ID，获取账号ID，日志组ID、日志流ID 缺省值：None 最小长度：36 最大长度：36

        :param stream_id: The stream_id of this CreateConsumerGroupRequest.
        :type stream_id: str
        """
        self._stream_id = stream_id

    @property
    def body(self):
        r"""Gets the body of this CreateConsumerGroupRequest.

        :return: The body of this CreateConsumerGroupRequest.
        :rtype: :class:`huaweicloudsdklts.v2.ConsumerGroupInfo`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CreateConsumerGroupRequest.

        :param body: The body of this CreateConsumerGroupRequest.
        :type body: :class:`huaweicloudsdklts.v2.ConsumerGroupInfo`
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
        if not isinstance(other, CreateConsumerGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
