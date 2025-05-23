# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAvailabilityZonesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'public_border_group': 'str',
        'loadbalancer_id': 'str'
    }

    attribute_map = {
        'public_border_group': 'public_border_group',
        'loadbalancer_id': 'loadbalancer_id'
    }

    def __init__(self, public_border_group=None, loadbalancer_id=None):
        r"""ListAvailabilityZonesRequest

        The model defined in huaweicloud sdk

        :param public_border_group: 参数解释：网络公共边界组。
        :type public_border_group: str
        :param loadbalancer_id: 参数解释：负载均衡器ID。
        :type loadbalancer_id: str
        """
        
        

        self._public_border_group = None
        self._loadbalancer_id = None
        self.discriminator = None

        if public_border_group is not None:
            self.public_border_group = public_border_group
        if loadbalancer_id is not None:
            self.loadbalancer_id = loadbalancer_id

    @property
    def public_border_group(self):
        r"""Gets the public_border_group of this ListAvailabilityZonesRequest.

        参数解释：网络公共边界组。

        :return: The public_border_group of this ListAvailabilityZonesRequest.
        :rtype: str
        """
        return self._public_border_group

    @public_border_group.setter
    def public_border_group(self, public_border_group):
        r"""Sets the public_border_group of this ListAvailabilityZonesRequest.

        参数解释：网络公共边界组。

        :param public_border_group: The public_border_group of this ListAvailabilityZonesRequest.
        :type public_border_group: str
        """
        self._public_border_group = public_border_group

    @property
    def loadbalancer_id(self):
        r"""Gets the loadbalancer_id of this ListAvailabilityZonesRequest.

        参数解释：负载均衡器ID。

        :return: The loadbalancer_id of this ListAvailabilityZonesRequest.
        :rtype: str
        """
        return self._loadbalancer_id

    @loadbalancer_id.setter
    def loadbalancer_id(self, loadbalancer_id):
        r"""Sets the loadbalancer_id of this ListAvailabilityZonesRequest.

        参数解释：负载均衡器ID。

        :param loadbalancer_id: The loadbalancer_id of this ListAvailabilityZonesRequest.
        :type loadbalancer_id: str
        """
        self._loadbalancer_id = loadbalancer_id

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
        if not isinstance(other, ListAvailabilityZonesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
