# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAvailableRdsForMigrateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data_nodes': 'list[AvailableDnInstance]'
    }

    attribute_map = {
        'data_nodes': 'data_nodes'
    }

    def __init__(self, data_nodes=None):
        r"""ListAvailableRdsForMigrateResponse

        The model defined in huaweicloud sdk

        :param data_nodes: 可用后端DN信息。
        :type data_nodes: list[:class:`huaweicloudsdkddm.v1.AvailableDnInstance`]
        """
        
        super().__init__()

        self._data_nodes = None
        self.discriminator = None

        if data_nodes is not None:
            self.data_nodes = data_nodes

    @property
    def data_nodes(self):
        r"""Gets the data_nodes of this ListAvailableRdsForMigrateResponse.

        可用后端DN信息。

        :return: The data_nodes of this ListAvailableRdsForMigrateResponse.
        :rtype: list[:class:`huaweicloudsdkddm.v1.AvailableDnInstance`]
        """
        return self._data_nodes

    @data_nodes.setter
    def data_nodes(self, data_nodes):
        r"""Sets the data_nodes of this ListAvailableRdsForMigrateResponse.

        可用后端DN信息。

        :param data_nodes: The data_nodes of this ListAvailableRdsForMigrateResponse.
        :type data_nodes: list[:class:`huaweicloudsdkddm.v1.AvailableDnInstance`]
        """
        self._data_nodes = data_nodes

    def to_dict(self):
        import warnings
        warnings.warn("ListAvailableRdsForMigrateResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListAvailableRdsForMigrateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
