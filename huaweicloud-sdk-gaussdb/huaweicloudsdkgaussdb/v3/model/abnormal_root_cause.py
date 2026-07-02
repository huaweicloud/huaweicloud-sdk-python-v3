# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AbnormalRootCause:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'abnormal_type': 'str',
        'lock_root_cause': 'LockRootCause'
    }

    attribute_map = {
        'abnormal_type': 'abnormal_type',
        'lock_root_cause': 'lock_root_cause'
    }

    def __init__(self, abnormal_type=None, lock_root_cause=None):
        r"""AbnormalRootCause

        The model defined in huaweicloud sdk

        :param abnormal_type: **参数解释**： 异常类型。 **取值范围**： LOCK_WAIT：锁等待。 
        :type abnormal_type: str
        :param lock_root_cause: 
        :type lock_root_cause: :class:`huaweicloudsdkgaussdb.v3.LockRootCause`
        """
        
        

        self._abnormal_type = None
        self._lock_root_cause = None
        self.discriminator = None

        if abnormal_type is not None:
            self.abnormal_type = abnormal_type
        if lock_root_cause is not None:
            self.lock_root_cause = lock_root_cause

    @property
    def abnormal_type(self):
        r"""Gets the abnormal_type of this AbnormalRootCause.

        **参数解释**： 异常类型。 **取值范围**： LOCK_WAIT：锁等待。 

        :return: The abnormal_type of this AbnormalRootCause.
        :rtype: str
        """
        return self._abnormal_type

    @abnormal_type.setter
    def abnormal_type(self, abnormal_type):
        r"""Sets the abnormal_type of this AbnormalRootCause.

        **参数解释**： 异常类型。 **取值范围**： LOCK_WAIT：锁等待。 

        :param abnormal_type: The abnormal_type of this AbnormalRootCause.
        :type abnormal_type: str
        """
        self._abnormal_type = abnormal_type

    @property
    def lock_root_cause(self):
        r"""Gets the lock_root_cause of this AbnormalRootCause.

        :return: The lock_root_cause of this AbnormalRootCause.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.LockRootCause`
        """
        return self._lock_root_cause

    @lock_root_cause.setter
    def lock_root_cause(self, lock_root_cause):
        r"""Sets the lock_root_cause of this AbnormalRootCause.

        :param lock_root_cause: The lock_root_cause of this AbnormalRootCause.
        :type lock_root_cause: :class:`huaweicloudsdkgaussdb.v3.LockRootCause`
        """
        self._lock_root_cause = lock_root_cause

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
        if not isinstance(other, AbnormalRootCause):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
