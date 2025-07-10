# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAdOusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ou_infos': 'list[AdOuInfo]',
        'total_count': 'int'
    }

    attribute_map = {
        'ou_infos': 'ou_infos',
        'total_count': 'total_count'
    }

    def __init__(self, ou_infos=None, total_count=None):
        r"""ListAdOusResponse

        The model defined in huaweicloud sdk

        :param ou_infos: OU对象。
        :type ou_infos: list[:class:`huaweicloudsdkworkspace.v2.AdOuInfo`]
        :param total_count: OU总记录数。
        :type total_count: int
        """
        
        super(ListAdOusResponse, self).__init__()

        self._ou_infos = None
        self._total_count = None
        self.discriminator = None

        if ou_infos is not None:
            self.ou_infos = ou_infos
        if total_count is not None:
            self.total_count = total_count

    @property
    def ou_infos(self):
        r"""Gets the ou_infos of this ListAdOusResponse.

        OU对象。

        :return: The ou_infos of this ListAdOusResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.AdOuInfo`]
        """
        return self._ou_infos

    @ou_infos.setter
    def ou_infos(self, ou_infos):
        r"""Sets the ou_infos of this ListAdOusResponse.

        OU对象。

        :param ou_infos: The ou_infos of this ListAdOusResponse.
        :type ou_infos: list[:class:`huaweicloudsdkworkspace.v2.AdOuInfo`]
        """
        self._ou_infos = ou_infos

    @property
    def total_count(self):
        r"""Gets the total_count of this ListAdOusResponse.

        OU总记录数。

        :return: The total_count of this ListAdOusResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListAdOusResponse.

        OU总记录数。

        :param total_count: The total_count of this ListAdOusResponse.
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
        if not isinstance(other, ListAdOusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
