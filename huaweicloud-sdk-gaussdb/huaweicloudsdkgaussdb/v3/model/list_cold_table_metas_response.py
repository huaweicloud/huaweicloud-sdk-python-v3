# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListColdTableMetasResponse(SdkResponse):

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
        'meta_info': 'list[ColdTableMetaInfo]',
        'total_data_size': 'float'
    }

    attribute_map = {
        'total': 'total',
        'meta_info': 'meta_info',
        'total_data_size': 'total_data_size'
    }

    def __init__(self, total=None, meta_info=None, total_data_size=None):
        r"""ListColdTableMetasResponse

        The model defined in huaweicloud sdk

        :param total: **参数解释**：  冷表元信息记录总数。  **取值范围**：  ≥0。
        :type total: int
        :param meta_info: **参数解释**：  冷表元记录列表。
        :type meta_info: list[:class:`huaweicloudsdkgaussdb.v3.ColdTableMetaInfo`]
        :param total_data_size: **参数解释**：  冷表数据量总大小（MB）。  **取值范围**：  ≥0。
        :type total_data_size: float
        """
        
        super().__init__()

        self._total = None
        self._meta_info = None
        self._total_data_size = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if meta_info is not None:
            self.meta_info = meta_info
        if total_data_size is not None:
            self.total_data_size = total_data_size

    @property
    def total(self):
        r"""Gets the total of this ListColdTableMetasResponse.

        **参数解释**：  冷表元信息记录总数。  **取值范围**：  ≥0。

        :return: The total of this ListColdTableMetasResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListColdTableMetasResponse.

        **参数解释**：  冷表元信息记录总数。  **取值范围**：  ≥0。

        :param total: The total of this ListColdTableMetasResponse.
        :type total: int
        """
        self._total = total

    @property
    def meta_info(self):
        r"""Gets the meta_info of this ListColdTableMetasResponse.

        **参数解释**：  冷表元记录列表。

        :return: The meta_info of this ListColdTableMetasResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.ColdTableMetaInfo`]
        """
        return self._meta_info

    @meta_info.setter
    def meta_info(self, meta_info):
        r"""Sets the meta_info of this ListColdTableMetasResponse.

        **参数解释**：  冷表元记录列表。

        :param meta_info: The meta_info of this ListColdTableMetasResponse.
        :type meta_info: list[:class:`huaweicloudsdkgaussdb.v3.ColdTableMetaInfo`]
        """
        self._meta_info = meta_info

    @property
    def total_data_size(self):
        r"""Gets the total_data_size of this ListColdTableMetasResponse.

        **参数解释**：  冷表数据量总大小（MB）。  **取值范围**：  ≥0。

        :return: The total_data_size of this ListColdTableMetasResponse.
        :rtype: float
        """
        return self._total_data_size

    @total_data_size.setter
    def total_data_size(self, total_data_size):
        r"""Sets the total_data_size of this ListColdTableMetasResponse.

        **参数解释**：  冷表数据量总大小（MB）。  **取值范围**：  ≥0。

        :param total_data_size: The total_data_size of this ListColdTableMetasResponse.
        :type total_data_size: float
        """
        self._total_data_size = total_data_size

    def to_dict(self):
        import warnings
        warnings.warn("ListColdTableMetasResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListColdTableMetasResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
