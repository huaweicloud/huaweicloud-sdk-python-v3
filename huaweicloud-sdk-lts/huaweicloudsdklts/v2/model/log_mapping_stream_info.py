# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LogMappingStreamInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_log_stream_id': 'str',
        'target_log_stream_id': 'str',
        'target_log_stream_name': 'str',
        'target_log_stream_eps_id': 'str',
        'target_log_stream_ttl': 'int'
    }

    attribute_map = {
        'source_log_stream_id': 'source_log_stream_id',
        'target_log_stream_id': 'target_log_stream_id',
        'target_log_stream_name': 'target_log_stream_name',
        'target_log_stream_eps_id': 'target_log_stream_eps_id',
        'target_log_stream_ttl': 'target_log_stream_ttl'
    }

    def __init__(self, source_log_stream_id=None, target_log_stream_id=None, target_log_stream_name=None, target_log_stream_eps_id=None, target_log_stream_ttl=None):
        """LogMappingStreamInfo

        The model defined in huaweicloud sdk

        :param source_log_stream_id: 源日志流ID
        :type source_log_stream_id: str
        :param target_log_stream_id: 目标日志流ID
        :type target_log_stream_id: str
        :param target_log_stream_name: 目标日志流名称
        :type target_log_stream_name: str
        :param target_log_stream_eps_id: 目标日志流EPS ID
        :type target_log_stream_eps_id: str
        :param target_log_stream_ttl: 目标日志流ttl
        :type target_log_stream_ttl: int
        """
        
        

        self._source_log_stream_id = None
        self._target_log_stream_id = None
        self._target_log_stream_name = None
        self._target_log_stream_eps_id = None
        self._target_log_stream_ttl = None
        self.discriminator = None

        self.source_log_stream_id = source_log_stream_id
        if target_log_stream_id is not None:
            self.target_log_stream_id = target_log_stream_id
        self.target_log_stream_name = target_log_stream_name
        if target_log_stream_eps_id is not None:
            self.target_log_stream_eps_id = target_log_stream_eps_id
        self.target_log_stream_ttl = target_log_stream_ttl

    @property
    def source_log_stream_id(self):
        """Gets the source_log_stream_id of this LogMappingStreamInfo.

        源日志流ID

        :return: The source_log_stream_id of this LogMappingStreamInfo.
        :rtype: str
        """
        return self._source_log_stream_id

    @source_log_stream_id.setter
    def source_log_stream_id(self, source_log_stream_id):
        """Sets the source_log_stream_id of this LogMappingStreamInfo.

        源日志流ID

        :param source_log_stream_id: The source_log_stream_id of this LogMappingStreamInfo.
        :type source_log_stream_id: str
        """
        self._source_log_stream_id = source_log_stream_id

    @property
    def target_log_stream_id(self):
        """Gets the target_log_stream_id of this LogMappingStreamInfo.

        目标日志流ID

        :return: The target_log_stream_id of this LogMappingStreamInfo.
        :rtype: str
        """
        return self._target_log_stream_id

    @target_log_stream_id.setter
    def target_log_stream_id(self, target_log_stream_id):
        """Sets the target_log_stream_id of this LogMappingStreamInfo.

        目标日志流ID

        :param target_log_stream_id: The target_log_stream_id of this LogMappingStreamInfo.
        :type target_log_stream_id: str
        """
        self._target_log_stream_id = target_log_stream_id

    @property
    def target_log_stream_name(self):
        """Gets the target_log_stream_name of this LogMappingStreamInfo.

        目标日志流名称

        :return: The target_log_stream_name of this LogMappingStreamInfo.
        :rtype: str
        """
        return self._target_log_stream_name

    @target_log_stream_name.setter
    def target_log_stream_name(self, target_log_stream_name):
        """Sets the target_log_stream_name of this LogMappingStreamInfo.

        目标日志流名称

        :param target_log_stream_name: The target_log_stream_name of this LogMappingStreamInfo.
        :type target_log_stream_name: str
        """
        self._target_log_stream_name = target_log_stream_name

    @property
    def target_log_stream_eps_id(self):
        """Gets the target_log_stream_eps_id of this LogMappingStreamInfo.

        目标日志流EPS ID

        :return: The target_log_stream_eps_id of this LogMappingStreamInfo.
        :rtype: str
        """
        return self._target_log_stream_eps_id

    @target_log_stream_eps_id.setter
    def target_log_stream_eps_id(self, target_log_stream_eps_id):
        """Sets the target_log_stream_eps_id of this LogMappingStreamInfo.

        目标日志流EPS ID

        :param target_log_stream_eps_id: The target_log_stream_eps_id of this LogMappingStreamInfo.
        :type target_log_stream_eps_id: str
        """
        self._target_log_stream_eps_id = target_log_stream_eps_id

    @property
    def target_log_stream_ttl(self):
        """Gets the target_log_stream_ttl of this LogMappingStreamInfo.

        目标日志流ttl

        :return: The target_log_stream_ttl of this LogMappingStreamInfo.
        :rtype: int
        """
        return self._target_log_stream_ttl

    @target_log_stream_ttl.setter
    def target_log_stream_ttl(self, target_log_stream_ttl):
        """Sets the target_log_stream_ttl of this LogMappingStreamInfo.

        目标日志流ttl

        :param target_log_stream_ttl: The target_log_stream_ttl of this LogMappingStreamInfo.
        :type target_log_stream_ttl: int
        """
        self._target_log_stream_ttl = target_log_stream_ttl

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
        if not isinstance(other, LogMappingStreamInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
