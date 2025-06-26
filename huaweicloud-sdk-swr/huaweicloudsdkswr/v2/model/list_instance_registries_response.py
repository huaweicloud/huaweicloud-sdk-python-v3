# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceRegistriesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'registries': 'list[Registry]',
        'total': 'int'
    }

    attribute_map = {
        'registries': 'registries',
        'total': 'total'
    }

    def __init__(self, registries=None, total=None):
        r"""ListInstanceRegistriesResponse

        The model defined in huaweicloud sdk

        :param registries: 同步仓库列表
        :type registries: list[:class:`huaweicloudsdkswr.v2.Registry`]
        :param total: 同步仓库总数
        :type total: int
        """
        
        super(ListInstanceRegistriesResponse, self).__init__()

        self._registries = None
        self._total = None
        self.discriminator = None

        if registries is not None:
            self.registries = registries
        if total is not None:
            self.total = total

    @property
    def registries(self):
        r"""Gets the registries of this ListInstanceRegistriesResponse.

        同步仓库列表

        :return: The registries of this ListInstanceRegistriesResponse.
        :rtype: list[:class:`huaweicloudsdkswr.v2.Registry`]
        """
        return self._registries

    @registries.setter
    def registries(self, registries):
        r"""Sets the registries of this ListInstanceRegistriesResponse.

        同步仓库列表

        :param registries: The registries of this ListInstanceRegistriesResponse.
        :type registries: list[:class:`huaweicloudsdkswr.v2.Registry`]
        """
        self._registries = registries

    @property
    def total(self):
        r"""Gets the total of this ListInstanceRegistriesResponse.

        同步仓库总数

        :return: The total of this ListInstanceRegistriesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListInstanceRegistriesResponse.

        同步仓库总数

        :param total: The total of this ListInstanceRegistriesResponse.
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
        if not isinstance(other, ListInstanceRegistriesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
