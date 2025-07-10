# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListUserEventsLtsConfigurationsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable': 'bool',
        'log_group_id': 'str',
        'log_stream_id': 'str'
    }

    attribute_map = {
        'enable': 'enable',
        'log_group_id': 'log_group_id',
        'log_stream_id': 'log_stream_id'
    }

    def __init__(self, enable=None, log_group_id=None, log_stream_id=None):
        r"""ListUserEventsLtsConfigurationsResponse

        The model defined in huaweicloud sdk

        :param enable: 是否启用日志流LTS。
        :type enable: bool
        :param log_group_id: 日志组id。
        :type log_group_id: str
        :param log_stream_id: 日志流id。
        :type log_stream_id: str
        """
        
        super(ListUserEventsLtsConfigurationsResponse, self).__init__()

        self._enable = None
        self._log_group_id = None
        self._log_stream_id = None
        self.discriminator = None

        if enable is not None:
            self.enable = enable
        if log_group_id is not None:
            self.log_group_id = log_group_id
        if log_stream_id is not None:
            self.log_stream_id = log_stream_id

    @property
    def enable(self):
        r"""Gets the enable of this ListUserEventsLtsConfigurationsResponse.

        是否启用日志流LTS。

        :return: The enable of this ListUserEventsLtsConfigurationsResponse.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this ListUserEventsLtsConfigurationsResponse.

        是否启用日志流LTS。

        :param enable: The enable of this ListUserEventsLtsConfigurationsResponse.
        :type enable: bool
        """
        self._enable = enable

    @property
    def log_group_id(self):
        r"""Gets the log_group_id of this ListUserEventsLtsConfigurationsResponse.

        日志组id。

        :return: The log_group_id of this ListUserEventsLtsConfigurationsResponse.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        r"""Sets the log_group_id of this ListUserEventsLtsConfigurationsResponse.

        日志组id。

        :param log_group_id: The log_group_id of this ListUserEventsLtsConfigurationsResponse.
        :type log_group_id: str
        """
        self._log_group_id = log_group_id

    @property
    def log_stream_id(self):
        r"""Gets the log_stream_id of this ListUserEventsLtsConfigurationsResponse.

        日志流id。

        :return: The log_stream_id of this ListUserEventsLtsConfigurationsResponse.
        :rtype: str
        """
        return self._log_stream_id

    @log_stream_id.setter
    def log_stream_id(self, log_stream_id):
        r"""Sets the log_stream_id of this ListUserEventsLtsConfigurationsResponse.

        日志流id。

        :param log_stream_id: The log_stream_id of this ListUserEventsLtsConfigurationsResponse.
        :type log_stream_id: str
        """
        self._log_stream_id = log_stream_id

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
        if not isinstance(other, ListUserEventsLtsConfigurationsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
