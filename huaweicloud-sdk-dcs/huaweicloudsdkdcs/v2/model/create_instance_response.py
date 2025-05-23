# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateInstanceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'order_id': 'str',
        'instances': 'list[Instances]'
    }

    attribute_map = {
        'order_id': 'order_id',
        'instances': 'instances'
    }

    def __init__(self, order_id=None, instances=None):
        r"""CreateInstanceResponse

        The model defined in huaweicloud sdk

        :param order_id: 订单ID，仅在创建包周期实例时返回。
        :type order_id: str
        :param instances: 缓存实例ID和名称，如果批量创建实例，则会返回多个。
        :type instances: list[:class:`huaweicloudsdkdcs.v2.Instances`]
        """
        
        super(CreateInstanceResponse, self).__init__()

        self._order_id = None
        self._instances = None
        self.discriminator = None

        if order_id is not None:
            self.order_id = order_id
        if instances is not None:
            self.instances = instances

    @property
    def order_id(self):
        r"""Gets the order_id of this CreateInstanceResponse.

        订单ID，仅在创建包周期实例时返回。

        :return: The order_id of this CreateInstanceResponse.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this CreateInstanceResponse.

        订单ID，仅在创建包周期实例时返回。

        :param order_id: The order_id of this CreateInstanceResponse.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def instances(self):
        r"""Gets the instances of this CreateInstanceResponse.

        缓存实例ID和名称，如果批量创建实例，则会返回多个。

        :return: The instances of this CreateInstanceResponse.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.Instances`]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        r"""Sets the instances of this CreateInstanceResponse.

        缓存实例ID和名称，如果批量创建实例，则会返回多个。

        :param instances: The instances of this CreateInstanceResponse.
        :type instances: list[:class:`huaweicloudsdkdcs.v2.Instances`]
        """
        self._instances = instances

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
        if not isinstance(other, CreateInstanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
