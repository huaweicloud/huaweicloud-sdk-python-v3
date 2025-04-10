# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEngineFlavorsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'optional_flavors': 'list[EngineFlavorData]',
        'total_count': 'int'
    }

    attribute_map = {
        'optional_flavors': 'optional_flavors',
        'total_count': 'total_count'
    }

    def __init__(self, optional_flavors=None, total_count=None):
        r"""ListEngineFlavorsResponse

        The model defined in huaweicloud sdk

        :param optional_flavors: 可用的规格列表信息
        :type optional_flavors: list[:class:`huaweicloudsdkrds.v3.EngineFlavorData`]
        :param total_count: 可用的规格总数
        :type total_count: int
        """
        
        super(ListEngineFlavorsResponse, self).__init__()

        self._optional_flavors = None
        self._total_count = None
        self.discriminator = None

        if optional_flavors is not None:
            self.optional_flavors = optional_flavors
        if total_count is not None:
            self.total_count = total_count

    @property
    def optional_flavors(self):
        r"""Gets the optional_flavors of this ListEngineFlavorsResponse.

        可用的规格列表信息

        :return: The optional_flavors of this ListEngineFlavorsResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.EngineFlavorData`]
        """
        return self._optional_flavors

    @optional_flavors.setter
    def optional_flavors(self, optional_flavors):
        r"""Sets the optional_flavors of this ListEngineFlavorsResponse.

        可用的规格列表信息

        :param optional_flavors: The optional_flavors of this ListEngineFlavorsResponse.
        :type optional_flavors: list[:class:`huaweicloudsdkrds.v3.EngineFlavorData`]
        """
        self._optional_flavors = optional_flavors

    @property
    def total_count(self):
        r"""Gets the total_count of this ListEngineFlavorsResponse.

        可用的规格总数

        :return: The total_count of this ListEngineFlavorsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListEngineFlavorsResponse.

        可用的规格总数

        :param total_count: The total_count of this ListEngineFlavorsResponse.
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
        if not isinstance(other, ListEngineFlavorsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
