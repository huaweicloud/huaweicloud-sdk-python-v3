# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOperationalTaskDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data': 'list[TaskStatusOpenResp]',
        'count': 'int'
    }

    attribute_map = {
        'data': 'data',
        'count': 'count'
    }

    def __init__(self, data=None, count=None):
        r"""ListOperationalTaskDetailResponse

        The model defined in huaweicloud sdk

        :param data: **参数解释**： 详细列表。 **默认取值**： 0
        :type data: list[:class:`huaweicloudsdkdws.v2.TaskStatusOpenResp`]
        :param count: **参数解释**： 总条数。 **默认取值**： 0
        :type count: int
        """
        
        super().__init__()

        self._data = None
        self._count = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if count is not None:
            self.count = count

    @property
    def data(self):
        r"""Gets the data of this ListOperationalTaskDetailResponse.

        **参数解释**： 详细列表。 **默认取值**： 0

        :return: The data of this ListOperationalTaskDetailResponse.
        :rtype: list[:class:`huaweicloudsdkdws.v2.TaskStatusOpenResp`]
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this ListOperationalTaskDetailResponse.

        **参数解释**： 详细列表。 **默认取值**： 0

        :param data: The data of this ListOperationalTaskDetailResponse.
        :type data: list[:class:`huaweicloudsdkdws.v2.TaskStatusOpenResp`]
        """
        self._data = data

    @property
    def count(self):
        r"""Gets the count of this ListOperationalTaskDetailResponse.

        **参数解释**： 总条数。 **默认取值**： 0

        :return: The count of this ListOperationalTaskDetailResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListOperationalTaskDetailResponse.

        **参数解释**： 总条数。 **默认取值**： 0

        :param count: The count of this ListOperationalTaskDetailResponse.
        :type count: int
        """
        self._count = count

    def to_dict(self):
        import warnings
        warnings.warn("ListOperationalTaskDetailResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListOperationalTaskDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
