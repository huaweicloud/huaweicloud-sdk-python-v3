# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowConsumerStateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_name': 'str',
        'app_id': 'str',
        'create_time': 'int',
        'commit_checkpoint_stream_names': 'list[str]'
    }

    attribute_map = {
        'app_name': 'app_name',
        'app_id': 'app_id',
        'create_time': 'create_time',
        'commit_checkpoint_stream_names': 'commit_checkpoint_stream_names'
    }

    def __init__(self, app_name=None, app_id=None, create_time=None, commit_checkpoint_stream_names=None):
        """ShowConsumerStateResponse

        The model defined in huaweicloud sdk

        :param app_name: App的名称。
        :type app_name: str
        :param app_id: App的唯一标识符。
        :type app_id: str
        :param create_time: App创建的时间，单位毫秒。
        :type create_time: int
        :param commit_checkpoint_stream_names: 关联通道列表。
        :type commit_checkpoint_stream_names: list[str]
        """
        
        super(ShowConsumerStateResponse, self).__init__()

        self._app_name = None
        self._app_id = None
        self._create_time = None
        self._commit_checkpoint_stream_names = None
        self.discriminator = None

        if app_name is not None:
            self.app_name = app_name
        if app_id is not None:
            self.app_id = app_id
        if create_time is not None:
            self.create_time = create_time
        if commit_checkpoint_stream_names is not None:
            self.commit_checkpoint_stream_names = commit_checkpoint_stream_names

    @property
    def app_name(self):
        """Gets the app_name of this ShowConsumerStateResponse.

        App的名称。

        :return: The app_name of this ShowConsumerStateResponse.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this ShowConsumerStateResponse.

        App的名称。

        :param app_name: The app_name of this ShowConsumerStateResponse.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def app_id(self):
        """Gets the app_id of this ShowConsumerStateResponse.

        App的唯一标识符。

        :return: The app_id of this ShowConsumerStateResponse.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ShowConsumerStateResponse.

        App的唯一标识符。

        :param app_id: The app_id of this ShowConsumerStateResponse.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def create_time(self):
        """Gets the create_time of this ShowConsumerStateResponse.

        App创建的时间，单位毫秒。

        :return: The create_time of this ShowConsumerStateResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowConsumerStateResponse.

        App创建的时间，单位毫秒。

        :param create_time: The create_time of this ShowConsumerStateResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def commit_checkpoint_stream_names(self):
        """Gets the commit_checkpoint_stream_names of this ShowConsumerStateResponse.

        关联通道列表。

        :return: The commit_checkpoint_stream_names of this ShowConsumerStateResponse.
        :rtype: list[str]
        """
        return self._commit_checkpoint_stream_names

    @commit_checkpoint_stream_names.setter
    def commit_checkpoint_stream_names(self, commit_checkpoint_stream_names):
        """Sets the commit_checkpoint_stream_names of this ShowConsumerStateResponse.

        关联通道列表。

        :param commit_checkpoint_stream_names: The commit_checkpoint_stream_names of this ShowConsumerStateResponse.
        :type commit_checkpoint_stream_names: list[str]
        """
        self._commit_checkpoint_stream_names = commit_checkpoint_stream_names

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
        if not isinstance(other, ShowConsumerStateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
