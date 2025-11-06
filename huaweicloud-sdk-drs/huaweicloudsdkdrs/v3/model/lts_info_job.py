# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LtsInfoJob:

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
        'log_stream_id': 'str',
        'lts_enabled': 'bool'
    }

    attribute_map = {
        'log_group_id': 'log_group_id',
        'log_stream_id': 'log_stream_id',
        'lts_enabled': 'lts_enabled'
    }

    def __init__(self, log_group_id=None, log_stream_id=None, lts_enabled=None):
        r"""LtsInfoJob

        The model defined in huaweicloud sdk

        :param log_group_id: 日志组ID。
        :type log_group_id: str
        :param log_stream_id: 日志流ID。
        :type log_stream_id: str
        :param lts_enabled: 是否开启LTS。
        :type lts_enabled: bool
        """
        
        

        self._log_group_id = None
        self._log_stream_id = None
        self._lts_enabled = None
        self.discriminator = None

        if log_group_id is not None:
            self.log_group_id = log_group_id
        if log_stream_id is not None:
            self.log_stream_id = log_stream_id
        if lts_enabled is not None:
            self.lts_enabled = lts_enabled

    @property
    def log_group_id(self):
        r"""Gets the log_group_id of this LtsInfoJob.

        日志组ID。

        :return: The log_group_id of this LtsInfoJob.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        r"""Sets the log_group_id of this LtsInfoJob.

        日志组ID。

        :param log_group_id: The log_group_id of this LtsInfoJob.
        :type log_group_id: str
        """
        self._log_group_id = log_group_id

    @property
    def log_stream_id(self):
        r"""Gets the log_stream_id of this LtsInfoJob.

        日志流ID。

        :return: The log_stream_id of this LtsInfoJob.
        :rtype: str
        """
        return self._log_stream_id

    @log_stream_id.setter
    def log_stream_id(self, log_stream_id):
        r"""Sets the log_stream_id of this LtsInfoJob.

        日志流ID。

        :param log_stream_id: The log_stream_id of this LtsInfoJob.
        :type log_stream_id: str
        """
        self._log_stream_id = log_stream_id

    @property
    def lts_enabled(self):
        r"""Gets the lts_enabled of this LtsInfoJob.

        是否开启LTS。

        :return: The lts_enabled of this LtsInfoJob.
        :rtype: bool
        """
        return self._lts_enabled

    @lts_enabled.setter
    def lts_enabled(self, lts_enabled):
        r"""Sets the lts_enabled of this LtsInfoJob.

        是否开启LTS。

        :param lts_enabled: The lts_enabled of this LtsInfoJob.
        :type lts_enabled: bool
        """
        self._lts_enabled = lts_enabled

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
        if not isinstance(other, LtsInfoJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
