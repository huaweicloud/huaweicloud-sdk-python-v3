# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApplyTmlDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'domain_name': 'str',
        'error_msg': 'str'
    }

    attribute_map = {
        'status': 'status',
        'domain_name': 'domain_name',
        'error_msg': 'error_msg'
    }

    def __init__(self, status=None, domain_name=None, error_msg=None):
        r"""ApplyTmlDetail

        The model defined in huaweicloud sdk

        :param status: **参数解释：** 应用模板状态（域名粒度） **约束限制：** 不涉及 **取值范围：** - success: 应用模板成功 - fail: 应用模板失败 **默认取值：** 不涉及
        :type status: str
        :param domain_name: **参数解释：** 域名 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type domain_name: str
        :param error_msg: **参数解释：** 错误信息 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type error_msg: str
        """
        
        

        self._status = None
        self._domain_name = None
        self._error_msg = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if domain_name is not None:
            self.domain_name = domain_name
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def status(self):
        r"""Gets the status of this ApplyTmlDetail.

        **参数解释：** 应用模板状态（域名粒度） **约束限制：** 不涉及 **取值范围：** - success: 应用模板成功 - fail: 应用模板失败 **默认取值：** 不涉及

        :return: The status of this ApplyTmlDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ApplyTmlDetail.

        **参数解释：** 应用模板状态（域名粒度） **约束限制：** 不涉及 **取值范围：** - success: 应用模板成功 - fail: 应用模板失败 **默认取值：** 不涉及

        :param status: The status of this ApplyTmlDetail.
        :type status: str
        """
        self._status = status

    @property
    def domain_name(self):
        r"""Gets the domain_name of this ApplyTmlDetail.

        **参数解释：** 域名 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The domain_name of this ApplyTmlDetail.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this ApplyTmlDetail.

        **参数解释：** 域名 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param domain_name: The domain_name of this ApplyTmlDetail.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def error_msg(self):
        r"""Gets the error_msg of this ApplyTmlDetail.

        **参数解释：** 错误信息 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The error_msg of this ApplyTmlDetail.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this ApplyTmlDetail.

        **参数解释：** 错误信息 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param error_msg: The error_msg of this ApplyTmlDetail.
        :type error_msg: str
        """
        self._error_msg = error_msg

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
        if not isinstance(other, ApplyTmlDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
