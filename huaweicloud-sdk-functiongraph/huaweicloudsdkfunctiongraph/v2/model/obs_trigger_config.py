# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OBSTriggerConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bucket': 'str',
        'events': 'list[str]',
        'prefix': 'str',
        'suffix': 'str'
    }

    attribute_map = {
        'bucket': 'bucket',
        'events': 'events',
        'prefix': 'prefix',
        'suffix': 'suffix'
    }

    def __init__(self, bucket=None, events=None, prefix=None, suffix=None):
        """OBSTriggerConfig

        The model defined in huaweicloud sdk

        :param bucket: OBS桶名（trigger_type为OBS时配置）
        :type bucket: str
        :param events: OBS事件列表（trigger_type为OBS时配置）
        :type events: list[str]
        :param prefix: 对象名前缀（trigger_type为OBS时配置）
        :type prefix: str
        :param suffix: 对象名后缀（trigger_type为OBS时配置）
        :type suffix: str
        """
        
        

        self._bucket = None
        self._events = None
        self._prefix = None
        self._suffix = None
        self.discriminator = None

        self.bucket = bucket
        self.events = events
        self.prefix = prefix
        self.suffix = suffix

    @property
    def bucket(self):
        """Gets the bucket of this OBSTriggerConfig.

        OBS桶名（trigger_type为OBS时配置）

        :return: The bucket of this OBSTriggerConfig.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this OBSTriggerConfig.

        OBS桶名（trigger_type为OBS时配置）

        :param bucket: The bucket of this OBSTriggerConfig.
        :type bucket: str
        """
        self._bucket = bucket

    @property
    def events(self):
        """Gets the events of this OBSTriggerConfig.

        OBS事件列表（trigger_type为OBS时配置）

        :return: The events of this OBSTriggerConfig.
        :rtype: list[str]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this OBSTriggerConfig.

        OBS事件列表（trigger_type为OBS时配置）

        :param events: The events of this OBSTriggerConfig.
        :type events: list[str]
        """
        self._events = events

    @property
    def prefix(self):
        """Gets the prefix of this OBSTriggerConfig.

        对象名前缀（trigger_type为OBS时配置）

        :return: The prefix of this OBSTriggerConfig.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this OBSTriggerConfig.

        对象名前缀（trigger_type为OBS时配置）

        :param prefix: The prefix of this OBSTriggerConfig.
        :type prefix: str
        """
        self._prefix = prefix

    @property
    def suffix(self):
        """Gets the suffix of this OBSTriggerConfig.

        对象名后缀（trigger_type为OBS时配置）

        :return: The suffix of this OBSTriggerConfig.
        :rtype: str
        """
        return self._suffix

    @suffix.setter
    def suffix(self, suffix):
        """Sets the suffix of this OBSTriggerConfig.

        对象名后缀（trigger_type为OBS时配置）

        :param suffix: The suffix of this OBSTriggerConfig.
        :type suffix: str
        """
        self._suffix = suffix

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
        if not isinstance(other, OBSTriggerConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
