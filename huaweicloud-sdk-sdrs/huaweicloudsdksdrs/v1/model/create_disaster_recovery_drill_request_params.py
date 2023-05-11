# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDisasterRecoveryDrillRequestParams:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_group_id': 'str',
        'drill_vpc_id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'server_group_id': 'server_group_id',
        'drill_vpc_id': 'drill_vpc_id',
        'name': 'name'
    }

    def __init__(self, server_group_id=None, drill_vpc_id=None, name=None):
        """CreateDisasterRecoveryDrillRequestParams

        The model defined in huaweicloud sdk

        :param server_group_id: 保护组的ID。
        :type server_group_id: str
        :param drill_vpc_id: 演练虚拟私有云ID，不指定时系统会自动创建演练VPC。
        :type drill_vpc_id: str
        :param name: 指定容灾演练的名称，最大支持长度为64个字节。只包含中文字符、英文字母（a～ｚ、Ａ～Ｚ）、数字（０~９）、小数点（．）、下划线（_）、中划线（-）。
        :type name: str
        """
        
        

        self._server_group_id = None
        self._drill_vpc_id = None
        self._name = None
        self.discriminator = None

        self.server_group_id = server_group_id
        if drill_vpc_id is not None:
            self.drill_vpc_id = drill_vpc_id
        self.name = name

    @property
    def server_group_id(self):
        """Gets the server_group_id of this CreateDisasterRecoveryDrillRequestParams.

        保护组的ID。

        :return: The server_group_id of this CreateDisasterRecoveryDrillRequestParams.
        :rtype: str
        """
        return self._server_group_id

    @server_group_id.setter
    def server_group_id(self, server_group_id):
        """Sets the server_group_id of this CreateDisasterRecoveryDrillRequestParams.

        保护组的ID。

        :param server_group_id: The server_group_id of this CreateDisasterRecoveryDrillRequestParams.
        :type server_group_id: str
        """
        self._server_group_id = server_group_id

    @property
    def drill_vpc_id(self):
        """Gets the drill_vpc_id of this CreateDisasterRecoveryDrillRequestParams.

        演练虚拟私有云ID，不指定时系统会自动创建演练VPC。

        :return: The drill_vpc_id of this CreateDisasterRecoveryDrillRequestParams.
        :rtype: str
        """
        return self._drill_vpc_id

    @drill_vpc_id.setter
    def drill_vpc_id(self, drill_vpc_id):
        """Sets the drill_vpc_id of this CreateDisasterRecoveryDrillRequestParams.

        演练虚拟私有云ID，不指定时系统会自动创建演练VPC。

        :param drill_vpc_id: The drill_vpc_id of this CreateDisasterRecoveryDrillRequestParams.
        :type drill_vpc_id: str
        """
        self._drill_vpc_id = drill_vpc_id

    @property
    def name(self):
        """Gets the name of this CreateDisasterRecoveryDrillRequestParams.

        指定容灾演练的名称，最大支持长度为64个字节。只包含中文字符、英文字母（a～ｚ、Ａ～Ｚ）、数字（０~９）、小数点（．）、下划线（_）、中划线（-）。

        :return: The name of this CreateDisasterRecoveryDrillRequestParams.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateDisasterRecoveryDrillRequestParams.

        指定容灾演练的名称，最大支持长度为64个字节。只包含中文字符、英文字母（a～ｚ、Ａ～Ｚ）、数字（０~９）、小数点（．）、下划线（_）、中划线（-）。

        :param name: The name of this CreateDisasterRecoveryDrillRequestParams.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, CreateDisasterRecoveryDrillRequestParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
