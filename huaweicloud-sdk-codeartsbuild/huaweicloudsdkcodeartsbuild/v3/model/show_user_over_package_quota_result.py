# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowUserOverPackageQuotaResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_over_quota': 'bool',
        'build_quota': 'str',
        'used_quota': 'str'
    }

    attribute_map = {
        'is_over_quota': 'is_over_quota',
        'build_quota': 'build_quota',
        'used_quota': 'used_quota'
    }

    def __init__(self, is_over_quota=None, build_quota=None, used_quota=None):
        r"""ShowUserOverPackageQuotaResult

        The model defined in huaweicloud sdk

        :param is_over_quota: 套餐超期
        :type is_over_quota: bool
        :param build_quota: 构建套餐
        :type build_quota: str
        :param used_quota: 已使用的套餐用量，套餐为unlimit时无此信息
        :type used_quota: str
        """
        
        

        self._is_over_quota = None
        self._build_quota = None
        self._used_quota = None
        self.discriminator = None

        if is_over_quota is not None:
            self.is_over_quota = is_over_quota
        if build_quota is not None:
            self.build_quota = build_quota
        if used_quota is not None:
            self.used_quota = used_quota

    @property
    def is_over_quota(self):
        r"""Gets the is_over_quota of this ShowUserOverPackageQuotaResult.

        套餐超期

        :return: The is_over_quota of this ShowUserOverPackageQuotaResult.
        :rtype: bool
        """
        return self._is_over_quota

    @is_over_quota.setter
    def is_over_quota(self, is_over_quota):
        r"""Sets the is_over_quota of this ShowUserOverPackageQuotaResult.

        套餐超期

        :param is_over_quota: The is_over_quota of this ShowUserOverPackageQuotaResult.
        :type is_over_quota: bool
        """
        self._is_over_quota = is_over_quota

    @property
    def build_quota(self):
        r"""Gets the build_quota of this ShowUserOverPackageQuotaResult.

        构建套餐

        :return: The build_quota of this ShowUserOverPackageQuotaResult.
        :rtype: str
        """
        return self._build_quota

    @build_quota.setter
    def build_quota(self, build_quota):
        r"""Sets the build_quota of this ShowUserOverPackageQuotaResult.

        构建套餐

        :param build_quota: The build_quota of this ShowUserOverPackageQuotaResult.
        :type build_quota: str
        """
        self._build_quota = build_quota

    @property
    def used_quota(self):
        r"""Gets the used_quota of this ShowUserOverPackageQuotaResult.

        已使用的套餐用量，套餐为unlimit时无此信息

        :return: The used_quota of this ShowUserOverPackageQuotaResult.
        :rtype: str
        """
        return self._used_quota

    @used_quota.setter
    def used_quota(self, used_quota):
        r"""Sets the used_quota of this ShowUserOverPackageQuotaResult.

        已使用的套餐用量，套餐为unlimit时无此信息

        :param used_quota: The used_quota of this ShowUserOverPackageQuotaResult.
        :type used_quota: str
        """
        self._used_quota = used_quota

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
        if not isinstance(other, ShowUserOverPackageQuotaResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
