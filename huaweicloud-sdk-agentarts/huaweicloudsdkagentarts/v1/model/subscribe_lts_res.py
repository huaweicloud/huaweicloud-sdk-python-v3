# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubscribeLtsRes:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'log_group_id': 'str',
        'log_group_name': 'str',
        'log_stream_list': 'list[LtsLogStream]'
    }

    attribute_map = {
        'log_group_id': 'log_group_id',
        'log_group_name': 'log_group_name',
        'log_stream_list': 'log_stream_list'
    }

    def __init__(self, log_group_id=None, log_group_name=None, log_stream_list=None):
        r"""SubscribeLtsRes

        The model defined in huaweicloud sdk

        :param log_group_id: 创建的日志组ID
        :type log_group_id: str
        :param log_group_name: 创建的日志组名称
        :type log_group_name: str
        :param log_stream_list: 日志组下的日志流信息
        :type log_stream_list: list[:class:`huaweicloudsdkagentarts.v1.LtsLogStream`]
        """
        
        

        self._log_group_id = None
        self._log_group_name = None
        self._log_stream_list = None
        self.discriminator = None

        if log_group_id is not None:
            self.log_group_id = log_group_id
        if log_group_name is not None:
            self.log_group_name = log_group_name
        if log_stream_list is not None:
            self.log_stream_list = log_stream_list

    @property
    def log_group_id(self):
        r"""Gets the log_group_id of this SubscribeLtsRes.

        创建的日志组ID

        :return: The log_group_id of this SubscribeLtsRes.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        r"""Sets the log_group_id of this SubscribeLtsRes.

        创建的日志组ID

        :param log_group_id: The log_group_id of this SubscribeLtsRes.
        :type log_group_id: str
        """
        self._log_group_id = log_group_id

    @property
    def log_group_name(self):
        r"""Gets the log_group_name of this SubscribeLtsRes.

        创建的日志组名称

        :return: The log_group_name of this SubscribeLtsRes.
        :rtype: str
        """
        return self._log_group_name

    @log_group_name.setter
    def log_group_name(self, log_group_name):
        r"""Sets the log_group_name of this SubscribeLtsRes.

        创建的日志组名称

        :param log_group_name: The log_group_name of this SubscribeLtsRes.
        :type log_group_name: str
        """
        self._log_group_name = log_group_name

    @property
    def log_stream_list(self):
        r"""Gets the log_stream_list of this SubscribeLtsRes.

        日志组下的日志流信息

        :return: The log_stream_list of this SubscribeLtsRes.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.LtsLogStream`]
        """
        return self._log_stream_list

    @log_stream_list.setter
    def log_stream_list(self, log_stream_list):
        r"""Sets the log_stream_list of this SubscribeLtsRes.

        日志组下的日志流信息

        :param log_stream_list: The log_stream_list of this SubscribeLtsRes.
        :type log_stream_list: list[:class:`huaweicloudsdkagentarts.v1.LtsLogStream`]
        """
        self._log_stream_list = log_stream_list

    def to_dict(self):
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
        if not isinstance(other, SubscribeLtsRes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
