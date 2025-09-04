# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CountdownRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service_type': 'str',
        'resource_id': 'str',
        'reminder_day': 'str'
    }

    attribute_map = {
        'service_type': 'service_type',
        'resource_id': 'resource_id',
        'reminder_day': 'reminder_day'
    }

    def __init__(self, service_type=None, resource_id=None, reminder_day=None):
        r"""CountdownRequestBody

        The model defined in huaweicloud sdk

        :param service_type: **参数解释**： 服务类型。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type service_type: str
        :param resource_id: **参数解释**： 资源id。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type resource_id: str
        :param reminder_day: **参数解释**： 提醒日期。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type reminder_day: str
        """
        
        

        self._service_type = None
        self._resource_id = None
        self._reminder_day = None
        self.discriminator = None

        self.service_type = service_type
        self.resource_id = resource_id
        self.reminder_day = reminder_day

    @property
    def service_type(self):
        r"""Gets the service_type of this CountdownRequestBody.

        **参数解释**： 服务类型。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The service_type of this CountdownRequestBody.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        r"""Sets the service_type of this CountdownRequestBody.

        **参数解释**： 服务类型。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param service_type: The service_type of this CountdownRequestBody.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def resource_id(self):
        r"""Gets the resource_id of this CountdownRequestBody.

        **参数解释**： 资源id。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The resource_id of this CountdownRequestBody.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this CountdownRequestBody.

        **参数解释**： 资源id。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param resource_id: The resource_id of this CountdownRequestBody.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def reminder_day(self):
        r"""Gets the reminder_day of this CountdownRequestBody.

        **参数解释**： 提醒日期。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The reminder_day of this CountdownRequestBody.
        :rtype: str
        """
        return self._reminder_day

    @reminder_day.setter
    def reminder_day(self, reminder_day):
        r"""Sets the reminder_day of this CountdownRequestBody.

        **参数解释**： 提醒日期。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param reminder_day: The reminder_day of this CountdownRequestBody.
        :type reminder_day: str
        """
        self._reminder_day = reminder_day

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
        if not isinstance(other, CountdownRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
