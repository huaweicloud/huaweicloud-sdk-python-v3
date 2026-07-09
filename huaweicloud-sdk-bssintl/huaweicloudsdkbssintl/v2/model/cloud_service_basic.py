# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CloudServiceBasic:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cloud_service_type': 'str',
        'cloud_service_type_name': 'str',
        'resource_type': 'str',
        'resource_type_name': 'str',
        'resource_spec': 'str',
        'resource_spec_name': 'str',
        'charge_mode': 'str',
        'region_code': 'str'
    }

    attribute_map = {
        'cloud_service_type': 'cloud_service_type',
        'cloud_service_type_name': 'cloud_service_type_name',
        'resource_type': 'resource_type',
        'resource_type_name': 'resource_type_name',
        'resource_spec': 'resource_spec',
        'resource_spec_name': 'resource_spec_name',
        'charge_mode': 'charge_mode',
        'region_code': 'region_code'
    }

    def __init__(self, cloud_service_type=None, cloud_service_type_name=None, resource_type=None, resource_type_name=None, resource_spec=None, resource_spec_name=None, charge_mode=None, region_code=None):
        r"""CloudServiceBasic

        The model defined in huaweicloud sdk

        :param cloud_service_type: |参数名称：云服务类型编码| |参数的约束及描述：云服务类型编码|
        :type cloud_service_type: str
        :param cloud_service_type_name: |参数名称：云服务类型名称| |参数的约束及描述：云服务类型名称|
        :type cloud_service_type_name: str
        :param resource_type: |参数名称：资源类型编码| |参数的约束及描述：资源类型编码|
        :type resource_type: str
        :param resource_type_name: |参数名称：资源类型名称| |参数的约束及描述：资源类型名称|
        :type resource_type_name: str
        :param resource_spec: |参数名称：资源规格编码| |参数的约束及描述：资源规格编码|
        :type resource_spec: str
        :param resource_spec_name: |参数名称：资源规格名称| |参数的约束及描述：资源规格名称|
        :type resource_spec_name: str
        :param charge_mode: |参数名称：计费模式| |参数的约束及描述：1：包年/包月，3：按需|
        :type charge_mode: str
        :param region_code: |参数名称：区域编码| |参数的约束及描述：区域编码|
        :type region_code: str
        """
        
        

        self._cloud_service_type = None
        self._cloud_service_type_name = None
        self._resource_type = None
        self._resource_type_name = None
        self._resource_spec = None
        self._resource_spec_name = None
        self._charge_mode = None
        self._region_code = None
        self.discriminator = None

        if cloud_service_type is not None:
            self.cloud_service_type = cloud_service_type
        if cloud_service_type_name is not None:
            self.cloud_service_type_name = cloud_service_type_name
        if resource_type is not None:
            self.resource_type = resource_type
        if resource_type_name is not None:
            self.resource_type_name = resource_type_name
        if resource_spec is not None:
            self.resource_spec = resource_spec
        if resource_spec_name is not None:
            self.resource_spec_name = resource_spec_name
        if charge_mode is not None:
            self.charge_mode = charge_mode
        if region_code is not None:
            self.region_code = region_code

    @property
    def cloud_service_type(self):
        r"""Gets the cloud_service_type of this CloudServiceBasic.

        |参数名称：云服务类型编码| |参数的约束及描述：云服务类型编码|

        :return: The cloud_service_type of this CloudServiceBasic.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        r"""Sets the cloud_service_type of this CloudServiceBasic.

        |参数名称：云服务类型编码| |参数的约束及描述：云服务类型编码|

        :param cloud_service_type: The cloud_service_type of this CloudServiceBasic.
        :type cloud_service_type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def cloud_service_type_name(self):
        r"""Gets the cloud_service_type_name of this CloudServiceBasic.

        |参数名称：云服务类型名称| |参数的约束及描述：云服务类型名称|

        :return: The cloud_service_type_name of this CloudServiceBasic.
        :rtype: str
        """
        return self._cloud_service_type_name

    @cloud_service_type_name.setter
    def cloud_service_type_name(self, cloud_service_type_name):
        r"""Sets the cloud_service_type_name of this CloudServiceBasic.

        |参数名称：云服务类型名称| |参数的约束及描述：云服务类型名称|

        :param cloud_service_type_name: The cloud_service_type_name of this CloudServiceBasic.
        :type cloud_service_type_name: str
        """
        self._cloud_service_type_name = cloud_service_type_name

    @property
    def resource_type(self):
        r"""Gets the resource_type of this CloudServiceBasic.

        |参数名称：资源类型编码| |参数的约束及描述：资源类型编码|

        :return: The resource_type of this CloudServiceBasic.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this CloudServiceBasic.

        |参数名称：资源类型编码| |参数的约束及描述：资源类型编码|

        :param resource_type: The resource_type of this CloudServiceBasic.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_type_name(self):
        r"""Gets the resource_type_name of this CloudServiceBasic.

        |参数名称：资源类型名称| |参数的约束及描述：资源类型名称|

        :return: The resource_type_name of this CloudServiceBasic.
        :rtype: str
        """
        return self._resource_type_name

    @resource_type_name.setter
    def resource_type_name(self, resource_type_name):
        r"""Sets the resource_type_name of this CloudServiceBasic.

        |参数名称：资源类型名称| |参数的约束及描述：资源类型名称|

        :param resource_type_name: The resource_type_name of this CloudServiceBasic.
        :type resource_type_name: str
        """
        self._resource_type_name = resource_type_name

    @property
    def resource_spec(self):
        r"""Gets the resource_spec of this CloudServiceBasic.

        |参数名称：资源规格编码| |参数的约束及描述：资源规格编码|

        :return: The resource_spec of this CloudServiceBasic.
        :rtype: str
        """
        return self._resource_spec

    @resource_spec.setter
    def resource_spec(self, resource_spec):
        r"""Sets the resource_spec of this CloudServiceBasic.

        |参数名称：资源规格编码| |参数的约束及描述：资源规格编码|

        :param resource_spec: The resource_spec of this CloudServiceBasic.
        :type resource_spec: str
        """
        self._resource_spec = resource_spec

    @property
    def resource_spec_name(self):
        r"""Gets the resource_spec_name of this CloudServiceBasic.

        |参数名称：资源规格名称| |参数的约束及描述：资源规格名称|

        :return: The resource_spec_name of this CloudServiceBasic.
        :rtype: str
        """
        return self._resource_spec_name

    @resource_spec_name.setter
    def resource_spec_name(self, resource_spec_name):
        r"""Sets the resource_spec_name of this CloudServiceBasic.

        |参数名称：资源规格名称| |参数的约束及描述：资源规格名称|

        :param resource_spec_name: The resource_spec_name of this CloudServiceBasic.
        :type resource_spec_name: str
        """
        self._resource_spec_name = resource_spec_name

    @property
    def charge_mode(self):
        r"""Gets the charge_mode of this CloudServiceBasic.

        |参数名称：计费模式| |参数的约束及描述：1：包年/包月，3：按需|

        :return: The charge_mode of this CloudServiceBasic.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        r"""Sets the charge_mode of this CloudServiceBasic.

        |参数名称：计费模式| |参数的约束及描述：1：包年/包月，3：按需|

        :param charge_mode: The charge_mode of this CloudServiceBasic.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def region_code(self):
        r"""Gets the region_code of this CloudServiceBasic.

        |参数名称：区域编码| |参数的约束及描述：区域编码|

        :return: The region_code of this CloudServiceBasic.
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        r"""Sets the region_code of this CloudServiceBasic.

        |参数名称：区域编码| |参数的约束及描述：区域编码|

        :param region_code: The region_code of this CloudServiceBasic.
        :type region_code: str
        """
        self._region_code = region_code

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
        if not isinstance(other, CloudServiceBasic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
