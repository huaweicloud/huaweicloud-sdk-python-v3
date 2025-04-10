# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSnapshotConfigsResponse(SdkResponse):

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
        'snapshot_config_list': 'list[LiveSnapshotConfig]',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'total': 'total',
        'snapshot_config_list': 'snapshot_config_list',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, total=None, snapshot_config_list=None, limit=None, offset=None):
        r"""ListSnapshotConfigsResponse

        The model defined in huaweicloud sdk

        :param total: 总条目数
        :type total: int
        :param snapshot_config_list: 截图配置
        :type snapshot_config_list: list[:class:`huaweicloudsdklive.v1.LiveSnapshotConfig`]
        :param limit: 每页记录数
        :type limit: int
        :param offset: 偏移量
        :type offset: int
        """
        
        super(ListSnapshotConfigsResponse, self).__init__()

        self._total = None
        self._snapshot_config_list = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if snapshot_config_list is not None:
            self.snapshot_config_list = snapshot_config_list
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def total(self):
        r"""Gets the total of this ListSnapshotConfigsResponse.

        总条目数

        :return: The total of this ListSnapshotConfigsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListSnapshotConfigsResponse.

        总条目数

        :param total: The total of this ListSnapshotConfigsResponse.
        :type total: int
        """
        self._total = total

    @property
    def snapshot_config_list(self):
        r"""Gets the snapshot_config_list of this ListSnapshotConfigsResponse.

        截图配置

        :return: The snapshot_config_list of this ListSnapshotConfigsResponse.
        :rtype: list[:class:`huaweicloudsdklive.v1.LiveSnapshotConfig`]
        """
        return self._snapshot_config_list

    @snapshot_config_list.setter
    def snapshot_config_list(self, snapshot_config_list):
        r"""Sets the snapshot_config_list of this ListSnapshotConfigsResponse.

        截图配置

        :param snapshot_config_list: The snapshot_config_list of this ListSnapshotConfigsResponse.
        :type snapshot_config_list: list[:class:`huaweicloudsdklive.v1.LiveSnapshotConfig`]
        """
        self._snapshot_config_list = snapshot_config_list

    @property
    def limit(self):
        r"""Gets the limit of this ListSnapshotConfigsResponse.

        每页记录数

        :return: The limit of this ListSnapshotConfigsResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSnapshotConfigsResponse.

        每页记录数

        :param limit: The limit of this ListSnapshotConfigsResponse.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListSnapshotConfigsResponse.

        偏移量

        :return: The offset of this ListSnapshotConfigsResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSnapshotConfigsResponse.

        偏移量

        :param offset: The offset of this ListSnapshotConfigsResponse.
        :type offset: int
        """
        self._offset = offset

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListSnapshotConfigsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
