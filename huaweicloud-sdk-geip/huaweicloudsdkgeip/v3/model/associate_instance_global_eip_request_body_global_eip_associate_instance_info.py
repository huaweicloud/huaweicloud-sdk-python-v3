# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssociateInstanceGlobalEipRequestBodyGlobalEipAssociateInstanceInfo:

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
        'instance_type': 'str',
        'instance_id': 'str',
        'project_id': 'str',
        'service_id': 'str',
        'service_type': 'str'
    }

    attribute_map = {
        'region': 'region',
        'instance_type': 'instance_type',
        'instance_id': 'instance_id',
        'project_id': 'project_id',
        'service_id': 'service_id',
        'service_type': 'service_type'
    }

    def __init__(self, region=None, instance_type=None, instance_id=None, project_id=None, service_id=None, service_type=None):
        r"""AssociateInstanceGlobalEipRequestBodyGlobalEipAssociateInstanceInfo

        The model defined in huaweicloud sdk

        :param region: region
        :type region: str
        :param instance_type: 支持绑定的实例类型
        :type instance_type: str
        :param instance_id: 实例ID
        :type instance_id: str
        :param project_id: 项目ID，获取项目ID请参见[获取项目ID](https://support.huaweicloud.com/api-vpc/vpc_api_0011.html)
        :type project_id: str
        :param service_id: 服务id
        :type service_id: str
        :param service_type: 服务类型
        :type service_type: str
        """
        
        

        self._region = None
        self._instance_type = None
        self._instance_id = None
        self._project_id = None
        self._service_id = None
        self._service_type = None
        self.discriminator = None

        if region is not None:
            self.region = region
        if instance_type is not None:
            self.instance_type = instance_type
        if instance_id is not None:
            self.instance_id = instance_id
        if project_id is not None:
            self.project_id = project_id
        if service_id is not None:
            self.service_id = service_id
        if service_type is not None:
            self.service_type = service_type

    @property
    def region(self):
        r"""Gets the region of this AssociateInstanceGlobalEipRequestBodyGlobalEipAssociateInstanceInfo.

        region

        :return: The region of this AssociateInstanceGlobalEipRequestBodyGlobalEipAssociateInstanceInfo.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this AssociateInstanceGlobalEipRequestBodyGlobalEipAssociateInstanceInfo.

        region

        :param region: The region of this AssociateInstanceGlobalEipRequestBodyGlobalEipAssociateInstanceInfo.
        :type region: str
        """
        self._region = region

    @property
    def instance_type(self):
        r"""Gets the instance_type of this AssociateInstanceGlobalEipRequestBodyGlobalEipAssociateInstanceInfo.

        支持绑定的实例类型

        :return: The instance_type of this AssociateInstanceGlobalEipRequestBodyGlobalEipAssociateInstanceInfo.
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        r"""Sets the instance_type of this AssociateInstanceGlobalEipRequestBodyGlobalEipAssociateInstanceInfo.

        支持绑定的实例类型

        :param instance_type: The instance_type of this AssociateInstanceGlobalEipRequestBodyGlobalEipAssociateInstanceInfo.
        :type instance_type: str
        """
        self._instance_type = instance_type

    @property
    def instance_id(self):
        r"""Gets the instance_id of this AssociateInstanceGlobalEipRequestBodyGlobalEipAssociateInstanceInfo.

        实例ID

        :return: The instance_id of this AssociateInstanceGlobalEipRequestBodyGlobalEipAssociateInstanceInfo.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this AssociateInstanceGlobalEipRequestBodyGlobalEipAssociateInstanceInfo.

        实例ID

        :param instance_id: The instance_id of this AssociateInstanceGlobalEipRequestBodyGlobalEipAssociateInstanceInfo.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def project_id(self):
        r"""Gets the project_id of this AssociateInstanceGlobalEipRequestBodyGlobalEipAssociateInstanceInfo.

        项目ID，获取项目ID请参见[获取项目ID](https://support.huaweicloud.com/api-vpc/vpc_api_0011.html)

        :return: The project_id of this AssociateInstanceGlobalEipRequestBodyGlobalEipAssociateInstanceInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this AssociateInstanceGlobalEipRequestBodyGlobalEipAssociateInstanceInfo.

        项目ID，获取项目ID请参见[获取项目ID](https://support.huaweicloud.com/api-vpc/vpc_api_0011.html)

        :param project_id: The project_id of this AssociateInstanceGlobalEipRequestBodyGlobalEipAssociateInstanceInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def service_id(self):
        r"""Gets the service_id of this AssociateInstanceGlobalEipRequestBodyGlobalEipAssociateInstanceInfo.

        服务id

        :return: The service_id of this AssociateInstanceGlobalEipRequestBodyGlobalEipAssociateInstanceInfo.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        r"""Sets the service_id of this AssociateInstanceGlobalEipRequestBodyGlobalEipAssociateInstanceInfo.

        服务id

        :param service_id: The service_id of this AssociateInstanceGlobalEipRequestBodyGlobalEipAssociateInstanceInfo.
        :type service_id: str
        """
        self._service_id = service_id

    @property
    def service_type(self):
        r"""Gets the service_type of this AssociateInstanceGlobalEipRequestBodyGlobalEipAssociateInstanceInfo.

        服务类型

        :return: The service_type of this AssociateInstanceGlobalEipRequestBodyGlobalEipAssociateInstanceInfo.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        r"""Sets the service_type of this AssociateInstanceGlobalEipRequestBodyGlobalEipAssociateInstanceInfo.

        服务类型

        :param service_type: The service_type of this AssociateInstanceGlobalEipRequestBodyGlobalEipAssociateInstanceInfo.
        :type service_type: str
        """
        self._service_type = service_type

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
        if not isinstance(other, AssociateInstanceGlobalEipRequestBodyGlobalEipAssociateInstanceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
