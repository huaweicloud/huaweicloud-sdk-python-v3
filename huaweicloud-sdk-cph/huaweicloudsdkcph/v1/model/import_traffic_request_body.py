# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportTrafficRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'traffic_type': 'str',
        'phone_ids': 'list[str]'
    }

    attribute_map = {
        'traffic_type': 'traffic_type',
        'phone_ids': 'phone_ids'
    }

    def __init__(self, traffic_type=None, phone_ids=None):
        """ImportTrafficRequestBody

        The model defined in huaweicloud sdk

        :param traffic_type: 手机路由类型。 - direct：默认路由 - routing：路由到编码容器
        :type traffic_type: str
        :param phone_ids: 手机id列表，一次调用最多支持100个。
        :type phone_ids: list[str]
        """
        
        

        self._traffic_type = None
        self._phone_ids = None
        self.discriminator = None

        self.traffic_type = traffic_type
        self.phone_ids = phone_ids

    @property
    def traffic_type(self):
        """Gets the traffic_type of this ImportTrafficRequestBody.

        手机路由类型。 - direct：默认路由 - routing：路由到编码容器

        :return: The traffic_type of this ImportTrafficRequestBody.
        :rtype: str
        """
        return self._traffic_type

    @traffic_type.setter
    def traffic_type(self, traffic_type):
        """Sets the traffic_type of this ImportTrafficRequestBody.

        手机路由类型。 - direct：默认路由 - routing：路由到编码容器

        :param traffic_type: The traffic_type of this ImportTrafficRequestBody.
        :type traffic_type: str
        """
        self._traffic_type = traffic_type

    @property
    def phone_ids(self):
        """Gets the phone_ids of this ImportTrafficRequestBody.

        手机id列表，一次调用最多支持100个。

        :return: The phone_ids of this ImportTrafficRequestBody.
        :rtype: list[str]
        """
        return self._phone_ids

    @phone_ids.setter
    def phone_ids(self, phone_ids):
        """Sets the phone_ids of this ImportTrafficRequestBody.

        手机id列表，一次调用最多支持100个。

        :param phone_ids: The phone_ids of this ImportTrafficRequestBody.
        :type phone_ids: list[str]
        """
        self._phone_ids = phone_ids

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
        if not isinstance(other, ImportTrafficRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
