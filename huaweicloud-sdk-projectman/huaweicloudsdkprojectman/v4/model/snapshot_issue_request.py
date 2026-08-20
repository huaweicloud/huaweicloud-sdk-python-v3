# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SnapshotIssueRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ids': 'list[str]',
        'simple_result': 'bool'
    }

    attribute_map = {
        'ids': 'ids',
        'simple_result': 'simple_result'
    }

    def __init__(self, ids=None, simple_result=None):
        r"""SnapshotIssueRequest

        The model defined in huaweicloud sdk

        :param ids: 快照的ID数组。可以通过查询工作项快照列表接口获取，响应消息体中的id字段的值就是工作项快照ID。
        :type ids: list[str]
        :param simple_result: 是否返回工作项简要信息。 当值为false时ids中仅支持5个快照ID；值为true时，ids最多支持50个快照ID。
        :type simple_result: bool
        """
        
        

        self._ids = None
        self._simple_result = None
        self.discriminator = None

        self.ids = ids
        if simple_result is not None:
            self.simple_result = simple_result

    @property
    def ids(self):
        r"""Gets the ids of this SnapshotIssueRequest.

        快照的ID数组。可以通过查询工作项快照列表接口获取，响应消息体中的id字段的值就是工作项快照ID。

        :return: The ids of this SnapshotIssueRequest.
        :rtype: list[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        r"""Sets the ids of this SnapshotIssueRequest.

        快照的ID数组。可以通过查询工作项快照列表接口获取，响应消息体中的id字段的值就是工作项快照ID。

        :param ids: The ids of this SnapshotIssueRequest.
        :type ids: list[str]
        """
        self._ids = ids

    @property
    def simple_result(self):
        r"""Gets the simple_result of this SnapshotIssueRequest.

        是否返回工作项简要信息。 当值为false时ids中仅支持5个快照ID；值为true时，ids最多支持50个快照ID。

        :return: The simple_result of this SnapshotIssueRequest.
        :rtype: bool
        """
        return self._simple_result

    @simple_result.setter
    def simple_result(self, simple_result):
        r"""Sets the simple_result of this SnapshotIssueRequest.

        是否返回工作项简要信息。 当值为false时ids中仅支持5个快照ID；值为true时，ids最多支持50个快照ID。

        :param simple_result: The simple_result of this SnapshotIssueRequest.
        :type simple_result: bool
        """
        self._simple_result = simple_result

    def to_dict(self):
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
        if not isinstance(other, SnapshotIssueRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
