# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDomainStatusResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'float',
        'free_quota': 'bool',
        'allow_custom_env': 'float'
    }

    attribute_map = {
        'status': 'status',
        'free_quota': 'free_quota',
        'allow_custom_env': 'allow_custom_env'
    }

    def __init__(self, status=None, free_quota=None, allow_custom_env=None):
        r"""ShowDomainStatusResult

        The model defined in huaweicloud sdk

        :param status: 租户状态0:未开通; 1:正常; 2:冻结; 3:关闭; 4、5:注销
        :type status: float
        :param free_quota: 是否包含免费额度
        :type free_quota: bool
        :param allow_custom_env: 是否启用自定义环境
        :type allow_custom_env: float
        """
        
        

        self._status = None
        self._free_quota = None
        self._allow_custom_env = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if free_quota is not None:
            self.free_quota = free_quota
        if allow_custom_env is not None:
            self.allow_custom_env = allow_custom_env

    @property
    def status(self):
        r"""Gets the status of this ShowDomainStatusResult.

        租户状态0:未开通; 1:正常; 2:冻结; 3:关闭; 4、5:注销

        :return: The status of this ShowDomainStatusResult.
        :rtype: float
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowDomainStatusResult.

        租户状态0:未开通; 1:正常; 2:冻结; 3:关闭; 4、5:注销

        :param status: The status of this ShowDomainStatusResult.
        :type status: float
        """
        self._status = status

    @property
    def free_quota(self):
        r"""Gets the free_quota of this ShowDomainStatusResult.

        是否包含免费额度

        :return: The free_quota of this ShowDomainStatusResult.
        :rtype: bool
        """
        return self._free_quota

    @free_quota.setter
    def free_quota(self, free_quota):
        r"""Sets the free_quota of this ShowDomainStatusResult.

        是否包含免费额度

        :param free_quota: The free_quota of this ShowDomainStatusResult.
        :type free_quota: bool
        """
        self._free_quota = free_quota

    @property
    def allow_custom_env(self):
        r"""Gets the allow_custom_env of this ShowDomainStatusResult.

        是否启用自定义环境

        :return: The allow_custom_env of this ShowDomainStatusResult.
        :rtype: float
        """
        return self._allow_custom_env

    @allow_custom_env.setter
    def allow_custom_env(self, allow_custom_env):
        r"""Sets the allow_custom_env of this ShowDomainStatusResult.

        是否启用自定义环境

        :param allow_custom_env: The allow_custom_env of this ShowDomainStatusResult.
        :type allow_custom_env: float
        """
        self._allow_custom_env = allow_custom_env

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
        if not isinstance(other, ShowDomainStatusResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
