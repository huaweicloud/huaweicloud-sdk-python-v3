# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssociateInstanceGlobalEipSegmentRequestBodyGlobalEipSegment:

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
        """AssociateInstanceGlobalEipSegmentRequestBodyGlobalEipSegment

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

        self.region = region
        self.instance_type = instance_type
        self.instance_id = instance_id
        self.project_id = project_id
        if service_id is not None:
            self.service_id = service_id
        if service_type is not None:
            self.service_type = service_type

    @property
    def region(self):
        """Gets the region of this AssociateInstanceGlobalEipSegmentRequestBodyGlobalEipSegment.

        region

        :return: The region of this AssociateInstanceGlobalEipSegmentRequestBodyGlobalEipSegment.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this AssociateInstanceGlobalEipSegmentRequestBodyGlobalEipSegment.

        region

        :param region: The region of this AssociateInstanceGlobalEipSegmentRequestBodyGlobalEipSegment.
        :type region: str
        """
        self._region = region

    @property
    def instance_type(self):
        """Gets the instance_type of this AssociateInstanceGlobalEipSegmentRequestBodyGlobalEipSegment.

        支持绑定的实例类型

        :return: The instance_type of this AssociateInstanceGlobalEipSegmentRequestBodyGlobalEipSegment.
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this AssociateInstanceGlobalEipSegmentRequestBodyGlobalEipSegment.

        支持绑定的实例类型

        :param instance_type: The instance_type of this AssociateInstanceGlobalEipSegmentRequestBodyGlobalEipSegment.
        :type instance_type: str
        """
        self._instance_type = instance_type

    @property
    def instance_id(self):
        """Gets the instance_id of this AssociateInstanceGlobalEipSegmentRequestBodyGlobalEipSegment.

        实例ID

        :return: The instance_id of this AssociateInstanceGlobalEipSegmentRequestBodyGlobalEipSegment.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this AssociateInstanceGlobalEipSegmentRequestBodyGlobalEipSegment.

        实例ID

        :param instance_id: The instance_id of this AssociateInstanceGlobalEipSegmentRequestBodyGlobalEipSegment.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def project_id(self):
        """Gets the project_id of this AssociateInstanceGlobalEipSegmentRequestBodyGlobalEipSegment.

        项目ID，获取项目ID请参见[获取项目ID](https://support.huaweicloud.com/api-vpc/vpc_api_0011.html)

        :return: The project_id of this AssociateInstanceGlobalEipSegmentRequestBodyGlobalEipSegment.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this AssociateInstanceGlobalEipSegmentRequestBodyGlobalEipSegment.

        项目ID，获取项目ID请参见[获取项目ID](https://support.huaweicloud.com/api-vpc/vpc_api_0011.html)

        :param project_id: The project_id of this AssociateInstanceGlobalEipSegmentRequestBodyGlobalEipSegment.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def service_id(self):
        """Gets the service_id of this AssociateInstanceGlobalEipSegmentRequestBodyGlobalEipSegment.

        服务id

        :return: The service_id of this AssociateInstanceGlobalEipSegmentRequestBodyGlobalEipSegment.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this AssociateInstanceGlobalEipSegmentRequestBodyGlobalEipSegment.

        服务id

        :param service_id: The service_id of this AssociateInstanceGlobalEipSegmentRequestBodyGlobalEipSegment.
        :type service_id: str
        """
        self._service_id = service_id

    @property
    def service_type(self):
        """Gets the service_type of this AssociateInstanceGlobalEipSegmentRequestBodyGlobalEipSegment.

        服务类型

        :return: The service_type of this AssociateInstanceGlobalEipSegmentRequestBodyGlobalEipSegment.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this AssociateInstanceGlobalEipSegmentRequestBodyGlobalEipSegment.

        服务类型

        :param service_type: The service_type of this AssociateInstanceGlobalEipSegmentRequestBodyGlobalEipSegment.
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
        if not isinstance(other, AssociateInstanceGlobalEipSegmentRequestBodyGlobalEipSegment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
