# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AIMResolveTask:

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
        'resolve_times': 'int',
        'aim_code_type': 'str',
        'generation_type': 'str',
        'domain': 'str',
        'expiration_time': 'int',
        'params': 'list[CreateResolveTaskParam]'
    }

    attribute_map = {
        'tpl_id': 'tpl_id',
        'resolve_times': 'resolve_times',
        'aim_code_type': 'aim_code_type',
        'generation_type': 'generation_type',
        'domain': 'domain',
        'expiration_time': 'expiration_time',
        'params': 'params'
    }

    def __init__(self, tpl_id=None, resolve_times=None, aim_code_type=None, generation_type=None, domain=None, expiration_time=None, params=None):
        r"""AIMResolveTask

        The model defined in huaweicloud sdk

        :param tpl_id: 智能信息模板ID，由9位数字组成。
        :type tpl_id: str
        :param resolve_times: 短链的最大解析次数。  &gt; 个性化短链只支持最大解析数为1，设置其他值无效 
        :type resolve_times: int
        :param aim_code_type: 智能信息编码类型。 - individual：个性化 
        :type aim_code_type: str
        :param generation_type: 生成短码方式。  - 1：标准 - 2：自定义  &gt; 默认1，即标准生成短码。 
        :type generation_type: str
        :param domain: 自定义短链域名，由大小写字母和数字组成的二级域名。   &gt; 自定义短码即generation_type为2时，此参数为必填。域名需要提前报备，请联系KooMessage运营人员进行域名报备，域名区分生成短码方式，如报备的是标准生成短码方式，则在自定义生成短码时不能使用此域名。 
        :type domain: str
        :param expiration_time: 失效时间（天）。aim_code_type为individual个性化时，取值范围为1~7。  &gt; 失效时间精确到秒，例如参数设置为1，创建时间为2022-07-22 21:10:12，过期时间为2022-07-23 21:10:12。 
        :type expiration_time: int
        :param params: 短链解析详情列表。一次请求最多100个短链。 
        :type params: list[:class:`huaweicloudsdkkoomessage.v1.CreateResolveTaskParam`]
        """
        
        

        self._tpl_id = None
        self._resolve_times = None
        self._aim_code_type = None
        self._generation_type = None
        self._domain = None
        self._expiration_time = None
        self._params = None
        self.discriminator = None

        self.tpl_id = tpl_id
        self.resolve_times = resolve_times
        self.aim_code_type = aim_code_type
        if generation_type is not None:
            self.generation_type = generation_type
        if domain is not None:
            self.domain = domain
        self.expiration_time = expiration_time
        self.params = params

    @property
    def tpl_id(self):
        r"""Gets the tpl_id of this AIMResolveTask.

        智能信息模板ID，由9位数字组成。

        :return: The tpl_id of this AIMResolveTask.
        :rtype: str
        """
        return self._tpl_id

    @tpl_id.setter
    def tpl_id(self, tpl_id):
        r"""Sets the tpl_id of this AIMResolveTask.

        智能信息模板ID，由9位数字组成。

        :param tpl_id: The tpl_id of this AIMResolveTask.
        :type tpl_id: str
        """
        self._tpl_id = tpl_id

    @property
    def resolve_times(self):
        r"""Gets the resolve_times of this AIMResolveTask.

        短链的最大解析次数。  > 个性化短链只支持最大解析数为1，设置其他值无效 

        :return: The resolve_times of this AIMResolveTask.
        :rtype: int
        """
        return self._resolve_times

    @resolve_times.setter
    def resolve_times(self, resolve_times):
        r"""Sets the resolve_times of this AIMResolveTask.

        短链的最大解析次数。  > 个性化短链只支持最大解析数为1，设置其他值无效 

        :param resolve_times: The resolve_times of this AIMResolveTask.
        :type resolve_times: int
        """
        self._resolve_times = resolve_times

    @property
    def aim_code_type(self):
        r"""Gets the aim_code_type of this AIMResolveTask.

        智能信息编码类型。 - individual：个性化 

        :return: The aim_code_type of this AIMResolveTask.
        :rtype: str
        """
        return self._aim_code_type

    @aim_code_type.setter
    def aim_code_type(self, aim_code_type):
        r"""Sets the aim_code_type of this AIMResolveTask.

        智能信息编码类型。 - individual：个性化 

        :param aim_code_type: The aim_code_type of this AIMResolveTask.
        :type aim_code_type: str
        """
        self._aim_code_type = aim_code_type

    @property
    def generation_type(self):
        r"""Gets the generation_type of this AIMResolveTask.

        生成短码方式。  - 1：标准 - 2：自定义  > 默认1，即标准生成短码。 

        :return: The generation_type of this AIMResolveTask.
        :rtype: str
        """
        return self._generation_type

    @generation_type.setter
    def generation_type(self, generation_type):
        r"""Sets the generation_type of this AIMResolveTask.

        生成短码方式。  - 1：标准 - 2：自定义  > 默认1，即标准生成短码。 

        :param generation_type: The generation_type of this AIMResolveTask.
        :type generation_type: str
        """
        self._generation_type = generation_type

    @property
    def domain(self):
        r"""Gets the domain of this AIMResolveTask.

        自定义短链域名，由大小写字母和数字组成的二级域名。   > 自定义短码即generation_type为2时，此参数为必填。域名需要提前报备，请联系KooMessage运营人员进行域名报备，域名区分生成短码方式，如报备的是标准生成短码方式，则在自定义生成短码时不能使用此域名。 

        :return: The domain of this AIMResolveTask.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this AIMResolveTask.

        自定义短链域名，由大小写字母和数字组成的二级域名。   > 自定义短码即generation_type为2时，此参数为必填。域名需要提前报备，请联系KooMessage运营人员进行域名报备，域名区分生成短码方式，如报备的是标准生成短码方式，则在自定义生成短码时不能使用此域名。 

        :param domain: The domain of this AIMResolveTask.
        :type domain: str
        """
        self._domain = domain

    @property
    def expiration_time(self):
        r"""Gets the expiration_time of this AIMResolveTask.

        失效时间（天）。aim_code_type为individual个性化时，取值范围为1~7。  > 失效时间精确到秒，例如参数设置为1，创建时间为2022-07-22 21:10:12，过期时间为2022-07-23 21:10:12。 

        :return: The expiration_time of this AIMResolveTask.
        :rtype: int
        """
        return self._expiration_time

    @expiration_time.setter
    def expiration_time(self, expiration_time):
        r"""Sets the expiration_time of this AIMResolveTask.

        失效时间（天）。aim_code_type为individual个性化时，取值范围为1~7。  > 失效时间精确到秒，例如参数设置为1，创建时间为2022-07-22 21:10:12，过期时间为2022-07-23 21:10:12。 

        :param expiration_time: The expiration_time of this AIMResolveTask.
        :type expiration_time: int
        """
        self._expiration_time = expiration_time

    @property
    def params(self):
        r"""Gets the params of this AIMResolveTask.

        短链解析详情列表。一次请求最多100个短链。 

        :return: The params of this AIMResolveTask.
        :rtype: list[:class:`huaweicloudsdkkoomessage.v1.CreateResolveTaskParam`]
        """
        return self._params

    @params.setter
    def params(self, params):
        r"""Sets the params of this AIMResolveTask.

        短链解析详情列表。一次请求最多100个短链。 

        :param params: The params of this AIMResolveTask.
        :type params: list[:class:`huaweicloudsdkkoomessage.v1.CreateResolveTaskParam`]
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
        if not isinstance(other, AIMResolveTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
