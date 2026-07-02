# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListConfsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'confs': 'list[Confs]',
        'total_size': 'int'
    }

    attribute_map = {
        'confs': 'confs',
        'total_size': 'totalSize'
    }

    def __init__(self, confs=None, total_size=None):
        r"""ListConfsResponse

        The model defined in huaweicloud sdk

        :param confs: 配置文件列表。
        :type confs: list[:class:`huaweicloudsdkcss.v1.Confs`]
        :param total_size: 
        :type total_size: int
        """
        
        super().__init__()

        self._confs = None
        self._total_size = None
        self.discriminator = None

        if confs is not None:
            self.confs = confs
        if total_size is not None:
            self.total_size = total_size

    @property
    def confs(self):
        r"""Gets the confs of this ListConfsResponse.

        配置文件列表。

        :return: The confs of this ListConfsResponse.
        :rtype: list[:class:`huaweicloudsdkcss.v1.Confs`]
        """
        return self._confs

    @confs.setter
    def confs(self, confs):
        r"""Sets the confs of this ListConfsResponse.

        配置文件列表。

        :param confs: The confs of this ListConfsResponse.
        :type confs: list[:class:`huaweicloudsdkcss.v1.Confs`]
        """
        self._confs = confs

    @property
    def total_size(self):
        r"""Gets the total_size of this ListConfsResponse.

        :return: The total_size of this ListConfsResponse.
        :rtype: int
        """
        return self._total_size

    @total_size.setter
    def total_size(self, total_size):
        r"""Sets the total_size of this ListConfsResponse.

        :param total_size: The total_size of this ListConfsResponse.
        :type total_size: int
        """
        self._total_size = total_size

    def to_dict(self):
        import warnings
        warnings.warn("ListConfsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListConfsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
