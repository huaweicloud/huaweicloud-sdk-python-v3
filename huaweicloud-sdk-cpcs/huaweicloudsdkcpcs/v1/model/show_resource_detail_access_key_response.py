# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowResourceDetailAccessKeyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metric_name': 'str',
        'ak_list': 'list[ShowResourceDetailAccessKeyResponseBodyAkList]',
        'total_count': 'int'
    }

    attribute_map = {
        'metric_name': 'metric_name',
        'ak_list': 'ak_list',
        'total_count': 'total_count'
    }

    def __init__(self, metric_name=None, ak_list=None, total_count=None):
        r"""ShowResourceDetailAccessKeyResponse

        The model defined in huaweicloud sdk

        :param metric_name: 资源名称
        :type metric_name: str
        :param ak_list: 访问密钥列表
        :type ak_list: list[:class:`huaweicloudsdkcpcs.v1.ShowResourceDetailAccessKeyResponseBodyAkList`]
        :param total_count: 访问密钥总数
        :type total_count: int
        """
        
        super().__init__()

        self._metric_name = None
        self._ak_list = None
        self._total_count = None
        self.discriminator = None

        if metric_name is not None:
            self.metric_name = metric_name
        if ak_list is not None:
            self.ak_list = ak_list
        if total_count is not None:
            self.total_count = total_count

    @property
    def metric_name(self):
        r"""Gets the metric_name of this ShowResourceDetailAccessKeyResponse.

        资源名称

        :return: The metric_name of this ShowResourceDetailAccessKeyResponse.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        r"""Sets the metric_name of this ShowResourceDetailAccessKeyResponse.

        资源名称

        :param metric_name: The metric_name of this ShowResourceDetailAccessKeyResponse.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def ak_list(self):
        r"""Gets the ak_list of this ShowResourceDetailAccessKeyResponse.

        访问密钥列表

        :return: The ak_list of this ShowResourceDetailAccessKeyResponse.
        :rtype: list[:class:`huaweicloudsdkcpcs.v1.ShowResourceDetailAccessKeyResponseBodyAkList`]
        """
        return self._ak_list

    @ak_list.setter
    def ak_list(self, ak_list):
        r"""Sets the ak_list of this ShowResourceDetailAccessKeyResponse.

        访问密钥列表

        :param ak_list: The ak_list of this ShowResourceDetailAccessKeyResponse.
        :type ak_list: list[:class:`huaweicloudsdkcpcs.v1.ShowResourceDetailAccessKeyResponseBodyAkList`]
        """
        self._ak_list = ak_list

    @property
    def total_count(self):
        r"""Gets the total_count of this ShowResourceDetailAccessKeyResponse.

        访问密钥总数

        :return: The total_count of this ShowResourceDetailAccessKeyResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ShowResourceDetailAccessKeyResponse.

        访问密钥总数

        :param total_count: The total_count of this ShowResourceDetailAccessKeyResponse.
        :type total_count: int
        """
        self._total_count = total_count

    def to_dict(self):
        import warnings
        warnings.warn("ShowResourceDetailAccessKeyResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowResourceDetailAccessKeyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
