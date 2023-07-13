# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCopyResultVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'reason': 'str',
        'status': 'str',
        'domain_name': 'str'
    }

    attribute_map = {
        'reason': 'reason',
        'status': 'status',
        'domain_name': 'domain_name'
    }

    def __init__(self, reason=None, status=None, domain_name=None):
        """BatchCopyResultVo

        The model defined in huaweicloud sdk

        :param reason: 失败原因,成功时没有该字段
        :type reason: str
        :param status: 批量操作结果。
        :type status: str
        :param domain_name: 域名。
        :type domain_name: str
        """
        
        

        self._reason = None
        self._status = None
        self._domain_name = None
        self.discriminator = None

        if reason is not None:
            self.reason = reason
        self.status = status
        self.domain_name = domain_name

    @property
    def reason(self):
        """Gets the reason of this BatchCopyResultVo.

        失败原因,成功时没有该字段

        :return: The reason of this BatchCopyResultVo.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this BatchCopyResultVo.

        失败原因,成功时没有该字段

        :param reason: The reason of this BatchCopyResultVo.
        :type reason: str
        """
        self._reason = reason

    @property
    def status(self):
        """Gets the status of this BatchCopyResultVo.

        批量操作结果。

        :return: The status of this BatchCopyResultVo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BatchCopyResultVo.

        批量操作结果。

        :param status: The status of this BatchCopyResultVo.
        :type status: str
        """
        self._status = status

    @property
    def domain_name(self):
        """Gets the domain_name of this BatchCopyResultVo.

        域名。

        :return: The domain_name of this BatchCopyResultVo.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this BatchCopyResultVo.

        域名。

        :param domain_name: The domain_name of this BatchCopyResultVo.
        :type domain_name: str
        """
        self._domain_name = domain_name

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
        if not isinstance(other, BatchCopyResultVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
