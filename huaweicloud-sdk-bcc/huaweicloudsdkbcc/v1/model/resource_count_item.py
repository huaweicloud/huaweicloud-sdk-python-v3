# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceCountItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'date': 'str',
        'total': 'int',
        'unprotected': 'ProtectionCount',
        'protected': 'ProtectionCount'
    }

    attribute_map = {
        'date': 'date',
        'total': 'total',
        'unprotected': 'unprotected',
        'protected': 'protected'
    }

    def __init__(self, date=None, total=None, unprotected=None, protected=None):
        r"""ResourceCountItem

        The model defined in huaweicloud sdk

        :param date: 日期, 如\&quot;2025-05-19\&quot;。
        :type date: str
        :param total: 资源总数
        :type total: int
        :param unprotected: 
        :type unprotected: :class:`huaweicloudsdkbcc.v1.ProtectionCount`
        :param protected: 
        :type protected: :class:`huaweicloudsdkbcc.v1.ProtectionCount`
        """
        
        

        self._date = None
        self._total = None
        self._unprotected = None
        self._protected = None
        self.discriminator = None

        if date is not None:
            self.date = date
        self.total = total
        if unprotected is not None:
            self.unprotected = unprotected
        if protected is not None:
            self.protected = protected

    @property
    def date(self):
        r"""Gets the date of this ResourceCountItem.

        日期, 如\"2025-05-19\"。

        :return: The date of this ResourceCountItem.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        r"""Sets the date of this ResourceCountItem.

        日期, 如\"2025-05-19\"。

        :param date: The date of this ResourceCountItem.
        :type date: str
        """
        self._date = date

    @property
    def total(self):
        r"""Gets the total of this ResourceCountItem.

        资源总数

        :return: The total of this ResourceCountItem.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ResourceCountItem.

        资源总数

        :param total: The total of this ResourceCountItem.
        :type total: int
        """
        self._total = total

    @property
    def unprotected(self):
        r"""Gets the unprotected of this ResourceCountItem.

        :return: The unprotected of this ResourceCountItem.
        :rtype: :class:`huaweicloudsdkbcc.v1.ProtectionCount`
        """
        return self._unprotected

    @unprotected.setter
    def unprotected(self, unprotected):
        r"""Sets the unprotected of this ResourceCountItem.

        :param unprotected: The unprotected of this ResourceCountItem.
        :type unprotected: :class:`huaweicloudsdkbcc.v1.ProtectionCount`
        """
        self._unprotected = unprotected

    @property
    def protected(self):
        r"""Gets the protected of this ResourceCountItem.

        :return: The protected of this ResourceCountItem.
        :rtype: :class:`huaweicloudsdkbcc.v1.ProtectionCount`
        """
        return self._protected

    @protected.setter
    def protected(self, protected):
        r"""Sets the protected of this ResourceCountItem.

        :param protected: The protected of this ResourceCountItem.
        :type protected: :class:`huaweicloudsdkbcc.v1.ProtectionCount`
        """
        self._protected = protected

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
        if not isinstance(other, ResourceCountItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
