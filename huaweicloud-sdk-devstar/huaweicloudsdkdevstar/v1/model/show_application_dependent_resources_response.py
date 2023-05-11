# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowApplicationDependentResourcesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dependent_services': 'list[ResouceInfo]',
        'count': 'int'
    }

    attribute_map = {
        'dependent_services': 'dependent_services',
        'count': 'count'
    }

    def __init__(self, dependent_services=None, count=None):
        """ShowApplicationDependentResourcesResponse

        The model defined in huaweicloud sdk

        :param dependent_services: 依赖云资源信息
        :type dependent_services: list[:class:`huaweicloudsdkdevstar.v1.ResouceInfo`]
        :param count: 资源总个数
        :type count: int
        """
        
        super(ShowApplicationDependentResourcesResponse, self).__init__()

        self._dependent_services = None
        self._count = None
        self.discriminator = None

        if dependent_services is not None:
            self.dependent_services = dependent_services
        if count is not None:
            self.count = count

    @property
    def dependent_services(self):
        """Gets the dependent_services of this ShowApplicationDependentResourcesResponse.

        依赖云资源信息

        :return: The dependent_services of this ShowApplicationDependentResourcesResponse.
        :rtype: list[:class:`huaweicloudsdkdevstar.v1.ResouceInfo`]
        """
        return self._dependent_services

    @dependent_services.setter
    def dependent_services(self, dependent_services):
        """Sets the dependent_services of this ShowApplicationDependentResourcesResponse.

        依赖云资源信息

        :param dependent_services: The dependent_services of this ShowApplicationDependentResourcesResponse.
        :type dependent_services: list[:class:`huaweicloudsdkdevstar.v1.ResouceInfo`]
        """
        self._dependent_services = dependent_services

    @property
    def count(self):
        """Gets the count of this ShowApplicationDependentResourcesResponse.

        资源总个数

        :return: The count of this ShowApplicationDependentResourcesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ShowApplicationDependentResourcesResponse.

        资源总个数

        :param count: The count of this ShowApplicationDependentResourcesResponse.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ShowApplicationDependentResourcesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
