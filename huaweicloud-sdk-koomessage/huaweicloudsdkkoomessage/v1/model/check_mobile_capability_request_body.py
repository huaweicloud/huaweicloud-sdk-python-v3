# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckMobileCapabilityRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'mobiles': 'list[str]',
        'tpl_id': 'str',
        'encryption_alg': 'str'
    }

    attribute_map = {
        'mobiles': 'mobiles',
        'tpl_id': 'tpl_id',
        'encryption_alg': 'encryption_alg'
    }

    def __init__(self, mobiles=None, tpl_id=None, encryption_alg=None):
        r"""CheckMobileCapabilityRequestBody

        The model defined in huaweicloud sdk

        :param mobiles: 待查询的手机号码，一次最多请求100个。  &gt;不加密时，参数可传入纯手机号或国家码加手机号，国家码不带“+”号，例如国内手机号“131****0000”，参数可传入“131****0000”、“86131****0000”、“0086131****0000”。使用SHA1加密，mobiles传入号码国家码与手机号码的SHA1算法后的摘要，国家码格式为纯数字，不带“+”，去掉前面的0，例如国内手机号“131****0000”，使用“86131****0000”进行SHA1加密。 
        :type mobiles: list[str]
        :param tpl_id: 智能信息模板ID，由9位数字组成。 &gt; - 填写时，根据该模板所支持的厂商返回手机终端展示智能信息的能力状态 &gt; - 不填则返回手机终端在所有厂商展示智能信息的能力状态 
        :type tpl_id: str
        :param encryption_alg: 加密类型。  - NONE：不加密 - SHA1：使用SHA1加密算法加密  &gt; 默认为NONE。 
        :type encryption_alg: str
        """
        
        

        self._mobiles = None
        self._tpl_id = None
        self._encryption_alg = None
        self.discriminator = None

        self.mobiles = mobiles
        if tpl_id is not None:
            self.tpl_id = tpl_id
        if encryption_alg is not None:
            self.encryption_alg = encryption_alg

    @property
    def mobiles(self):
        r"""Gets the mobiles of this CheckMobileCapabilityRequestBody.

        待查询的手机号码，一次最多请求100个。  >不加密时，参数可传入纯手机号或国家码加手机号，国家码不带“+”号，例如国内手机号“131****0000”，参数可传入“131****0000”、“86131****0000”、“0086131****0000”。使用SHA1加密，mobiles传入号码国家码与手机号码的SHA1算法后的摘要，国家码格式为纯数字，不带“+”，去掉前面的0，例如国内手机号“131****0000”，使用“86131****0000”进行SHA1加密。 

        :return: The mobiles of this CheckMobileCapabilityRequestBody.
        :rtype: list[str]
        """
        return self._mobiles

    @mobiles.setter
    def mobiles(self, mobiles):
        r"""Sets the mobiles of this CheckMobileCapabilityRequestBody.

        待查询的手机号码，一次最多请求100个。  >不加密时，参数可传入纯手机号或国家码加手机号，国家码不带“+”号，例如国内手机号“131****0000”，参数可传入“131****0000”、“86131****0000”、“0086131****0000”。使用SHA1加密，mobiles传入号码国家码与手机号码的SHA1算法后的摘要，国家码格式为纯数字，不带“+”，去掉前面的0，例如国内手机号“131****0000”，使用“86131****0000”进行SHA1加密。 

        :param mobiles: The mobiles of this CheckMobileCapabilityRequestBody.
        :type mobiles: list[str]
        """
        self._mobiles = mobiles

    @property
    def tpl_id(self):
        r"""Gets the tpl_id of this CheckMobileCapabilityRequestBody.

        智能信息模板ID，由9位数字组成。 > - 填写时，根据该模板所支持的厂商返回手机终端展示智能信息的能力状态 > - 不填则返回手机终端在所有厂商展示智能信息的能力状态 

        :return: The tpl_id of this CheckMobileCapabilityRequestBody.
        :rtype: str
        """
        return self._tpl_id

    @tpl_id.setter
    def tpl_id(self, tpl_id):
        r"""Sets the tpl_id of this CheckMobileCapabilityRequestBody.

        智能信息模板ID，由9位数字组成。 > - 填写时，根据该模板所支持的厂商返回手机终端展示智能信息的能力状态 > - 不填则返回手机终端在所有厂商展示智能信息的能力状态 

        :param tpl_id: The tpl_id of this CheckMobileCapabilityRequestBody.
        :type tpl_id: str
        """
        self._tpl_id = tpl_id

    @property
    def encryption_alg(self):
        r"""Gets the encryption_alg of this CheckMobileCapabilityRequestBody.

        加密类型。  - NONE：不加密 - SHA1：使用SHA1加密算法加密  > 默认为NONE。 

        :return: The encryption_alg of this CheckMobileCapabilityRequestBody.
        :rtype: str
        """
        return self._encryption_alg

    @encryption_alg.setter
    def encryption_alg(self, encryption_alg):
        r"""Sets the encryption_alg of this CheckMobileCapabilityRequestBody.

        加密类型。  - NONE：不加密 - SHA1：使用SHA1加密算法加密  > 默认为NONE。 

        :param encryption_alg: The encryption_alg of this CheckMobileCapabilityRequestBody.
        :type encryption_alg: str
        """
        self._encryption_alg = encryption_alg

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
        if not isinstance(other, CheckMobileCapabilityRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
