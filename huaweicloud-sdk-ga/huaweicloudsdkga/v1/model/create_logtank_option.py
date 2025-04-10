# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateLogtankOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_type': 'LogtankResourceType',
        'resource_id': 'str',
        'log_group_id': 'str',
        'log_stream_id': 'str'
    }

    attribute_map = {
        'resource_type': 'resource_type',
        'resource_id': 'resource_id',
        'log_group_id': 'log_group_id',
        'log_stream_id': 'log_stream_id'
    }

    def __init__(self, resource_type=None, resource_id=None, log_group_id=None, log_stream_id=None):
        r"""CreateLogtankOption

        The model defined in huaweicloud sdk

        :param resource_type: 
        :type resource_type: :class:`huaweicloudsdkga.v1.LogtankResourceType`
        :param resource_id: 开启云日志的资源ID。
        :type resource_id: str
        :param log_group_id: 云日志服务提供的日志组ID。
        :type log_group_id: str
        :param log_stream_id: 云日志服务提供的日志流ID。
        :type log_stream_id: str
        """
        
        

        self._resource_type = None
        self._resource_id = None
        self._log_group_id = None
        self._log_stream_id = None
        self.discriminator = None

        self.resource_type = resource_type
        self.resource_id = resource_id
        self.log_group_id = log_group_id
        self.log_stream_id = log_stream_id

    @property
    def resource_type(self):
        r"""Gets the resource_type of this CreateLogtankOption.

        :return: The resource_type of this CreateLogtankOption.
        :rtype: :class:`huaweicloudsdkga.v1.LogtankResourceType`
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this CreateLogtankOption.

        :param resource_type: The resource_type of this CreateLogtankOption.
        :type resource_type: :class:`huaweicloudsdkga.v1.LogtankResourceType`
        """
        self._resource_type = resource_type

    @property
    def resource_id(self):
        r"""Gets the resource_id of this CreateLogtankOption.

        开启云日志的资源ID。

        :return: The resource_id of this CreateLogtankOption.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this CreateLogtankOption.

        开启云日志的资源ID。

        :param resource_id: The resource_id of this CreateLogtankOption.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def log_group_id(self):
        r"""Gets the log_group_id of this CreateLogtankOption.

        云日志服务提供的日志组ID。

        :return: The log_group_id of this CreateLogtankOption.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        r"""Sets the log_group_id of this CreateLogtankOption.

        云日志服务提供的日志组ID。

        :param log_group_id: The log_group_id of this CreateLogtankOption.
        :type log_group_id: str
        """
        self._log_group_id = log_group_id

    @property
    def log_stream_id(self):
        r"""Gets the log_stream_id of this CreateLogtankOption.

        云日志服务提供的日志流ID。

        :return: The log_stream_id of this CreateLogtankOption.
        :rtype: str
        """
        return self._log_stream_id

    @log_stream_id.setter
    def log_stream_id(self, log_stream_id):
        r"""Sets the log_stream_id of this CreateLogtankOption.

        云日志服务提供的日志流ID。

        :param log_stream_id: The log_stream_id of this CreateLogtankOption.
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
        if not isinstance(other, CreateLogtankOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
