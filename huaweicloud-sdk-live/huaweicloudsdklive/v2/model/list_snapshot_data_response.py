# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSnapshotDataResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'snapshot_list': 'list[SnapshotData]',
        'total': 'int',
        'x_request_id': 'str'
    }

    attribute_map = {
        'snapshot_list': 'snapshot_list',
        'total': 'total',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, snapshot_list=None, total=None, x_request_id=None):
        """ListSnapshotDataResponse

        The model defined in huaweicloud sdk

        :param snapshot_list: 采样数据列表。 
        :type snapshot_list: list[:class:`huaweicloudsdklive.v2.SnapshotData`]
        :param total: 指定时间区间内截图数量总和。
        :type total: int
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListSnapshotDataResponse, self).__init__()

        self._snapshot_list = None
        self._total = None
        self._x_request_id = None
        self.discriminator = None

        if snapshot_list is not None:
            self.snapshot_list = snapshot_list
        if total is not None:
            self.total = total
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def snapshot_list(self):
        """Gets the snapshot_list of this ListSnapshotDataResponse.

        采样数据列表。 

        :return: The snapshot_list of this ListSnapshotDataResponse.
        :rtype: list[:class:`huaweicloudsdklive.v2.SnapshotData`]
        """
        return self._snapshot_list

    @snapshot_list.setter
    def snapshot_list(self, snapshot_list):
        """Sets the snapshot_list of this ListSnapshotDataResponse.

        采样数据列表。 

        :param snapshot_list: The snapshot_list of this ListSnapshotDataResponse.
        :type snapshot_list: list[:class:`huaweicloudsdklive.v2.SnapshotData`]
        """
        self._snapshot_list = snapshot_list

    @property
    def total(self):
        """Gets the total of this ListSnapshotDataResponse.

        指定时间区间内截图数量总和。

        :return: The total of this ListSnapshotDataResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListSnapshotDataResponse.

        指定时间区间内截图数量总和。

        :param total: The total of this ListSnapshotDataResponse.
        :type total: int
        """
        self._total = total

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ListSnapshotDataResponse.

        :return: The x_request_id of this ListSnapshotDataResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ListSnapshotDataResponse.

        :param x_request_id: The x_request_id of this ListSnapshotDataResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ListSnapshotDataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
