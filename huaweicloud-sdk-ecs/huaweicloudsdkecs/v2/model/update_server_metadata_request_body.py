# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateServerMetadataRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metadata': 'dict(str, str)'
    }

    attribute_map = {
        'metadata': 'metadata'
    }

    def __init__(self, metadata=None):
        """UpdateServerMetadataRequestBody

        The model defined in huaweicloud sdk

        :param metadata: 用户自定义metadata键值对。  结构体允许为空，取值为空时不更新数据。  键。最大长度255个Unicode字符，不能为空。可以为大写字母（A-Z）、小写字母（a-z）、数字（0-9）、中划线（-）、下划线（_）、冒号（:）和小数点（.）。  值。最大长度为255个Unicode字符。
        :type metadata: dict(str, str)
        """
        
        

        self._metadata = None
        self.discriminator = None

        self.metadata = metadata

    @property
    def metadata(self):
        """Gets the metadata of this UpdateServerMetadataRequestBody.

        用户自定义metadata键值对。  结构体允许为空，取值为空时不更新数据。  键。最大长度255个Unicode字符，不能为空。可以为大写字母（A-Z）、小写字母（a-z）、数字（0-9）、中划线（-）、下划线（_）、冒号（:）和小数点（.）。  值。最大长度为255个Unicode字符。

        :return: The metadata of this UpdateServerMetadataRequestBody.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this UpdateServerMetadataRequestBody.

        用户自定义metadata键值对。  结构体允许为空，取值为空时不更新数据。  键。最大长度255个Unicode字符，不能为空。可以为大写字母（A-Z）、小写字母（a-z）、数字（0-9）、中划线（-）、下划线（_）、冒号（:）和小数点（.）。  值。最大长度为255个Unicode字符。

        :param metadata: The metadata of this UpdateServerMetadataRequestBody.
        :type metadata: dict(str, str)
        """
        self._metadata = metadata

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
        if not isinstance(other, UpdateServerMetadataRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
