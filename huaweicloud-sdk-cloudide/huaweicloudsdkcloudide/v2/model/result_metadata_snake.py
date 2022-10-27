# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResultMetadataSnake:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'metadata_type': 'str',
        'metadata_items': 'list[dict(str, object)]'
    }

    attribute_map = {
        'metadata_type': 'metadata_type',
        'metadata_items': 'metadata_items'
    }

    def __init__(self, metadata_type=None, metadata_items=None):
        """ResultMetadataSnake

        The model defined in huaweicloud sdk

        :param metadata_type: 元数据类型
        :type metadata_type: str
        :param metadata_items: 元数据列表
        :type metadata_items: list[dict(str, object)]
        """
        
        

        self._metadata_type = None
        self._metadata_items = None
        self.discriminator = None

        if metadata_type is not None:
            self.metadata_type = metadata_type
        if metadata_items is not None:
            self.metadata_items = metadata_items

    @property
    def metadata_type(self):
        """Gets the metadata_type of this ResultMetadataSnake.

        元数据类型

        :return: The metadata_type of this ResultMetadataSnake.
        :rtype: str
        """
        return self._metadata_type

    @metadata_type.setter
    def metadata_type(self, metadata_type):
        """Sets the metadata_type of this ResultMetadataSnake.

        元数据类型

        :param metadata_type: The metadata_type of this ResultMetadataSnake.
        :type metadata_type: str
        """
        self._metadata_type = metadata_type

    @property
    def metadata_items(self):
        """Gets the metadata_items of this ResultMetadataSnake.

        元数据列表

        :return: The metadata_items of this ResultMetadataSnake.
        :rtype: list[dict(str, object)]
        """
        return self._metadata_items

    @metadata_items.setter
    def metadata_items(self, metadata_items):
        """Sets the metadata_items of this ResultMetadataSnake.

        元数据列表

        :param metadata_items: The metadata_items of this ResultMetadataSnake.
        :type metadata_items: list[dict(str, object)]
        """
        self._metadata_items = metadata_items

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
        if not isinstance(other, ResultMetadataSnake):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
