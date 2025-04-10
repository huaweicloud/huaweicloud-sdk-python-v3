# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region': 'str',
        'quark_vpc_endpoint': 'str',
        'project_id': 'str',
        'instance_type': 'str',
        'instance_id': 'str',
        'service_type': 'str',
        'service_id': 'str',
        'public_border_group': 'str',
        'instance_site': 'str'
    }

    attribute_map = {
        'region': 'region',
        'quark_vpc_endpoint': 'quarkVpcEndpoint',
        'project_id': 'project_id',
        'instance_type': 'instance_type',
        'instance_id': 'instance_id',
        'service_type': 'service_type',
        'service_id': 'service_id',
        'public_border_group': 'public_border_group',
        'instance_site': 'instance_site'
    }

    def __init__(self, region=None, quark_vpc_endpoint=None, project_id=None, instance_type=None, instance_id=None, service_type=None, service_id=None, public_border_group=None, instance_site=None):
        r"""InstanceInfo

        The model defined in huaweicloud sdk

        :param region: region
        :type region: str
        :param quark_vpc_endpoint: quark后端地址
        :type quark_vpc_endpoint: str
        :param project_id: 项目ID，获取项目ID请参见[获取项目ID](https://support.huaweicloud.com/api-vpc/vpc_api_0011.html)
        :type project_id: str
        :param instance_type: 支持绑定的实例类型
        :type instance_type: str
        :param instance_id: 实例ID
        :type instance_id: str
        :param service_type: 服务类型
        :type service_type: str
        :param service_id: 服务id
        :type service_id: str
        :param public_border_group: - 功能说明：表示中心站点资源或者边缘站点资源 - 取值范围：center、边缘站点名称
        :type public_border_group: str
        :param instance_site: 绑定实例所在的站点
        :type instance_site: str
        """
        
        

        self._region = None
        self._quark_vpc_endpoint = None
        self._project_id = None
        self._instance_type = None
        self._instance_id = None
        self._service_type = None
        self._service_id = None
        self._public_border_group = None
        self._instance_site = None
        self.discriminator = None

        if region is not None:
            self.region = region
        if quark_vpc_endpoint is not None:
            self.quark_vpc_endpoint = quark_vpc_endpoint
        if project_id is not None:
            self.project_id = project_id
        if instance_type is not None:
            self.instance_type = instance_type
        if instance_id is not None:
            self.instance_id = instance_id
        if service_type is not None:
            self.service_type = service_type
        if service_id is not None:
            self.service_id = service_id
        if public_border_group is not None:
            self.public_border_group = public_border_group
        if instance_site is not None:
            self.instance_site = instance_site

    @property
    def region(self):
        r"""Gets the region of this InstanceInfo.

        region

        :return: The region of this InstanceInfo.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this InstanceInfo.

        region

        :param region: The region of this InstanceInfo.
        :type region: str
        """
        self._region = region

    @property
    def quark_vpc_endpoint(self):
        r"""Gets the quark_vpc_endpoint of this InstanceInfo.

        quark后端地址

        :return: The quark_vpc_endpoint of this InstanceInfo.
        :rtype: str
        """
        return self._quark_vpc_endpoint

    @quark_vpc_endpoint.setter
    def quark_vpc_endpoint(self, quark_vpc_endpoint):
        r"""Sets the quark_vpc_endpoint of this InstanceInfo.

        quark后端地址

        :param quark_vpc_endpoint: The quark_vpc_endpoint of this InstanceInfo.
        :type quark_vpc_endpoint: str
        """
        self._quark_vpc_endpoint = quark_vpc_endpoint

    @property
    def project_id(self):
        r"""Gets the project_id of this InstanceInfo.

        项目ID，获取项目ID请参见[获取项目ID](https://support.huaweicloud.com/api-vpc/vpc_api_0011.html)

        :return: The project_id of this InstanceInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this InstanceInfo.

        项目ID，获取项目ID请参见[获取项目ID](https://support.huaweicloud.com/api-vpc/vpc_api_0011.html)

        :param project_id: The project_id of this InstanceInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def instance_type(self):
        r"""Gets the instance_type of this InstanceInfo.

        支持绑定的实例类型

        :return: The instance_type of this InstanceInfo.
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        r"""Sets the instance_type of this InstanceInfo.

        支持绑定的实例类型

        :param instance_type: The instance_type of this InstanceInfo.
        :type instance_type: str
        """
        self._instance_type = instance_type

    @property
    def instance_id(self):
        r"""Gets the instance_id of this InstanceInfo.

        实例ID

        :return: The instance_id of this InstanceInfo.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this InstanceInfo.

        实例ID

        :param instance_id: The instance_id of this InstanceInfo.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def service_type(self):
        r"""Gets the service_type of this InstanceInfo.

        服务类型

        :return: The service_type of this InstanceInfo.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        r"""Sets the service_type of this InstanceInfo.

        服务类型

        :param service_type: The service_type of this InstanceInfo.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def service_id(self):
        r"""Gets the service_id of this InstanceInfo.

        服务id

        :return: The service_id of this InstanceInfo.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        r"""Sets the service_id of this InstanceInfo.

        服务id

        :param service_id: The service_id of this InstanceInfo.
        :type service_id: str
        """
        self._service_id = service_id

    @property
    def public_border_group(self):
        r"""Gets the public_border_group of this InstanceInfo.

        - 功能说明：表示中心站点资源或者边缘站点资源 - 取值范围：center、边缘站点名称

        :return: The public_border_group of this InstanceInfo.
        :rtype: str
        """
        return self._public_border_group

    @public_border_group.setter
    def public_border_group(self, public_border_group):
        r"""Sets the public_border_group of this InstanceInfo.

        - 功能说明：表示中心站点资源或者边缘站点资源 - 取值范围：center、边缘站点名称

        :param public_border_group: The public_border_group of this InstanceInfo.
        :type public_border_group: str
        """
        self._public_border_group = public_border_group

    @property
    def instance_site(self):
        r"""Gets the instance_site of this InstanceInfo.

        绑定实例所在的站点

        :return: The instance_site of this InstanceInfo.
        :rtype: str
        """
        return self._instance_site

    @instance_site.setter
    def instance_site(self, instance_site):
        r"""Sets the instance_site of this InstanceInfo.

        绑定实例所在的站点

        :param instance_site: The instance_site of this InstanceInfo.
        :type instance_site: str
        """
        self._instance_site = instance_site

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
        if not isinstance(other, InstanceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
