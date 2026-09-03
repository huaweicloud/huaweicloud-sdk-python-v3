# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PingVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'address': 'str',
        'sub_task_name': 'str'
    }

    attribute_map = {
        'address': 'address',
        'sub_task_name': 'sub_task_name'
    }

    def __init__(self, address=None, sub_task_name=None):
        r"""PingVo

        The model defined in huaweicloud sdk

        :param address: ping地址
        :type address: str
        :param sub_task_name: 节点名称
        :type sub_task_name: str
        """
        
        

        self._address = None
        self._sub_task_name = None
        self.discriminator = None

        if address is not None:
            self.address = address
        if sub_task_name is not None:
            self.sub_task_name = sub_task_name

    @property
    def address(self):
        r"""Gets the address of this PingVo.

        ping地址

        :return: The address of this PingVo.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        r"""Sets the address of this PingVo.

        ping地址

        :param address: The address of this PingVo.
        :type address: str
        """
        self._address = address

    @property
    def sub_task_name(self):
        r"""Gets the sub_task_name of this PingVo.

        节点名称

        :return: The sub_task_name of this PingVo.
        :rtype: str
        """
        return self._sub_task_name

    @sub_task_name.setter
    def sub_task_name(self, sub_task_name):
        r"""Sets the sub_task_name of this PingVo.

        节点名称

        :param sub_task_name: The sub_task_name of this PingVo.
        :type sub_task_name: str
        """
        self._sub_task_name = sub_task_name

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
        if not isinstance(other, PingVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
