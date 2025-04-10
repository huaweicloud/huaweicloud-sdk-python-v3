# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDataServiceInstancesDetailResponse(SdkResponse):

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
        'instances': 'list[InstanceDetailDTO]'
    }

    attribute_map = {
        'total': 'total',
        'instances': 'instances'
    }

    def __init__(self, total=None, instances=None):
        r"""ListDataServiceInstancesDetailResponse

        The model defined in huaweicloud sdk

        :param total: 集群数量。
        :type total: int
        :param instances: 集群概览信息。
        :type instances: list[:class:`huaweicloudsdkdataartsstudio.v1.InstanceDetailDTO`]
        """
        
        super(ListDataServiceInstancesDetailResponse, self).__init__()

        self._total = None
        self._instances = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if instances is not None:
            self.instances = instances

    @property
    def total(self):
        r"""Gets the total of this ListDataServiceInstancesDetailResponse.

        集群数量。

        :return: The total of this ListDataServiceInstancesDetailResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListDataServiceInstancesDetailResponse.

        集群数量。

        :param total: The total of this ListDataServiceInstancesDetailResponse.
        :type total: int
        """
        self._total = total

    @property
    def instances(self):
        r"""Gets the instances of this ListDataServiceInstancesDetailResponse.

        集群概览信息。

        :return: The instances of this ListDataServiceInstancesDetailResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.InstanceDetailDTO`]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        r"""Sets the instances of this ListDataServiceInstancesDetailResponse.

        集群概览信息。

        :param instances: The instances of this ListDataServiceInstancesDetailResponse.
        :type instances: list[:class:`huaweicloudsdkdataartsstudio.v1.InstanceDetailDTO`]
        """
        self._instances = instances

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
        if not isinstance(other, ListDataServiceInstancesDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
