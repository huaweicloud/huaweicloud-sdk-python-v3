# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCapacityViewResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data': 'list[CapacityOverviewResponseData]'
    }

    attribute_map = {
        'data': 'data'
    }

    def __init__(self, data=None):
        r"""ListCapacityViewResponse

        The model defined in huaweicloud sdk

        :param data: **参数解释：** 容量数据列表。 **取值范围：** 查询已选应用下的云服务容量数据组成列表，大小在0到500之间。
        :type data: list[:class:`huaweicloudsdkcoc.v1.CapacityOverviewResponseData`]
        """
        
        super().__init__()

        self._data = None
        self.discriminator = None

        if data is not None:
            self.data = data

    @property
    def data(self):
        r"""Gets the data of this ListCapacityViewResponse.

        **参数解释：** 容量数据列表。 **取值范围：** 查询已选应用下的云服务容量数据组成列表，大小在0到500之间。

        :return: The data of this ListCapacityViewResponse.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.CapacityOverviewResponseData`]
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this ListCapacityViewResponse.

        **参数解释：** 容量数据列表。 **取值范围：** 查询已选应用下的云服务容量数据组成列表，大小在0到500之间。

        :param data: The data of this ListCapacityViewResponse.
        :type data: list[:class:`huaweicloudsdkcoc.v1.CapacityOverviewResponseData`]
        """
        self._data = data

    def to_dict(self):
        import warnings
        warnings.warn("ListCapacityViewResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListCapacityViewResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
