# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowStatusInstanceItemInstanceList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_name': 'str',
        'value': 'int'
    }

    attribute_map = {
        'instance_name': 'instance_name',
        'value': 'value'
    }

    def __init__(self, instance_name=None, value=None):
        r"""ShowStatusInstanceItemInstanceList

        The model defined in huaweicloud sdk

        :param instance_name: 实例名称
        :type instance_name: str
        :param value: 采集值
        :type value: int
        """
        
        

        self._instance_name = None
        self._value = None
        self.discriminator = None

        if instance_name is not None:
            self.instance_name = instance_name
        if value is not None:
            self.value = value

    @property
    def instance_name(self):
        r"""Gets the instance_name of this ShowStatusInstanceItemInstanceList.

        实例名称

        :return: The instance_name of this ShowStatusInstanceItemInstanceList.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this ShowStatusInstanceItemInstanceList.

        实例名称

        :param instance_name: The instance_name of this ShowStatusInstanceItemInstanceList.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def value(self):
        r"""Gets the value of this ShowStatusInstanceItemInstanceList.

        采集值

        :return: The value of this ShowStatusInstanceItemInstanceList.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this ShowStatusInstanceItemInstanceList.

        采集值

        :param value: The value of this ShowStatusInstanceItemInstanceList.
        :type value: int
        """
        self._value = value

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
        if not isinstance(other, ShowStatusInstanceItemInstanceList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
