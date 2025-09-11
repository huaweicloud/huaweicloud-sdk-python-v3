# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceSaveLtsConfigOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'log_type': 'str',
        'lts_group_id': 'str',
        'lts_stream_id': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'log_type': 'log_type',
        'lts_group_id': 'lts_group_id',
        'lts_stream_id': 'lts_stream_id'
    }

    def __init__(self, instance_id=None, log_type=None, lts_group_id=None, lts_stream_id=None):
        r"""InstanceSaveLtsConfigOption

        The model defined in huaweicloud sdk

        :param instance_id: **参数解释**: 实例ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type instance_id: str
        :param log_type: **参数解释**: 日志类型。 **约束限制**: 不涉及。 **取值范围**: - audit_log：审计日志。  **默认取值**: 不涉及。
        :type log_type: str
        :param lts_group_id: **参数解释**: LTS日志组ID。 **约束限制**: 不涉及。 **取值范围**: 可通过云日志服务-\&quot;查询账号下所有日志组\&quot;API接口获取。 **默认取值**: 不涉及。
        :type lts_group_id: str
        :param lts_stream_id: **参数解释**: LTS日志流ID。 **约束限制**: 不涉及。 **取值范围**: 可通过云日志服务-”查询指定日志组下的所有日志流“API接口获取。 **默认取值**: 不涉及。
        :type lts_stream_id: str
        """
        
        

        self._instance_id = None
        self._log_type = None
        self._lts_group_id = None
        self._lts_stream_id = None
        self.discriminator = None

        self.instance_id = instance_id
        self.log_type = log_type
        self.lts_group_id = lts_group_id
        self.lts_stream_id = lts_stream_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this InstanceSaveLtsConfigOption.

        **参数解释**: 实例ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The instance_id of this InstanceSaveLtsConfigOption.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this InstanceSaveLtsConfigOption.

        **参数解释**: 实例ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param instance_id: The instance_id of this InstanceSaveLtsConfigOption.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def log_type(self):
        r"""Gets the log_type of this InstanceSaveLtsConfigOption.

        **参数解释**: 日志类型。 **约束限制**: 不涉及。 **取值范围**: - audit_log：审计日志。  **默认取值**: 不涉及。

        :return: The log_type of this InstanceSaveLtsConfigOption.
        :rtype: str
        """
        return self._log_type

    @log_type.setter
    def log_type(self, log_type):
        r"""Sets the log_type of this InstanceSaveLtsConfigOption.

        **参数解释**: 日志类型。 **约束限制**: 不涉及。 **取值范围**: - audit_log：审计日志。  **默认取值**: 不涉及。

        :param log_type: The log_type of this InstanceSaveLtsConfigOption.
        :type log_type: str
        """
        self._log_type = log_type

    @property
    def lts_group_id(self):
        r"""Gets the lts_group_id of this InstanceSaveLtsConfigOption.

        **参数解释**: LTS日志组ID。 **约束限制**: 不涉及。 **取值范围**: 可通过云日志服务-\"查询账号下所有日志组\"API接口获取。 **默认取值**: 不涉及。

        :return: The lts_group_id of this InstanceSaveLtsConfigOption.
        :rtype: str
        """
        return self._lts_group_id

    @lts_group_id.setter
    def lts_group_id(self, lts_group_id):
        r"""Sets the lts_group_id of this InstanceSaveLtsConfigOption.

        **参数解释**: LTS日志组ID。 **约束限制**: 不涉及。 **取值范围**: 可通过云日志服务-\"查询账号下所有日志组\"API接口获取。 **默认取值**: 不涉及。

        :param lts_group_id: The lts_group_id of this InstanceSaveLtsConfigOption.
        :type lts_group_id: str
        """
        self._lts_group_id = lts_group_id

    @property
    def lts_stream_id(self):
        r"""Gets the lts_stream_id of this InstanceSaveLtsConfigOption.

        **参数解释**: LTS日志流ID。 **约束限制**: 不涉及。 **取值范围**: 可通过云日志服务-”查询指定日志组下的所有日志流“API接口获取。 **默认取值**: 不涉及。

        :return: The lts_stream_id of this InstanceSaveLtsConfigOption.
        :rtype: str
        """
        return self._lts_stream_id

    @lts_stream_id.setter
    def lts_stream_id(self, lts_stream_id):
        r"""Sets the lts_stream_id of this InstanceSaveLtsConfigOption.

        **参数解释**: LTS日志流ID。 **约束限制**: 不涉及。 **取值范围**: 可通过云日志服务-”查询指定日志组下的所有日志流“API接口获取。 **默认取值**: 不涉及。

        :param lts_stream_id: The lts_stream_id of this InstanceSaveLtsConfigOption.
        :type lts_stream_id: str
        """
        self._lts_stream_id = lts_stream_id

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
        if not isinstance(other, InstanceSaveLtsConfigOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
