# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDataServiceInstancesOverviewResponse(SdkResponse):

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
        'scale_down': 'bool',
        'scale_out': 'bool',
        'instances': 'list[InstanceOverviewDTO]'
    }

    attribute_map = {
        'total': 'total',
        'scale_down': 'scale_down',
        'scale_out': 'scale_out',
        'instances': 'instances'
    }

    def __init__(self, total=None, scale_down=None, scale_out=None, instances=None):
        """ListDataServiceInstancesOverviewResponse

        The model defined in huaweicloud sdk

        :param total: 集群数量。
        :type total: int
        :param scale_down: 是否支持缩容。
        :type scale_down: bool
        :param scale_out: 是否支持扩容。
        :type scale_out: bool
        :param instances: 集群概览信息。
        :type instances: list[:class:`huaweicloudsdkdataartsstudio.v1.InstanceOverviewDTO`]
        """
        
        super(ListDataServiceInstancesOverviewResponse, self).__init__()

        self._total = None
        self._scale_down = None
        self._scale_out = None
        self._instances = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if scale_down is not None:
            self.scale_down = scale_down
        if scale_out is not None:
            self.scale_out = scale_out
        if instances is not None:
            self.instances = instances

    @property
    def total(self):
        """Gets the total of this ListDataServiceInstancesOverviewResponse.

        集群数量。

        :return: The total of this ListDataServiceInstancesOverviewResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListDataServiceInstancesOverviewResponse.

        集群数量。

        :param total: The total of this ListDataServiceInstancesOverviewResponse.
        :type total: int
        """
        self._total = total

    @property
    def scale_down(self):
        """Gets the scale_down of this ListDataServiceInstancesOverviewResponse.

        是否支持缩容。

        :return: The scale_down of this ListDataServiceInstancesOverviewResponse.
        :rtype: bool
        """
        return self._scale_down

    @scale_down.setter
    def scale_down(self, scale_down):
        """Sets the scale_down of this ListDataServiceInstancesOverviewResponse.

        是否支持缩容。

        :param scale_down: The scale_down of this ListDataServiceInstancesOverviewResponse.
        :type scale_down: bool
        """
        self._scale_down = scale_down

    @property
    def scale_out(self):
        """Gets the scale_out of this ListDataServiceInstancesOverviewResponse.

        是否支持扩容。

        :return: The scale_out of this ListDataServiceInstancesOverviewResponse.
        :rtype: bool
        """
        return self._scale_out

    @scale_out.setter
    def scale_out(self, scale_out):
        """Sets the scale_out of this ListDataServiceInstancesOverviewResponse.

        是否支持扩容。

        :param scale_out: The scale_out of this ListDataServiceInstancesOverviewResponse.
        :type scale_out: bool
        """
        self._scale_out = scale_out

    @property
    def instances(self):
        """Gets the instances of this ListDataServiceInstancesOverviewResponse.

        集群概览信息。

        :return: The instances of this ListDataServiceInstancesOverviewResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.InstanceOverviewDTO`]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """Sets the instances of this ListDataServiceInstancesOverviewResponse.

        集群概览信息。

        :param instances: The instances of this ListDataServiceInstancesOverviewResponse.
        :type instances: list[:class:`huaweicloudsdkdataartsstudio.v1.InstanceOverviewDTO`]
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
        if not isinstance(other, ListDataServiceInstancesOverviewResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
