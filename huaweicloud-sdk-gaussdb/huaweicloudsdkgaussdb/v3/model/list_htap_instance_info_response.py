# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHtapInstanceInfoResponse(SdkResponse):

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
        'instances': 'list[HtapInstanceListInstances]',
        'max_htap_instance_num_of_taurus': 'int'
    }

    attribute_map = {
        'total': 'total',
        'instances': 'instances',
        'max_htap_instance_num_of_taurus': 'max_htap_instance_num_of_taurus'
    }

    def __init__(self, total=None, instances=None, max_htap_instance_num_of_taurus=None):
        r"""ListHtapInstanceInfoResponse

        The model defined in huaweicloud sdk

        :param total: HTAP实例个数。
        :type total: int
        :param instances: HTAP实例信息。
        :type instances: list[:class:`huaweicloudsdkgaussdb.v3.HtapInstanceListInstances`]
        :param max_htap_instance_num_of_taurus: 最大HTAP实例个数。
        :type max_htap_instance_num_of_taurus: int
        """
        
        super(ListHtapInstanceInfoResponse, self).__init__()

        self._total = None
        self._instances = None
        self._max_htap_instance_num_of_taurus = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if instances is not None:
            self.instances = instances
        if max_htap_instance_num_of_taurus is not None:
            self.max_htap_instance_num_of_taurus = max_htap_instance_num_of_taurus

    @property
    def total(self):
        r"""Gets the total of this ListHtapInstanceInfoResponse.

        HTAP实例个数。

        :return: The total of this ListHtapInstanceInfoResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListHtapInstanceInfoResponse.

        HTAP实例个数。

        :param total: The total of this ListHtapInstanceInfoResponse.
        :type total: int
        """
        self._total = total

    @property
    def instances(self):
        r"""Gets the instances of this ListHtapInstanceInfoResponse.

        HTAP实例信息。

        :return: The instances of this ListHtapInstanceInfoResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.HtapInstanceListInstances`]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        r"""Sets the instances of this ListHtapInstanceInfoResponse.

        HTAP实例信息。

        :param instances: The instances of this ListHtapInstanceInfoResponse.
        :type instances: list[:class:`huaweicloudsdkgaussdb.v3.HtapInstanceListInstances`]
        """
        self._instances = instances

    @property
    def max_htap_instance_num_of_taurus(self):
        r"""Gets the max_htap_instance_num_of_taurus of this ListHtapInstanceInfoResponse.

        最大HTAP实例个数。

        :return: The max_htap_instance_num_of_taurus of this ListHtapInstanceInfoResponse.
        :rtype: int
        """
        return self._max_htap_instance_num_of_taurus

    @max_htap_instance_num_of_taurus.setter
    def max_htap_instance_num_of_taurus(self, max_htap_instance_num_of_taurus):
        r"""Sets the max_htap_instance_num_of_taurus of this ListHtapInstanceInfoResponse.

        最大HTAP实例个数。

        :param max_htap_instance_num_of_taurus: The max_htap_instance_num_of_taurus of this ListHtapInstanceInfoResponse.
        :type max_htap_instance_num_of_taurus: int
        """
        self._max_htap_instance_num_of_taurus = max_htap_instance_num_of_taurus

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
        if not isinstance(other, ListHtapInstanceInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
