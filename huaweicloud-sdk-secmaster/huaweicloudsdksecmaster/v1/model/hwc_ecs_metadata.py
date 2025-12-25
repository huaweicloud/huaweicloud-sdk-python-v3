# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HwcEcsMetadata:

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
        'image_type': 'str',
        'image_name': 'str',
        'os_bit': 'str',
        'os_type': 'str',
        'vpc_id': 'str',
        'resource_spec_code': 'str',
        'resource_type': 'str',
        'agency_name': 'str'
    }

    attribute_map = {
        'image_id': 'image_id',
        'image_type': 'image_type',
        'image_name': 'image_name',
        'os_bit': 'os_bit',
        'os_type': 'os_type',
        'vpc_id': 'vpc_id',
        'resource_spec_code': 'resource_spec_code',
        'resource_type': 'resource_type',
        'agency_name': 'agency_name'
    }

    def __init__(self, image_id=None, image_type=None, image_name=None, os_bit=None, os_type=None, vpc_id=None, resource_spec_code=None, resource_type=None, agency_name=None):
        r"""HwcEcsMetadata

        The model defined in huaweicloud sdk

        :param image_id: 云服务器操作系统对应的镜像ID。
        :type image_id: str
        :param image_type: 镜像类型，目前支持： 公共镜像（gold） 私有镜像（private） 共享镜像（shared）
        :type image_type: str
        :param image_name: 云服务器操作系统对应的镜像名称。
        :type image_name: str
        :param os_bit: 操作系统位数，一般取值为“32”或者“64”。
        :type os_bit: str
        :param os_type: 操作系统类型，取值为：Linux、Windows。
        :type os_type: str
        :param vpc_id: 云服务器所属的虚拟私有云ID。
        :type vpc_id: str
        :param resource_spec_code: 云服务器对应的资源规格。
        :type resource_spec_code: str
        :param resource_type: 云服务器对应的资源类型。 取值为“1”，代表资源类型为云服务器。
        :type resource_type: str
        :param agency_name: 委托的名称。 委托是由租户管理员在统一身份认证服务（Identity and Access Management，IAM）上创建的，可以为弹性云服务器提供访问云服务器的临时凭证。
        :type agency_name: str
        """
        
        

        self._image_id = None
        self._image_type = None
        self._image_name = None
        self._os_bit = None
        self._os_type = None
        self._vpc_id = None
        self._resource_spec_code = None
        self._resource_type = None
        self._agency_name = None
        self.discriminator = None

        if image_id is not None:
            self.image_id = image_id
        if image_type is not None:
            self.image_type = image_type
        if image_name is not None:
            self.image_name = image_name
        if os_bit is not None:
            self.os_bit = os_bit
        if os_type is not None:
            self.os_type = os_type
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if resource_spec_code is not None:
            self.resource_spec_code = resource_spec_code
        if resource_type is not None:
            self.resource_type = resource_type
        if agency_name is not None:
            self.agency_name = agency_name

    @property
    def image_id(self):
        r"""Gets the image_id of this HwcEcsMetadata.

        云服务器操作系统对应的镜像ID。

        :return: The image_id of this HwcEcsMetadata.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this HwcEcsMetadata.

        云服务器操作系统对应的镜像ID。

        :param image_id: The image_id of this HwcEcsMetadata.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def image_type(self):
        r"""Gets the image_type of this HwcEcsMetadata.

        镜像类型，目前支持： 公共镜像（gold） 私有镜像（private） 共享镜像（shared）

        :return: The image_type of this HwcEcsMetadata.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        r"""Sets the image_type of this HwcEcsMetadata.

        镜像类型，目前支持： 公共镜像（gold） 私有镜像（private） 共享镜像（shared）

        :param image_type: The image_type of this HwcEcsMetadata.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def image_name(self):
        r"""Gets the image_name of this HwcEcsMetadata.

        云服务器操作系统对应的镜像名称。

        :return: The image_name of this HwcEcsMetadata.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this HwcEcsMetadata.

        云服务器操作系统对应的镜像名称。

        :param image_name: The image_name of this HwcEcsMetadata.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def os_bit(self):
        r"""Gets the os_bit of this HwcEcsMetadata.

        操作系统位数，一般取值为“32”或者“64”。

        :return: The os_bit of this HwcEcsMetadata.
        :rtype: str
        """
        return self._os_bit

    @os_bit.setter
    def os_bit(self, os_bit):
        r"""Sets the os_bit of this HwcEcsMetadata.

        操作系统位数，一般取值为“32”或者“64”。

        :param os_bit: The os_bit of this HwcEcsMetadata.
        :type os_bit: str
        """
        self._os_bit = os_bit

    @property
    def os_type(self):
        r"""Gets the os_type of this HwcEcsMetadata.

        操作系统类型，取值为：Linux、Windows。

        :return: The os_type of this HwcEcsMetadata.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this HwcEcsMetadata.

        操作系统类型，取值为：Linux、Windows。

        :param os_type: The os_type of this HwcEcsMetadata.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this HwcEcsMetadata.

        云服务器所属的虚拟私有云ID。

        :return: The vpc_id of this HwcEcsMetadata.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this HwcEcsMetadata.

        云服务器所属的虚拟私有云ID。

        :param vpc_id: The vpc_id of this HwcEcsMetadata.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def resource_spec_code(self):
        r"""Gets the resource_spec_code of this HwcEcsMetadata.

        云服务器对应的资源规格。

        :return: The resource_spec_code of this HwcEcsMetadata.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        r"""Sets the resource_spec_code of this HwcEcsMetadata.

        云服务器对应的资源规格。

        :param resource_spec_code: The resource_spec_code of this HwcEcsMetadata.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def resource_type(self):
        r"""Gets the resource_type of this HwcEcsMetadata.

        云服务器对应的资源类型。 取值为“1”，代表资源类型为云服务器。

        :return: The resource_type of this HwcEcsMetadata.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this HwcEcsMetadata.

        云服务器对应的资源类型。 取值为“1”，代表资源类型为云服务器。

        :param resource_type: The resource_type of this HwcEcsMetadata.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def agency_name(self):
        r"""Gets the agency_name of this HwcEcsMetadata.

        委托的名称。 委托是由租户管理员在统一身份认证服务（Identity and Access Management，IAM）上创建的，可以为弹性云服务器提供访问云服务器的临时凭证。

        :return: The agency_name of this HwcEcsMetadata.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        r"""Sets the agency_name of this HwcEcsMetadata.

        委托的名称。 委托是由租户管理员在统一身份认证服务（Identity and Access Management，IAM）上创建的，可以为弹性云服务器提供访问云服务器的临时凭证。

        :param agency_name: The agency_name of this HwcEcsMetadata.
        :type agency_name: str
        """
        self._agency_name = agency_name

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
        if not isinstance(other, HwcEcsMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
