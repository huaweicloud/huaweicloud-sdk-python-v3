# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInferDeploymentsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data': 'list[InferDeploymentItemResponseData]',
        'current': 'int',
        'size': 'int',
        'pages': 'int',
        'total': 'int'
    }

    attribute_map = {
        'data': 'data',
        'current': 'current',
        'size': 'size',
        'pages': 'pages',
        'total': 'total'
    }

    def __init__(self, data=None, current=None, size=None, pages=None, total=None):
        r"""ListInferDeploymentsResponse

        The model defined in huaweicloud sdk

        :param data: **参数解释：** 在线服务数据。
        :type data: list[:class:`huaweicloudsdkmodelarts.v1.InferDeploymentItemResponseData`]
        :param current: **参数解释：** 当前页码，从0开始计数。 **取值范围：** 不涉及。
        :type current: int
        :param size: **参数解释：** 当前页数量。 **取值范围：** 不涉及。
        :type size: int
        :param pages: **参数解释：** 总页数，根据传入的limit字段和数据总条数计算得出。如总记录条数为10，limit（单页最大条目数）为3，则页数为4。 **取值范围：** 不涉及。
        :type pages: int
        :param total: **参数解释：** 总记录条数。 **取值范围：** 不涉及。
        :type total: int
        """
        
        super().__init__()

        self._data = None
        self._current = None
        self._size = None
        self._pages = None
        self._total = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if current is not None:
            self.current = current
        if size is not None:
            self.size = size
        if pages is not None:
            self.pages = pages
        if total is not None:
            self.total = total

    @property
    def data(self):
        r"""Gets the data of this ListInferDeploymentsResponse.

        **参数解释：** 在线服务数据。

        :return: The data of this ListInferDeploymentsResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.InferDeploymentItemResponseData`]
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this ListInferDeploymentsResponse.

        **参数解释：** 在线服务数据。

        :param data: The data of this ListInferDeploymentsResponse.
        :type data: list[:class:`huaweicloudsdkmodelarts.v1.InferDeploymentItemResponseData`]
        """
        self._data = data

    @property
    def current(self):
        r"""Gets the current of this ListInferDeploymentsResponse.

        **参数解释：** 当前页码，从0开始计数。 **取值范围：** 不涉及。

        :return: The current of this ListInferDeploymentsResponse.
        :rtype: int
        """
        return self._current

    @current.setter
    def current(self, current):
        r"""Sets the current of this ListInferDeploymentsResponse.

        **参数解释：** 当前页码，从0开始计数。 **取值范围：** 不涉及。

        :param current: The current of this ListInferDeploymentsResponse.
        :type current: int
        """
        self._current = current

    @property
    def size(self):
        r"""Gets the size of this ListInferDeploymentsResponse.

        **参数解释：** 当前页数量。 **取值范围：** 不涉及。

        :return: The size of this ListInferDeploymentsResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ListInferDeploymentsResponse.

        **参数解释：** 当前页数量。 **取值范围：** 不涉及。

        :param size: The size of this ListInferDeploymentsResponse.
        :type size: int
        """
        self._size = size

    @property
    def pages(self):
        r"""Gets the pages of this ListInferDeploymentsResponse.

        **参数解释：** 总页数，根据传入的limit字段和数据总条数计算得出。如总记录条数为10，limit（单页最大条目数）为3，则页数为4。 **取值范围：** 不涉及。

        :return: The pages of this ListInferDeploymentsResponse.
        :rtype: int
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        r"""Sets the pages of this ListInferDeploymentsResponse.

        **参数解释：** 总页数，根据传入的limit字段和数据总条数计算得出。如总记录条数为10，limit（单页最大条目数）为3，则页数为4。 **取值范围：** 不涉及。

        :param pages: The pages of this ListInferDeploymentsResponse.
        :type pages: int
        """
        self._pages = pages

    @property
    def total(self):
        r"""Gets the total of this ListInferDeploymentsResponse.

        **参数解释：** 总记录条数。 **取值范围：** 不涉及。

        :return: The total of this ListInferDeploymentsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListInferDeploymentsResponse.

        **参数解释：** 总记录条数。 **取值范围：** 不涉及。

        :param total: The total of this ListInferDeploymentsResponse.
        :type total: int
        """
        self._total = total

    def to_dict(self):
        import warnings
        warnings.warn("ListInferDeploymentsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListInferDeploymentsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
