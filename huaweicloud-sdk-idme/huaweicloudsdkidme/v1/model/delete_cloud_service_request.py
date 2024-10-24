# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteCloudServiceRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service_type': 'str',
        'instance_id': 'str'
    }

    attribute_map = {
        'service_type': 'service_type',
        'instance_id': 'instance_id'
    }

    def __init__(self, service_type=None, instance_id=None):
        """DeleteCloudServiceRequest

        The model defined in huaweicloud sdk

        :param service_type: iDME服务的类型。  说明：目前仅支持删除CLOUD_LINK按需资源  示例：CLOUD_LINKX
        :type service_type: str
        :param instance_id: 待删除的实例ID。
        :type instance_id: str
        """
        
        

        self._service_type = None
        self._instance_id = None
        self.discriminator = None

        self.service_type = service_type
        self.instance_id = instance_id

    @property
    def service_type(self):
        """Gets the service_type of this DeleteCloudServiceRequest.

        iDME服务的类型。  说明：目前仅支持删除CLOUD_LINK按需资源  示例：CLOUD_LINKX

        :return: The service_type of this DeleteCloudServiceRequest.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this DeleteCloudServiceRequest.

        iDME服务的类型。  说明：目前仅支持删除CLOUD_LINK按需资源  示例：CLOUD_LINKX

        :param service_type: The service_type of this DeleteCloudServiceRequest.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def instance_id(self):
        """Gets the instance_id of this DeleteCloudServiceRequest.

        待删除的实例ID。

        :return: The instance_id of this DeleteCloudServiceRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this DeleteCloudServiceRequest.

        待删除的实例ID。

        :param instance_id: The instance_id of this DeleteCloudServiceRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

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
        if not isinstance(other, DeleteCloudServiceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
