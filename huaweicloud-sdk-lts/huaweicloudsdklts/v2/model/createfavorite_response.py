# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatefavoriteResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'create_time': 'str',
        'eps_id': 'str',
        'favorite_resource_id': 'str',
        'favorite_resource_type': 'str',
        'log_group_id': 'str',
        'log_group_name': 'str',
        'log_stream_id': 'str',
        'log_stream_name': 'str',
        'project_id': 'str'
    }

    attribute_map = {
        'create_time': 'create_time',
        'eps_id': 'eps_id',
        'favorite_resource_id': 'favorite_resource_id',
        'favorite_resource_type': 'favorite_resource_type',
        'log_group_id': 'log_group_id',
        'log_group_name': 'log_group_name',
        'log_stream_id': 'log_stream_id',
        'log_stream_name': 'log_stream_name',
        'project_id': 'project_id'
    }

    def __init__(self, create_time=None, eps_id=None, favorite_resource_id=None, favorite_resource_type=None, log_group_id=None, log_group_name=None, log_stream_id=None, log_stream_name=None, project_id=None):
        """CreatefavoriteResponse

        The model defined in huaweicloud sdk

        :param create_time: 创建时间
        :type create_time: str
        :param eps_id: 企业项目id
        :type eps_id: str
        :param favorite_resource_id: 收藏资源id
        :type favorite_resource_id: str
        :param favorite_resource_type: 收藏资源类型
        :type favorite_resource_type: str
        :param log_group_id: 日志组id
        :type log_group_id: str
        :param log_group_name: 日志组名称
        :type log_group_name: str
        :param log_stream_id: 日志流id
        :type log_stream_id: str
        :param log_stream_name: 日志流名称
        :type log_stream_name: str
        :param project_id: 项目id
        :type project_id: str
        """
        
        super(CreatefavoriteResponse, self).__init__()

        self._create_time = None
        self._eps_id = None
        self._favorite_resource_id = None
        self._favorite_resource_type = None
        self._log_group_id = None
        self._log_group_name = None
        self._log_stream_id = None
        self._log_stream_name = None
        self._project_id = None
        self.discriminator = None

        if create_time is not None:
            self.create_time = create_time
        if eps_id is not None:
            self.eps_id = eps_id
        if favorite_resource_id is not None:
            self.favorite_resource_id = favorite_resource_id
        if favorite_resource_type is not None:
            self.favorite_resource_type = favorite_resource_type
        if log_group_id is not None:
            self.log_group_id = log_group_id
        if log_group_name is not None:
            self.log_group_name = log_group_name
        if log_stream_id is not None:
            self.log_stream_id = log_stream_id
        if log_stream_name is not None:
            self.log_stream_name = log_stream_name
        if project_id is not None:
            self.project_id = project_id

    @property
    def create_time(self):
        """Gets the create_time of this CreatefavoriteResponse.

        创建时间

        :return: The create_time of this CreatefavoriteResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this CreatefavoriteResponse.

        创建时间

        :param create_time: The create_time of this CreatefavoriteResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def eps_id(self):
        """Gets the eps_id of this CreatefavoriteResponse.

        企业项目id

        :return: The eps_id of this CreatefavoriteResponse.
        :rtype: str
        """
        return self._eps_id

    @eps_id.setter
    def eps_id(self, eps_id):
        """Sets the eps_id of this CreatefavoriteResponse.

        企业项目id

        :param eps_id: The eps_id of this CreatefavoriteResponse.
        :type eps_id: str
        """
        self._eps_id = eps_id

    @property
    def favorite_resource_id(self):
        """Gets the favorite_resource_id of this CreatefavoriteResponse.

        收藏资源id

        :return: The favorite_resource_id of this CreatefavoriteResponse.
        :rtype: str
        """
        return self._favorite_resource_id

    @favorite_resource_id.setter
    def favorite_resource_id(self, favorite_resource_id):
        """Sets the favorite_resource_id of this CreatefavoriteResponse.

        收藏资源id

        :param favorite_resource_id: The favorite_resource_id of this CreatefavoriteResponse.
        :type favorite_resource_id: str
        """
        self._favorite_resource_id = favorite_resource_id

    @property
    def favorite_resource_type(self):
        """Gets the favorite_resource_type of this CreatefavoriteResponse.

        收藏资源类型

        :return: The favorite_resource_type of this CreatefavoriteResponse.
        :rtype: str
        """
        return self._favorite_resource_type

    @favorite_resource_type.setter
    def favorite_resource_type(self, favorite_resource_type):
        """Sets the favorite_resource_type of this CreatefavoriteResponse.

        收藏资源类型

        :param favorite_resource_type: The favorite_resource_type of this CreatefavoriteResponse.
        :type favorite_resource_type: str
        """
        self._favorite_resource_type = favorite_resource_type

    @property
    def log_group_id(self):
        """Gets the log_group_id of this CreatefavoriteResponse.

        日志组id

        :return: The log_group_id of this CreatefavoriteResponse.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        """Sets the log_group_id of this CreatefavoriteResponse.

        日志组id

        :param log_group_id: The log_group_id of this CreatefavoriteResponse.
        :type log_group_id: str
        """
        self._log_group_id = log_group_id

    @property
    def log_group_name(self):
        """Gets the log_group_name of this CreatefavoriteResponse.

        日志组名称

        :return: The log_group_name of this CreatefavoriteResponse.
        :rtype: str
        """
        return self._log_group_name

    @log_group_name.setter
    def log_group_name(self, log_group_name):
        """Sets the log_group_name of this CreatefavoriteResponse.

        日志组名称

        :param log_group_name: The log_group_name of this CreatefavoriteResponse.
        :type log_group_name: str
        """
        self._log_group_name = log_group_name

    @property
    def log_stream_id(self):
        """Gets the log_stream_id of this CreatefavoriteResponse.

        日志流id

        :return: The log_stream_id of this CreatefavoriteResponse.
        :rtype: str
        """
        return self._log_stream_id

    @log_stream_id.setter
    def log_stream_id(self, log_stream_id):
        """Sets the log_stream_id of this CreatefavoriteResponse.

        日志流id

        :param log_stream_id: The log_stream_id of this CreatefavoriteResponse.
        :type log_stream_id: str
        """
        self._log_stream_id = log_stream_id

    @property
    def log_stream_name(self):
        """Gets the log_stream_name of this CreatefavoriteResponse.

        日志流名称

        :return: The log_stream_name of this CreatefavoriteResponse.
        :rtype: str
        """
        return self._log_stream_name

    @log_stream_name.setter
    def log_stream_name(self, log_stream_name):
        """Sets the log_stream_name of this CreatefavoriteResponse.

        日志流名称

        :param log_stream_name: The log_stream_name of this CreatefavoriteResponse.
        :type log_stream_name: str
        """
        self._log_stream_name = log_stream_name

    @property
    def project_id(self):
        """Gets the project_id of this CreatefavoriteResponse.

        项目id

        :return: The project_id of this CreatefavoriteResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CreatefavoriteResponse.

        项目id

        :param project_id: The project_id of this CreatefavoriteResponse.
        :type project_id: str
        """
        self._project_id = project_id

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
        if not isinstance(other, CreatefavoriteResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
