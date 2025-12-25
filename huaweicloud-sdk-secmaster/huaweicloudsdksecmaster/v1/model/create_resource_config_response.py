# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateResourceConfigResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'datasets': 'list[DatasetItem]'
    }

    attribute_map = {
        'datasets': 'datasets'
    }

    def __init__(self, datasets=None):
        r"""CreateResourceConfigResponse

        The model defined in huaweicloud sdk

        :param datasets: 数据集列表，包含多个数据集对象
        :type datasets: list[:class:`huaweicloudsdksecmaster.v1.DatasetItem`]
        """
        
        super().__init__()

        self._datasets = None
        self.discriminator = None

        if datasets is not None:
            self.datasets = datasets

    @property
    def datasets(self):
        r"""Gets the datasets of this CreateResourceConfigResponse.

        数据集列表，包含多个数据集对象

        :return: The datasets of this CreateResourceConfigResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.DatasetItem`]
        """
        return self._datasets

    @datasets.setter
    def datasets(self, datasets):
        r"""Sets the datasets of this CreateResourceConfigResponse.

        数据集列表，包含多个数据集对象

        :param datasets: The datasets of this CreateResourceConfigResponse.
        :type datasets: list[:class:`huaweicloudsdksecmaster.v1.DatasetItem`]
        """
        self._datasets = datasets

    def to_dict(self):
        import warnings
        warnings.warn("CreateResourceConfigResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, CreateResourceConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
