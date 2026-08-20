# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FailureDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'snapshot_id': 'str',
        'snapshot_title': 'str',
        'failure_reason': 'str',
        'error_code': 'str'
    }

    attribute_map = {
        'snapshot_id': 'snapshot_id',
        'snapshot_title': 'snapshot_title',
        'failure_reason': 'failure_reason',
        'error_code': 'error_code'
    }

    def __init__(self, snapshot_id=None, snapshot_title=None, failure_reason=None, error_code=None):
        r"""FailureDetail

        The model defined in huaweicloud sdk

        :param snapshot_id: 快照ID。
        :type snapshot_id: str
        :param snapshot_title: 快照标题。
        :type snapshot_title: str
        :param failure_reason: 失败原因。
        :type failure_reason: str
        :param error_code: 错误码。
        :type error_code: str
        """
        
        

        self._snapshot_id = None
        self._snapshot_title = None
        self._failure_reason = None
        self._error_code = None
        self.discriminator = None

        if snapshot_id is not None:
            self.snapshot_id = snapshot_id
        if snapshot_title is not None:
            self.snapshot_title = snapshot_title
        if failure_reason is not None:
            self.failure_reason = failure_reason
        if error_code is not None:
            self.error_code = error_code

    @property
    def snapshot_id(self):
        r"""Gets the snapshot_id of this FailureDetail.

        快照ID。

        :return: The snapshot_id of this FailureDetail.
        :rtype: str
        """
        return self._snapshot_id

    @snapshot_id.setter
    def snapshot_id(self, snapshot_id):
        r"""Sets the snapshot_id of this FailureDetail.

        快照ID。

        :param snapshot_id: The snapshot_id of this FailureDetail.
        :type snapshot_id: str
        """
        self._snapshot_id = snapshot_id

    @property
    def snapshot_title(self):
        r"""Gets the snapshot_title of this FailureDetail.

        快照标题。

        :return: The snapshot_title of this FailureDetail.
        :rtype: str
        """
        return self._snapshot_title

    @snapshot_title.setter
    def snapshot_title(self, snapshot_title):
        r"""Sets the snapshot_title of this FailureDetail.

        快照标题。

        :param snapshot_title: The snapshot_title of this FailureDetail.
        :type snapshot_title: str
        """
        self._snapshot_title = snapshot_title

    @property
    def failure_reason(self):
        r"""Gets the failure_reason of this FailureDetail.

        失败原因。

        :return: The failure_reason of this FailureDetail.
        :rtype: str
        """
        return self._failure_reason

    @failure_reason.setter
    def failure_reason(self, failure_reason):
        r"""Sets the failure_reason of this FailureDetail.

        失败原因。

        :param failure_reason: The failure_reason of this FailureDetail.
        :type failure_reason: str
        """
        self._failure_reason = failure_reason

    @property
    def error_code(self):
        r"""Gets the error_code of this FailureDetail.

        错误码。

        :return: The error_code of this FailureDetail.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this FailureDetail.

        错误码。

        :param error_code: The error_code of this FailureDetail.
        :type error_code: str
        """
        self._error_code = error_code

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
        if not isinstance(other, FailureDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
