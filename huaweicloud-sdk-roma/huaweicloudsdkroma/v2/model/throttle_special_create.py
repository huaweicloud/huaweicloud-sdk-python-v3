# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ThrottleSpecialCreate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'call_limits': 'int',
        'object_id': 'str',
        'object_type': 'str'
    }

    attribute_map = {
        'call_limits': 'call_limits',
        'object_id': 'object_id',
        'object_type': 'object_type'
    }

    def __init__(self, call_limits=None, object_id=None, object_type=None):
        """ThrottleSpecialCreate

        The model defined in huaweicloud sdk

        :param call_limits: 流控时间内特殊对象能够访问API的最大次数限制
        :type call_limits: int
        :param object_id: 特殊APP的编号[或特殊租户的帐号ID](tag:hws,hws_hk,hcs,hcs_sm,fcs,g42)
        :type object_id: str
        :param object_type: 特殊对象类型
        :type object_type: str
        """
        
        

        self._call_limits = None
        self._object_id = None
        self._object_type = None
        self.discriminator = None

        self.call_limits = call_limits
        self.object_id = object_id
        self.object_type = object_type

    @property
    def call_limits(self):
        """Gets the call_limits of this ThrottleSpecialCreate.

        流控时间内特殊对象能够访问API的最大次数限制

        :return: The call_limits of this ThrottleSpecialCreate.
        :rtype: int
        """
        return self._call_limits

    @call_limits.setter
    def call_limits(self, call_limits):
        """Sets the call_limits of this ThrottleSpecialCreate.

        流控时间内特殊对象能够访问API的最大次数限制

        :param call_limits: The call_limits of this ThrottleSpecialCreate.
        :type call_limits: int
        """
        self._call_limits = call_limits

    @property
    def object_id(self):
        """Gets the object_id of this ThrottleSpecialCreate.

        特殊APP的编号[或特殊租户的帐号ID](tag:hws,hws_hk,hcs,hcs_sm,fcs,g42)

        :return: The object_id of this ThrottleSpecialCreate.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this ThrottleSpecialCreate.

        特殊APP的编号[或特殊租户的帐号ID](tag:hws,hws_hk,hcs,hcs_sm,fcs,g42)

        :param object_id: The object_id of this ThrottleSpecialCreate.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def object_type(self):
        """Gets the object_type of this ThrottleSpecialCreate.

        特殊对象类型

        :return: The object_type of this ThrottleSpecialCreate.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this ThrottleSpecialCreate.

        特殊对象类型

        :param object_type: The object_type of this ThrottleSpecialCreate.
        :type object_type: str
        """
        self._object_type = object_type

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
        if not isinstance(other, ThrottleSpecialCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
