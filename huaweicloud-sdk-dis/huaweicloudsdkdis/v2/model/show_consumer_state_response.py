# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowConsumerStateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'has_more': 'bool',
        'stream_name': 'str',
        'app_name': 'str',
        'partition_consuming_states': 'list[PartitionConsumingStates]'
    }

    attribute_map = {
        'has_more': 'has_more',
        'stream_name': 'stream_name',
        'app_name': 'app_name',
        'partition_consuming_states': 'partition_consuming_states'
    }

    def __init__(self, has_more=None, stream_name=None, app_name=None, partition_consuming_states=None):
        r"""ShowConsumerStateResponse

        The model defined in huaweicloud sdk

        :param has_more: 是否还有更多满足条件的App。  - true：是。 - false：否。
        :type has_more: bool
        :param stream_name: 要查询的通道名称。
        :type stream_name: str
        :param app_name: 要查询的APP的名称，用户数据消费程序的唯一标识符。
        :type app_name: str
        :param partition_consuming_states: 当前分区消费状态.
        :type partition_consuming_states: list[:class:`huaweicloudsdkdis.v2.PartitionConsumingStates`]
        """
        
        super().__init__()

        self._has_more = None
        self._stream_name = None
        self._app_name = None
        self._partition_consuming_states = None
        self.discriminator = None

        if has_more is not None:
            self.has_more = has_more
        if stream_name is not None:
            self.stream_name = stream_name
        if app_name is not None:
            self.app_name = app_name
        if partition_consuming_states is not None:
            self.partition_consuming_states = partition_consuming_states

    @property
    def has_more(self):
        r"""Gets the has_more of this ShowConsumerStateResponse.

        是否还有更多满足条件的App。  - true：是。 - false：否。

        :return: The has_more of this ShowConsumerStateResponse.
        :rtype: bool
        """
        return self._has_more

    @has_more.setter
    def has_more(self, has_more):
        r"""Sets the has_more of this ShowConsumerStateResponse.

        是否还有更多满足条件的App。  - true：是。 - false：否。

        :param has_more: The has_more of this ShowConsumerStateResponse.
        :type has_more: bool
        """
        self._has_more = has_more

    @property
    def stream_name(self):
        r"""Gets the stream_name of this ShowConsumerStateResponse.

        要查询的通道名称。

        :return: The stream_name of this ShowConsumerStateResponse.
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        r"""Sets the stream_name of this ShowConsumerStateResponse.

        要查询的通道名称。

        :param stream_name: The stream_name of this ShowConsumerStateResponse.
        :type stream_name: str
        """
        self._stream_name = stream_name

    @property
    def app_name(self):
        r"""Gets the app_name of this ShowConsumerStateResponse.

        要查询的APP的名称，用户数据消费程序的唯一标识符。

        :return: The app_name of this ShowConsumerStateResponse.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this ShowConsumerStateResponse.

        要查询的APP的名称，用户数据消费程序的唯一标识符。

        :param app_name: The app_name of this ShowConsumerStateResponse.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def partition_consuming_states(self):
        r"""Gets the partition_consuming_states of this ShowConsumerStateResponse.

        当前分区消费状态.

        :return: The partition_consuming_states of this ShowConsumerStateResponse.
        :rtype: list[:class:`huaweicloudsdkdis.v2.PartitionConsumingStates`]
        """
        return self._partition_consuming_states

    @partition_consuming_states.setter
    def partition_consuming_states(self, partition_consuming_states):
        r"""Sets the partition_consuming_states of this ShowConsumerStateResponse.

        当前分区消费状态.

        :param partition_consuming_states: The partition_consuming_states of this ShowConsumerStateResponse.
        :type partition_consuming_states: list[:class:`huaweicloudsdkdis.v2.PartitionConsumingStates`]
        """
        self._partition_consuming_states = partition_consuming_states

    def to_dict(self):
        import warnings
        warnings.warn("ShowConsumerStateResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowConsumerStateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
