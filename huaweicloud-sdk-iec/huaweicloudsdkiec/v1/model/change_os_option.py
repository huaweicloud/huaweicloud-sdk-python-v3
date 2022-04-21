# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeOsOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'image_id': 'str',
        'metadata': 'ChangeOsMetadata',
        'key_name': 'str'
    }

    attribute_map = {
        'image_id': 'image_id',
        'metadata': 'metadata',
        'key_name': 'key_name'
    }

    def __init__(self, image_id=None, metadata=None, key_name=None):
        """ChangeOsOption

        The model defined in huaweicloud sdk

        :param image_id: 切换系统所使用的新镜像的ID。
        :type image_id: str
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkiec.v1.ChangeOsMetadata`
        :param key_name: 密钥对名称。 如果需要使用SSH密钥方式登录边缘实例，请指定已创建密钥的名称。
        :type key_name: str
        """
        
        

        self._image_id = None
        self._metadata = None
        self._key_name = None
        self.discriminator = None

        self.image_id = image_id
        if metadata is not None:
            self.metadata = metadata
        if key_name is not None:
            self.key_name = key_name

    @property
    def image_id(self):
        """Gets the image_id of this ChangeOsOption.

        切换系统所使用的新镜像的ID。

        :return: The image_id of this ChangeOsOption.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this ChangeOsOption.

        切换系统所使用的新镜像的ID。

        :param image_id: The image_id of this ChangeOsOption.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def metadata(self):
        """Gets the metadata of this ChangeOsOption.


        :return: The metadata of this ChangeOsOption.
        :rtype: :class:`huaweicloudsdkiec.v1.ChangeOsMetadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this ChangeOsOption.


        :param metadata: The metadata of this ChangeOsOption.
        :type metadata: :class:`huaweicloudsdkiec.v1.ChangeOsMetadata`
        """
        self._metadata = metadata

    @property
    def key_name(self):
        """Gets the key_name of this ChangeOsOption.

        密钥对名称。 如果需要使用SSH密钥方式登录边缘实例，请指定已创建密钥的名称。

        :return: The key_name of this ChangeOsOption.
        :rtype: str
        """
        return self._key_name

    @key_name.setter
    def key_name(self, key_name):
        """Sets the key_name of this ChangeOsOption.

        密钥对名称。 如果需要使用SSH密钥方式登录边缘实例，请指定已创建密钥的名称。

        :param key_name: The key_name of this ChangeOsOption.
        :type key_name: str
        """
        self._key_name = key_name

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
        if not isinstance(other, ChangeOsOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
