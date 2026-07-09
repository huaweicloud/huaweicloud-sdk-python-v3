# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCloudWafPostPaidResourceRequestbody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'console_area': 'str',
        'postpaid_name': 'str',
        'extend_params': 'object'
    }

    attribute_map = {
        'console_area': 'console_area',
        'postpaid_name': 'postpaid_name',
        'extend_params': 'extend_params'
    }

    def __init__(self, console_area=None, postpaid_name=None, extend_params=None):
        r"""CreateCloudWafPostPaidResourceRequestbody

        The model defined in huaweicloud sdk

        :param console_area: 租户所在的站点 - hec-hk：华为云国际站 - hws：华为云大陆站
        :type console_area: str
        :param postpaid_name: **参数解释：** 按需功能名称 **取值范围：**  - CLOUD_WAF：按需云模式  - LARGE_MODEL_FIREWALL_AI_GUARD_DETECT: AI安全护栏
        :type postpaid_name: str
        :param extend_params: **参数解释：** 扩展参数 **取值范围：** 不涉及
        :type extend_params: object
        """
        
        

        self._console_area = None
        self._postpaid_name = None
        self._extend_params = None
        self.discriminator = None

        self.console_area = console_area
        if postpaid_name is not None:
            self.postpaid_name = postpaid_name
        if extend_params is not None:
            self.extend_params = extend_params

    @property
    def console_area(self):
        r"""Gets the console_area of this CreateCloudWafPostPaidResourceRequestbody.

        租户所在的站点 - hec-hk：华为云国际站 - hws：华为云大陆站

        :return: The console_area of this CreateCloudWafPostPaidResourceRequestbody.
        :rtype: str
        """
        return self._console_area

    @console_area.setter
    def console_area(self, console_area):
        r"""Sets the console_area of this CreateCloudWafPostPaidResourceRequestbody.

        租户所在的站点 - hec-hk：华为云国际站 - hws：华为云大陆站

        :param console_area: The console_area of this CreateCloudWafPostPaidResourceRequestbody.
        :type console_area: str
        """
        self._console_area = console_area

    @property
    def postpaid_name(self):
        r"""Gets the postpaid_name of this CreateCloudWafPostPaidResourceRequestbody.

        **参数解释：** 按需功能名称 **取值范围：**  - CLOUD_WAF：按需云模式  - LARGE_MODEL_FIREWALL_AI_GUARD_DETECT: AI安全护栏

        :return: The postpaid_name of this CreateCloudWafPostPaidResourceRequestbody.
        :rtype: str
        """
        return self._postpaid_name

    @postpaid_name.setter
    def postpaid_name(self, postpaid_name):
        r"""Sets the postpaid_name of this CreateCloudWafPostPaidResourceRequestbody.

        **参数解释：** 按需功能名称 **取值范围：**  - CLOUD_WAF：按需云模式  - LARGE_MODEL_FIREWALL_AI_GUARD_DETECT: AI安全护栏

        :param postpaid_name: The postpaid_name of this CreateCloudWafPostPaidResourceRequestbody.
        :type postpaid_name: str
        """
        self._postpaid_name = postpaid_name

    @property
    def extend_params(self):
        r"""Gets the extend_params of this CreateCloudWafPostPaidResourceRequestbody.

        **参数解释：** 扩展参数 **取值范围：** 不涉及

        :return: The extend_params of this CreateCloudWafPostPaidResourceRequestbody.
        :rtype: object
        """
        return self._extend_params

    @extend_params.setter
    def extend_params(self, extend_params):
        r"""Sets the extend_params of this CreateCloudWafPostPaidResourceRequestbody.

        **参数解释：** 扩展参数 **取值范围：** 不涉及

        :param extend_params: The extend_params of this CreateCloudWafPostPaidResourceRequestbody.
        :type extend_params: object
        """
        self._extend_params = extend_params

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateCloudWafPostPaidResourceRequestbody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
