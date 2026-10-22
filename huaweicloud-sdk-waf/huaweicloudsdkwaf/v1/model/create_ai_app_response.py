# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAiAppResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'create_time': 'int',
        'api_sign': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'create_time': 'createTime',
        'api_sign': 'apiSign'
    }

    def __init__(self, id=None, name=None, description=None, create_time=None, api_sign=None):
        r"""CreateAiAppResponse

        The model defined in huaweicloud sdk

        :param id: AI应用ID
        :type id: str
        :param name: AI应用名称
        :type name: str
        :param description: 应用描述
        :type description: str
        :param create_time: 创建时间戳（毫秒Unix时间戳）
        :type create_time: int
        :param api_sign: API签名
        :type api_sign: str
        """
        
        super().__init__()

        self._id = None
        self._name = None
        self._description = None
        self._create_time = None
        self._api_sign = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if create_time is not None:
            self.create_time = create_time
        if api_sign is not None:
            self.api_sign = api_sign

    @property
    def id(self):
        r"""Gets the id of this CreateAiAppResponse.

        AI应用ID

        :return: The id of this CreateAiAppResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateAiAppResponse.

        AI应用ID

        :param id: The id of this CreateAiAppResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this CreateAiAppResponse.

        AI应用名称

        :return: The name of this CreateAiAppResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateAiAppResponse.

        AI应用名称

        :param name: The name of this CreateAiAppResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateAiAppResponse.

        应用描述

        :return: The description of this CreateAiAppResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateAiAppResponse.

        应用描述

        :param description: The description of this CreateAiAppResponse.
        :type description: str
        """
        self._description = description

    @property
    def create_time(self):
        r"""Gets the create_time of this CreateAiAppResponse.

        创建时间戳（毫秒Unix时间戳）

        :return: The create_time of this CreateAiAppResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this CreateAiAppResponse.

        创建时间戳（毫秒Unix时间戳）

        :param create_time: The create_time of this CreateAiAppResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def api_sign(self):
        r"""Gets the api_sign of this CreateAiAppResponse.

        API签名

        :return: The api_sign of this CreateAiAppResponse.
        :rtype: str
        """
        return self._api_sign

    @api_sign.setter
    def api_sign(self, api_sign):
        r"""Sets the api_sign of this CreateAiAppResponse.

        API签名

        :param api_sign: The api_sign of this CreateAiAppResponse.
        :type api_sign: str
        """
        self._api_sign = api_sign

    def to_dict(self):
        import warnings
        warnings.warn("CreateAiAppResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, CreateAiAppResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
