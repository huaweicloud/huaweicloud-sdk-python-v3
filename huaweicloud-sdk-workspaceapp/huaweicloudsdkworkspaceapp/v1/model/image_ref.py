# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageRef:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'image_type': 'str',
        'spce_code': 'str',
        'product_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'image_type': 'image_type',
        'spce_code': 'spce_code',
        'product_id': 'product_id'
    }

    def __init__(self, id=None, image_type=None, spce_code=None, product_id=None):
        """ImageRef

        The model defined in huaweicloud sdk

        :param id: 镜像源的唯一标识。
        :type id: str
        :param image_type: 镜像源的镜像类型: * &#x60;gold&#x60; - 云市场镜像 * &#x60;public&#x60; - 公共镜像 * &#x60;private&#x60; - 私有镜像 * &#x60;shared&#x60; - 共享镜像 * &#x60;other&#x60; - 其他
        :type image_type: str
        :param spce_code: 镜像源的规格编码，对于&#x60;gold&#x60;镜像类型，这个值是的必须项。
        :type spce_code: str
        :param product_id: 镜像源的产品ID，对于&#x60;gold&#x60;镜像类型，这个值是的必须项。
        :type product_id: str
        """
        
        

        self._id = None
        self._image_type = None
        self._spce_code = None
        self._product_id = None
        self.discriminator = None

        self.id = id
        self.image_type = image_type
        if spce_code is not None:
            self.spce_code = spce_code
        if product_id is not None:
            self.product_id = product_id

    @property
    def id(self):
        """Gets the id of this ImageRef.

        镜像源的唯一标识。

        :return: The id of this ImageRef.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ImageRef.

        镜像源的唯一标识。

        :param id: The id of this ImageRef.
        :type id: str
        """
        self._id = id

    @property
    def image_type(self):
        """Gets the image_type of this ImageRef.

        镜像源的镜像类型: * `gold` - 云市场镜像 * `public` - 公共镜像 * `private` - 私有镜像 * `shared` - 共享镜像 * `other` - 其他

        :return: The image_type of this ImageRef.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        """Sets the image_type of this ImageRef.

        镜像源的镜像类型: * `gold` - 云市场镜像 * `public` - 公共镜像 * `private` - 私有镜像 * `shared` - 共享镜像 * `other` - 其他

        :param image_type: The image_type of this ImageRef.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def spce_code(self):
        """Gets the spce_code of this ImageRef.

        镜像源的规格编码，对于`gold`镜像类型，这个值是的必须项。

        :return: The spce_code of this ImageRef.
        :rtype: str
        """
        return self._spce_code

    @spce_code.setter
    def spce_code(self, spce_code):
        """Sets the spce_code of this ImageRef.

        镜像源的规格编码，对于`gold`镜像类型，这个值是的必须项。

        :param spce_code: The spce_code of this ImageRef.
        :type spce_code: str
        """
        self._spce_code = spce_code

    @property
    def product_id(self):
        """Gets the product_id of this ImageRef.

        镜像源的产品ID，对于`gold`镜像类型，这个值是的必须项。

        :return: The product_id of this ImageRef.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this ImageRef.

        镜像源的产品ID，对于`gold`镜像类型，这个值是的必须项。

        :param product_id: The product_id of this ImageRef.
        :type product_id: str
        """
        self._product_id = product_id

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
        if not isinstance(other, ImageRef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
