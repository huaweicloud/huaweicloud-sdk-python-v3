# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSpecsResponse(SdkResponse):

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
        'spec_codes': 'list[Spec]'
    }

    attribute_map = {
        'total': 'total',
        'spec_codes': 'spec_codes'
    }

    def __init__(self, total=None, spec_codes=None):
        """ListSpecsResponse

        The model defined in huaweicloud sdk

        :param total: 总数
        :type total: int
        :param spec_codes: 规格编码列表
        :type spec_codes: list[:class:`huaweicloudsdklakeformation.v1.Spec`]
        """
        
        super(ListSpecsResponse, self).__init__()

        self._total = None
        self._spec_codes = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if spec_codes is not None:
            self.spec_codes = spec_codes

    @property
    def total(self):
        """Gets the total of this ListSpecsResponse.

        总数

        :return: The total of this ListSpecsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListSpecsResponse.

        总数

        :param total: The total of this ListSpecsResponse.
        :type total: int
        """
        self._total = total

    @property
    def spec_codes(self):
        """Gets the spec_codes of this ListSpecsResponse.

        规格编码列表

        :return: The spec_codes of this ListSpecsResponse.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.Spec`]
        """
        return self._spec_codes

    @spec_codes.setter
    def spec_codes(self, spec_codes):
        """Sets the spec_codes of this ListSpecsResponse.

        规格编码列表

        :param spec_codes: The spec_codes of this ListSpecsResponse.
        :type spec_codes: list[:class:`huaweicloudsdklakeformation.v1.Spec`]
        """
        self._spec_codes = spec_codes

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
        if not isinstance(other, ListSpecsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
