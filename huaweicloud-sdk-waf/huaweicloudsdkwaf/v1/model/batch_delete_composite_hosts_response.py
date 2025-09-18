# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteCompositeHostsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_ids': 'list[str]'
    }

    attribute_map = {
        'host_ids': 'host_ids'
    }

    def __init__(self, host_ids=None):
        r"""BatchDeleteCompositeHostsResponse

        The model defined in huaweicloud sdk

        :param host_ids: **参数解释：** 域名id数组，返回已成功批量删除的租户域名唯一标识。 **约束限制：** 不涉及 **取值范围：** 数组内元素为字符串类型，与请求体中传入的有效域名ID对应 **默认取值：** 不涉及
        :type host_ids: list[str]
        """
        
        super(BatchDeleteCompositeHostsResponse, self).__init__()

        self._host_ids = None
        self.discriminator = None

        if host_ids is not None:
            self.host_ids = host_ids

    @property
    def host_ids(self):
        r"""Gets the host_ids of this BatchDeleteCompositeHostsResponse.

        **参数解释：** 域名id数组，返回已成功批量删除的租户域名唯一标识。 **约束限制：** 不涉及 **取值范围：** 数组内元素为字符串类型，与请求体中传入的有效域名ID对应 **默认取值：** 不涉及

        :return: The host_ids of this BatchDeleteCompositeHostsResponse.
        :rtype: list[str]
        """
        return self._host_ids

    @host_ids.setter
    def host_ids(self, host_ids):
        r"""Sets the host_ids of this BatchDeleteCompositeHostsResponse.

        **参数解释：** 域名id数组，返回已成功批量删除的租户域名唯一标识。 **约束限制：** 不涉及 **取值范围：** 数组内元素为字符串类型，与请求体中传入的有效域名ID对应 **默认取值：** 不涉及

        :param host_ids: The host_ids of this BatchDeleteCompositeHostsResponse.
        :type host_ids: list[str]
        """
        self._host_ids = host_ids

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
        if not isinstance(other, BatchDeleteCompositeHostsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
