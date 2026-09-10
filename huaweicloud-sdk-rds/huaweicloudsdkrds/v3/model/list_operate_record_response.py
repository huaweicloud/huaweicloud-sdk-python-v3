# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOperateRecordResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'traces': 'list[OperateRecord]',
        'all_operate_type': 'list[str]'
    }

    attribute_map = {
        'count': 'count',
        'traces': 'traces',
        'all_operate_type': 'all_operate_type'
    }

    def __init__(self, count=None, traces=None, all_operate_type=None):
        r"""ListOperateRecordResponse

        The model defined in huaweicloud sdk

        :param count: 本次查询事件列表返回的事件记录的总条数
        :type count: int
        :param traces: 本次查询事件列表返回的事件记录
        :type traces: list[:class:`huaweicloudsdkrds.v3.OperateRecord`]
        :param all_operate_type: 所有事件类型
        :type all_operate_type: list[str]
        """
        
        super().__init__()

        self._count = None
        self._traces = None
        self._all_operate_type = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if traces is not None:
            self.traces = traces
        if all_operate_type is not None:
            self.all_operate_type = all_operate_type

    @property
    def count(self):
        r"""Gets the count of this ListOperateRecordResponse.

        本次查询事件列表返回的事件记录的总条数

        :return: The count of this ListOperateRecordResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListOperateRecordResponse.

        本次查询事件列表返回的事件记录的总条数

        :param count: The count of this ListOperateRecordResponse.
        :type count: int
        """
        self._count = count

    @property
    def traces(self):
        r"""Gets the traces of this ListOperateRecordResponse.

        本次查询事件列表返回的事件记录

        :return: The traces of this ListOperateRecordResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.OperateRecord`]
        """
        return self._traces

    @traces.setter
    def traces(self, traces):
        r"""Sets the traces of this ListOperateRecordResponse.

        本次查询事件列表返回的事件记录

        :param traces: The traces of this ListOperateRecordResponse.
        :type traces: list[:class:`huaweicloudsdkrds.v3.OperateRecord`]
        """
        self._traces = traces

    @property
    def all_operate_type(self):
        r"""Gets the all_operate_type of this ListOperateRecordResponse.

        所有事件类型

        :return: The all_operate_type of this ListOperateRecordResponse.
        :rtype: list[str]
        """
        return self._all_operate_type

    @all_operate_type.setter
    def all_operate_type(self, all_operate_type):
        r"""Sets the all_operate_type of this ListOperateRecordResponse.

        所有事件类型

        :param all_operate_type: The all_operate_type of this ListOperateRecordResponse.
        :type all_operate_type: list[str]
        """
        self._all_operate_type = all_operate_type

    def to_dict(self):
        import warnings
        warnings.warn("ListOperateRecordResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListOperateRecordResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
