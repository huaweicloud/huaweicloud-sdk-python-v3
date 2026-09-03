# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ObsObjectInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'object_key': 'str',
        'content_length': 'int'
    }

    attribute_map = {
        'object_key': 'object_key',
        'content_length': 'content_length'
    }

    def __init__(self, object_key=None, content_length=None):
        r"""ObsObjectInfo

        The model defined in huaweicloud sdk

        :param object_key: 对象的名称
        :type object_key: str
        :param content_length: 对象文件的大小
        :type content_length: int
        """
        
        

        self._object_key = None
        self._content_length = None
        self.discriminator = None

        if object_key is not None:
            self.object_key = object_key
        if content_length is not None:
            self.content_length = content_length

    @property
    def object_key(self):
        r"""Gets the object_key of this ObsObjectInfo.

        对象的名称

        :return: The object_key of this ObsObjectInfo.
        :rtype: str
        """
        return self._object_key

    @object_key.setter
    def object_key(self, object_key):
        r"""Sets the object_key of this ObsObjectInfo.

        对象的名称

        :param object_key: The object_key of this ObsObjectInfo.
        :type object_key: str
        """
        self._object_key = object_key

    @property
    def content_length(self):
        r"""Gets the content_length of this ObsObjectInfo.

        对象文件的大小

        :return: The content_length of this ObsObjectInfo.
        :rtype: int
        """
        return self._content_length

    @content_length.setter
    def content_length(self, content_length):
        r"""Sets the content_length of this ObsObjectInfo.

        对象文件的大小

        :param content_length: The content_length of this ObsObjectInfo.
        :type content_length: int
        """
        self._content_length = content_length

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ObsObjectInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
