# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServiceStatusItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service_name': 'str',
        'status': 'bool'
    }

    attribute_map = {
        'service_name': 'service_name',
        'status': 'status'
    }

    def __init__(self, service_name=None, status=None):
        r"""ServiceStatusItem

        The model defined in huaweicloud sdk

        :param service_name: **参数解释**：服务编码。 **取值范围**：长度限制64个字符。
        :type service_name: str
        :param status: **参数解释**：服务开通状态。 **取值范围**：不涉及。 - true：已开通。 - false：未开通。
        :type status: bool
        """
        
        

        self._service_name = None
        self._status = None
        self.discriminator = None

        self.service_name = service_name
        self.status = status

    @property
    def service_name(self):
        r"""Gets the service_name of this ServiceStatusItem.

        **参数解释**：服务编码。 **取值范围**：长度限制64个字符。

        :return: The service_name of this ServiceStatusItem.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        r"""Sets the service_name of this ServiceStatusItem.

        **参数解释**：服务编码。 **取值范围**：长度限制64个字符。

        :param service_name: The service_name of this ServiceStatusItem.
        :type service_name: str
        """
        self._service_name = service_name

    @property
    def status(self):
        r"""Gets the status of this ServiceStatusItem.

        **参数解释**：服务开通状态。 **取值范围**：不涉及。 - true：已开通。 - false：未开通。

        :return: The status of this ServiceStatusItem.
        :rtype: bool
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ServiceStatusItem.

        **参数解释**：服务开通状态。 **取值范围**：不涉及。 - true：已开通。 - false：未开通。

        :param status: The status of this ServiceStatusItem.
        :type status: bool
        """
        self._status = status

    def to_dict(self):
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
        if not isinstance(other, ServiceStatusItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
