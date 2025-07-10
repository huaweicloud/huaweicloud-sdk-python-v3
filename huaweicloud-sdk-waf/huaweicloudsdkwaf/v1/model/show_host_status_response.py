# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowHostStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'status': 'str',
        'waf_instance_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'status': 'status',
        'waf_instance_id': 'waf_instance_id'
    }

    def __init__(self, name=None, status=None, waf_instance_id=None):
        r"""ShowHostStatusResponse

        The model defined in huaweicloud sdk

        :param name: **参数解释：** 域名 **取值范围：** 不涉及
        :type name: str
        :param status: **参数解释：** 域名的防护状态 **取值范围：** - enabled：防护中，WAF根据您配置的策略进行攻击检测 - disabled：未防护，WAF只转发该域名的请求，不做攻击检测 - bypassed：该域名的请求直接到达其后端服务器，不再经过WAF
        :type status: str
        :param waf_instance_id: **参数解释：** 域名ID **取值范围：** 不涉及
        :type waf_instance_id: str
        """
        
        super(ShowHostStatusResponse, self).__init__()

        self._name = None
        self._status = None
        self._waf_instance_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if waf_instance_id is not None:
            self.waf_instance_id = waf_instance_id

    @property
    def name(self):
        r"""Gets the name of this ShowHostStatusResponse.

        **参数解释：** 域名 **取值范围：** 不涉及

        :return: The name of this ShowHostStatusResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowHostStatusResponse.

        **参数解释：** 域名 **取值范围：** 不涉及

        :param name: The name of this ShowHostStatusResponse.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this ShowHostStatusResponse.

        **参数解释：** 域名的防护状态 **取值范围：** - enabled：防护中，WAF根据您配置的策略进行攻击检测 - disabled：未防护，WAF只转发该域名的请求，不做攻击检测 - bypassed：该域名的请求直接到达其后端服务器，不再经过WAF

        :return: The status of this ShowHostStatusResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowHostStatusResponse.

        **参数解释：** 域名的防护状态 **取值范围：** - enabled：防护中，WAF根据您配置的策略进行攻击检测 - disabled：未防护，WAF只转发该域名的请求，不做攻击检测 - bypassed：该域名的请求直接到达其后端服务器，不再经过WAF

        :param status: The status of this ShowHostStatusResponse.
        :type status: str
        """
        self._status = status

    @property
    def waf_instance_id(self):
        r"""Gets the waf_instance_id of this ShowHostStatusResponse.

        **参数解释：** 域名ID **取值范围：** 不涉及

        :return: The waf_instance_id of this ShowHostStatusResponse.
        :rtype: str
        """
        return self._waf_instance_id

    @waf_instance_id.setter
    def waf_instance_id(self, waf_instance_id):
        r"""Sets the waf_instance_id of this ShowHostStatusResponse.

        **参数解释：** 域名ID **取值范围：** 不涉及

        :param waf_instance_id: The waf_instance_id of this ShowHostStatusResponse.
        :type waf_instance_id: str
        """
        self._waf_instance_id = waf_instance_id

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
        if not isinstance(other, ShowHostStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
