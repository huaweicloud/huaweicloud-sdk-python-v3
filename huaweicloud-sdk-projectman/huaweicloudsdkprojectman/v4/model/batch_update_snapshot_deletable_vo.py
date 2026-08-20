# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpdateSnapshotDeletableVO:

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
        'deletable': 'bool'
    }

    attribute_map = {
        'ids': 'ids',
        'deletable': 'deletable'
    }

    def __init__(self, ids=None, deletable=None):
        r"""BatchUpdateSnapshotDeletableVO

        The model defined in huaweicloud sdk

        :param ids: 快照ID列表。通过接口查询工作项计划管理快照列表获取响应参数中的id字段。
        :type ids: list[str]
        :param deletable: 是否为可删除标识。
        :type deletable: bool
        """
        
        

        self._ids = None
        self._deletable = None
        self.discriminator = None

        self.ids = ids
        self.deletable = deletable

    @property
    def ids(self):
        r"""Gets the ids of this BatchUpdateSnapshotDeletableVO.

        快照ID列表。通过接口查询工作项计划管理快照列表获取响应参数中的id字段。

        :return: The ids of this BatchUpdateSnapshotDeletableVO.
        :rtype: list[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        r"""Sets the ids of this BatchUpdateSnapshotDeletableVO.

        快照ID列表。通过接口查询工作项计划管理快照列表获取响应参数中的id字段。

        :param ids: The ids of this BatchUpdateSnapshotDeletableVO.
        :type ids: list[str]
        """
        self._ids = ids

    @property
    def deletable(self):
        r"""Gets the deletable of this BatchUpdateSnapshotDeletableVO.

        是否为可删除标识。

        :return: The deletable of this BatchUpdateSnapshotDeletableVO.
        :rtype: bool
        """
        return self._deletable

    @deletable.setter
    def deletable(self, deletable):
        r"""Sets the deletable of this BatchUpdateSnapshotDeletableVO.

        是否为可删除标识。

        :param deletable: The deletable of this BatchUpdateSnapshotDeletableVO.
        :type deletable: bool
        """
        self._deletable = deletable

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
        if not isinstance(other, BatchUpdateSnapshotDeletableVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
