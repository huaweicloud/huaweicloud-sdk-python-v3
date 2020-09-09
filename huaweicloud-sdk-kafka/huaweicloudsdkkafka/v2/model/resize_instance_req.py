# coding: utf-8

import pprint
import re

import six





class ResizeInstanceReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'new_spec_code': 'str',
        'new_storage_space': 'int'
    }

    attribute_map = {
        'new_spec_code': 'new_spec_code',
        'new_storage_space': 'new_storage_space'
    }

    def __init__(self, new_spec_code=None, new_storage_space=None):
        """ResizeInstanceReq - a model defined in huaweicloud sdk"""
        
        

        self._new_spec_code = None
        self._new_storage_space = None
        self.discriminator = None

        if new_spec_code is not None:
            self.new_spec_code = new_spec_code
        if new_storage_space is not None:
            self.new_storage_space = new_storage_space

    @property
    def new_spec_code(self):
        """Gets the new_spec_code of this ResizeInstanceReq.

        规格变更后的规格ID。  若只扩展磁盘大小，则规格ID保持和原实例不变。  规格ID请参考[查询实例的扩容规格列表](https://support.huaweicloud.com/api-kafka/ShowInstanceExtendProductInfo.html)接口。

        :return: The new_spec_code of this ResizeInstanceReq.
        :rtype: str
        """
        return self._new_spec_code

    @new_spec_code.setter
    def new_spec_code(self, new_spec_code):
        """Sets the new_spec_code of this ResizeInstanceReq.

        规格变更后的规格ID。  若只扩展磁盘大小，则规格ID保持和原实例不变。  规格ID请参考[查询实例的扩容规格列表](https://support.huaweicloud.com/api-kafka/ShowInstanceExtendProductInfo.html)接口。

        :param new_spec_code: The new_spec_code of this ResizeInstanceReq.
        :type: str
        """
        self._new_spec_code = new_spec_code

    @property
    def new_storage_space(self):
        """Gets the new_storage_space of this ResizeInstanceReq.

        规格变更后的消息存储空间，单位：GB。  若扩展实例基准带宽，则new_storage_space不能低于基准带宽规定的最小磁盘大小。  磁盘空间大小请参考[查询实例的扩容规格列表](https://support.huaweicloud.com/api-kafka/ShowInstanceExtendProductInfo.html)接口。

        :return: The new_storage_space of this ResizeInstanceReq.
        :rtype: int
        """
        return self._new_storage_space

    @new_storage_space.setter
    def new_storage_space(self, new_storage_space):
        """Sets the new_storage_space of this ResizeInstanceReq.

        规格变更后的消息存储空间，单位：GB。  若扩展实例基准带宽，则new_storage_space不能低于基准带宽规定的最小磁盘大小。  磁盘空间大小请参考[查询实例的扩容规格列表](https://support.huaweicloud.com/api-kafka/ShowInstanceExtendProductInfo.html)接口。

        :param new_storage_space: The new_storage_space of this ResizeInstanceReq.
        :type: int
        """
        self._new_storage_space = new_storage_space

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ResizeInstanceReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
