# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TagOperationDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'object_id': 'str',
        'tag_id': 'str'
    }

    attribute_map = {
        'object_id': 'objectId',
        'tag_id': 'tagId'
    }

    def __init__(self, object_id=None, tag_id=None):
        """TagOperationDTO

        The model defined in huaweicloud sdk

        :param object_id: 数据实例ID。
        :type object_id: str
        :param tag_id: 标签ID。
        :type tag_id: str
        """
        
        

        self._object_id = None
        self._tag_id = None
        self.discriminator = None

        self.object_id = object_id
        self.tag_id = tag_id

    @property
    def object_id(self):
        """Gets the object_id of this TagOperationDTO.

        数据实例ID。

        :return: The object_id of this TagOperationDTO.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this TagOperationDTO.

        数据实例ID。

        :param object_id: The object_id of this TagOperationDTO.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def tag_id(self):
        """Gets the tag_id of this TagOperationDTO.

        标签ID。

        :return: The tag_id of this TagOperationDTO.
        :rtype: str
        """
        return self._tag_id

    @tag_id.setter
    def tag_id(self, tag_id):
        """Sets the tag_id of this TagOperationDTO.

        标签ID。

        :param tag_id: The tag_id of this TagOperationDTO.
        :type tag_id: str
        """
        self._tag_id = tag_id

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
        if not isinstance(other, TagOperationDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
