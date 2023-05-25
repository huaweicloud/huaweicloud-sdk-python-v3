# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateComponentConfigurationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version': 'str',
        'create_time': 'int',
        'creator': 'str',
        'source': 'str',
        'envs': 'list[ComponentConfigEnvs]'
    }

    attribute_map = {
        'version': 'version',
        'create_time': 'create_time',
        'creator': 'creator',
        'source': 'source',
        'envs': 'envs'
    }

    def __init__(self, version=None, create_time=None, creator=None, source=None, envs=None):
        """CreateComponentConfigurationResponse

        The model defined in huaweicloud sdk

        :param version: 
        :type version: str
        :param create_time: 创建时间。
        :type create_time: int
        :param creator: 
        :type creator: str
        :param source: 来源版本号
        :type source: str
        :param envs: application environment parameters
        :type envs: list[:class:`huaweicloudsdkservicestage.v3.ComponentConfigEnvs`]
        """
        
        super(CreateComponentConfigurationResponse, self).__init__()

        self._version = None
        self._create_time = None
        self._creator = None
        self._source = None
        self._envs = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if create_time is not None:
            self.create_time = create_time
        if creator is not None:
            self.creator = creator
        if source is not None:
            self.source = source
        if envs is not None:
            self.envs = envs

    @property
    def version(self):
        """Gets the version of this CreateComponentConfigurationResponse.

        :return: The version of this CreateComponentConfigurationResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this CreateComponentConfigurationResponse.

        :param version: The version of this CreateComponentConfigurationResponse.
        :type version: str
        """
        self._version = version

    @property
    def create_time(self):
        """Gets the create_time of this CreateComponentConfigurationResponse.

        创建时间。

        :return: The create_time of this CreateComponentConfigurationResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this CreateComponentConfigurationResponse.

        创建时间。

        :param create_time: The create_time of this CreateComponentConfigurationResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def creator(self):
        """Gets the creator of this CreateComponentConfigurationResponse.

        :return: The creator of this CreateComponentConfigurationResponse.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this CreateComponentConfigurationResponse.

        :param creator: The creator of this CreateComponentConfigurationResponse.
        :type creator: str
        """
        self._creator = creator

    @property
    def source(self):
        """Gets the source of this CreateComponentConfigurationResponse.

        来源版本号

        :return: The source of this CreateComponentConfigurationResponse.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this CreateComponentConfigurationResponse.

        来源版本号

        :param source: The source of this CreateComponentConfigurationResponse.
        :type source: str
        """
        self._source = source

    @property
    def envs(self):
        """Gets the envs of this CreateComponentConfigurationResponse.

        application environment parameters

        :return: The envs of this CreateComponentConfigurationResponse.
        :rtype: list[:class:`huaweicloudsdkservicestage.v3.ComponentConfigEnvs`]
        """
        return self._envs

    @envs.setter
    def envs(self, envs):
        """Sets the envs of this CreateComponentConfigurationResponse.

        application environment parameters

        :param envs: The envs of this CreateComponentConfigurationResponse.
        :type envs: list[:class:`huaweicloudsdkservicestage.v3.ComponentConfigEnvs`]
        """
        self._envs = envs

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
        if not isinstance(other, CreateComponentConfigurationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
