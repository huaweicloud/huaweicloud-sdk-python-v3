# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListModelVersionsResponse(SdkResponse):

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
        'versions': 'list[ModelVersionInfo]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'total': 'total',
        'versions': 'versions',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, total=None, versions=None, x_request_id=None):
        r"""ListModelVersionsResponse

        The model defined in huaweicloud sdk

        :param total: 符合条件的Version总数
        :type total: int
        :param versions: 列表信息
        :type versions: list[:class:`huaweicloudsdkdataartsfabric.v1.ModelVersionInfo`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListModelVersionsResponse, self).__init__()

        self._total = None
        self._versions = None
        self._x_request_id = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if versions is not None:
            self.versions = versions
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def total(self):
        r"""Gets the total of this ListModelVersionsResponse.

        符合条件的Version总数

        :return: The total of this ListModelVersionsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListModelVersionsResponse.

        符合条件的Version总数

        :param total: The total of this ListModelVersionsResponse.
        :type total: int
        """
        self._total = total

    @property
    def versions(self):
        r"""Gets the versions of this ListModelVersionsResponse.

        列表信息

        :return: The versions of this ListModelVersionsResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsfabric.v1.ModelVersionInfo`]
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        r"""Sets the versions of this ListModelVersionsResponse.

        列表信息

        :param versions: The versions of this ListModelVersionsResponse.
        :type versions: list[:class:`huaweicloudsdkdataartsfabric.v1.ModelVersionInfo`]
        """
        self._versions = versions

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ListModelVersionsResponse.

        :return: The x_request_id of this ListModelVersionsResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ListModelVersionsResponse.

        :param x_request_id: The x_request_id of this ListModelVersionsResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ListModelVersionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
