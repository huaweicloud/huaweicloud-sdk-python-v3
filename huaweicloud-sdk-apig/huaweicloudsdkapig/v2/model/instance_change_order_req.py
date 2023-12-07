# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceChangeOrderReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'product_id': 'str',
        'resize_info': 'ResizeInstanceReq'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'product_id': 'product_id',
        'resize_info': 'resize_info'
    }

    def __init__(self, instance_id=None, product_id=None, resize_info=None):
        """InstanceChangeOrderReq

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param product_id: 产品编号
        :type product_id: str
        :param resize_info: 
        :type resize_info: :class:`huaweicloudsdkapig.v2.ResizeInstanceReq`
        """
        
        

        self._instance_id = None
        self._product_id = None
        self._resize_info = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if product_id is not None:
            self.product_id = product_id
        if resize_info is not None:
            self.resize_info = resize_info

    @property
    def instance_id(self):
        """Gets the instance_id of this InstanceChangeOrderReq.

        实例ID

        :return: The instance_id of this InstanceChangeOrderReq.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this InstanceChangeOrderReq.

        实例ID

        :param instance_id: The instance_id of this InstanceChangeOrderReq.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def product_id(self):
        """Gets the product_id of this InstanceChangeOrderReq.

        产品编号

        :return: The product_id of this InstanceChangeOrderReq.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this InstanceChangeOrderReq.

        产品编号

        :param product_id: The product_id of this InstanceChangeOrderReq.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def resize_info(self):
        """Gets the resize_info of this InstanceChangeOrderReq.

        :return: The resize_info of this InstanceChangeOrderReq.
        :rtype: :class:`huaweicloudsdkapig.v2.ResizeInstanceReq`
        """
        return self._resize_info

    @resize_info.setter
    def resize_info(self, resize_info):
        """Sets the resize_info of this InstanceChangeOrderReq.

        :param resize_info: The resize_info of this InstanceChangeOrderReq.
        :type resize_info: :class:`huaweicloudsdkapig.v2.ResizeInstanceReq`
        """
        self._resize_info = resize_info

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
        if not isinstance(other, InstanceChangeOrderReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
