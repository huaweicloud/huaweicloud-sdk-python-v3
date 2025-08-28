# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageWhiteListDetailResponseInfoImageInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'image_id': 'str',
        'image_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'image_id': 'image_id',
        'image_name': 'image_name'
    }

    def __init__(self, id=None, image_id=None, image_name=None):
        r"""ImageWhiteListDetailResponseInfoImageInfo

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 仓库镜像ID **取值范围**： 取值1-9223372036854775807 
        :type id: int
        :param image_id: **参数解释**： 本地镜像ID **取值范围**： 字符长度1-64位 
        :type image_id: str
        :param image_name: **参数解释**： 镜像名称 **取值范围**： 字符长度1-256位 
        :type image_name: str
        """
        
        

        self._id = None
        self._image_id = None
        self._image_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if image_id is not None:
            self.image_id = image_id
        if image_name is not None:
            self.image_name = image_name

    @property
    def id(self):
        r"""Gets the id of this ImageWhiteListDetailResponseInfoImageInfo.

        **参数解释**： 仓库镜像ID **取值范围**： 取值1-9223372036854775807 

        :return: The id of this ImageWhiteListDetailResponseInfoImageInfo.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ImageWhiteListDetailResponseInfoImageInfo.

        **参数解释**： 仓库镜像ID **取值范围**： 取值1-9223372036854775807 

        :param id: The id of this ImageWhiteListDetailResponseInfoImageInfo.
        :type id: int
        """
        self._id = id

    @property
    def image_id(self):
        r"""Gets the image_id of this ImageWhiteListDetailResponseInfoImageInfo.

        **参数解释**： 本地镜像ID **取值范围**： 字符长度1-64位 

        :return: The image_id of this ImageWhiteListDetailResponseInfoImageInfo.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this ImageWhiteListDetailResponseInfoImageInfo.

        **参数解释**： 本地镜像ID **取值范围**： 字符长度1-64位 

        :param image_id: The image_id of this ImageWhiteListDetailResponseInfoImageInfo.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def image_name(self):
        r"""Gets the image_name of this ImageWhiteListDetailResponseInfoImageInfo.

        **参数解释**： 镜像名称 **取值范围**： 字符长度1-256位 

        :return: The image_name of this ImageWhiteListDetailResponseInfoImageInfo.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this ImageWhiteListDetailResponseInfoImageInfo.

        **参数解释**： 镜像名称 **取值范围**： 字符长度1-256位 

        :param image_name: The image_name of this ImageWhiteListDetailResponseInfoImageInfo.
        :type image_name: str
        """
        self._image_name = image_name

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
        if not isinstance(other, ImageWhiteListDetailResponseInfoImageInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
