# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowReplicationStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'replication_status': 'str',
        'abnormal_reason': 'str'
    }

    attribute_map = {
        'replication_status': 'replication_status',
        'abnormal_reason': 'abnormal_reason'
    }

    def __init__(self, replication_status=None, abnormal_reason=None):
        r"""ShowReplicationStatusResponse

        The model defined in huaweicloud sdk

        :param replication_status: 复制状态。
        :type replication_status: str
        :param abnormal_reason: 复制异常原因。
        :type abnormal_reason: str
        """
        
        super(ShowReplicationStatusResponse, self).__init__()

        self._replication_status = None
        self._abnormal_reason = None
        self.discriminator = None

        if replication_status is not None:
            self.replication_status = replication_status
        if abnormal_reason is not None:
            self.abnormal_reason = abnormal_reason

    @property
    def replication_status(self):
        r"""Gets the replication_status of this ShowReplicationStatusResponse.

        复制状态。

        :return: The replication_status of this ShowReplicationStatusResponse.
        :rtype: str
        """
        return self._replication_status

    @replication_status.setter
    def replication_status(self, replication_status):
        r"""Sets the replication_status of this ShowReplicationStatusResponse.

        复制状态。

        :param replication_status: The replication_status of this ShowReplicationStatusResponse.
        :type replication_status: str
        """
        self._replication_status = replication_status

    @property
    def abnormal_reason(self):
        r"""Gets the abnormal_reason of this ShowReplicationStatusResponse.

        复制异常原因。

        :return: The abnormal_reason of this ShowReplicationStatusResponse.
        :rtype: str
        """
        return self._abnormal_reason

    @abnormal_reason.setter
    def abnormal_reason(self, abnormal_reason):
        r"""Sets the abnormal_reason of this ShowReplicationStatusResponse.

        复制异常原因。

        :param abnormal_reason: The abnormal_reason of this ShowReplicationStatusResponse.
        :type abnormal_reason: str
        """
        self._abnormal_reason = abnormal_reason

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
        if not isinstance(other, ShowReplicationStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
