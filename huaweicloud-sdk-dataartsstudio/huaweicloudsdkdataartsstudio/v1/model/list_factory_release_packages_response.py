# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFactoryReleasePackagesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data': 'list[ListReleasePackagesRespData]',
        'total': 'int',
        'x_request_id': 'str'
    }

    attribute_map = {
        'data': 'data',
        'total': 'total',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, data=None, total=None, x_request_id=None):
        r"""ListFactoryReleasePackagesResponse

        The model defined in huaweicloud sdk

        :param data: 发布包信息
        :type data: list[:class:`huaweicloudsdkdataartsstudio.v1.ListReleasePackagesRespData`]
        :param total: 发布包个数
        :type total: int
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListFactoryReleasePackagesResponse, self).__init__()

        self._data = None
        self._total = None
        self._x_request_id = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if total is not None:
            self.total = total
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def data(self):
        r"""Gets the data of this ListFactoryReleasePackagesResponse.

        发布包信息

        :return: The data of this ListFactoryReleasePackagesResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.ListReleasePackagesRespData`]
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this ListFactoryReleasePackagesResponse.

        发布包信息

        :param data: The data of this ListFactoryReleasePackagesResponse.
        :type data: list[:class:`huaweicloudsdkdataartsstudio.v1.ListReleasePackagesRespData`]
        """
        self._data = data

    @property
    def total(self):
        r"""Gets the total of this ListFactoryReleasePackagesResponse.

        发布包个数

        :return: The total of this ListFactoryReleasePackagesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListFactoryReleasePackagesResponse.

        发布包个数

        :param total: The total of this ListFactoryReleasePackagesResponse.
        :type total: int
        """
        self._total = total

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ListFactoryReleasePackagesResponse.

        :return: The x_request_id of this ListFactoryReleasePackagesResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ListFactoryReleasePackagesResponse.

        :param x_request_id: The x_request_id of this ListFactoryReleasePackagesResponse.
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
        if not isinstance(other, ListFactoryReleasePackagesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
