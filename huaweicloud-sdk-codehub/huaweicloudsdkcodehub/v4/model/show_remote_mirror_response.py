# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRemoteMirrorResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'repository_id': 'int',
        'update_status': 'str',
        'last_update_at': 'str',
        'url': 'str',
        'last_successful_update_at': 'str',
        'number_of_failures': 'int',
        'mirroring_enabled': 'bool',
        'is_private': 'bool',
        'endpoint_uuid': 'str',
        'last_error': 'str'
    }

    attribute_map = {
        'id': 'id',
        'repository_id': 'repository_id',
        'update_status': 'update_status',
        'last_update_at': 'last_update_at',
        'url': 'url',
        'last_successful_update_at': 'last_successful_update_at',
        'number_of_failures': 'number_of_failures',
        'mirroring_enabled': 'mirroring_enabled',
        'is_private': 'is_private',
        'endpoint_uuid': 'endpoint_uuid',
        'last_error': 'last_error'
    }

    def __init__(self, id=None, repository_id=None, update_status=None, last_update_at=None, url=None, last_successful_update_at=None, number_of_failures=None, mirroring_enabled=None, is_private=None, endpoint_uuid=None, last_error=None):
        r"""ShowRemoteMirrorResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 仓库镜像配置ID。
        :type id: int
        :param repository_id: **参数解释：** 仓库ID。
        :type repository_id: int
        :param update_status: **参数解释：** 同步状态。
        :type update_status: str
        :param last_update_at: **参数解释：** 最近修改时间。
        :type last_update_at: str
        :param url: **参数解释：** 镜像地址。
        :type url: str
        :param last_successful_update_at: **参数解释：** 最近同步成功时间。
        :type last_successful_update_at: str
        :param number_of_failures: **参数解释：** 同步失败次数。
        :type number_of_failures: int
        :param mirroring_enabled: **参数解释：** 开启定时同步。
        :type mirroring_enabled: bool
        :param is_private: **参数解释：** 私有镜像。
        :type is_private: bool
        :param endpoint_uuid: **参数解释：** 拓展点uuid。
        :type endpoint_uuid: str
        :param last_error: **参数解释：** 最近失败信息。
        :type last_error: str
        """
        
        super(ShowRemoteMirrorResponse, self).__init__()

        self._id = None
        self._repository_id = None
        self._update_status = None
        self._last_update_at = None
        self._url = None
        self._last_successful_update_at = None
        self._number_of_failures = None
        self._mirroring_enabled = None
        self._is_private = None
        self._endpoint_uuid = None
        self._last_error = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if repository_id is not None:
            self.repository_id = repository_id
        if update_status is not None:
            self.update_status = update_status
        if last_update_at is not None:
            self.last_update_at = last_update_at
        if url is not None:
            self.url = url
        if last_successful_update_at is not None:
            self.last_successful_update_at = last_successful_update_at
        if number_of_failures is not None:
            self.number_of_failures = number_of_failures
        if mirroring_enabled is not None:
            self.mirroring_enabled = mirroring_enabled
        if is_private is not None:
            self.is_private = is_private
        if endpoint_uuid is not None:
            self.endpoint_uuid = endpoint_uuid
        if last_error is not None:
            self.last_error = last_error

    @property
    def id(self):
        r"""Gets the id of this ShowRemoteMirrorResponse.

        **参数解释：** 仓库镜像配置ID。

        :return: The id of this ShowRemoteMirrorResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowRemoteMirrorResponse.

        **参数解释：** 仓库镜像配置ID。

        :param id: The id of this ShowRemoteMirrorResponse.
        :type id: int
        """
        self._id = id

    @property
    def repository_id(self):
        r"""Gets the repository_id of this ShowRemoteMirrorResponse.

        **参数解释：** 仓库ID。

        :return: The repository_id of this ShowRemoteMirrorResponse.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this ShowRemoteMirrorResponse.

        **参数解释：** 仓库ID。

        :param repository_id: The repository_id of this ShowRemoteMirrorResponse.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def update_status(self):
        r"""Gets the update_status of this ShowRemoteMirrorResponse.

        **参数解释：** 同步状态。

        :return: The update_status of this ShowRemoteMirrorResponse.
        :rtype: str
        """
        return self._update_status

    @update_status.setter
    def update_status(self, update_status):
        r"""Sets the update_status of this ShowRemoteMirrorResponse.

        **参数解释：** 同步状态。

        :param update_status: The update_status of this ShowRemoteMirrorResponse.
        :type update_status: str
        """
        self._update_status = update_status

    @property
    def last_update_at(self):
        r"""Gets the last_update_at of this ShowRemoteMirrorResponse.

        **参数解释：** 最近修改时间。

        :return: The last_update_at of this ShowRemoteMirrorResponse.
        :rtype: str
        """
        return self._last_update_at

    @last_update_at.setter
    def last_update_at(self, last_update_at):
        r"""Sets the last_update_at of this ShowRemoteMirrorResponse.

        **参数解释：** 最近修改时间。

        :param last_update_at: The last_update_at of this ShowRemoteMirrorResponse.
        :type last_update_at: str
        """
        self._last_update_at = last_update_at

    @property
    def url(self):
        r"""Gets the url of this ShowRemoteMirrorResponse.

        **参数解释：** 镜像地址。

        :return: The url of this ShowRemoteMirrorResponse.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this ShowRemoteMirrorResponse.

        **参数解释：** 镜像地址。

        :param url: The url of this ShowRemoteMirrorResponse.
        :type url: str
        """
        self._url = url

    @property
    def last_successful_update_at(self):
        r"""Gets the last_successful_update_at of this ShowRemoteMirrorResponse.

        **参数解释：** 最近同步成功时间。

        :return: The last_successful_update_at of this ShowRemoteMirrorResponse.
        :rtype: str
        """
        return self._last_successful_update_at

    @last_successful_update_at.setter
    def last_successful_update_at(self, last_successful_update_at):
        r"""Sets the last_successful_update_at of this ShowRemoteMirrorResponse.

        **参数解释：** 最近同步成功时间。

        :param last_successful_update_at: The last_successful_update_at of this ShowRemoteMirrorResponse.
        :type last_successful_update_at: str
        """
        self._last_successful_update_at = last_successful_update_at

    @property
    def number_of_failures(self):
        r"""Gets the number_of_failures of this ShowRemoteMirrorResponse.

        **参数解释：** 同步失败次数。

        :return: The number_of_failures of this ShowRemoteMirrorResponse.
        :rtype: int
        """
        return self._number_of_failures

    @number_of_failures.setter
    def number_of_failures(self, number_of_failures):
        r"""Sets the number_of_failures of this ShowRemoteMirrorResponse.

        **参数解释：** 同步失败次数。

        :param number_of_failures: The number_of_failures of this ShowRemoteMirrorResponse.
        :type number_of_failures: int
        """
        self._number_of_failures = number_of_failures

    @property
    def mirroring_enabled(self):
        r"""Gets the mirroring_enabled of this ShowRemoteMirrorResponse.

        **参数解释：** 开启定时同步。

        :return: The mirroring_enabled of this ShowRemoteMirrorResponse.
        :rtype: bool
        """
        return self._mirroring_enabled

    @mirroring_enabled.setter
    def mirroring_enabled(self, mirroring_enabled):
        r"""Sets the mirroring_enabled of this ShowRemoteMirrorResponse.

        **参数解释：** 开启定时同步。

        :param mirroring_enabled: The mirroring_enabled of this ShowRemoteMirrorResponse.
        :type mirroring_enabled: bool
        """
        self._mirroring_enabled = mirroring_enabled

    @property
    def is_private(self):
        r"""Gets the is_private of this ShowRemoteMirrorResponse.

        **参数解释：** 私有镜像。

        :return: The is_private of this ShowRemoteMirrorResponse.
        :rtype: bool
        """
        return self._is_private

    @is_private.setter
    def is_private(self, is_private):
        r"""Sets the is_private of this ShowRemoteMirrorResponse.

        **参数解释：** 私有镜像。

        :param is_private: The is_private of this ShowRemoteMirrorResponse.
        :type is_private: bool
        """
        self._is_private = is_private

    @property
    def endpoint_uuid(self):
        r"""Gets the endpoint_uuid of this ShowRemoteMirrorResponse.

        **参数解释：** 拓展点uuid。

        :return: The endpoint_uuid of this ShowRemoteMirrorResponse.
        :rtype: str
        """
        return self._endpoint_uuid

    @endpoint_uuid.setter
    def endpoint_uuid(self, endpoint_uuid):
        r"""Sets the endpoint_uuid of this ShowRemoteMirrorResponse.

        **参数解释：** 拓展点uuid。

        :param endpoint_uuid: The endpoint_uuid of this ShowRemoteMirrorResponse.
        :type endpoint_uuid: str
        """
        self._endpoint_uuid = endpoint_uuid

    @property
    def last_error(self):
        r"""Gets the last_error of this ShowRemoteMirrorResponse.

        **参数解释：** 最近失败信息。

        :return: The last_error of this ShowRemoteMirrorResponse.
        :rtype: str
        """
        return self._last_error

    @last_error.setter
    def last_error(self, last_error):
        r"""Sets the last_error of this ShowRemoteMirrorResponse.

        **参数解释：** 最近失败信息。

        :param last_error: The last_error of this ShowRemoteMirrorResponse.
        :type last_error: str
        """
        self._last_error = last_error

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
        if not isinstance(other, ShowRemoteMirrorResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
