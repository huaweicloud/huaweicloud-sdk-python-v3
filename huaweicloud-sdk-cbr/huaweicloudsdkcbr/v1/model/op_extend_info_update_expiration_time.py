# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpExtendInfoUpdateExpirationTime:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'affected_backups_count': 'int',
        'expiration_day': 'str'
    }

    attribute_map = {
        'affected_backups_count': 'affected_backups_count',
        'expiration_day': 'expiration_day'
    }

    def __init__(self, affected_backups_count=None, expiration_day=None):
        r"""OpExtendInfoUpdateExpirationTime

        The model defined in huaweicloud sdk

        :param affected_backups_count: 本次任务受影响的备份个数
        :type affected_backups_count: int
        :param expiration_day: 本次任务预期过期日期，格式：YYYY-MM-DD。
        :type expiration_day: str
        """
        
        

        self._affected_backups_count = None
        self._expiration_day = None
        self.discriminator = None

        if affected_backups_count is not None:
            self.affected_backups_count = affected_backups_count
        if expiration_day is not None:
            self.expiration_day = expiration_day

    @property
    def affected_backups_count(self):
        r"""Gets the affected_backups_count of this OpExtendInfoUpdateExpirationTime.

        本次任务受影响的备份个数

        :return: The affected_backups_count of this OpExtendInfoUpdateExpirationTime.
        :rtype: int
        """
        return self._affected_backups_count

    @affected_backups_count.setter
    def affected_backups_count(self, affected_backups_count):
        r"""Sets the affected_backups_count of this OpExtendInfoUpdateExpirationTime.

        本次任务受影响的备份个数

        :param affected_backups_count: The affected_backups_count of this OpExtendInfoUpdateExpirationTime.
        :type affected_backups_count: int
        """
        self._affected_backups_count = affected_backups_count

    @property
    def expiration_day(self):
        r"""Gets the expiration_day of this OpExtendInfoUpdateExpirationTime.

        本次任务预期过期日期，格式：YYYY-MM-DD。

        :return: The expiration_day of this OpExtendInfoUpdateExpirationTime.
        :rtype: str
        """
        return self._expiration_day

    @expiration_day.setter
    def expiration_day(self, expiration_day):
        r"""Sets the expiration_day of this OpExtendInfoUpdateExpirationTime.

        本次任务预期过期日期，格式：YYYY-MM-DD。

        :param expiration_day: The expiration_day of this OpExtendInfoUpdateExpirationTime.
        :type expiration_day: str
        """
        self._expiration_day = expiration_day

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
        if not isinstance(other, OpExtendInfoUpdateExpirationTime):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
