# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListServicesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'services': 'list[ServiceRespDetail]'
    }

    attribute_map = {
        'count': 'count',
        'services': 'services'
    }

    def __init__(self, count=None, services=None):
        r"""ListServicesResponse

        The model defined in huaweicloud sdk

        :param count: 满足条件的端点个数
        :type count: int
        :param services: 服务列表
        :type services: list[:class:`huaweicloudsdkief.v1.ServiceRespDetail`]
        """
        
        super(ListServicesResponse, self).__init__()

        self._count = None
        self._services = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if services is not None:
            self.services = services

    @property
    def count(self):
        r"""Gets the count of this ListServicesResponse.

        满足条件的端点个数

        :return: The count of this ListServicesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListServicesResponse.

        满足条件的端点个数

        :param count: The count of this ListServicesResponse.
        :type count: int
        """
        self._count = count

    @property
    def services(self):
        r"""Gets the services of this ListServicesResponse.

        服务列表

        :return: The services of this ListServicesResponse.
        :rtype: list[:class:`huaweicloudsdkief.v1.ServiceRespDetail`]
        """
        return self._services

    @services.setter
    def services(self, services):
        r"""Sets the services of this ListServicesResponse.

        服务列表

        :param services: The services of this ListServicesResponse.
        :type services: list[:class:`huaweicloudsdkief.v1.ServiceRespDetail`]
        """
        self._services = services

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
        if not isinstance(other, ListServicesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
