# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppQuotaAppInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_id': 'str',
        'name': 'str',
        'status': 'int',
        'app_key': 'str',
        'remark': 'str',
        'register_time': 'datetime',
        'update_time': 'datetime',
        'app_quota_id': 'str',
        'app_quota_name': 'str',
        'bound_time': 'datetime'
    }

    attribute_map = {
        'app_id': 'app_id',
        'name': 'name',
        'status': 'status',
        'app_key': 'app_key',
        'remark': 'remark',
        'register_time': 'register_time',
        'update_time': 'update_time',
        'app_quota_id': 'app_quota_id',
        'app_quota_name': 'app_quota_name',
        'bound_time': 'bound_time'
    }

    def __init__(self, app_id=None, name=None, status=None, app_key=None, remark=None, register_time=None, update_time=None, app_quota_id=None, app_quota_name=None, bound_time=None):
        r"""AppQuotaAppInfo

        The model defined in huaweicloud sdk

        :param app_id: 客户端应用编号
        :type app_id: str
        :param name: 客户端应用名称
        :type name: str
        :param status: 客户端应用状态： - 1：启用 - 2：禁用
        :type status: int
        :param app_key: 客户端应用的Key
        :type app_key: str
        :param remark: 客户端应用描述
        :type remark: str
        :param register_time: 创建时间
        :type register_time: datetime
        :param update_time: 更新时间
        :type update_time: datetime
        :param app_quota_id: 客户端配额编号
        :type app_quota_id: str
        :param app_quota_name: 配额名称。支持汉字，英文，数字，下划线，且只能以英文和汉字开头，3-255字符
        :type app_quota_name: str
        :param bound_time: 绑定时间
        :type bound_time: datetime
        """
        
        

        self._app_id = None
        self._name = None
        self._status = None
        self._app_key = None
        self._remark = None
        self._register_time = None
        self._update_time = None
        self._app_quota_id = None
        self._app_quota_name = None
        self._bound_time = None
        self.discriminator = None

        if app_id is not None:
            self.app_id = app_id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if app_key is not None:
            self.app_key = app_key
        if remark is not None:
            self.remark = remark
        if register_time is not None:
            self.register_time = register_time
        if update_time is not None:
            self.update_time = update_time
        if app_quota_id is not None:
            self.app_quota_id = app_quota_id
        if app_quota_name is not None:
            self.app_quota_name = app_quota_name
        if bound_time is not None:
            self.bound_time = bound_time

    @property
    def app_id(self):
        r"""Gets the app_id of this AppQuotaAppInfo.

        客户端应用编号

        :return: The app_id of this AppQuotaAppInfo.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this AppQuotaAppInfo.

        客户端应用编号

        :param app_id: The app_id of this AppQuotaAppInfo.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def name(self):
        r"""Gets the name of this AppQuotaAppInfo.

        客户端应用名称

        :return: The name of this AppQuotaAppInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AppQuotaAppInfo.

        客户端应用名称

        :param name: The name of this AppQuotaAppInfo.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this AppQuotaAppInfo.

        客户端应用状态： - 1：启用 - 2：禁用

        :return: The status of this AppQuotaAppInfo.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this AppQuotaAppInfo.

        客户端应用状态： - 1：启用 - 2：禁用

        :param status: The status of this AppQuotaAppInfo.
        :type status: int
        """
        self._status = status

    @property
    def app_key(self):
        r"""Gets the app_key of this AppQuotaAppInfo.

        客户端应用的Key

        :return: The app_key of this AppQuotaAppInfo.
        :rtype: str
        """
        return self._app_key

    @app_key.setter
    def app_key(self, app_key):
        r"""Sets the app_key of this AppQuotaAppInfo.

        客户端应用的Key

        :param app_key: The app_key of this AppQuotaAppInfo.
        :type app_key: str
        """
        self._app_key = app_key

    @property
    def remark(self):
        r"""Gets the remark of this AppQuotaAppInfo.

        客户端应用描述

        :return: The remark of this AppQuotaAppInfo.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        r"""Sets the remark of this AppQuotaAppInfo.

        客户端应用描述

        :param remark: The remark of this AppQuotaAppInfo.
        :type remark: str
        """
        self._remark = remark

    @property
    def register_time(self):
        r"""Gets the register_time of this AppQuotaAppInfo.

        创建时间

        :return: The register_time of this AppQuotaAppInfo.
        :rtype: datetime
        """
        return self._register_time

    @register_time.setter
    def register_time(self, register_time):
        r"""Sets the register_time of this AppQuotaAppInfo.

        创建时间

        :param register_time: The register_time of this AppQuotaAppInfo.
        :type register_time: datetime
        """
        self._register_time = register_time

    @property
    def update_time(self):
        r"""Gets the update_time of this AppQuotaAppInfo.

        更新时间

        :return: The update_time of this AppQuotaAppInfo.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this AppQuotaAppInfo.

        更新时间

        :param update_time: The update_time of this AppQuotaAppInfo.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def app_quota_id(self):
        r"""Gets the app_quota_id of this AppQuotaAppInfo.

        客户端配额编号

        :return: The app_quota_id of this AppQuotaAppInfo.
        :rtype: str
        """
        return self._app_quota_id

    @app_quota_id.setter
    def app_quota_id(self, app_quota_id):
        r"""Sets the app_quota_id of this AppQuotaAppInfo.

        客户端配额编号

        :param app_quota_id: The app_quota_id of this AppQuotaAppInfo.
        :type app_quota_id: str
        """
        self._app_quota_id = app_quota_id

    @property
    def app_quota_name(self):
        r"""Gets the app_quota_name of this AppQuotaAppInfo.

        配额名称。支持汉字，英文，数字，下划线，且只能以英文和汉字开头，3-255字符

        :return: The app_quota_name of this AppQuotaAppInfo.
        :rtype: str
        """
        return self._app_quota_name

    @app_quota_name.setter
    def app_quota_name(self, app_quota_name):
        r"""Sets the app_quota_name of this AppQuotaAppInfo.

        配额名称。支持汉字，英文，数字，下划线，且只能以英文和汉字开头，3-255字符

        :param app_quota_name: The app_quota_name of this AppQuotaAppInfo.
        :type app_quota_name: str
        """
        self._app_quota_name = app_quota_name

    @property
    def bound_time(self):
        r"""Gets the bound_time of this AppQuotaAppInfo.

        绑定时间

        :return: The bound_time of this AppQuotaAppInfo.
        :rtype: datetime
        """
        return self._bound_time

    @bound_time.setter
    def bound_time(self, bound_time):
        r"""Sets the bound_time of this AppQuotaAppInfo.

        绑定时间

        :param bound_time: The bound_time of this AppQuotaAppInfo.
        :type bound_time: datetime
        """
        self._bound_time = bound_time

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
        if not isinstance(other, AppQuotaAppInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
