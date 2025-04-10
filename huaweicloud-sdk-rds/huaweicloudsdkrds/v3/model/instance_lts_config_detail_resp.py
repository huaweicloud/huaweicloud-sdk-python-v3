# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceLtsConfigDetailResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'log_type': 'str',
        'lts_group_id': 'str',
        'lts_stream_id': 'str',
        'enabled': 'bool'
    }

    attribute_map = {
        'log_type': 'log_type',
        'lts_group_id': 'lts_group_id',
        'lts_stream_id': 'lts_stream_id',
        'enabled': 'enabled'
    }

    def __init__(self, log_type=None, lts_group_id=None, lts_stream_id=None, enabled=None):
        r"""InstanceLtsConfigDetailResp

        The model defined in huaweicloud sdk

        :param log_type: 日志类型
        :type log_type: str
        :param lts_group_id: 日志组id
        :type lts_group_id: str
        :param lts_stream_id: 日志流id
        :type lts_stream_id: str
        :param enabled: 是否开启上传至lts
        :type enabled: bool
        """
        
        

        self._log_type = None
        self._lts_group_id = None
        self._lts_stream_id = None
        self._enabled = None
        self.discriminator = None

        if log_type is not None:
            self.log_type = log_type
        if lts_group_id is not None:
            self.lts_group_id = lts_group_id
        if lts_stream_id is not None:
            self.lts_stream_id = lts_stream_id
        if enabled is not None:
            self.enabled = enabled

    @property
    def log_type(self):
        r"""Gets the log_type of this InstanceLtsConfigDetailResp.

        日志类型

        :return: The log_type of this InstanceLtsConfigDetailResp.
        :rtype: str
        """
        return self._log_type

    @log_type.setter
    def log_type(self, log_type):
        r"""Sets the log_type of this InstanceLtsConfigDetailResp.

        日志类型

        :param log_type: The log_type of this InstanceLtsConfigDetailResp.
        :type log_type: str
        """
        self._log_type = log_type

    @property
    def lts_group_id(self):
        r"""Gets the lts_group_id of this InstanceLtsConfigDetailResp.

        日志组id

        :return: The lts_group_id of this InstanceLtsConfigDetailResp.
        :rtype: str
        """
        return self._lts_group_id

    @lts_group_id.setter
    def lts_group_id(self, lts_group_id):
        r"""Sets the lts_group_id of this InstanceLtsConfigDetailResp.

        日志组id

        :param lts_group_id: The lts_group_id of this InstanceLtsConfigDetailResp.
        :type lts_group_id: str
        """
        self._lts_group_id = lts_group_id

    @property
    def lts_stream_id(self):
        r"""Gets the lts_stream_id of this InstanceLtsConfigDetailResp.

        日志流id

        :return: The lts_stream_id of this InstanceLtsConfigDetailResp.
        :rtype: str
        """
        return self._lts_stream_id

    @lts_stream_id.setter
    def lts_stream_id(self, lts_stream_id):
        r"""Sets the lts_stream_id of this InstanceLtsConfigDetailResp.

        日志流id

        :param lts_stream_id: The lts_stream_id of this InstanceLtsConfigDetailResp.
        :type lts_stream_id: str
        """
        self._lts_stream_id = lts_stream_id

    @property
    def enabled(self):
        r"""Gets the enabled of this InstanceLtsConfigDetailResp.

        是否开启上传至lts

        :return: The enabled of this InstanceLtsConfigDetailResp.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this InstanceLtsConfigDetailResp.

        是否开启上传至lts

        :param enabled: The enabled of this InstanceLtsConfigDetailResp.
        :type enabled: bool
        """
        self._enabled = enabled

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
        if not isinstance(other, InstanceLtsConfigDetailResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
