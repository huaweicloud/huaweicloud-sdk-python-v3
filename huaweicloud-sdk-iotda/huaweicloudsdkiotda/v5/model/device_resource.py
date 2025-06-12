# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeviceResource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'device_name': 'ParameterRef',
        'device_id': 'ParameterRef',
        'node_id': 'ParameterRef',
        'product_id': 'object',
        'tags': 'list[TagRef]'
    }

    attribute_map = {
        'device_name': 'device_name',
        'device_id': 'device_id',
        'node_id': 'node_id',
        'product_id': 'product_id',
        'tags': 'tags'
    }

    def __init__(self, device_name=None, device_id=None, node_id=None, product_id=None, tags=None):
        r"""DeviceResource

        The model defined in huaweicloud sdk

        :param device_name: 
        :type device_name: :class:`huaweicloudsdkiotda.v5.ParameterRef`
        :param device_id: 
        :type device_id: :class:`huaweicloudsdkiotda.v5.ParameterRef`
        :param node_id: 
        :type node_id: :class:`huaweicloudsdkiotda.v5.ParameterRef`
        :param product_id: **参数说明**：设备所属的产品id，可以是一个明确的静态字符串id，也可以是动态的模板参数引用 - 明确的静态字符串：\&quot;642bf260f2f9030e44210d8d\&quot;。**取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。\&quot; - 参数引用: {\&quot;ref\&quot; : \&quot;iotda::certificate::country\&quot;}
        :type product_id: object
        :param tags: **参数说明**：设备绑定的标签列表
        :type tags: list[:class:`huaweicloudsdkiotda.v5.TagRef`]
        """
        
        

        self._device_name = None
        self._device_id = None
        self._node_id = None
        self._product_id = None
        self._tags = None
        self.discriminator = None

        if device_name is not None:
            self.device_name = device_name
        if device_id is not None:
            self.device_id = device_id
        self.node_id = node_id
        self.product_id = product_id
        if tags is not None:
            self.tags = tags

    @property
    def device_name(self):
        r"""Gets the device_name of this DeviceResource.

        :return: The device_name of this DeviceResource.
        :rtype: :class:`huaweicloudsdkiotda.v5.ParameterRef`
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        r"""Sets the device_name of this DeviceResource.

        :param device_name: The device_name of this DeviceResource.
        :type device_name: :class:`huaweicloudsdkiotda.v5.ParameterRef`
        """
        self._device_name = device_name

    @property
    def device_id(self):
        r"""Gets the device_id of this DeviceResource.

        :return: The device_id of this DeviceResource.
        :rtype: :class:`huaweicloudsdkiotda.v5.ParameterRef`
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        r"""Sets the device_id of this DeviceResource.

        :param device_id: The device_id of this DeviceResource.
        :type device_id: :class:`huaweicloudsdkiotda.v5.ParameterRef`
        """
        self._device_id = device_id

    @property
    def node_id(self):
        r"""Gets the node_id of this DeviceResource.

        :return: The node_id of this DeviceResource.
        :rtype: :class:`huaweicloudsdkiotda.v5.ParameterRef`
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this DeviceResource.

        :param node_id: The node_id of this DeviceResource.
        :type node_id: :class:`huaweicloudsdkiotda.v5.ParameterRef`
        """
        self._node_id = node_id

    @property
    def product_id(self):
        r"""Gets the product_id of this DeviceResource.

        **参数说明**：设备所属的产品id，可以是一个明确的静态字符串id，也可以是动态的模板参数引用 - 明确的静态字符串：\"642bf260f2f9030e44210d8d\"。**取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。\" - 参数引用: {\"ref\" : \"iotda::certificate::country\"}

        :return: The product_id of this DeviceResource.
        :rtype: object
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this DeviceResource.

        **参数说明**：设备所属的产品id，可以是一个明确的静态字符串id，也可以是动态的模板参数引用 - 明确的静态字符串：\"642bf260f2f9030e44210d8d\"。**取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。\" - 参数引用: {\"ref\" : \"iotda::certificate::country\"}

        :param product_id: The product_id of this DeviceResource.
        :type product_id: object
        """
        self._product_id = product_id

    @property
    def tags(self):
        r"""Gets the tags of this DeviceResource.

        **参数说明**：设备绑定的标签列表

        :return: The tags of this DeviceResource.
        :rtype: list[:class:`huaweicloudsdkiotda.v5.TagRef`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this DeviceResource.

        **参数说明**：设备绑定的标签列表

        :param tags: The tags of this DeviceResource.
        :type tags: list[:class:`huaweicloudsdkiotda.v5.TagRef`]
        """
        self._tags = tags

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
        if not isinstance(other, DeviceResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
