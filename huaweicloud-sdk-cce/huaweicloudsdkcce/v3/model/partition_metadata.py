# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PartitionMetadata:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'creation_timestamp': 'str'
    }

    attribute_map = {
        'name': 'name',
        'creation_timestamp': 'creationTimestamp'
    }

    def __init__(self, name=None, creation_timestamp=None):
        r"""PartitionMetadata

        The model defined in huaweicloud sdk

        :param name: 分区名称
        :type name: str
        :param creation_timestamp: 创建时间
        :type creation_timestamp: str
        """
        
        

        self._name = None
        self._creation_timestamp = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if creation_timestamp is not None:
            self.creation_timestamp = creation_timestamp

    @property
    def name(self):
        r"""Gets the name of this PartitionMetadata.

        分区名称

        :return: The name of this PartitionMetadata.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this PartitionMetadata.

        分区名称

        :param name: The name of this PartitionMetadata.
        :type name: str
        """
        self._name = name

    @property
    def creation_timestamp(self):
        r"""Gets the creation_timestamp of this PartitionMetadata.

        创建时间

        :return: The creation_timestamp of this PartitionMetadata.
        :rtype: str
        """
        return self._creation_timestamp

    @creation_timestamp.setter
    def creation_timestamp(self, creation_timestamp):
        r"""Sets the creation_timestamp of this PartitionMetadata.

        创建时间

        :param creation_timestamp: The creation_timestamp of this PartitionMetadata.
        :type creation_timestamp: str
        """
        self._creation_timestamp = creation_timestamp

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
        if not isinstance(other, PartitionMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
