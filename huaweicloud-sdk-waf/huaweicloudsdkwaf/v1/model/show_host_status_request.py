# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowHostStatusRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_id': 'str'
    }

    attribute_map = {
        'host_id': 'host_id'
    }

    def __init__(self, host_id=None):
        r"""ShowHostStatusRequest

        The model defined in huaweicloud sdk

        :param host_id: **参数解释：** 域名ID，您可以通过调用查询全部防护域名列表（ListCompositeHosts）获取域名ID。 **约束限制：** 不涉及 **取值范围：** 只能由英文字母、数字组成，且长度为32个字符。 **默认取值：** 不涉及
        :type host_id: str
        """
        
        

        self._host_id = None
        self.discriminator = None

        self.host_id = host_id

    @property
    def host_id(self):
        r"""Gets the host_id of this ShowHostStatusRequest.

        **参数解释：** 域名ID，您可以通过调用查询全部防护域名列表（ListCompositeHosts）获取域名ID。 **约束限制：** 不涉及 **取值范围：** 只能由英文字母、数字组成，且长度为32个字符。 **默认取值：** 不涉及

        :return: The host_id of this ShowHostStatusRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ShowHostStatusRequest.

        **参数解释：** 域名ID，您可以通过调用查询全部防护域名列表（ListCompositeHosts）获取域名ID。 **约束限制：** 不涉及 **取值范围：** 只能由英文字母、数字组成，且长度为32个字符。 **默认取值：** 不涉及

        :param host_id: The host_id of this ShowHostStatusRequest.
        :type host_id: str
        """
        self._host_id = host_id

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
        if not isinstance(other, ShowHostStatusRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
