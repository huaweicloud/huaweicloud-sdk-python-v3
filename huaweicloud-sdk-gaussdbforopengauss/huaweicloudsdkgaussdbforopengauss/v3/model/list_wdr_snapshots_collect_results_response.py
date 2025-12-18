# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWdrSnapshotsCollectResultsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'wdr_snapshots': 'list[CollectedWdrSnapshotInfoResult]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'wdr_snapshots': 'wdr_snapshots'
    }

    def __init__(self, total_count=None, wdr_snapshots=None):
        r"""ListWdrSnapshotsCollectResultsResponse

        The model defined in huaweicloud sdk

        :param total_count: **参数解释**： 总记录数。 **取值范围**： 不涉及。
        :type total_count: int
        :param wdr_snapshots: **参数解释**： WDR快照信息列表。
        :type wdr_snapshots: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.CollectedWdrSnapshotInfoResult`]
        """
        
        super().__init__()

        self._total_count = None
        self._wdr_snapshots = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if wdr_snapshots is not None:
            self.wdr_snapshots = wdr_snapshots

    @property
    def total_count(self):
        r"""Gets the total_count of this ListWdrSnapshotsCollectResultsResponse.

        **参数解释**： 总记录数。 **取值范围**： 不涉及。

        :return: The total_count of this ListWdrSnapshotsCollectResultsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListWdrSnapshotsCollectResultsResponse.

        **参数解释**： 总记录数。 **取值范围**： 不涉及。

        :param total_count: The total_count of this ListWdrSnapshotsCollectResultsResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def wdr_snapshots(self):
        r"""Gets the wdr_snapshots of this ListWdrSnapshotsCollectResultsResponse.

        **参数解释**： WDR快照信息列表。

        :return: The wdr_snapshots of this ListWdrSnapshotsCollectResultsResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.CollectedWdrSnapshotInfoResult`]
        """
        return self._wdr_snapshots

    @wdr_snapshots.setter
    def wdr_snapshots(self, wdr_snapshots):
        r"""Sets the wdr_snapshots of this ListWdrSnapshotsCollectResultsResponse.

        **参数解释**： WDR快照信息列表。

        :param wdr_snapshots: The wdr_snapshots of this ListWdrSnapshotsCollectResultsResponse.
        :type wdr_snapshots: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.CollectedWdrSnapshotInfoResult`]
        """
        self._wdr_snapshots = wdr_snapshots

    def to_dict(self):
        import warnings
        warnings.warn("ListWdrSnapshotsCollectResultsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListWdrSnapshotsCollectResultsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
