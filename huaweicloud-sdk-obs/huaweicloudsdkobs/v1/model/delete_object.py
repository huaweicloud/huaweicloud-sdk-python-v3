# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteObject:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "DeleteObject"

    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'version_id': 'str'
    }

    attribute_map = {
        'key': 'Key',
        'version_id': 'VersionId'
    }

    def __init__(self, key=None, version_id=None):
        """DeleteObject

        The model defined in huaweicloud sdk

        :param key: 待删除的对象Key。如果设置了EncodingType元素，对象Key需要按照对应的编码类型进行编码。 
        :type key: str
        :param version_id: 待删除的对象版本号。 
        :type version_id: str
        """
        
        

        self._key = None
        self._version_id = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if version_id is not None:
            self.version_id = version_id

    @property
    def key(self):
        """Gets the key of this DeleteObject.

        待删除的对象Key。如果设置了EncodingType元素，对象Key需要按照对应的编码类型进行编码。 

        :return: The key of this DeleteObject.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this DeleteObject.

        待删除的对象Key。如果设置了EncodingType元素，对象Key需要按照对应的编码类型进行编码。 

        :param key: The key of this DeleteObject.
        :type key: str
        """
        self._key = key

    @property
    def version_id(self):
        """Gets the version_id of this DeleteObject.

        待删除的对象版本号。 

        :return: The version_id of this DeleteObject.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this DeleteObject.

        待删除的对象版本号。 

        :param version_id: The version_id of this DeleteObject.
        :type version_id: str
        """
        self._version_id = version_id

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
        if not isinstance(other, DeleteObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
