# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceListRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'dlm_type': 'str',
        'api_id': 'str',
        'action': 'str',
        'show_all': 'bool',
        'check_status': 'bool',
        'check_debug': 'bool',
        'app_id': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'workspace': 'workspace',
        'dlm_type': 'Dlm-Type',
        'api_id': 'api_id',
        'action': 'action',
        'show_all': 'show_all',
        'check_status': 'check_status',
        'check_debug': 'check_debug',
        'app_id': 'app_id',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, workspace=None, dlm_type=None, api_id=None, action=None, show_all=None, check_status=None, check_debug=None, app_id=None, limit=None, offset=None):
        """ListInstanceListRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间id
        :type workspace: str
        :param dlm_type: dlm版本类型
        :type dlm_type: str
        :param api_id: api编号
        :type api_id: str
        :param action: api操作
        :type action: str
        :param show_all: 全部展示(包括不可执行当前操作的实例)
        :type show_all: bool
        :param check_status: 校验api状态
        :type check_status: bool
        :param check_debug: 校验api调试状态
        :type check_debug: bool
        :param app_id: app编号(用于判断授权操作app可选的实例)
        :type app_id: str
        :param limit: limit
        :type limit: int
        :param offset: offset
        :type offset: int
        """
        
        

        self._workspace = None
        self._dlm_type = None
        self._api_id = None
        self._action = None
        self._show_all = None
        self._check_status = None
        self._check_debug = None
        self._app_id = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.workspace = workspace
        self.dlm_type = dlm_type
        self.api_id = api_id
        self.action = action
        if show_all is not None:
            self.show_all = show_all
        if check_status is not None:
            self.check_status = check_status
        if check_debug is not None:
            self.check_debug = check_debug
        if app_id is not None:
            self.app_id = app_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def workspace(self):
        """Gets the workspace of this ListInstanceListRequest.

        工作空间id

        :return: The workspace of this ListInstanceListRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this ListInstanceListRequest.

        工作空间id

        :param workspace: The workspace of this ListInstanceListRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def dlm_type(self):
        """Gets the dlm_type of this ListInstanceListRequest.

        dlm版本类型

        :return: The dlm_type of this ListInstanceListRequest.
        :rtype: str
        """
        return self._dlm_type

    @dlm_type.setter
    def dlm_type(self, dlm_type):
        """Sets the dlm_type of this ListInstanceListRequest.

        dlm版本类型

        :param dlm_type: The dlm_type of this ListInstanceListRequest.
        :type dlm_type: str
        """
        self._dlm_type = dlm_type

    @property
    def api_id(self):
        """Gets the api_id of this ListInstanceListRequest.

        api编号

        :return: The api_id of this ListInstanceListRequest.
        :rtype: str
        """
        return self._api_id

    @api_id.setter
    def api_id(self, api_id):
        """Sets the api_id of this ListInstanceListRequest.

        api编号

        :param api_id: The api_id of this ListInstanceListRequest.
        :type api_id: str
        """
        self._api_id = api_id

    @property
    def action(self):
        """Gets the action of this ListInstanceListRequest.

        api操作

        :return: The action of this ListInstanceListRequest.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ListInstanceListRequest.

        api操作

        :param action: The action of this ListInstanceListRequest.
        :type action: str
        """
        self._action = action

    @property
    def show_all(self):
        """Gets the show_all of this ListInstanceListRequest.

        全部展示(包括不可执行当前操作的实例)

        :return: The show_all of this ListInstanceListRequest.
        :rtype: bool
        """
        return self._show_all

    @show_all.setter
    def show_all(self, show_all):
        """Sets the show_all of this ListInstanceListRequest.

        全部展示(包括不可执行当前操作的实例)

        :param show_all: The show_all of this ListInstanceListRequest.
        :type show_all: bool
        """
        self._show_all = show_all

    @property
    def check_status(self):
        """Gets the check_status of this ListInstanceListRequest.

        校验api状态

        :return: The check_status of this ListInstanceListRequest.
        :rtype: bool
        """
        return self._check_status

    @check_status.setter
    def check_status(self, check_status):
        """Sets the check_status of this ListInstanceListRequest.

        校验api状态

        :param check_status: The check_status of this ListInstanceListRequest.
        :type check_status: bool
        """
        self._check_status = check_status

    @property
    def check_debug(self):
        """Gets the check_debug of this ListInstanceListRequest.

        校验api调试状态

        :return: The check_debug of this ListInstanceListRequest.
        :rtype: bool
        """
        return self._check_debug

    @check_debug.setter
    def check_debug(self, check_debug):
        """Sets the check_debug of this ListInstanceListRequest.

        校验api调试状态

        :param check_debug: The check_debug of this ListInstanceListRequest.
        :type check_debug: bool
        """
        self._check_debug = check_debug

    @property
    def app_id(self):
        """Gets the app_id of this ListInstanceListRequest.

        app编号(用于判断授权操作app可选的实例)

        :return: The app_id of this ListInstanceListRequest.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ListInstanceListRequest.

        app编号(用于判断授权操作app可选的实例)

        :param app_id: The app_id of this ListInstanceListRequest.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def limit(self):
        """Gets the limit of this ListInstanceListRequest.

        limit

        :return: The limit of this ListInstanceListRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListInstanceListRequest.

        limit

        :param limit: The limit of this ListInstanceListRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListInstanceListRequest.

        offset

        :return: The offset of this ListInstanceListRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListInstanceListRequest.

        offset

        :param offset: The offset of this ListInstanceListRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListInstanceListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
