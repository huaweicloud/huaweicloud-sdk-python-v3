# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMonitorItemDetailRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'monitor_item_id': 'int',
        'env_id': 'int',
        'x_business_id': 'int'
    }

    attribute_map = {
        'monitor_item_id': 'monitor_item_id',
        'env_id': 'env_id',
        'x_business_id': 'x-business-id'
    }

    def __init__(self, monitor_item_id=None, env_id=None, x_business_id=None):
        r"""ShowMonitorItemDetailRequest

        The model defined in huaweicloud sdk

        :param monitor_item_id: 监控项ID
        :type monitor_item_id: int
        :param env_id: 环境ID
        :type env_id: int
        :param x_business_id: 
        :type x_business_id: int
        """
        
        

        self._monitor_item_id = None
        self._env_id = None
        self._x_business_id = None
        self.discriminator = None

        self.monitor_item_id = monitor_item_id
        self.env_id = env_id
        self.x_business_id = x_business_id

    @property
    def monitor_item_id(self):
        r"""Gets the monitor_item_id of this ShowMonitorItemDetailRequest.

        监控项ID

        :return: The monitor_item_id of this ShowMonitorItemDetailRequest.
        :rtype: int
        """
        return self._monitor_item_id

    @monitor_item_id.setter
    def monitor_item_id(self, monitor_item_id):
        r"""Sets the monitor_item_id of this ShowMonitorItemDetailRequest.

        监控项ID

        :param monitor_item_id: The monitor_item_id of this ShowMonitorItemDetailRequest.
        :type monitor_item_id: int
        """
        self._monitor_item_id = monitor_item_id

    @property
    def env_id(self):
        r"""Gets the env_id of this ShowMonitorItemDetailRequest.

        环境ID

        :return: The env_id of this ShowMonitorItemDetailRequest.
        :rtype: int
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        r"""Sets the env_id of this ShowMonitorItemDetailRequest.

        环境ID

        :param env_id: The env_id of this ShowMonitorItemDetailRequest.
        :type env_id: int
        """
        self._env_id = env_id

    @property
    def x_business_id(self):
        r"""Gets the x_business_id of this ShowMonitorItemDetailRequest.

        :return: The x_business_id of this ShowMonitorItemDetailRequest.
        :rtype: int
        """
        return self._x_business_id

    @x_business_id.setter
    def x_business_id(self, x_business_id):
        r"""Sets the x_business_id of this ShowMonitorItemDetailRequest.

        :param x_business_id: The x_business_id of this ShowMonitorItemDetailRequest.
        :type x_business_id: int
        """
        self._x_business_id = x_business_id

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
        if not isinstance(other, ShowMonitorItemDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
