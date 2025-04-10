# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowWafPolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_name': 'str',
        'overseas_type': 'int',
        'options': 'WafPolicyOptions',
        'level': 'int',
        'mode': 'int'
    }

    attribute_map = {
        'domain_name': 'domain_name',
        'overseas_type': 'overseas_type',
        'options': 'options',
        'level': 'level',
        'mode': 'mode'
    }

    def __init__(self, domain_name=None, overseas_type=None, options=None, level=None, mode=None):
        r"""ShowWafPolicyResponse

        The model defined in huaweicloud sdk

        :param domain_name: 域名(包含端口)
        :type domain_name: str
        :param overseas_type: 0-中国大陆，1-中国大陆外
        :type overseas_type: int
        :param options: 
        :type options: :class:`huaweicloudsdkaad.v2.WafPolicyOptions`
        :param level: 智能CC防护等级：[0-宽松,1- 正常, 2- 严格]
        :type level: int
        :param mode: 智能CC模式：0-预警，1-防护
        :type mode: int
        """
        
        super(ShowWafPolicyResponse, self).__init__()

        self._domain_name = None
        self._overseas_type = None
        self._options = None
        self._level = None
        self._mode = None
        self.discriminator = None

        if domain_name is not None:
            self.domain_name = domain_name
        if overseas_type is not None:
            self.overseas_type = overseas_type
        if options is not None:
            self.options = options
        if level is not None:
            self.level = level
        if mode is not None:
            self.mode = mode

    @property
    def domain_name(self):
        r"""Gets the domain_name of this ShowWafPolicyResponse.

        域名(包含端口)

        :return: The domain_name of this ShowWafPolicyResponse.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this ShowWafPolicyResponse.

        域名(包含端口)

        :param domain_name: The domain_name of this ShowWafPolicyResponse.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def overseas_type(self):
        r"""Gets the overseas_type of this ShowWafPolicyResponse.

        0-中国大陆，1-中国大陆外

        :return: The overseas_type of this ShowWafPolicyResponse.
        :rtype: int
        """
        return self._overseas_type

    @overseas_type.setter
    def overseas_type(self, overseas_type):
        r"""Sets the overseas_type of this ShowWafPolicyResponse.

        0-中国大陆，1-中国大陆外

        :param overseas_type: The overseas_type of this ShowWafPolicyResponse.
        :type overseas_type: int
        """
        self._overseas_type = overseas_type

    @property
    def options(self):
        r"""Gets the options of this ShowWafPolicyResponse.

        :return: The options of this ShowWafPolicyResponse.
        :rtype: :class:`huaweicloudsdkaad.v2.WafPolicyOptions`
        """
        return self._options

    @options.setter
    def options(self, options):
        r"""Sets the options of this ShowWafPolicyResponse.

        :param options: The options of this ShowWafPolicyResponse.
        :type options: :class:`huaweicloudsdkaad.v2.WafPolicyOptions`
        """
        self._options = options

    @property
    def level(self):
        r"""Gets the level of this ShowWafPolicyResponse.

        智能CC防护等级：[0-宽松,1- 正常, 2- 严格]

        :return: The level of this ShowWafPolicyResponse.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this ShowWafPolicyResponse.

        智能CC防护等级：[0-宽松,1- 正常, 2- 严格]

        :param level: The level of this ShowWafPolicyResponse.
        :type level: int
        """
        self._level = level

    @property
    def mode(self):
        r"""Gets the mode of this ShowWafPolicyResponse.

        智能CC模式：0-预警，1-防护

        :return: The mode of this ShowWafPolicyResponse.
        :rtype: int
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this ShowWafPolicyResponse.

        智能CC模式：0-预警，1-防护

        :param mode: The mode of this ShowWafPolicyResponse.
        :type mode: int
        """
        self._mode = mode

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
        if not isinstance(other, ShowWafPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
