# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCcspTenantImagesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'image_name': 'str',
        'service_type': 'str',
        'sort_key': 'str',
        'sort_dir': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'image_name': 'image_name',
        'service_type': 'service_type',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir'
    }

    def __init__(self, limit=None, offset=None, image_name=None, service_type=None, sort_key=None, sort_dir=None):
        r"""ListCcspTenantImagesRequest

        The model defined in huaweicloud sdk

        :param limit: 指定查询返回记录条数，默认值10
        :type limit: int
        :param offset: 索引位置，从offset指定的下一条数据开始查询默认值为0
        :type offset: int
        :param image_name: 镜像名称
        :type image_name: str
        :param service_type: 镜像所属的服务类型： - **ENCRYPT_DECRYPT** : 加解密服务； - **SIGN_VERIFY** : 签名验签服务； - **KMS** : 密钥管理服务； - **TIMESTAMP** : 时间戳服务； - **COLLA_SIGN** : 协同签名服务； - **OTP** : 动态令牌服务； - **DB_ENCRYPT** : 数据库加密服务； - **FILE_ENCRYPT** : 文件加密服务 - **TIMESTAMP** : 时间戳服务； - **DIGIT_SEAL** : 电子签章服务； - **SSL_VPN** : ssl vpn服务；
        :type service_type: str
        :param sort_key: 排序属性，目前支持以下属性： - **create_time** : 镜像的创建时间（默认）
        :type sort_key: str
        :param sort_dir: 排序方向，支持以下值： - **DESC** : 降序（默认） - **ASC** : 升序
        :type sort_dir: str
        """
        
        

        self._limit = None
        self._offset = None
        self._image_name = None
        self._service_type = None
        self._sort_key = None
        self._sort_dir = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if image_name is not None:
            self.image_name = image_name
        if service_type is not None:
            self.service_type = service_type
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir

    @property
    def limit(self):
        r"""Gets the limit of this ListCcspTenantImagesRequest.

        指定查询返回记录条数，默认值10

        :return: The limit of this ListCcspTenantImagesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListCcspTenantImagesRequest.

        指定查询返回记录条数，默认值10

        :param limit: The limit of this ListCcspTenantImagesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListCcspTenantImagesRequest.

        索引位置，从offset指定的下一条数据开始查询默认值为0

        :return: The offset of this ListCcspTenantImagesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListCcspTenantImagesRequest.

        索引位置，从offset指定的下一条数据开始查询默认值为0

        :param offset: The offset of this ListCcspTenantImagesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def image_name(self):
        r"""Gets the image_name of this ListCcspTenantImagesRequest.

        镜像名称

        :return: The image_name of this ListCcspTenantImagesRequest.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this ListCcspTenantImagesRequest.

        镜像名称

        :param image_name: The image_name of this ListCcspTenantImagesRequest.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def service_type(self):
        r"""Gets the service_type of this ListCcspTenantImagesRequest.

        镜像所属的服务类型： - **ENCRYPT_DECRYPT** : 加解密服务； - **SIGN_VERIFY** : 签名验签服务； - **KMS** : 密钥管理服务； - **TIMESTAMP** : 时间戳服务； - **COLLA_SIGN** : 协同签名服务； - **OTP** : 动态令牌服务； - **DB_ENCRYPT** : 数据库加密服务； - **FILE_ENCRYPT** : 文件加密服务 - **TIMESTAMP** : 时间戳服务； - **DIGIT_SEAL** : 电子签章服务； - **SSL_VPN** : ssl vpn服务；

        :return: The service_type of this ListCcspTenantImagesRequest.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        r"""Sets the service_type of this ListCcspTenantImagesRequest.

        镜像所属的服务类型： - **ENCRYPT_DECRYPT** : 加解密服务； - **SIGN_VERIFY** : 签名验签服务； - **KMS** : 密钥管理服务； - **TIMESTAMP** : 时间戳服务； - **COLLA_SIGN** : 协同签名服务； - **OTP** : 动态令牌服务； - **DB_ENCRYPT** : 数据库加密服务； - **FILE_ENCRYPT** : 文件加密服务 - **TIMESTAMP** : 时间戳服务； - **DIGIT_SEAL** : 电子签章服务； - **SSL_VPN** : ssl vpn服务；

        :param service_type: The service_type of this ListCcspTenantImagesRequest.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListCcspTenantImagesRequest.

        排序属性，目前支持以下属性： - **create_time** : 镜像的创建时间（默认）

        :return: The sort_key of this ListCcspTenantImagesRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListCcspTenantImagesRequest.

        排序属性，目前支持以下属性： - **create_time** : 镜像的创建时间（默认）

        :param sort_key: The sort_key of this ListCcspTenantImagesRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListCcspTenantImagesRequest.

        排序方向，支持以下值： - **DESC** : 降序（默认） - **ASC** : 升序

        :return: The sort_dir of this ListCcspTenantImagesRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListCcspTenantImagesRequest.

        排序方向，支持以下值： - **DESC** : 降序（默认） - **ASC** : 升序

        :param sort_dir: The sort_dir of this ListCcspTenantImagesRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

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
        if not isinstance(other, ListCcspTenantImagesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
