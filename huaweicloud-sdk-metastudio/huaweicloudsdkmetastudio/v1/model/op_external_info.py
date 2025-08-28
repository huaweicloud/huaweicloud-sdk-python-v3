# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpExternalInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'review_id_list': 'list[str]',
        'algorithm_failure_reason': 'str',
        'admin_audit_failure_reason': 'str'
    }

    attribute_map = {
        'review_id_list': 'review_id_list',
        'algorithm_failure_reason': 'algorithm_failure_reason',
        'admin_audit_failure_reason': 'admin_audit_failure_reason'
    }

    def __init__(self, review_id_list=None, algorithm_failure_reason=None, admin_audit_failure_reason=None):
        r"""OpExternalInfo

        The model defined in huaweicloud sdk

        :param review_id_list: 审核详情id列表
        :type review_id_list: list[str]
        :param algorithm_failure_reason: 算法侧失败原因
        :type algorithm_failure_reason: str
        :param admin_audit_failure_reason: 管理员驳回的原因
        :type admin_audit_failure_reason: str
        """
        
        

        self._review_id_list = None
        self._algorithm_failure_reason = None
        self._admin_audit_failure_reason = None
        self.discriminator = None

        if review_id_list is not None:
            self.review_id_list = review_id_list
        if algorithm_failure_reason is not None:
            self.algorithm_failure_reason = algorithm_failure_reason
        if admin_audit_failure_reason is not None:
            self.admin_audit_failure_reason = admin_audit_failure_reason

    @property
    def review_id_list(self):
        r"""Gets the review_id_list of this OpExternalInfo.

        审核详情id列表

        :return: The review_id_list of this OpExternalInfo.
        :rtype: list[str]
        """
        return self._review_id_list

    @review_id_list.setter
    def review_id_list(self, review_id_list):
        r"""Sets the review_id_list of this OpExternalInfo.

        审核详情id列表

        :param review_id_list: The review_id_list of this OpExternalInfo.
        :type review_id_list: list[str]
        """
        self._review_id_list = review_id_list

    @property
    def algorithm_failure_reason(self):
        r"""Gets the algorithm_failure_reason of this OpExternalInfo.

        算法侧失败原因

        :return: The algorithm_failure_reason of this OpExternalInfo.
        :rtype: str
        """
        return self._algorithm_failure_reason

    @algorithm_failure_reason.setter
    def algorithm_failure_reason(self, algorithm_failure_reason):
        r"""Sets the algorithm_failure_reason of this OpExternalInfo.

        算法侧失败原因

        :param algorithm_failure_reason: The algorithm_failure_reason of this OpExternalInfo.
        :type algorithm_failure_reason: str
        """
        self._algorithm_failure_reason = algorithm_failure_reason

    @property
    def admin_audit_failure_reason(self):
        r"""Gets the admin_audit_failure_reason of this OpExternalInfo.

        管理员驳回的原因

        :return: The admin_audit_failure_reason of this OpExternalInfo.
        :rtype: str
        """
        return self._admin_audit_failure_reason

    @admin_audit_failure_reason.setter
    def admin_audit_failure_reason(self, admin_audit_failure_reason):
        r"""Sets the admin_audit_failure_reason of this OpExternalInfo.

        管理员驳回的原因

        :param admin_audit_failure_reason: The admin_audit_failure_reason of this OpExternalInfo.
        :type admin_audit_failure_reason: str
        """
        self._admin_audit_failure_reason = admin_audit_failure_reason

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
        if not isinstance(other, OpExternalInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
