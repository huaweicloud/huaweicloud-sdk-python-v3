# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSourceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_id': 'int',
        'product_id': 'int',
        'device_id': 'int',
        'topic': 'str',
        'device_name': 'str',
        'product_name': 'str',
        'is_base64': 'int',
        'contain_device_info': 'int'
    }

    attribute_map = {
        'source_id': 'source_id',
        'product_id': 'product_id',
        'device_id': 'device_id',
        'topic': 'topic',
        'device_name': 'device_name',
        'product_name': 'product_name',
        'is_base64': 'is_base64',
        'contain_device_info': 'contain_device_info'
    }

    def __init__(self, source_id=None, product_id=None, device_id=None, topic=None, device_name=None, product_name=None, is_base64=None, contain_device_info=None):
        """CreateSourceResponse

        The model defined in huaweicloud sdk

        :param source_id: 源数据源ID
        :type source_id: int
        :param product_id: 产品ID
        :type product_id: int
        :param device_id: 设备ID，不填为全部设备
        :type device_id: int
        :param topic: 主题，当设备ID为空时为产品级主题，设备ID不为空时为设备级主题
        :type topic: str
        :param device_name: 设备名称
        :type device_name: str
        :param product_name: 产品名称
        :type product_name: str
        :param is_base64: 是否payload使用base64，0-是 1-否
        :type is_base64: int
        :param contain_device_info: 是否包含设备信息，0-是，1-否
        :type contain_device_info: int
        """
        
        super(CreateSourceResponse, self).__init__()

        self._source_id = None
        self._product_id = None
        self._device_id = None
        self._topic = None
        self._device_name = None
        self._product_name = None
        self._is_base64 = None
        self._contain_device_info = None
        self.discriminator = None

        if source_id is not None:
            self.source_id = source_id
        if product_id is not None:
            self.product_id = product_id
        if device_id is not None:
            self.device_id = device_id
        if topic is not None:
            self.topic = topic
        if device_name is not None:
            self.device_name = device_name
        if product_name is not None:
            self.product_name = product_name
        if is_base64 is not None:
            self.is_base64 = is_base64
        if contain_device_info is not None:
            self.contain_device_info = contain_device_info

    @property
    def source_id(self):
        """Gets the source_id of this CreateSourceResponse.

        源数据源ID

        :return: The source_id of this CreateSourceResponse.
        :rtype: int
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """Sets the source_id of this CreateSourceResponse.

        源数据源ID

        :param source_id: The source_id of this CreateSourceResponse.
        :type source_id: int
        """
        self._source_id = source_id

    @property
    def product_id(self):
        """Gets the product_id of this CreateSourceResponse.

        产品ID

        :return: The product_id of this CreateSourceResponse.
        :rtype: int
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this CreateSourceResponse.

        产品ID

        :param product_id: The product_id of this CreateSourceResponse.
        :type product_id: int
        """
        self._product_id = product_id

    @property
    def device_id(self):
        """Gets the device_id of this CreateSourceResponse.

        设备ID，不填为全部设备

        :return: The device_id of this CreateSourceResponse.
        :rtype: int
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this CreateSourceResponse.

        设备ID，不填为全部设备

        :param device_id: The device_id of this CreateSourceResponse.
        :type device_id: int
        """
        self._device_id = device_id

    @property
    def topic(self):
        """Gets the topic of this CreateSourceResponse.

        主题，当设备ID为空时为产品级主题，设备ID不为空时为设备级主题

        :return: The topic of this CreateSourceResponse.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this CreateSourceResponse.

        主题，当设备ID为空时为产品级主题，设备ID不为空时为设备级主题

        :param topic: The topic of this CreateSourceResponse.
        :type topic: str
        """
        self._topic = topic

    @property
    def device_name(self):
        """Gets the device_name of this CreateSourceResponse.

        设备名称

        :return: The device_name of this CreateSourceResponse.
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """Sets the device_name of this CreateSourceResponse.

        设备名称

        :param device_name: The device_name of this CreateSourceResponse.
        :type device_name: str
        """
        self._device_name = device_name

    @property
    def product_name(self):
        """Gets the product_name of this CreateSourceResponse.

        产品名称

        :return: The product_name of this CreateSourceResponse.
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this CreateSourceResponse.

        产品名称

        :param product_name: The product_name of this CreateSourceResponse.
        :type product_name: str
        """
        self._product_name = product_name

    @property
    def is_base64(self):
        """Gets the is_base64 of this CreateSourceResponse.

        是否payload使用base64，0-是 1-否

        :return: The is_base64 of this CreateSourceResponse.
        :rtype: int
        """
        return self._is_base64

    @is_base64.setter
    def is_base64(self, is_base64):
        """Sets the is_base64 of this CreateSourceResponse.

        是否payload使用base64，0-是 1-否

        :param is_base64: The is_base64 of this CreateSourceResponse.
        :type is_base64: int
        """
        self._is_base64 = is_base64

    @property
    def contain_device_info(self):
        """Gets the contain_device_info of this CreateSourceResponse.

        是否包含设备信息，0-是，1-否

        :return: The contain_device_info of this CreateSourceResponse.
        :rtype: int
        """
        return self._contain_device_info

    @contain_device_info.setter
    def contain_device_info(self, contain_device_info):
        """Sets the contain_device_info of this CreateSourceResponse.

        是否包含设备信息，0-是，1-否

        :param contain_device_info: The contain_device_info of this CreateSourceResponse.
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
        if not isinstance(other, CreateSourceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
