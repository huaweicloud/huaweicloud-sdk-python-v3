# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GeneralImageVulOperationsResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_id': 'str',
        'image_name': 'str',
        'user_name': 'str',
        'handle_time': 'int',
        'handle_type': 'str',
        'status': 'str',
        'app_name': 'str',
        'app_version': 'str',
        'app_path': 'str',
        'remark': 'str',
        'image_digest': 'str',
        'image_version': 'str',
        'agent_id': 'str'
    }

    attribute_map = {
        'image_id': 'image_id',
        'image_name': 'image_name',
        'user_name': 'user_name',
        'handle_time': 'handle_time',
        'handle_type': 'handle_type',
        'status': 'status',
        'app_name': 'app_name',
        'app_version': 'app_version',
        'app_path': 'app_path',
        'remark': 'remark',
        'image_digest': 'image_digest',
        'image_version': 'image_version',
        'agent_id': 'agent_id'
    }

    def __init__(self, image_id=None, image_name=None, user_name=None, handle_time=None, handle_type=None, status=None, app_name=None, app_version=None, app_path=None, remark=None, image_digest=None, image_version=None, agent_id=None):
        r"""GeneralImageVulOperationsResponseInfo

        The model defined in huaweicloud sdk

        :param image_id: 镜像id
        :type image_id: str
        :param image_name: 镜像名称
        :type image_name: str
        :param user_name: 处置用户名称
        :type user_name: str
        :param handle_time: 处置时间，时间单位：毫秒（ms）
        :type handle_time: int
        :param handle_type: 操作类型，包含如下：   -ignore : 忽略   -not_ignore : 取消忽略   -add_to_whitelist ：加入白名单
        :type handle_type: str
        :param status: 漏洞当前状态，包含如下：   -vul_status_unfix : 未处理   -vul_status_ignored : 已忽略
        :type status: str
        :param app_name: 软件名称
        :type app_name: str
        :param app_version: 软件版本
        :type app_version: str
        :param app_path: 软件路径
        :type app_path: str
        :param remark: 备注
        :type remark: str
        :param image_digest: 镜像标识
        :type image_digest: str
        :param image_version: 镜像版本
        :type image_version: str
        :param agent_id: Agent ID
        :type agent_id: str
        """
        
        

        self._image_id = None
        self._image_name = None
        self._user_name = None
        self._handle_time = None
        self._handle_type = None
        self._status = None
        self._app_name = None
        self._app_version = None
        self._app_path = None
        self._remark = None
        self._image_digest = None
        self._image_version = None
        self._agent_id = None
        self.discriminator = None

        if image_id is not None:
            self.image_id = image_id
        if image_name is not None:
            self.image_name = image_name
        if user_name is not None:
            self.user_name = user_name
        if handle_time is not None:
            self.handle_time = handle_time
        if handle_type is not None:
            self.handle_type = handle_type
        if status is not None:
            self.status = status
        if app_name is not None:
            self.app_name = app_name
        if app_version is not None:
            self.app_version = app_version
        if app_path is not None:
            self.app_path = app_path
        if remark is not None:
            self.remark = remark
        if image_digest is not None:
            self.image_digest = image_digest
        if image_version is not None:
            self.image_version = image_version
        if agent_id is not None:
            self.agent_id = agent_id

    @property
    def image_id(self):
        r"""Gets the image_id of this GeneralImageVulOperationsResponseInfo.

        镜像id

        :return: The image_id of this GeneralImageVulOperationsResponseInfo.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this GeneralImageVulOperationsResponseInfo.

        镜像id

        :param image_id: The image_id of this GeneralImageVulOperationsResponseInfo.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def image_name(self):
        r"""Gets the image_name of this GeneralImageVulOperationsResponseInfo.

        镜像名称

        :return: The image_name of this GeneralImageVulOperationsResponseInfo.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this GeneralImageVulOperationsResponseInfo.

        镜像名称

        :param image_name: The image_name of this GeneralImageVulOperationsResponseInfo.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def user_name(self):
        r"""Gets the user_name of this GeneralImageVulOperationsResponseInfo.

        处置用户名称

        :return: The user_name of this GeneralImageVulOperationsResponseInfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this GeneralImageVulOperationsResponseInfo.

        处置用户名称

        :param user_name: The user_name of this GeneralImageVulOperationsResponseInfo.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def handle_time(self):
        r"""Gets the handle_time of this GeneralImageVulOperationsResponseInfo.

        处置时间，时间单位：毫秒（ms）

        :return: The handle_time of this GeneralImageVulOperationsResponseInfo.
        :rtype: int
        """
        return self._handle_time

    @handle_time.setter
    def handle_time(self, handle_time):
        r"""Sets the handle_time of this GeneralImageVulOperationsResponseInfo.

        处置时间，时间单位：毫秒（ms）

        :param handle_time: The handle_time of this GeneralImageVulOperationsResponseInfo.
        :type handle_time: int
        """
        self._handle_time = handle_time

    @property
    def handle_type(self):
        r"""Gets the handle_type of this GeneralImageVulOperationsResponseInfo.

        操作类型，包含如下：   -ignore : 忽略   -not_ignore : 取消忽略   -add_to_whitelist ：加入白名单

        :return: The handle_type of this GeneralImageVulOperationsResponseInfo.
        :rtype: str
        """
        return self._handle_type

    @handle_type.setter
    def handle_type(self, handle_type):
        r"""Sets the handle_type of this GeneralImageVulOperationsResponseInfo.

        操作类型，包含如下：   -ignore : 忽略   -not_ignore : 取消忽略   -add_to_whitelist ：加入白名单

        :param handle_type: The handle_type of this GeneralImageVulOperationsResponseInfo.
        :type handle_type: str
        """
        self._handle_type = handle_type

    @property
    def status(self):
        r"""Gets the status of this GeneralImageVulOperationsResponseInfo.

        漏洞当前状态，包含如下：   -vul_status_unfix : 未处理   -vul_status_ignored : 已忽略

        :return: The status of this GeneralImageVulOperationsResponseInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this GeneralImageVulOperationsResponseInfo.

        漏洞当前状态，包含如下：   -vul_status_unfix : 未处理   -vul_status_ignored : 已忽略

        :param status: The status of this GeneralImageVulOperationsResponseInfo.
        :type status: str
        """
        self._status = status

    @property
    def app_name(self):
        r"""Gets the app_name of this GeneralImageVulOperationsResponseInfo.

        软件名称

        :return: The app_name of this GeneralImageVulOperationsResponseInfo.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this GeneralImageVulOperationsResponseInfo.

        软件名称

        :param app_name: The app_name of this GeneralImageVulOperationsResponseInfo.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def app_version(self):
        r"""Gets the app_version of this GeneralImageVulOperationsResponseInfo.

        软件版本

        :return: The app_version of this GeneralImageVulOperationsResponseInfo.
        :rtype: str
        """
        return self._app_version

    @app_version.setter
    def app_version(self, app_version):
        r"""Sets the app_version of this GeneralImageVulOperationsResponseInfo.

        软件版本

        :param app_version: The app_version of this GeneralImageVulOperationsResponseInfo.
        :type app_version: str
        """
        self._app_version = app_version

    @property
    def app_path(self):
        r"""Gets the app_path of this GeneralImageVulOperationsResponseInfo.

        软件路径

        :return: The app_path of this GeneralImageVulOperationsResponseInfo.
        :rtype: str
        """
        return self._app_path

    @app_path.setter
    def app_path(self, app_path):
        r"""Sets the app_path of this GeneralImageVulOperationsResponseInfo.

        软件路径

        :param app_path: The app_path of this GeneralImageVulOperationsResponseInfo.
        :type app_path: str
        """
        self._app_path = app_path

    @property
    def remark(self):
        r"""Gets the remark of this GeneralImageVulOperationsResponseInfo.

        备注

        :return: The remark of this GeneralImageVulOperationsResponseInfo.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        r"""Sets the remark of this GeneralImageVulOperationsResponseInfo.

        备注

        :param remark: The remark of this GeneralImageVulOperationsResponseInfo.
        :type remark: str
        """
        self._remark = remark

    @property
    def image_digest(self):
        r"""Gets the image_digest of this GeneralImageVulOperationsResponseInfo.

        镜像标识

        :return: The image_digest of this GeneralImageVulOperationsResponseInfo.
        :rtype: str
        """
        return self._image_digest

    @image_digest.setter
    def image_digest(self, image_digest):
        r"""Sets the image_digest of this GeneralImageVulOperationsResponseInfo.

        镜像标识

        :param image_digest: The image_digest of this GeneralImageVulOperationsResponseInfo.
        :type image_digest: str
        """
        self._image_digest = image_digest

    @property
    def image_version(self):
        r"""Gets the image_version of this GeneralImageVulOperationsResponseInfo.

        镜像版本

        :return: The image_version of this GeneralImageVulOperationsResponseInfo.
        :rtype: str
        """
        return self._image_version

    @image_version.setter
    def image_version(self, image_version):
        r"""Sets the image_version of this GeneralImageVulOperationsResponseInfo.

        镜像版本

        :param image_version: The image_version of this GeneralImageVulOperationsResponseInfo.
        :type image_version: str
        """
        self._image_version = image_version

    @property
    def agent_id(self):
        r"""Gets the agent_id of this GeneralImageVulOperationsResponseInfo.

        Agent ID

        :return: The agent_id of this GeneralImageVulOperationsResponseInfo.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this GeneralImageVulOperationsResponseInfo.

        Agent ID

        :param agent_id: The agent_id of this GeneralImageVulOperationsResponseInfo.
        :type agent_id: str
        """
        self._agent_id = agent_id

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
        if not isinstance(other, GeneralImageVulOperationsResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
