# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowConsumerStateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_name': 'str',
        'stream_name': 'str',
        'limit': 'int',
        'start_partition_id': 'str',
        'checkpoint_type': 'str'
    }

    attribute_map = {
        'app_name': 'app_name',
        'stream_name': 'stream_name',
        'limit': 'limit',
        'start_partition_id': 'start_partition_id',
        'checkpoint_type': 'checkpoint_type'
    }

    def __init__(self, app_name=None, stream_name=None, limit=None, start_partition_id=None, checkpoint_type=None):
        """ShowConsumerStateRequest

        The model defined in huaweicloud sdk

        :param app_name: 需要查询的App名称。
        :type app_name: str
        :param stream_name: 需要查询的通道名称。
        :type stream_name: str
        :param limit: 单次请求返回的最大分区数。最小值是1，最大值是1000；默认值是100。
        :type limit: int
        :param start_partition_id: 从该分区值开始返回分区列表，返回的分区列表不包括此分区。
        :type start_partition_id: str
        :param checkpoint_type: Checkpoint类型。  - LAST_READ：在数据库中只记录序列号。
        :type checkpoint_type: str
        """
        
        

        self._app_name = None
        self._stream_name = None
        self._limit = None
        self._start_partition_id = None
        self._checkpoint_type = None
        self.discriminator = None

        self.app_name = app_name
        self.stream_name = stream_name
        if limit is not None:
            self.limit = limit
        if start_partition_id is not None:
            self.start_partition_id = start_partition_id
        self.checkpoint_type = checkpoint_type

    @property
    def app_name(self):
        """Gets the app_name of this ShowConsumerStateRequest.

        需要查询的App名称。

        :return: The app_name of this ShowConsumerStateRequest.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this ShowConsumerStateRequest.

        需要查询的App名称。

        :param app_name: The app_name of this ShowConsumerStateRequest.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def stream_name(self):
        """Gets the stream_name of this ShowConsumerStateRequest.

        需要查询的通道名称。

        :return: The stream_name of this ShowConsumerStateRequest.
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        """Sets the stream_name of this ShowConsumerStateRequest.

        需要查询的通道名称。

        :param stream_name: The stream_name of this ShowConsumerStateRequest.
        :type stream_name: str
        """
        self._stream_name = stream_name

    @property
    def limit(self):
        """Gets the limit of this ShowConsumerStateRequest.

        单次请求返回的最大分区数。最小值是1，最大值是1000；默认值是100。

        :return: The limit of this ShowConsumerStateRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowConsumerStateRequest.

        单次请求返回的最大分区数。最小值是1，最大值是1000；默认值是100。

        :param limit: The limit of this ShowConsumerStateRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def start_partition_id(self):
        """Gets the start_partition_id of this ShowConsumerStateRequest.

        从该分区值开始返回分区列表，返回的分区列表不包括此分区。

        :return: The start_partition_id of this ShowConsumerStateRequest.
        :rtype: str
        """
        return self._start_partition_id

    @start_partition_id.setter
    def start_partition_id(self, start_partition_id):
        """Sets the start_partition_id of this ShowConsumerStateRequest.

        从该分区值开始返回分区列表，返回的分区列表不包括此分区。

        :param start_partition_id: The start_partition_id of this ShowConsumerStateRequest.
        :type start_partition_id: str
        """
        self._start_partition_id = start_partition_id

    @property
    def checkpoint_type(self):
        """Gets the checkpoint_type of this ShowConsumerStateRequest.

        Checkpoint类型。  - LAST_READ：在数据库中只记录序列号。

        :return: The checkpoint_type of this ShowConsumerStateRequest.
        :rtype: str
        """
        return self._checkpoint_type

    @checkpoint_type.setter
    def checkpoint_type(self, checkpoint_type):
        """Sets the checkpoint_type of this ShowConsumerStateRequest.

        Checkpoint类型。  - LAST_READ：在数据库中只记录序列号。

        :param checkpoint_type: The checkpoint_type of this ShowConsumerStateRequest.
        :type checkpoint_type: str
        """
        self._checkpoint_type = checkpoint_type

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
        if not isinstance(other, ShowConsumerStateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
