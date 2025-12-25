# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LtsResponseVoLtsInfos:

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
        'streams': 'list[LtsResponseVoStreams]'
    }

    attribute_map = {
        'log_group_id': 'log_group_id',
        'log_group_name': 'log_group_name',
        'streams': 'streams'
    }

    def __init__(self, log_group_id=None, log_group_name=None, streams=None):
        r"""LtsResponseVoLtsInfos

        The model defined in huaweicloud sdk

        :param log_group_id: 日志组id
        :type log_group_id: str
        :param log_group_name: 组名称
        :type log_group_name: str
        :param streams: 流列表
        :type streams: list[:class:`huaweicloudsdksecmaster.v1.LtsResponseVoStreams`]
        """
        
        

        self._log_group_id = None
        self._log_group_name = None
        self._streams = None
        self.discriminator = None

        if log_group_id is not None:
            self.log_group_id = log_group_id
        if log_group_name is not None:
            self.log_group_name = log_group_name
        if streams is not None:
            self.streams = streams

    @property
    def log_group_id(self):
        r"""Gets the log_group_id of this LtsResponseVoLtsInfos.

        日志组id

        :return: The log_group_id of this LtsResponseVoLtsInfos.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        r"""Sets the log_group_id of this LtsResponseVoLtsInfos.

        日志组id

        :param log_group_id: The log_group_id of this LtsResponseVoLtsInfos.
        :type log_group_id: str
        """
        self._log_group_id = log_group_id

    @property
    def log_group_name(self):
        r"""Gets the log_group_name of this LtsResponseVoLtsInfos.

        组名称

        :return: The log_group_name of this LtsResponseVoLtsInfos.
        :rtype: str
        """
        return self._log_group_name

    @log_group_name.setter
    def log_group_name(self, log_group_name):
        r"""Sets the log_group_name of this LtsResponseVoLtsInfos.

        组名称

        :param log_group_name: The log_group_name of this LtsResponseVoLtsInfos.
        :type log_group_name: str
        """
        self._log_group_name = log_group_name

    @property
    def streams(self):
        r"""Gets the streams of this LtsResponseVoLtsInfos.

        流列表

        :return: The streams of this LtsResponseVoLtsInfos.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.LtsResponseVoStreams`]
        """
        return self._streams

    @streams.setter
    def streams(self, streams):
        r"""Sets the streams of this LtsResponseVoLtsInfos.

        流列表

        :param streams: The streams of this LtsResponseVoLtsInfos.
        :type streams: list[:class:`huaweicloudsdksecmaster.v1.LtsResponseVoStreams`]
        """
        self._streams = streams

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
        if not isinstance(other, LtsResponseVoLtsInfos):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
