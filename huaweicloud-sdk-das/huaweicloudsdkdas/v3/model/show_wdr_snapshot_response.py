# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowWdrSnapshotResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'snapshot_list': 'list[WdrSnapshot]'
    }

    attribute_map = {
        'snapshot_list': 'snapshot_list'
    }

    def __init__(self, snapshot_list=None):
        r"""ShowWdrSnapshotResponse

        The model defined in huaweicloud sdk

        :param snapshot_list: WDR快照文件列表
        :type snapshot_list: list[:class:`huaweicloudsdkdas.v3.WdrSnapshot`]
        """
        
        super().__init__()

        self._snapshot_list = None
        self.discriminator = None

        if snapshot_list is not None:
            self.snapshot_list = snapshot_list

    @property
    def snapshot_list(self):
        r"""Gets the snapshot_list of this ShowWdrSnapshotResponse.

        WDR快照文件列表

        :return: The snapshot_list of this ShowWdrSnapshotResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.WdrSnapshot`]
        """
        return self._snapshot_list

    @snapshot_list.setter
    def snapshot_list(self, snapshot_list):
        r"""Sets the snapshot_list of this ShowWdrSnapshotResponse.

        WDR快照文件列表

        :param snapshot_list: The snapshot_list of this ShowWdrSnapshotResponse.
        :type snapshot_list: list[:class:`huaweicloudsdkdas.v3.WdrSnapshot`]
        """
        self._snapshot_list = snapshot_list

    def to_dict(self):
        import warnings
        warnings.warn("ShowWdrSnapshotResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowWdrSnapshotResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
