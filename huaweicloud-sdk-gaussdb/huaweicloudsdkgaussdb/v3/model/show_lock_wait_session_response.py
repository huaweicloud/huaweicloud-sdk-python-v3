# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowLockWaitSessionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'abnormal_root_cause': 'AbnormalRootCause'
    }

    attribute_map = {
        'abnormal_root_cause': 'abnormal_root_cause'
    }

    def __init__(self, abnormal_root_cause=None):
        r"""ShowLockWaitSessionResponse

        The model defined in huaweicloud sdk

        :param abnormal_root_cause: 
        :type abnormal_root_cause: :class:`huaweicloudsdkgaussdb.v3.AbnormalRootCause`
        """
        
        super().__init__()

        self._abnormal_root_cause = None
        self.discriminator = None

        if abnormal_root_cause is not None:
            self.abnormal_root_cause = abnormal_root_cause

    @property
    def abnormal_root_cause(self):
        r"""Gets the abnormal_root_cause of this ShowLockWaitSessionResponse.

        :return: The abnormal_root_cause of this ShowLockWaitSessionResponse.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.AbnormalRootCause`
        """
        return self._abnormal_root_cause

    @abnormal_root_cause.setter
    def abnormal_root_cause(self, abnormal_root_cause):
        r"""Sets the abnormal_root_cause of this ShowLockWaitSessionResponse.

        :param abnormal_root_cause: The abnormal_root_cause of this ShowLockWaitSessionResponse.
        :type abnormal_root_cause: :class:`huaweicloudsdkgaussdb.v3.AbnormalRootCause`
        """
        self._abnormal_root_cause = abnormal_root_cause

    def to_dict(self):
        import warnings
        warnings.warn("ShowLockWaitSessionResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowLockWaitSessionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
