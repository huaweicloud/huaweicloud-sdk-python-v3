# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateResolveTaskRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tpl_id': 'str',
        'sms_signs': 'list[str]',
        'resolving_times': 'int',
        'aim_code_type': 'str',
        'generation_type': 'str',
        'domain': 'str',
        'expiration_time': 'int',
        'params': 'list[CreateShortChainParam]'
    }

    attribute_map = {
        'tpl_id': 'tpl_id',
        'sms_signs': 'sms_signs',
        'resolving_times': 'resolving_times',
        'aim_code_type': 'aim_code_type',
        'generation_type': 'generation_type',
        'domain': 'domain',
        'expiration_time': 'expiration_time',
        'params': 'params'
    }

    def __init__(self, tpl_id=None, sms_signs=None, resolving_times=None, aim_code_type=None, generation_type=None, domain=None, expiration_time=None, params=None):
        """CreateResolveTaskRequestBody

        The model defined in huaweicloud sdk

        :param tpl_id: 智能信息模板ID，由9位数字组成。
        :type tpl_id: str
        :param sms_signs: 短信签名列表，需要与最终发送短信的签名一致，才能解析。  &gt; 最多传入10个签名。 
        :type sms_signs: list[str]
        :param resolving_times: 短链最大解析次数。  &gt;个性化短链只支持最大解析数为1，设置其他值无效。 
        :type resolving_times: int
        :param aim_code_type: 生成短链类型。  - group：群发 - individual：个性化  &gt; 使用动态参数模板时，该字段只能为individual。 
        :type aim_code_type: str
        :param generation_type: 生成短码方式。  - 1：标准 - 2：自定义  &gt; 默认1，即标准生成短码。 
        :type generation_type: str
        :param domain: 自定义短链域名，由大小写字母和数字组成的二级域名。  &gt; generation_type为2时，此参数为必填。域名需要提前报备，请联系KooMessage运营人员进行域名报备，域名区分生成短码方式，如报备的是标准生成短码方式，则在自定义生成短码时不能使用此域名。 
        :type domain: str
        :param expiration_time: 失效时间（天）。aim_code_type为group时，取值范围为1~180；aim_code_type为individual个性化时，取值范围为1~7。  &gt; 失效时间精确到秒，例如参数设置为1，创建时间为2022-07-22 21:10:12，过期时间为2022-07-23 21:10:12。 
        :type expiration_time: int
        :param params: 短链参数列表。一次请求最多生成100个短链。  &gt; OPPO模板一次最多申请10个短链。 
        :type params: list[:class:`huaweicloudsdkkoomessage.v1.CreateShortChainParam`]
        """
        
        

        self._tpl_id = None
        self._sms_signs = None
        self._resolving_times = None
        self._aim_code_type = None
        self._generation_type = None
        self._domain = None
        self._expiration_time = None
        self._params = None
        self.discriminator = None

        self.tpl_id = tpl_id
        self.sms_signs = sms_signs
        self.resolving_times = resolving_times
        self.aim_code_type = aim_code_type
        if generation_type is not None:
            self.generation_type = generation_type
        if domain is not None:
            self.domain = domain
        self.expiration_time = expiration_time
        self.params = params

    @property
    def tpl_id(self):
        """Gets the tpl_id of this CreateResolveTaskRequestBody.

        智能信息模板ID，由9位数字组成。

        :return: The tpl_id of this CreateResolveTaskRequestBody.
        :rtype: str
        """
        return self._tpl_id

    @tpl_id.setter
    def tpl_id(self, tpl_id):
        """Sets the tpl_id of this CreateResolveTaskRequestBody.

        智能信息模板ID，由9位数字组成。

        :param tpl_id: The tpl_id of this CreateResolveTaskRequestBody.
        :type tpl_id: str
        """
        self._tpl_id = tpl_id

    @property
    def sms_signs(self):
        """Gets the sms_signs of this CreateResolveTaskRequestBody.

        短信签名列表，需要与最终发送短信的签名一致，才能解析。  > 最多传入10个签名。 

        :return: The sms_signs of this CreateResolveTaskRequestBody.
        :rtype: list[str]
        """
        return self._sms_signs

    @sms_signs.setter
    def sms_signs(self, sms_signs):
        """Sets the sms_signs of this CreateResolveTaskRequestBody.

        短信签名列表，需要与最终发送短信的签名一致，才能解析。  > 最多传入10个签名。 

        :param sms_signs: The sms_signs of this CreateResolveTaskRequestBody.
        :type sms_signs: list[str]
        """
        self._sms_signs = sms_signs

    @property
    def resolving_times(self):
        """Gets the resolving_times of this CreateResolveTaskRequestBody.

        短链最大解析次数。  >个性化短链只支持最大解析数为1，设置其他值无效。 

        :return: The resolving_times of this CreateResolveTaskRequestBody.
        :rtype: int
        """
        return self._resolving_times

    @resolving_times.setter
    def resolving_times(self, resolving_times):
        """Sets the resolving_times of this CreateResolveTaskRequestBody.

        短链最大解析次数。  >个性化短链只支持最大解析数为1，设置其他值无效。 

        :param resolving_times: The resolving_times of this CreateResolveTaskRequestBody.
        :type resolving_times: int
        """
        self._resolving_times = resolving_times

    @property
    def aim_code_type(self):
        """Gets the aim_code_type of this CreateResolveTaskRequestBody.

        生成短链类型。  - group：群发 - individual：个性化  > 使用动态参数模板时，该字段只能为individual。 

        :return: The aim_code_type of this CreateResolveTaskRequestBody.
        :rtype: str
        """
        return self._aim_code_type

    @aim_code_type.setter
    def aim_code_type(self, aim_code_type):
        """Sets the aim_code_type of this CreateResolveTaskRequestBody.

        生成短链类型。  - group：群发 - individual：个性化  > 使用动态参数模板时，该字段只能为individual。 

        :param aim_code_type: The aim_code_type of this CreateResolveTaskRequestBody.
        :type aim_code_type: str
        """
        self._aim_code_type = aim_code_type

    @property
    def generation_type(self):
        """Gets the generation_type of this CreateResolveTaskRequestBody.

        生成短码方式。  - 1：标准 - 2：自定义  > 默认1，即标准生成短码。 

        :return: The generation_type of this CreateResolveTaskRequestBody.
        :rtype: str
        """
        return self._generation_type

    @generation_type.setter
    def generation_type(self, generation_type):
        """Sets the generation_type of this CreateResolveTaskRequestBody.

        生成短码方式。  - 1：标准 - 2：自定义  > 默认1，即标准生成短码。 

        :param generation_type: The generation_type of this CreateResolveTaskRequestBody.
        :type generation_type: str
        """
        self._generation_type = generation_type

    @property
    def domain(self):
        """Gets the domain of this CreateResolveTaskRequestBody.

        自定义短链域名，由大小写字母和数字组成的二级域名。  > generation_type为2时，此参数为必填。域名需要提前报备，请联系KooMessage运营人员进行域名报备，域名区分生成短码方式，如报备的是标准生成短码方式，则在自定义生成短码时不能使用此域名。 

        :return: The domain of this CreateResolveTaskRequestBody.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this CreateResolveTaskRequestBody.

        自定义短链域名，由大小写字母和数字组成的二级域名。  > generation_type为2时，此参数为必填。域名需要提前报备，请联系KooMessage运营人员进行域名报备，域名区分生成短码方式，如报备的是标准生成短码方式，则在自定义生成短码时不能使用此域名。 

        :param domain: The domain of this CreateResolveTaskRequestBody.
        :type domain: str
        """
        self._domain = domain

    @property
    def expiration_time(self):
        """Gets the expiration_time of this CreateResolveTaskRequestBody.

        失效时间（天）。aim_code_type为group时，取值范围为1~180；aim_code_type为individual个性化时，取值范围为1~7。  > 失效时间精确到秒，例如参数设置为1，创建时间为2022-07-22 21:10:12，过期时间为2022-07-23 21:10:12。 

        :return: The expiration_time of this CreateResolveTaskRequestBody.
        :rtype: int
        """
        return self._expiration_time

    @expiration_time.setter
    def expiration_time(self, expiration_time):
        """Sets the expiration_time of this CreateResolveTaskRequestBody.

        失效时间（天）。aim_code_type为group时，取值范围为1~180；aim_code_type为individual个性化时，取值范围为1~7。  > 失效时间精确到秒，例如参数设置为1，创建时间为2022-07-22 21:10:12，过期时间为2022-07-23 21:10:12。 

        :param expiration_time: The expiration_time of this CreateResolveTaskRequestBody.
        :type expiration_time: int
        """
        self._expiration_time = expiration_time

    @property
    def params(self):
        """Gets the params of this CreateResolveTaskRequestBody.

        短链参数列表。一次请求最多生成100个短链。  > OPPO模板一次最多申请10个短链。 

        :return: The params of this CreateResolveTaskRequestBody.
        :rtype: list[:class:`huaweicloudsdkkoomessage.v1.CreateShortChainParam`]
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this CreateResolveTaskRequestBody.

        短链参数列表。一次请求最多生成100个短链。  > OPPO模板一次最多申请10个短链。 

        :param params: The params of this CreateResolveTaskRequestBody.
        :type params: list[:class:`huaweicloudsdkkoomessage.v1.CreateShortChainParam`]
        """
        self._params = params

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
        if not isinstance(other, CreateResolveTaskRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
