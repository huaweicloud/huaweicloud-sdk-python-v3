# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AiApiKeyBaseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ai_api_key': 'str',
        'alias': 'str',
        'app_id': 'str',
        'create_time': 'datetime',
        'id': 'str'
    }

    attribute_map = {
        'ai_api_key': 'ai_api_key',
        'alias': 'alias',
        'app_id': 'app_id',
        'create_time': 'create_time',
        'id': 'id'
    }

    def __init__(self, ai_api_key=None, alias=None, app_id=None, create_time=None, id=None):
        r"""AiApiKeyBaseInfo

        The model defined in huaweicloud sdk

        :param ai_api_key: AIAPIKey值，不指定具体值时，由后台自动生成随机字符串。 支持大小写英文字母、数字，以及+-_/&#x3D;特殊字符，长度为8~128个字符。 
        :type ai_api_key: str
        :param alias: AIAPIKey的别名。支持大小写字母，数字，下划线，中划线，长度为1~100个字符。
        :type alias: str
        :param app_id: 凭据编号。
        :type app_id: str
        :param create_time: 创建时间。
        :type create_time: datetime
        :param id: AIAPIKey编号。
        :type id: str
        """
        
        

        self._ai_api_key = None
        self._alias = None
        self._app_id = None
        self._create_time = None
        self._id = None
        self.discriminator = None

        if ai_api_key is not None:
            self.ai_api_key = ai_api_key
        if alias is not None:
            self.alias = alias
        if app_id is not None:
            self.app_id = app_id
        if create_time is not None:
            self.create_time = create_time
        if id is not None:
            self.id = id

    @property
    def ai_api_key(self):
        r"""Gets the ai_api_key of this AiApiKeyBaseInfo.

        AIAPIKey值，不指定具体值时，由后台自动生成随机字符串。 支持大小写英文字母、数字，以及+-_/=特殊字符，长度为8~128个字符。 

        :return: The ai_api_key of this AiApiKeyBaseInfo.
        :rtype: str
        """
        return self._ai_api_key

    @ai_api_key.setter
    def ai_api_key(self, ai_api_key):
        r"""Sets the ai_api_key of this AiApiKeyBaseInfo.

        AIAPIKey值，不指定具体值时，由后台自动生成随机字符串。 支持大小写英文字母、数字，以及+-_/=特殊字符，长度为8~128个字符。 

        :param ai_api_key: The ai_api_key of this AiApiKeyBaseInfo.
        :type ai_api_key: str
        """
        self._ai_api_key = ai_api_key

    @property
    def alias(self):
        r"""Gets the alias of this AiApiKeyBaseInfo.

        AIAPIKey的别名。支持大小写字母，数字，下划线，中划线，长度为1~100个字符。

        :return: The alias of this AiApiKeyBaseInfo.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        r"""Sets the alias of this AiApiKeyBaseInfo.

        AIAPIKey的别名。支持大小写字母，数字，下划线，中划线，长度为1~100个字符。

        :param alias: The alias of this AiApiKeyBaseInfo.
        :type alias: str
        """
        self._alias = alias

    @property
    def app_id(self):
        r"""Gets the app_id of this AiApiKeyBaseInfo.

        凭据编号。

        :return: The app_id of this AiApiKeyBaseInfo.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this AiApiKeyBaseInfo.

        凭据编号。

        :param app_id: The app_id of this AiApiKeyBaseInfo.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def create_time(self):
        r"""Gets the create_time of this AiApiKeyBaseInfo.

        创建时间。

        :return: The create_time of this AiApiKeyBaseInfo.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this AiApiKeyBaseInfo.

        创建时间。

        :param create_time: The create_time of this AiApiKeyBaseInfo.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def id(self):
        r"""Gets the id of this AiApiKeyBaseInfo.

        AIAPIKey编号。

        :return: The id of this AiApiKeyBaseInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AiApiKeyBaseInfo.

        AIAPIKey编号。

        :param id: The id of this AiApiKeyBaseInfo.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, AiApiKeyBaseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
