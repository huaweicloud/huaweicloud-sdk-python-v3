# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowLlmConfigResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'llm_config_id': 'str',
        'name': 'str',
        'llm_url': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'llm_config_id': 'llm_config_id',
        'name': 'name',
        'llm_url': 'llm_url',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, llm_config_id=None, name=None, llm_url=None, create_time=None, update_time=None, x_request_id=None):
        r"""ShowLlmConfigResponse

        The model defined in huaweicloud sdk

        :param llm_config_id: 大语言模型配置ID。
        :type llm_config_id: str
        :param name: 大语言模型配置名称。
        :type name: str
        :param llm_url: 大语言模型地址。
        :type llm_url: str
        :param create_time: 创建时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type create_time: str
        :param update_time: 更新时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type update_time: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ShowLlmConfigResponse, self).__init__()

        self._llm_config_id = None
        self._name = None
        self._llm_url = None
        self._create_time = None
        self._update_time = None
        self._x_request_id = None
        self.discriminator = None

        if llm_config_id is not None:
            self.llm_config_id = llm_config_id
        if name is not None:
            self.name = name
        if llm_url is not None:
            self.llm_url = llm_url
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def llm_config_id(self):
        r"""Gets the llm_config_id of this ShowLlmConfigResponse.

        大语言模型配置ID。

        :return: The llm_config_id of this ShowLlmConfigResponse.
        :rtype: str
        """
        return self._llm_config_id

    @llm_config_id.setter
    def llm_config_id(self, llm_config_id):
        r"""Sets the llm_config_id of this ShowLlmConfigResponse.

        大语言模型配置ID。

        :param llm_config_id: The llm_config_id of this ShowLlmConfigResponse.
        :type llm_config_id: str
        """
        self._llm_config_id = llm_config_id

    @property
    def name(self):
        r"""Gets the name of this ShowLlmConfigResponse.

        大语言模型配置名称。

        :return: The name of this ShowLlmConfigResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowLlmConfigResponse.

        大语言模型配置名称。

        :param name: The name of this ShowLlmConfigResponse.
        :type name: str
        """
        self._name = name

    @property
    def llm_url(self):
        r"""Gets the llm_url of this ShowLlmConfigResponse.

        大语言模型地址。

        :return: The llm_url of this ShowLlmConfigResponse.
        :rtype: str
        """
        return self._llm_url

    @llm_url.setter
    def llm_url(self, llm_url):
        r"""Sets the llm_url of this ShowLlmConfigResponse.

        大语言模型地址。

        :param llm_url: The llm_url of this ShowLlmConfigResponse.
        :type llm_url: str
        """
        self._llm_url = llm_url

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowLlmConfigResponse.

        创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The create_time of this ShowLlmConfigResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowLlmConfigResponse.

        创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param create_time: The create_time of this ShowLlmConfigResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowLlmConfigResponse.

        更新时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The update_time of this ShowLlmConfigResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowLlmConfigResponse.

        更新时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param update_time: The update_time of this ShowLlmConfigResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ShowLlmConfigResponse.

        :return: The x_request_id of this ShowLlmConfigResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ShowLlmConfigResponse.

        :param x_request_id: The x_request_id of this ShowLlmConfigResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ShowLlmConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
