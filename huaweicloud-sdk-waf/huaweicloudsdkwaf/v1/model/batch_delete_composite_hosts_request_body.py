# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteCompositeHostsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_ids': 'list[str]',
        'keep_policy_enable': 'bool'
    }

    attribute_map = {
        'host_ids': 'host_ids',
        'keep_policy_enable': 'keep_policy_enable'
    }

    def __init__(self, host_ids=None, keep_policy_enable=None):
        r"""BatchDeleteCompositeHostsRequestBody

        The model defined in huaweicloud sdk

        :param host_ids: **参数解释：** 域名id数组，包含待批量删除的租户域名唯一标识，从查询租户域名列表接口获取。 **约束限制：** 不涉及 **取值范围：** 数组内元素为字符串类型，每个元素对应一个域名ID **默认取值：** 不涉及
        :type host_ids: list[str]
        :param keep_policy_enable: **参数解释：** 保留域名的防护策略，标识删除域名后是否保留其关联的防护策略（true表示保留，false表示不保留）。 **约束限制：** 不涉及 **取值范围：** 仅支持true、false两个布尔值 **默认取值：** false
        :type keep_policy_enable: bool
        """
        
        

        self._host_ids = None
        self._keep_policy_enable = None
        self.discriminator = None

        if host_ids is not None:
            self.host_ids = host_ids
        if keep_policy_enable is not None:
            self.keep_policy_enable = keep_policy_enable

    @property
    def host_ids(self):
        r"""Gets the host_ids of this BatchDeleteCompositeHostsRequestBody.

        **参数解释：** 域名id数组，包含待批量删除的租户域名唯一标识，从查询租户域名列表接口获取。 **约束限制：** 不涉及 **取值范围：** 数组内元素为字符串类型，每个元素对应一个域名ID **默认取值：** 不涉及

        :return: The host_ids of this BatchDeleteCompositeHostsRequestBody.
        :rtype: list[str]
        """
        return self._host_ids

    @host_ids.setter
    def host_ids(self, host_ids):
        r"""Sets the host_ids of this BatchDeleteCompositeHostsRequestBody.

        **参数解释：** 域名id数组，包含待批量删除的租户域名唯一标识，从查询租户域名列表接口获取。 **约束限制：** 不涉及 **取值范围：** 数组内元素为字符串类型，每个元素对应一个域名ID **默认取值：** 不涉及

        :param host_ids: The host_ids of this BatchDeleteCompositeHostsRequestBody.
        :type host_ids: list[str]
        """
        self._host_ids = host_ids

    @property
    def keep_policy_enable(self):
        r"""Gets the keep_policy_enable of this BatchDeleteCompositeHostsRequestBody.

        **参数解释：** 保留域名的防护策略，标识删除域名后是否保留其关联的防护策略（true表示保留，false表示不保留）。 **约束限制：** 不涉及 **取值范围：** 仅支持true、false两个布尔值 **默认取值：** false

        :return: The keep_policy_enable of this BatchDeleteCompositeHostsRequestBody.
        :rtype: bool
        """
        return self._keep_policy_enable

    @keep_policy_enable.setter
    def keep_policy_enable(self, keep_policy_enable):
        r"""Sets the keep_policy_enable of this BatchDeleteCompositeHostsRequestBody.

        **参数解释：** 保留域名的防护策略，标识删除域名后是否保留其关联的防护策略（true表示保留，false表示不保留）。 **约束限制：** 不涉及 **取值范围：** 仅支持true、false两个布尔值 **默认取值：** false

        :param keep_policy_enable: The keep_policy_enable of this BatchDeleteCompositeHostsRequestBody.
        :type keep_policy_enable: bool
        """
        self._keep_policy_enable = keep_policy_enable

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
        if not isinstance(other, BatchDeleteCompositeHostsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
