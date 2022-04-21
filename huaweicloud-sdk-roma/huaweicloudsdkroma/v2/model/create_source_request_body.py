# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSourceRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'product_id': 'int',
        'device_id': 'int',
        'topic': 'str',
        'is_base64': 'int',
        'contain_device_info': 'int'
    }

    attribute_map = {
        'product_id': 'product_id',
        'device_id': 'device_id',
        'topic': 'topic',
        'is_base64': 'is_base64',
        'contain_device_info': 'contain_device_info'
    }

    def __init__(self, product_id=None, device_id=None, topic=None, is_base64=None, contain_device_info=None):
        """CreateSourceRequestBody

        The model defined in huaweicloud sdk

        :param product_id: 产品ID，自动向下取整
        :type product_id: int
        :param device_id: 设备ID，自动向下取整，不填为全部设备
        :type device_id: int
        :param topic: 主题，当设备ID为空时为产品级主题，设备ID不为空时为设备级主题
        :type topic: str
        :param is_base64: 是否payload使用base64，0-是 1-否
        :type is_base64: int
        :param contain_device_info: 是否包含设备信息是否包含设备信息，0-是 1-否
        :type contain_device_info: int
        """
        
        

        self._product_id = None
        self._device_id = None
        self._topic = None
        self._is_base64 = None
        self._contain_device_info = None
        self.discriminator = None

        self.product_id = product_id
        if device_id is not None:
            self.device_id = device_id
        self.topic = topic
        if is_base64 is not None:
            self.is_base64 = is_base64
        if contain_device_info is not None:
            self.contain_device_info = contain_device_info

    @property
    def product_id(self):
        """Gets the product_id of this CreateSourceRequestBody.

        产品ID，自动向下取整

        :return: The product_id of this CreateSourceRequestBody.
        :rtype: int
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this CreateSourceRequestBody.

        产品ID，自动向下取整

        :param product_id: The product_id of this CreateSourceRequestBody.
        :type product_id: int
        """
        self._product_id = product_id

    @property
    def device_id(self):
        """Gets the device_id of this CreateSourceRequestBody.

        设备ID，自动向下取整，不填为全部设备

        :return: The device_id of this CreateSourceRequestBody.
        :rtype: int
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this CreateSourceRequestBody.

        设备ID，自动向下取整，不填为全部设备

        :param device_id: The device_id of this CreateSourceRequestBody.
        :type device_id: int
        """
        self._device_id = device_id

    @property
    def topic(self):
        """Gets the topic of this CreateSourceRequestBody.

        主题，当设备ID为空时为产品级主题，设备ID不为空时为设备级主题

        :return: The topic of this CreateSourceRequestBody.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this CreateSourceRequestBody.

        主题，当设备ID为空时为产品级主题，设备ID不为空时为设备级主题

        :param topic: The topic of this CreateSourceRequestBody.
        :type topic: str
        """
        self._topic = topic

    @property
    def is_base64(self):
        """Gets the is_base64 of this CreateSourceRequestBody.

        是否payload使用base64，0-是 1-否

        :return: The is_base64 of this CreateSourceRequestBody.
        :rtype: int
        """
        return self._is_base64

    @is_base64.setter
    def is_base64(self, is_base64):
        """Sets the is_base64 of this CreateSourceRequestBody.

        是否payload使用base64，0-是 1-否

        :param is_base64: The is_base64 of this CreateSourceRequestBody.
        :type is_base64: int
        """
        self._is_base64 = is_base64

    @property
    def contain_device_info(self):
        """Gets the contain_device_info of this CreateSourceRequestBody.

        是否包含设备信息是否包含设备信息，0-是 1-否

        :return: The contain_device_info of this CreateSourceRequestBody.
        :rtype: int
        """
        return self._contain_device_info

    @contain_device_info.setter
    def contain_device_info(self, contain_device_info):
        """Sets the contain_device_info of this CreateSourceRequestBody.

        是否包含设备信息是否包含设备信息，0-是 1-否

        :param contain_device_info: The contain_device_info of this CreateSourceRequestBody.
        :type contain_device_info: int
        """
        self._contain_device_info = contain_device_info

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
        if not isinstance(other, CreateSourceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
