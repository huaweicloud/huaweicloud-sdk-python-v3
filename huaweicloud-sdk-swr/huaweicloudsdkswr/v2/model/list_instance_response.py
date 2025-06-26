# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instances': 'list[Instance]',
        'total': 'int'
    }

    attribute_map = {
        'instances': 'instances',
        'total': 'total'
    }

    def __init__(self, instances=None, total=None):
        r"""ListInstanceResponse

        The model defined in huaweicloud sdk

        :param instances: 实例列表
        :type instances: list[:class:`huaweicloudsdkswr.v2.Instance`]
        :param total: 实例总数
        :type total: int
        """
        
        super(ListInstanceResponse, self).__init__()

        self._instances = None
        self._total = None
        self.discriminator = None

        if instances is not None:
            self.instances = instances
        if total is not None:
            self.total = total

    @property
    def instances(self):
        r"""Gets the instances of this ListInstanceResponse.

        实例列表

        :return: The instances of this ListInstanceResponse.
        :rtype: list[:class:`huaweicloudsdkswr.v2.Instance`]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        r"""Sets the instances of this ListInstanceResponse.

        实例列表

        :param instances: The instances of this ListInstanceResponse.
        :type instances: list[:class:`huaweicloudsdkswr.v2.Instance`]
        """
        self._instances = instances

    @property
    def total(self):
        r"""Gets the total of this ListInstanceResponse.

        实例总数

        :return: The total of this ListInstanceResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListInstanceResponse.

        实例总数

        :param total: The total of this ListInstanceResponse.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, ListInstanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
