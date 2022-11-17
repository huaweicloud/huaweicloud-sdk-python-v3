# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReinstallVolumeSpec:

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
        'cmk_id': 'str'
    }

    attribute_map = {
        'image_id': 'imageID',
        'cmk_id': 'cmkID'
    }

    def __init__(self, image_id=None, cmk_id=None):
        """ReinstallVolumeSpec

        The model defined in huaweicloud sdk

        :param image_id: 用户自定义镜像ID
        :type image_id: str
        :param cmk_id: 用户主密钥ID。默认为空时，表示云硬盘不加密。
        :type cmk_id: str
        """
        
        

        self._image_id = None
        self._cmk_id = None
        self.discriminator = None

        if image_id is not None:
            self.image_id = image_id
        if cmk_id is not None:
            self.cmk_id = cmk_id

    @property
    def image_id(self):
        """Gets the image_id of this ReinstallVolumeSpec.

        用户自定义镜像ID

        :return: The image_id of this ReinstallVolumeSpec.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this ReinstallVolumeSpec.

        用户自定义镜像ID

        :param image_id: The image_id of this ReinstallVolumeSpec.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def cmk_id(self):
        """Gets the cmk_id of this ReinstallVolumeSpec.

        用户主密钥ID。默认为空时，表示云硬盘不加密。

        :return: The cmk_id of this ReinstallVolumeSpec.
        :rtype: str
        """
        return self._cmk_id

    @cmk_id.setter
    def cmk_id(self, cmk_id):
        """Sets the cmk_id of this ReinstallVolumeSpec.

        用户主密钥ID。默认为空时，表示云硬盘不加密。

        :param cmk_id: The cmk_id of this ReinstallVolumeSpec.
        :type cmk_id: str
        """
        self._cmk_id = cmk_id

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
        if not isinstance(other, ReinstallVolumeSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
