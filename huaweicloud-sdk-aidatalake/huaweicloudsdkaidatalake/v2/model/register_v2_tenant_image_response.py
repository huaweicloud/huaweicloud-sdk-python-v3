# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RegisterV2TenantImageResponse(SdkResponse):

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
        'category': 'V2ImageCategory',
        'image_registry': 'str',
        'image_namespace': 'str',
        'image_name': 'str',
        'visibility': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'image_id': 'image_id',
        'category': 'category',
        'image_registry': 'image_registry',
        'image_namespace': 'image_namespace',
        'image_name': 'image_name',
        'visibility': 'visibility',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, image_id=None, category=None, image_registry=None, image_namespace=None, image_name=None, visibility=None, x_request_id=None):
        r"""RegisterV2TenantImageResponse

        The model defined in huaweicloud sdk

        :param image_id: **参数解释**：镜像ID。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 
        :type image_id: str
        :param category: 
        :type category: :class:`huaweicloudsdkaidatalake.v2.V2ImageCategory`
        :param image_registry: **参数解释**：镜像域名。 **取值范围**：支持英文字母、数字、小数点及连字符，长度0~255个字符。 
        :type image_registry: str
        :param image_namespace: **参数解释**：镜像命名空间。 **取值范围**：由英文字母、数字、中划线和下划线组成，长度0~64个字符。 
        :type image_namespace: str
        :param image_name: **参数解释**：镜像名。 **取值范围**：由中文字符、英文字母、数字、中划线和下划线组成，长度0~128个字符。 
        :type image_name: str
        :param visibility: **参数解释**：可见性。 **取值范围**：   - PRIVATE：私有。用户自己创建的。   - PUBLIC：公共。查询所有公共的，包括其他用户创建的。 
        :type visibility: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super().__init__()

        self._image_id = None
        self._category = None
        self._image_registry = None
        self._image_namespace = None
        self._image_name = None
        self._visibility = None
        self._x_request_id = None
        self.discriminator = None

        if image_id is not None:
            self.image_id = image_id
        if category is not None:
            self.category = category
        if image_registry is not None:
            self.image_registry = image_registry
        if image_namespace is not None:
            self.image_namespace = image_namespace
        if image_name is not None:
            self.image_name = image_name
        if visibility is not None:
            self.visibility = visibility
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def image_id(self):
        r"""Gets the image_id of this RegisterV2TenantImageResponse.

        **参数解释**：镜像ID。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 

        :return: The image_id of this RegisterV2TenantImageResponse.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this RegisterV2TenantImageResponse.

        **参数解释**：镜像ID。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 

        :param image_id: The image_id of this RegisterV2TenantImageResponse.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def category(self):
        r"""Gets the category of this RegisterV2TenantImageResponse.

        :return: The category of this RegisterV2TenantImageResponse.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.V2ImageCategory`
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this RegisterV2TenantImageResponse.

        :param category: The category of this RegisterV2TenantImageResponse.
        :type category: :class:`huaweicloudsdkaidatalake.v2.V2ImageCategory`
        """
        self._category = category

    @property
    def image_registry(self):
        r"""Gets the image_registry of this RegisterV2TenantImageResponse.

        **参数解释**：镜像域名。 **取值范围**：支持英文字母、数字、小数点及连字符，长度0~255个字符。 

        :return: The image_registry of this RegisterV2TenantImageResponse.
        :rtype: str
        """
        return self._image_registry

    @image_registry.setter
    def image_registry(self, image_registry):
        r"""Sets the image_registry of this RegisterV2TenantImageResponse.

        **参数解释**：镜像域名。 **取值范围**：支持英文字母、数字、小数点及连字符，长度0~255个字符。 

        :param image_registry: The image_registry of this RegisterV2TenantImageResponse.
        :type image_registry: str
        """
        self._image_registry = image_registry

    @property
    def image_namespace(self):
        r"""Gets the image_namespace of this RegisterV2TenantImageResponse.

        **参数解释**：镜像命名空间。 **取值范围**：由英文字母、数字、中划线和下划线组成，长度0~64个字符。 

        :return: The image_namespace of this RegisterV2TenantImageResponse.
        :rtype: str
        """
        return self._image_namespace

    @image_namespace.setter
    def image_namespace(self, image_namespace):
        r"""Sets the image_namespace of this RegisterV2TenantImageResponse.

        **参数解释**：镜像命名空间。 **取值范围**：由英文字母、数字、中划线和下划线组成，长度0~64个字符。 

        :param image_namespace: The image_namespace of this RegisterV2TenantImageResponse.
        :type image_namespace: str
        """
        self._image_namespace = image_namespace

    @property
    def image_name(self):
        r"""Gets the image_name of this RegisterV2TenantImageResponse.

        **参数解释**：镜像名。 **取值范围**：由中文字符、英文字母、数字、中划线和下划线组成，长度0~128个字符。 

        :return: The image_name of this RegisterV2TenantImageResponse.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this RegisterV2TenantImageResponse.

        **参数解释**：镜像名。 **取值范围**：由中文字符、英文字母、数字、中划线和下划线组成，长度0~128个字符。 

        :param image_name: The image_name of this RegisterV2TenantImageResponse.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def visibility(self):
        r"""Gets the visibility of this RegisterV2TenantImageResponse.

        **参数解释**：可见性。 **取值范围**：   - PRIVATE：私有。用户自己创建的。   - PUBLIC：公共。查询所有公共的，包括其他用户创建的。 

        :return: The visibility of this RegisterV2TenantImageResponse.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        r"""Sets the visibility of this RegisterV2TenantImageResponse.

        **参数解释**：可见性。 **取值范围**：   - PRIVATE：私有。用户自己创建的。   - PUBLIC：公共。查询所有公共的，包括其他用户创建的。 

        :param visibility: The visibility of this RegisterV2TenantImageResponse.
        :type visibility: str
        """
        self._visibility = visibility

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this RegisterV2TenantImageResponse.

        :return: The x_request_id of this RegisterV2TenantImageResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this RegisterV2TenantImageResponse.

        :param x_request_id: The x_request_id of this RegisterV2TenantImageResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    def to_dict(self):
        import warnings
        warnings.warn("RegisterV2TenantImageResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, RegisterV2TenantImageResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
