# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAllConfigValueByTypeAndKeyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'comments': 'str',
        'config_key': 'str',
        'config_type': 'str',
        'config_value': 'str',
        'create_time': 'datetime',
        'create_user': 'str',
        'id': 'str',
        'test_service_id': 'str',
        'update_time': 'datetime',
        'update_user': 'str'
    }

    attribute_map = {
        'comments': 'comments',
        'config_key': 'config_key',
        'config_type': 'config_type',
        'config_value': 'config_value',
        'create_time': 'create_time',
        'create_user': 'create_user',
        'id': 'id',
        'test_service_id': 'test_service_id',
        'update_time': 'update_time',
        'update_user': 'update_user'
    }

    def __init__(self, comments=None, config_key=None, config_type=None, config_value=None, create_time=None, create_user=None, id=None, test_service_id=None, update_time=None, update_user=None):
        r"""ShowAllConfigValueByTypeAndKeyResponse

        The model defined in huaweicloud sdk

        :param comments: 备注
        :type comments: str
        :param config_key: 配置键
        :type config_key: str
        :param config_type: 配置类型
        :type config_type: str
        :param config_value: 配置值
        :type config_value: str
        :param create_time: 创建时间
        :type create_time: datetime
        :param create_user: 创建者
        :type create_user: str
        :param id: UUID
        :type id: str
        :param test_service_id: 服务id
        :type test_service_id: str
        :param update_time: 修改时间
        :type update_time: datetime
        :param update_user: 修改者
        :type update_user: str
        """
        
        super(ShowAllConfigValueByTypeAndKeyResponse, self).__init__()

        self._comments = None
        self._config_key = None
        self._config_type = None
        self._config_value = None
        self._create_time = None
        self._create_user = None
        self._id = None
        self._test_service_id = None
        self._update_time = None
        self._update_user = None
        self.discriminator = None

        if comments is not None:
            self.comments = comments
        if config_key is not None:
            self.config_key = config_key
        if config_type is not None:
            self.config_type = config_type
        if config_value is not None:
            self.config_value = config_value
        if create_time is not None:
            self.create_time = create_time
        if create_user is not None:
            self.create_user = create_user
        if id is not None:
            self.id = id
        if test_service_id is not None:
            self.test_service_id = test_service_id
        if update_time is not None:
            self.update_time = update_time
        if update_user is not None:
            self.update_user = update_user

    @property
    def comments(self):
        r"""Gets the comments of this ShowAllConfigValueByTypeAndKeyResponse.

        备注

        :return: The comments of this ShowAllConfigValueByTypeAndKeyResponse.
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        r"""Sets the comments of this ShowAllConfigValueByTypeAndKeyResponse.

        备注

        :param comments: The comments of this ShowAllConfigValueByTypeAndKeyResponse.
        :type comments: str
        """
        self._comments = comments

    @property
    def config_key(self):
        r"""Gets the config_key of this ShowAllConfigValueByTypeAndKeyResponse.

        配置键

        :return: The config_key of this ShowAllConfigValueByTypeAndKeyResponse.
        :rtype: str
        """
        return self._config_key

    @config_key.setter
    def config_key(self, config_key):
        r"""Sets the config_key of this ShowAllConfigValueByTypeAndKeyResponse.

        配置键

        :param config_key: The config_key of this ShowAllConfigValueByTypeAndKeyResponse.
        :type config_key: str
        """
        self._config_key = config_key

    @property
    def config_type(self):
        r"""Gets the config_type of this ShowAllConfigValueByTypeAndKeyResponse.

        配置类型

        :return: The config_type of this ShowAllConfigValueByTypeAndKeyResponse.
        :rtype: str
        """
        return self._config_type

    @config_type.setter
    def config_type(self, config_type):
        r"""Sets the config_type of this ShowAllConfigValueByTypeAndKeyResponse.

        配置类型

        :param config_type: The config_type of this ShowAllConfigValueByTypeAndKeyResponse.
        :type config_type: str
        """
        self._config_type = config_type

    @property
    def config_value(self):
        r"""Gets the config_value of this ShowAllConfigValueByTypeAndKeyResponse.

        配置值

        :return: The config_value of this ShowAllConfigValueByTypeAndKeyResponse.
        :rtype: str
        """
        return self._config_value

    @config_value.setter
    def config_value(self, config_value):
        r"""Sets the config_value of this ShowAllConfigValueByTypeAndKeyResponse.

        配置值

        :param config_value: The config_value of this ShowAllConfigValueByTypeAndKeyResponse.
        :type config_value: str
        """
        self._config_value = config_value

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowAllConfigValueByTypeAndKeyResponse.

        创建时间

        :return: The create_time of this ShowAllConfigValueByTypeAndKeyResponse.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowAllConfigValueByTypeAndKeyResponse.

        创建时间

        :param create_time: The create_time of this ShowAllConfigValueByTypeAndKeyResponse.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def create_user(self):
        r"""Gets the create_user of this ShowAllConfigValueByTypeAndKeyResponse.

        创建者

        :return: The create_user of this ShowAllConfigValueByTypeAndKeyResponse.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        r"""Sets the create_user of this ShowAllConfigValueByTypeAndKeyResponse.

        创建者

        :param create_user: The create_user of this ShowAllConfigValueByTypeAndKeyResponse.
        :type create_user: str
        """
        self._create_user = create_user

    @property
    def id(self):
        r"""Gets the id of this ShowAllConfigValueByTypeAndKeyResponse.

        UUID

        :return: The id of this ShowAllConfigValueByTypeAndKeyResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowAllConfigValueByTypeAndKeyResponse.

        UUID

        :param id: The id of this ShowAllConfigValueByTypeAndKeyResponse.
        :type id: str
        """
        self._id = id

    @property
    def test_service_id(self):
        r"""Gets the test_service_id of this ShowAllConfigValueByTypeAndKeyResponse.

        服务id

        :return: The test_service_id of this ShowAllConfigValueByTypeAndKeyResponse.
        :rtype: str
        """
        return self._test_service_id

    @test_service_id.setter
    def test_service_id(self, test_service_id):
        r"""Sets the test_service_id of this ShowAllConfigValueByTypeAndKeyResponse.

        服务id

        :param test_service_id: The test_service_id of this ShowAllConfigValueByTypeAndKeyResponse.
        :type test_service_id: str
        """
        self._test_service_id = test_service_id

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowAllConfigValueByTypeAndKeyResponse.

        修改时间

        :return: The update_time of this ShowAllConfigValueByTypeAndKeyResponse.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowAllConfigValueByTypeAndKeyResponse.

        修改时间

        :param update_time: The update_time of this ShowAllConfigValueByTypeAndKeyResponse.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def update_user(self):
        r"""Gets the update_user of this ShowAllConfigValueByTypeAndKeyResponse.

        修改者

        :return: The update_user of this ShowAllConfigValueByTypeAndKeyResponse.
        :rtype: str
        """
        return self._update_user

    @update_user.setter
    def update_user(self, update_user):
        r"""Sets the update_user of this ShowAllConfigValueByTypeAndKeyResponse.

        修改者

        :param update_user: The update_user of this ShowAllConfigValueByTypeAndKeyResponse.
        :type update_user: str
        """
        self._update_user = update_user

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
        if not isinstance(other, ShowAllConfigValueByTypeAndKeyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
