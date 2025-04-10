# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SinkObsParameters:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'access_key': 'str',
        'secret_key': 'str',
        'obs_bucket': 'str',
        'obs_path': 'str',
        'time_format': 'str'
    }

    attribute_map = {
        'access_key': 'access_key',
        'secret_key': 'secret_key',
        'obs_bucket': 'obs_bucket',
        'obs_path': 'obs_path',
        'time_format': 'time_format'
    }

    def __init__(self, access_key=None, secret_key=None, obs_bucket=None, obs_path=None, time_format=None):
        r"""SinkObsParameters

        The model defined in huaweicloud sdk

        :param access_key: AK
        :type access_key: str
        :param secret_key: SK
        :type secret_key: str
        :param obs_bucket: 桶
        :type obs_bucket: str
        :param obs_path: 转储目录
        :type obs_path: str
        :param time_format: 时间目录格式
        :type time_format: str
        """
        
        

        self._access_key = None
        self._secret_key = None
        self._obs_bucket = None
        self._obs_path = None
        self._time_format = None
        self.discriminator = None

        self.access_key = access_key
        self.secret_key = secret_key
        self.obs_bucket = obs_bucket
        if obs_path is not None:
            self.obs_path = obs_path
        self.time_format = time_format

    @property
    def access_key(self):
        r"""Gets the access_key of this SinkObsParameters.

        AK

        :return: The access_key of this SinkObsParameters.
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        r"""Sets the access_key of this SinkObsParameters.

        AK

        :param access_key: The access_key of this SinkObsParameters.
        :type access_key: str
        """
        self._access_key = access_key

    @property
    def secret_key(self):
        r"""Gets the secret_key of this SinkObsParameters.

        SK

        :return: The secret_key of this SinkObsParameters.
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        r"""Sets the secret_key of this SinkObsParameters.

        SK

        :param secret_key: The secret_key of this SinkObsParameters.
        :type secret_key: str
        """
        self._secret_key = secret_key

    @property
    def obs_bucket(self):
        r"""Gets the obs_bucket of this SinkObsParameters.

        桶

        :return: The obs_bucket of this SinkObsParameters.
        :rtype: str
        """
        return self._obs_bucket

    @obs_bucket.setter
    def obs_bucket(self, obs_bucket):
        r"""Sets the obs_bucket of this SinkObsParameters.

        桶

        :param obs_bucket: The obs_bucket of this SinkObsParameters.
        :type obs_bucket: str
        """
        self._obs_bucket = obs_bucket

    @property
    def obs_path(self):
        r"""Gets the obs_path of this SinkObsParameters.

        转储目录

        :return: The obs_path of this SinkObsParameters.
        :rtype: str
        """
        return self._obs_path

    @obs_path.setter
    def obs_path(self, obs_path):
        r"""Sets the obs_path of this SinkObsParameters.

        转储目录

        :param obs_path: The obs_path of this SinkObsParameters.
        :type obs_path: str
        """
        self._obs_path = obs_path

    @property
    def time_format(self):
        r"""Gets the time_format of this SinkObsParameters.

        时间目录格式

        :return: The time_format of this SinkObsParameters.
        :rtype: str
        """
        return self._time_format

    @time_format.setter
    def time_format(self, time_format):
        r"""Sets the time_format of this SinkObsParameters.

        时间目录格式

        :param time_format: The time_format of this SinkObsParameters.
        :type time_format: str
        """
        self._time_format = time_format

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
        if not isinstance(other, SinkObsParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
