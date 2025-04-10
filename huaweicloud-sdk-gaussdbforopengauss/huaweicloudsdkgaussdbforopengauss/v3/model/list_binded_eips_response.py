# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBindedEipsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'public_ips': 'list[BindedEipResult]',
        'total_count': 'int'
    }

    attribute_map = {
        'public_ips': 'public_ips',
        'total_count': 'total_count'
    }

    def __init__(self, public_ips=None, total_count=None):
        r"""ListBindedEipsResponse

        The model defined in huaweicloud sdk

        :param public_ips: 查询实例已绑定EIP列表。
        :type public_ips: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.BindedEipResult`]
        :param total_count: 总记录数。
        :type total_count: int
        """
        
        super(ListBindedEipsResponse, self).__init__()

        self._public_ips = None
        self._total_count = None
        self.discriminator = None

        if public_ips is not None:
            self.public_ips = public_ips
        if total_count is not None:
            self.total_count = total_count

    @property
    def public_ips(self):
        r"""Gets the public_ips of this ListBindedEipsResponse.

        查询实例已绑定EIP列表。

        :return: The public_ips of this ListBindedEipsResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.BindedEipResult`]
        """
        return self._public_ips

    @public_ips.setter
    def public_ips(self, public_ips):
        r"""Sets the public_ips of this ListBindedEipsResponse.

        查询实例已绑定EIP列表。

        :param public_ips: The public_ips of this ListBindedEipsResponse.
        :type public_ips: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.BindedEipResult`]
        """
        self._public_ips = public_ips

    @property
    def total_count(self):
        r"""Gets the total_count of this ListBindedEipsResponse.

        总记录数。

        :return: The total_count of this ListBindedEipsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListBindedEipsResponse.

        总记录数。

        :param total_count: The total_count of this ListBindedEipsResponse.
        :type total_count: int
        """
        self._total_count = total_count

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
        if not isinstance(other, ListBindedEipsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
