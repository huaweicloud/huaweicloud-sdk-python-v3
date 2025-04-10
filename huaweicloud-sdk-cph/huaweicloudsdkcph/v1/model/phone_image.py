# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PhoneImage:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_name': 'str',
        'os_type': 'str',
        'is_public': 'int',
        'os_name': 'str',
        'image_label': 'str',
        'image_id': 'str',
        'is_support_encrypt': 'bool'
    }

    attribute_map = {
        'image_name': 'image_name',
        'os_type': 'os_type',
        'is_public': 'is_public',
        'os_name': 'os_name',
        'image_label': 'image_label',
        'image_id': 'image_id',
        'is_support_encrypt': 'is_support_encrypt'
    }

    def __init__(self, image_name=None, os_type=None, is_public=None, os_name=None, image_label=None, image_id=None, is_support_encrypt=None):
        r"""PhoneImage

        The model defined in huaweicloud sdk

        :param image_name: 手机镜像名称，不超过128个字节。
        :type image_name: str
        :param os_type: 镜像操作系统类型，不超过16个字节。
        :type os_type: str
        :param is_public: 镜像类型。 - 1：公有镜像 - 2 ：私有镜像
        :type is_public: int
        :param os_name: 手机操作系统，不超过36个字节。
        :type os_name: str
        :param image_label: 镜像适用的云手机规格。 - cloud_phone：适用于physical.rx1.xlarge 类型云手机服务器 - cloud_phone_1620：适用于physical.kg1.4xlarge.cp类型云手机服务器 - cloud_game：适用于physical.rx1.xlarge.cg 类型云手游服务器 - cloud_game_1620：适用于physical.kg1.4xlarge.cg 类型云手游服务器 - qemu_phone： 适用于physical.rx1.xlarge 类型云手机服务器中 qemu类型云手机规格
        :type image_label: str
        :param image_id: 手机镜像唯一标识ID，不超过32个字节。
        :type image_id: str
        :param is_support_encrypt: 当前镜像是否支持文件级加密
        :type is_support_encrypt: bool
        """
        
        

        self._image_name = None
        self._os_type = None
        self._is_public = None
        self._os_name = None
        self._image_label = None
        self._image_id = None
        self._is_support_encrypt = None
        self.discriminator = None

        if image_name is not None:
            self.image_name = image_name
        if os_type is not None:
            self.os_type = os_type
        if is_public is not None:
            self.is_public = is_public
        if os_name is not None:
            self.os_name = os_name
        if image_label is not None:
            self.image_label = image_label
        if image_id is not None:
            self.image_id = image_id
        if is_support_encrypt is not None:
            self.is_support_encrypt = is_support_encrypt

    @property
    def image_name(self):
        r"""Gets the image_name of this PhoneImage.

        手机镜像名称，不超过128个字节。

        :return: The image_name of this PhoneImage.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this PhoneImage.

        手机镜像名称，不超过128个字节。

        :param image_name: The image_name of this PhoneImage.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def os_type(self):
        r"""Gets the os_type of this PhoneImage.

        镜像操作系统类型，不超过16个字节。

        :return: The os_type of this PhoneImage.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this PhoneImage.

        镜像操作系统类型，不超过16个字节。

        :param os_type: The os_type of this PhoneImage.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def is_public(self):
        r"""Gets the is_public of this PhoneImage.

        镜像类型。 - 1：公有镜像 - 2 ：私有镜像

        :return: The is_public of this PhoneImage.
        :rtype: int
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        r"""Sets the is_public of this PhoneImage.

        镜像类型。 - 1：公有镜像 - 2 ：私有镜像

        :param is_public: The is_public of this PhoneImage.
        :type is_public: int
        """
        self._is_public = is_public

    @property
    def os_name(self):
        r"""Gets the os_name of this PhoneImage.

        手机操作系统，不超过36个字节。

        :return: The os_name of this PhoneImage.
        :rtype: str
        """
        return self._os_name

    @os_name.setter
    def os_name(self, os_name):
        r"""Sets the os_name of this PhoneImage.

        手机操作系统，不超过36个字节。

        :param os_name: The os_name of this PhoneImage.
        :type os_name: str
        """
        self._os_name = os_name

    @property
    def image_label(self):
        r"""Gets the image_label of this PhoneImage.

        镜像适用的云手机规格。 - cloud_phone：适用于physical.rx1.xlarge 类型云手机服务器 - cloud_phone_1620：适用于physical.kg1.4xlarge.cp类型云手机服务器 - cloud_game：适用于physical.rx1.xlarge.cg 类型云手游服务器 - cloud_game_1620：适用于physical.kg1.4xlarge.cg 类型云手游服务器 - qemu_phone： 适用于physical.rx1.xlarge 类型云手机服务器中 qemu类型云手机规格

        :return: The image_label of this PhoneImage.
        :rtype: str
        """
        return self._image_label

    @image_label.setter
    def image_label(self, image_label):
        r"""Sets the image_label of this PhoneImage.

        镜像适用的云手机规格。 - cloud_phone：适用于physical.rx1.xlarge 类型云手机服务器 - cloud_phone_1620：适用于physical.kg1.4xlarge.cp类型云手机服务器 - cloud_game：适用于physical.rx1.xlarge.cg 类型云手游服务器 - cloud_game_1620：适用于physical.kg1.4xlarge.cg 类型云手游服务器 - qemu_phone： 适用于physical.rx1.xlarge 类型云手机服务器中 qemu类型云手机规格

        :param image_label: The image_label of this PhoneImage.
        :type image_label: str
        """
        self._image_label = image_label

    @property
    def image_id(self):
        r"""Gets the image_id of this PhoneImage.

        手机镜像唯一标识ID，不超过32个字节。

        :return: The image_id of this PhoneImage.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this PhoneImage.

        手机镜像唯一标识ID，不超过32个字节。

        :param image_id: The image_id of this PhoneImage.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def is_support_encrypt(self):
        r"""Gets the is_support_encrypt of this PhoneImage.

        当前镜像是否支持文件级加密

        :return: The is_support_encrypt of this PhoneImage.
        :rtype: bool
        """
        return self._is_support_encrypt

    @is_support_encrypt.setter
    def is_support_encrypt(self, is_support_encrypt):
        r"""Sets the is_support_encrypt of this PhoneImage.

        当前镜像是否支持文件级加密

        :param is_support_encrypt: The is_support_encrypt of this PhoneImage.
        :type is_support_encrypt: bool
        """
        self._is_support_encrypt = is_support_encrypt

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
        if not isinstance(other, PhoneImage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
