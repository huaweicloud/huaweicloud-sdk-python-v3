# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRecycleInstancesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'retention_days': 'int',
        'default_use_recycle': 'bool',
        'recycle_instances': 'list[InstanceRecycleInfo]'
    }

    attribute_map = {
        'retention_days': 'retention_days',
        'default_use_recycle': 'default_use_recycle',
        'recycle_instances': 'recycle_instances'
    }

    def __init__(self, retention_days=None, default_use_recycle=None, recycle_instances=None):
        r"""ShowRecycleInstancesResponse

        The model defined in huaweicloud sdk

        :param retention_days: **参数解释**： 保留天数。 **取值范围**： 1~7天。
        :type retention_days: int
        :param default_use_recycle: **参数解释**： 是否使用回收站。 **取值范围**： - true：使用回收站。 - false：不使用回收站。
        :type default_use_recycle: bool
        :param recycle_instances: **参数解释**： 回收实例列表。
        :type recycle_instances: list[:class:`huaweicloudsdkkafka.v2.InstanceRecycleInfo`]
        """
        
        super().__init__()

        self._retention_days = None
        self._default_use_recycle = None
        self._recycle_instances = None
        self.discriminator = None

        if retention_days is not None:
            self.retention_days = retention_days
        if default_use_recycle is not None:
            self.default_use_recycle = default_use_recycle
        if recycle_instances is not None:
            self.recycle_instances = recycle_instances

    @property
    def retention_days(self):
        r"""Gets the retention_days of this ShowRecycleInstancesResponse.

        **参数解释**： 保留天数。 **取值范围**： 1~7天。

        :return: The retention_days of this ShowRecycleInstancesResponse.
        :rtype: int
        """
        return self._retention_days

    @retention_days.setter
    def retention_days(self, retention_days):
        r"""Sets the retention_days of this ShowRecycleInstancesResponse.

        **参数解释**： 保留天数。 **取值范围**： 1~7天。

        :param retention_days: The retention_days of this ShowRecycleInstancesResponse.
        :type retention_days: int
        """
        self._retention_days = retention_days

    @property
    def default_use_recycle(self):
        r"""Gets the default_use_recycle of this ShowRecycleInstancesResponse.

        **参数解释**： 是否使用回收站。 **取值范围**： - true：使用回收站。 - false：不使用回收站。

        :return: The default_use_recycle of this ShowRecycleInstancesResponse.
        :rtype: bool
        """
        return self._default_use_recycle

    @default_use_recycle.setter
    def default_use_recycle(self, default_use_recycle):
        r"""Sets the default_use_recycle of this ShowRecycleInstancesResponse.

        **参数解释**： 是否使用回收站。 **取值范围**： - true：使用回收站。 - false：不使用回收站。

        :param default_use_recycle: The default_use_recycle of this ShowRecycleInstancesResponse.
        :type default_use_recycle: bool
        """
        self._default_use_recycle = default_use_recycle

    @property
    def recycle_instances(self):
        r"""Gets the recycle_instances of this ShowRecycleInstancesResponse.

        **参数解释**： 回收实例列表。

        :return: The recycle_instances of this ShowRecycleInstancesResponse.
        :rtype: list[:class:`huaweicloudsdkkafka.v2.InstanceRecycleInfo`]
        """
        return self._recycle_instances

    @recycle_instances.setter
    def recycle_instances(self, recycle_instances):
        r"""Sets the recycle_instances of this ShowRecycleInstancesResponse.

        **参数解释**： 回收实例列表。

        :param recycle_instances: The recycle_instances of this ShowRecycleInstancesResponse.
        :type recycle_instances: list[:class:`huaweicloudsdkkafka.v2.InstanceRecycleInfo`]
        """
        self._recycle_instances = recycle_instances

    def to_dict(self):
        import warnings
        warnings.warn("ShowRecycleInstancesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowRecycleInstancesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
