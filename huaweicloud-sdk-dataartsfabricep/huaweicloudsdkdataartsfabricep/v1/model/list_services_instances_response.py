# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListServicesInstancesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'service_instances': 'list[ServiceInstanceBriefInfo]'
    }

    attribute_map = {
        'total': 'total',
        'service_instances': 'service_instances'
    }

    def __init__(self, total=None, service_instances=None):
        r"""ListServicesInstancesResponse

        The model defined in huaweicloud sdk

        :param total: 符合条件的service Istance总数
        :type total: int
        :param service_instances: 符合条件的service Instance列表
        :type service_instances: list[:class:`huaweicloudsdkdataartsfabricep.v1.ServiceInstanceBriefInfo`]
        """
        
        super(ListServicesInstancesResponse, self).__init__()

        self._total = None
        self._service_instances = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if service_instances is not None:
            self.service_instances = service_instances

    @property
    def total(self):
        r"""Gets the total of this ListServicesInstancesResponse.

        符合条件的service Istance总数

        :return: The total of this ListServicesInstancesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListServicesInstancesResponse.

        符合条件的service Istance总数

        :param total: The total of this ListServicesInstancesResponse.
        :type total: int
        """
        self._total = total

    @property
    def service_instances(self):
        r"""Gets the service_instances of this ListServicesInstancesResponse.

        符合条件的service Instance列表

        :return: The service_instances of this ListServicesInstancesResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsfabricep.v1.ServiceInstanceBriefInfo`]
        """
        return self._service_instances

    @service_instances.setter
    def service_instances(self, service_instances):
        r"""Sets the service_instances of this ListServicesInstancesResponse.

        符合条件的service Instance列表

        :param service_instances: The service_instances of this ListServicesInstancesResponse.
        :type service_instances: list[:class:`huaweicloudsdkdataartsfabricep.v1.ServiceInstanceBriefInfo`]
        """
        self._service_instances = service_instances

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
        if not isinstance(other, ListServicesInstancesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
