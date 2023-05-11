# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeSqlLimitSwitchStatusBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'switch_status': 'str',
        'datastore_type': 'str'
    }

    attribute_map = {
        'switch_status': 'switch_status',
        'datastore_type': 'datastore_type'
    }

    def __init__(self, switch_status=None, datastore_type=None):
        """ChangeSqlLimitSwitchStatusBody

        The model defined in huaweicloud sdk

        :param switch_status: 开关状态
        :type switch_status: str
        :param datastore_type: 数据库类型
        :type datastore_type: str
        """
        
        

        self._switch_status = None
        self._datastore_type = None
        self.discriminator = None

        self.switch_status = switch_status
        self.datastore_type = datastore_type

    @property
    def switch_status(self):
        """Gets the switch_status of this ChangeSqlLimitSwitchStatusBody.

        开关状态

        :return: The switch_status of this ChangeSqlLimitSwitchStatusBody.
        :rtype: str
        """
        return self._switch_status

    @switch_status.setter
    def switch_status(self, switch_status):
        """Sets the switch_status of this ChangeSqlLimitSwitchStatusBody.

        开关状态

        :param switch_status: The switch_status of this ChangeSqlLimitSwitchStatusBody.
        :type switch_status: str
        """
        self._switch_status = switch_status

    @property
    def datastore_type(self):
        """Gets the datastore_type of this ChangeSqlLimitSwitchStatusBody.

        数据库类型

        :return: The datastore_type of this ChangeSqlLimitSwitchStatusBody.
        :rtype: str
        """
        return self._datastore_type

    @datastore_type.setter
    def datastore_type(self, datastore_type):
        """Sets the datastore_type of this ChangeSqlLimitSwitchStatusBody.

        数据库类型

        :param datastore_type: The datastore_type of this ChangeSqlLimitSwitchStatusBody.
        :type datastore_type: str
        """
        self._datastore_type = datastore_type

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
        if not isinstance(other, ChangeSqlLimitSwitchStatusBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
