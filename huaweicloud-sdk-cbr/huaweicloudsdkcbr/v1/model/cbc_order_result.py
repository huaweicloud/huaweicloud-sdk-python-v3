# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CbcOrderResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'cloud_service_id': 'str',
        'order_id': 'str',
        'subscribe_result': 'int',
        'resource_id': 'str'
    }

    attribute_map = {
        'cloud_service_id': 'cloudServiceId',
        'order_id': 'orderId',
        'subscribe_result': 'subscribeResult',
        'resource_id': 'resourceId'
    }

    def __init__(self, cloud_service_id=None, order_id=None, subscribe_result=None, resource_id=None):
        """CbcOrderResult

        The model defined in huaweicloud sdk

        :param cloud_service_id: 云服务ID
        :type cloud_service_id: str
        :param order_id: 订单ID
        :type order_id: str
        :param subscribe_result: 订购结果，1：成功；0：失败
        :type subscribe_result: int
        :param resource_id: 包周期资源预生成资源id。
        :type resource_id: str
        """
        
        

        self._cloud_service_id = None
        self._order_id = None
        self._subscribe_result = None
        self._resource_id = None
        self.discriminator = None

        if cloud_service_id is not None:
            self.cloud_service_id = cloud_service_id
        self.order_id = order_id
        self.subscribe_result = subscribe_result
        if resource_id is not None:
            self.resource_id = resource_id

    @property
    def cloud_service_id(self):
        """Gets the cloud_service_id of this CbcOrderResult.

        云服务ID

        :return: The cloud_service_id of this CbcOrderResult.
        :rtype: str
        """
        return self._cloud_service_id

    @cloud_service_id.setter
    def cloud_service_id(self, cloud_service_id):
        """Sets the cloud_service_id of this CbcOrderResult.

        云服务ID

        :param cloud_service_id: The cloud_service_id of this CbcOrderResult.
        :type cloud_service_id: str
        """
        self._cloud_service_id = cloud_service_id

    @property
    def order_id(self):
        """Gets the order_id of this CbcOrderResult.

        订单ID

        :return: The order_id of this CbcOrderResult.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this CbcOrderResult.

        订单ID

        :param order_id: The order_id of this CbcOrderResult.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def subscribe_result(self):
        """Gets the subscribe_result of this CbcOrderResult.

        订购结果，1：成功；0：失败

        :return: The subscribe_result of this CbcOrderResult.
        :rtype: int
        """
        return self._subscribe_result

    @subscribe_result.setter
    def subscribe_result(self, subscribe_result):
        """Sets the subscribe_result of this CbcOrderResult.

        订购结果，1：成功；0：失败

        :param subscribe_result: The subscribe_result of this CbcOrderResult.
        :type subscribe_result: int
        """
        self._subscribe_result = subscribe_result

    @property
    def resource_id(self):
        """Gets the resource_id of this CbcOrderResult.

        包周期资源预生成资源id。

        :return: The resource_id of this CbcOrderResult.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this CbcOrderResult.

        包周期资源预生成资源id。

        :param resource_id: The resource_id of this CbcOrderResult.
        :type resource_id: str
        """
        self._resource_id = resource_id

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
        if not isinstance(other, CbcOrderResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
