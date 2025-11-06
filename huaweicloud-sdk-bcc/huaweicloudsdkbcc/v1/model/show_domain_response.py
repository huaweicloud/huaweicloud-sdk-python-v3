# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDomainResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enabled': 'bool',
        'data_sync_finished': 'bool',
        'data_sync_percent': 'int',
        'resource_level_created': 'bool',
        'backup_compliance_rule_created': 'bool',
        'backup_compliance_rule_bound': 'bool'
    }

    attribute_map = {
        'enabled': 'enabled',
        'data_sync_finished': 'data_sync_finished',
        'data_sync_percent': 'data_sync_percent',
        'resource_level_created': 'resource_level_created',
        'backup_compliance_rule_created': 'backup_compliance_rule_created',
        'backup_compliance_rule_bound': 'backup_compliance_rule_bound'
    }

    def __init__(self, enabled=None, data_sync_finished=None, data_sync_percent=None, resource_level_created=None, backup_compliance_rule_created=None, backup_compliance_rule_bound=None):
        r"""ShowDomainResponse

        The model defined in huaweicloud sdk

        :param enabled: 是否完成启用
        :type enabled: bool
        :param data_sync_finished: 数据是否同步完成
        :type data_sync_finished: bool
        :param data_sync_percent: 数据同步进度百分比，只有data_sync_finished为false时才有值
        :type data_sync_percent: int
        :param resource_level_created: 是否创建资源等级
        :type resource_level_created: bool
        :param backup_compliance_rule_created: 是否创建合规规则
        :type backup_compliance_rule_created: bool
        :param backup_compliance_rule_bound: 是否绑定合规规则
        :type backup_compliance_rule_bound: bool
        """
        
        super().__init__()

        self._enabled = None
        self._data_sync_finished = None
        self._data_sync_percent = None
        self._resource_level_created = None
        self._backup_compliance_rule_created = None
        self._backup_compliance_rule_bound = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if data_sync_finished is not None:
            self.data_sync_finished = data_sync_finished
        if data_sync_percent is not None:
            self.data_sync_percent = data_sync_percent
        if resource_level_created is not None:
            self.resource_level_created = resource_level_created
        if backup_compliance_rule_created is not None:
            self.backup_compliance_rule_created = backup_compliance_rule_created
        if backup_compliance_rule_bound is not None:
            self.backup_compliance_rule_bound = backup_compliance_rule_bound

    @property
    def enabled(self):
        r"""Gets the enabled of this ShowDomainResponse.

        是否完成启用

        :return: The enabled of this ShowDomainResponse.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this ShowDomainResponse.

        是否完成启用

        :param enabled: The enabled of this ShowDomainResponse.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def data_sync_finished(self):
        r"""Gets the data_sync_finished of this ShowDomainResponse.

        数据是否同步完成

        :return: The data_sync_finished of this ShowDomainResponse.
        :rtype: bool
        """
        return self._data_sync_finished

    @data_sync_finished.setter
    def data_sync_finished(self, data_sync_finished):
        r"""Sets the data_sync_finished of this ShowDomainResponse.

        数据是否同步完成

        :param data_sync_finished: The data_sync_finished of this ShowDomainResponse.
        :type data_sync_finished: bool
        """
        self._data_sync_finished = data_sync_finished

    @property
    def data_sync_percent(self):
        r"""Gets the data_sync_percent of this ShowDomainResponse.

        数据同步进度百分比，只有data_sync_finished为false时才有值

        :return: The data_sync_percent of this ShowDomainResponse.
        :rtype: int
        """
        return self._data_sync_percent

    @data_sync_percent.setter
    def data_sync_percent(self, data_sync_percent):
        r"""Sets the data_sync_percent of this ShowDomainResponse.

        数据同步进度百分比，只有data_sync_finished为false时才有值

        :param data_sync_percent: The data_sync_percent of this ShowDomainResponse.
        :type data_sync_percent: int
        """
        self._data_sync_percent = data_sync_percent

    @property
    def resource_level_created(self):
        r"""Gets the resource_level_created of this ShowDomainResponse.

        是否创建资源等级

        :return: The resource_level_created of this ShowDomainResponse.
        :rtype: bool
        """
        return self._resource_level_created

    @resource_level_created.setter
    def resource_level_created(self, resource_level_created):
        r"""Sets the resource_level_created of this ShowDomainResponse.

        是否创建资源等级

        :param resource_level_created: The resource_level_created of this ShowDomainResponse.
        :type resource_level_created: bool
        """
        self._resource_level_created = resource_level_created

    @property
    def backup_compliance_rule_created(self):
        r"""Gets the backup_compliance_rule_created of this ShowDomainResponse.

        是否创建合规规则

        :return: The backup_compliance_rule_created of this ShowDomainResponse.
        :rtype: bool
        """
        return self._backup_compliance_rule_created

    @backup_compliance_rule_created.setter
    def backup_compliance_rule_created(self, backup_compliance_rule_created):
        r"""Sets the backup_compliance_rule_created of this ShowDomainResponse.

        是否创建合规规则

        :param backup_compliance_rule_created: The backup_compliance_rule_created of this ShowDomainResponse.
        :type backup_compliance_rule_created: bool
        """
        self._backup_compliance_rule_created = backup_compliance_rule_created

    @property
    def backup_compliance_rule_bound(self):
        r"""Gets the backup_compliance_rule_bound of this ShowDomainResponse.

        是否绑定合规规则

        :return: The backup_compliance_rule_bound of this ShowDomainResponse.
        :rtype: bool
        """
        return self._backup_compliance_rule_bound

    @backup_compliance_rule_bound.setter
    def backup_compliance_rule_bound(self, backup_compliance_rule_bound):
        r"""Sets the backup_compliance_rule_bound of this ShowDomainResponse.

        是否绑定合规规则

        :param backup_compliance_rule_bound: The backup_compliance_rule_bound of this ShowDomainResponse.
        :type backup_compliance_rule_bound: bool
        """
        self._backup_compliance_rule_bound = backup_compliance_rule_bound

    def to_dict(self):
        import warnings
        warnings.warn("ShowDomainResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowDomainResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
