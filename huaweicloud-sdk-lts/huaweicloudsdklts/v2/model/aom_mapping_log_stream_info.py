# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AomMappingLogStreamInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target_log_group_id': 'str',
        'target_log_group_name': 'str',
        'target_log_stream_id': 'str',
        'target_log_stream_name': 'str'
    }

    attribute_map = {
        'target_log_group_id': 'target_log_group_id',
        'target_log_group_name': 'target_log_group_name',
        'target_log_stream_id': 'target_log_stream_id',
        'target_log_stream_name': 'target_log_stream_name'
    }

    def __init__(self, target_log_group_id=None, target_log_group_name=None, target_log_stream_id=None, target_log_stream_name=None):
        """AomMappingLogStreamInfo

        The model defined in huaweicloud sdk

        :param target_log_group_id: 日志组id
        :type target_log_group_id: str
        :param target_log_group_name: 目标日志组名称。
        :type target_log_group_name: str
        :param target_log_stream_id: 日志流id
        :type target_log_stream_id: str
        :param target_log_stream_name: 目标日志组名称。
        :type target_log_stream_name: str
        """
        
        

        self._target_log_group_id = None
        self._target_log_group_name = None
        self._target_log_stream_id = None
        self._target_log_stream_name = None
        self.discriminator = None

        self.target_log_group_id = target_log_group_id
        self.target_log_group_name = target_log_group_name
        self.target_log_stream_id = target_log_stream_id
        self.target_log_stream_name = target_log_stream_name

    @property
    def target_log_group_id(self):
        """Gets the target_log_group_id of this AomMappingLogStreamInfo.

        日志组id

        :return: The target_log_group_id of this AomMappingLogStreamInfo.
        :rtype: str
        """
        return self._target_log_group_id

    @target_log_group_id.setter
    def target_log_group_id(self, target_log_group_id):
        """Sets the target_log_group_id of this AomMappingLogStreamInfo.

        日志组id

        :param target_log_group_id: The target_log_group_id of this AomMappingLogStreamInfo.
        :type target_log_group_id: str
        """
        self._target_log_group_id = target_log_group_id

    @property
    def target_log_group_name(self):
        """Gets the target_log_group_name of this AomMappingLogStreamInfo.

        目标日志组名称。

        :return: The target_log_group_name of this AomMappingLogStreamInfo.
        :rtype: str
        """
        return self._target_log_group_name

    @target_log_group_name.setter
    def target_log_group_name(self, target_log_group_name):
        """Sets the target_log_group_name of this AomMappingLogStreamInfo.

        目标日志组名称。

        :param target_log_group_name: The target_log_group_name of this AomMappingLogStreamInfo.
        :type target_log_group_name: str
        """
        self._target_log_group_name = target_log_group_name

    @property
    def target_log_stream_id(self):
        """Gets the target_log_stream_id of this AomMappingLogStreamInfo.

        日志流id

        :return: The target_log_stream_id of this AomMappingLogStreamInfo.
        :rtype: str
        """
        return self._target_log_stream_id

    @target_log_stream_id.setter
    def target_log_stream_id(self, target_log_stream_id):
        """Sets the target_log_stream_id of this AomMappingLogStreamInfo.

        日志流id

        :param target_log_stream_id: The target_log_stream_id of this AomMappingLogStreamInfo.
        :type target_log_stream_id: str
        """
        self._target_log_stream_id = target_log_stream_id

    @property
    def target_log_stream_name(self):
        """Gets the target_log_stream_name of this AomMappingLogStreamInfo.

        目标日志组名称。

        :return: The target_log_stream_name of this AomMappingLogStreamInfo.
        :rtype: str
        """
        return self._target_log_stream_name

    @target_log_stream_name.setter
    def target_log_stream_name(self, target_log_stream_name):
        """Sets the target_log_stream_name of this AomMappingLogStreamInfo.

        目标日志组名称。

        :param target_log_stream_name: The target_log_stream_name of this AomMappingLogStreamInfo.
        :type target_log_stream_name: str
        """
        self._target_log_stream_name = target_log_stream_name

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
        if not isinstance(other, AomMappingLogStreamInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
