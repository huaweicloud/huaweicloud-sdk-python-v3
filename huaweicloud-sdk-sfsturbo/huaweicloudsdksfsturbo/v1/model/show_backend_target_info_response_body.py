# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBackendTargetInfoResponseBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target_id': 'str',
        'creation_time': 'str',
        'file_system_path': 'str',
        'failure_details': 'FailureDetailsMessage',
        'lifecycle': 'str',
        'obs': 'ObsDataRepository'
    }

    attribute_map = {
        'target_id': 'target_id',
        'creation_time': 'creation_time',
        'file_system_path': 'file_system_path',
        'failure_details': 'failure_details',
        'lifecycle': 'lifecycle',
        'obs': 'obs'
    }

    def __init__(self, target_id=None, creation_time=None, file_system_path=None, failure_details=None, lifecycle=None, obs=None):
        r"""ShowBackendTargetInfoResponseBody

        The model defined in huaweicloud sdk

        :param target_id: 绑定关系ID
        :type target_id: str
        :param creation_time: 绑定关系创建时间
        :type creation_time: str
        :param file_system_path: 联动目录名称
        :type file_system_path: str
        :param failure_details: 
        :type failure_details: :class:`huaweicloudsdksfsturbo.v1.FailureDetailsMessage`
        :param lifecycle: 绑定状态
        :type lifecycle: str
        :param obs: 
        :type obs: :class:`huaweicloudsdksfsturbo.v1.ObsDataRepository`
        """
        
        

        self._target_id = None
        self._creation_time = None
        self._file_system_path = None
        self._failure_details = None
        self._lifecycle = None
        self._obs = None
        self.discriminator = None

        if target_id is not None:
            self.target_id = target_id
        if creation_time is not None:
            self.creation_time = creation_time
        if file_system_path is not None:
            self.file_system_path = file_system_path
        if failure_details is not None:
            self.failure_details = failure_details
        if lifecycle is not None:
            self.lifecycle = lifecycle
        if obs is not None:
            self.obs = obs

    @property
    def target_id(self):
        r"""Gets the target_id of this ShowBackendTargetInfoResponseBody.

        绑定关系ID

        :return: The target_id of this ShowBackendTargetInfoResponseBody.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        r"""Sets the target_id of this ShowBackendTargetInfoResponseBody.

        绑定关系ID

        :param target_id: The target_id of this ShowBackendTargetInfoResponseBody.
        :type target_id: str
        """
        self._target_id = target_id

    @property
    def creation_time(self):
        r"""Gets the creation_time of this ShowBackendTargetInfoResponseBody.

        绑定关系创建时间

        :return: The creation_time of this ShowBackendTargetInfoResponseBody.
        :rtype: str
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        r"""Sets the creation_time of this ShowBackendTargetInfoResponseBody.

        绑定关系创建时间

        :param creation_time: The creation_time of this ShowBackendTargetInfoResponseBody.
        :type creation_time: str
        """
        self._creation_time = creation_time

    @property
    def file_system_path(self):
        r"""Gets the file_system_path of this ShowBackendTargetInfoResponseBody.

        联动目录名称

        :return: The file_system_path of this ShowBackendTargetInfoResponseBody.
        :rtype: str
        """
        return self._file_system_path

    @file_system_path.setter
    def file_system_path(self, file_system_path):
        r"""Sets the file_system_path of this ShowBackendTargetInfoResponseBody.

        联动目录名称

        :param file_system_path: The file_system_path of this ShowBackendTargetInfoResponseBody.
        :type file_system_path: str
        """
        self._file_system_path = file_system_path

    @property
    def failure_details(self):
        r"""Gets the failure_details of this ShowBackendTargetInfoResponseBody.

        :return: The failure_details of this ShowBackendTargetInfoResponseBody.
        :rtype: :class:`huaweicloudsdksfsturbo.v1.FailureDetailsMessage`
        """
        return self._failure_details

    @failure_details.setter
    def failure_details(self, failure_details):
        r"""Sets the failure_details of this ShowBackendTargetInfoResponseBody.

        :param failure_details: The failure_details of this ShowBackendTargetInfoResponseBody.
        :type failure_details: :class:`huaweicloudsdksfsturbo.v1.FailureDetailsMessage`
        """
        self._failure_details = failure_details

    @property
    def lifecycle(self):
        r"""Gets the lifecycle of this ShowBackendTargetInfoResponseBody.

        绑定状态

        :return: The lifecycle of this ShowBackendTargetInfoResponseBody.
        :rtype: str
        """
        return self._lifecycle

    @lifecycle.setter
    def lifecycle(self, lifecycle):
        r"""Sets the lifecycle of this ShowBackendTargetInfoResponseBody.

        绑定状态

        :param lifecycle: The lifecycle of this ShowBackendTargetInfoResponseBody.
        :type lifecycle: str
        """
        self._lifecycle = lifecycle

    @property
    def obs(self):
        r"""Gets the obs of this ShowBackendTargetInfoResponseBody.

        :return: The obs of this ShowBackendTargetInfoResponseBody.
        :rtype: :class:`huaweicloudsdksfsturbo.v1.ObsDataRepository`
        """
        return self._obs

    @obs.setter
    def obs(self, obs):
        r"""Sets the obs of this ShowBackendTargetInfoResponseBody.

        :param obs: The obs of this ShowBackendTargetInfoResponseBody.
        :type obs: :class:`huaweicloudsdksfsturbo.v1.ObsDataRepository`
        """
        self._obs = obs

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
        if not isinstance(other, ShowBackendTargetInfoResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
