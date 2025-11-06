# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LinkSettingDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'active': 'bool',
        'url': 'str',
        'app_auth_type': 'str',
        'app_ak': 'str',
        'app_sk': 'str',
        'categories': 'str',
        'exclude_statuses': 'str'
    }

    attribute_map = {
        'active': 'active',
        'url': 'url',
        'app_auth_type': 'app_auth_type',
        'app_ak': 'app_ak',
        'app_sk': 'app_sk',
        'categories': 'categories',
        'exclude_statuses': 'exclude_statuses'
    }

    def __init__(self, active=None, url=None, app_auth_type=None, app_ak=None, app_sk=None, categories=None, exclude_statuses=None):
        r"""LinkSettingDto

        The model defined in huaweicloud sdk

        :param active: **参数解释：** 是否开启集成Link服务 **取值范围：** true：开启集成Link服务，false：未开启集成Link服务。
        :type active: bool
        :param url: **参数解释：** Link服务的对接地址。
        :type url: str
        :param app_auth_type: **参数解释：** Link服务的对接鉴权类型，ak_sk代表使用ak和sk来鉴权。
        :type app_auth_type: str
        :param app_ak: **参数解释：** Link服务的对接鉴权ak。
        :type app_ak: str
        :param app_sk: **参数解释：** Link服务的对接鉴权sk，作为返回值时若已配置则返回掩码，掩码格式为************。
        :type app_sk: str
        :param categories: **参数解释：** 可关联类型列表，逗号分隔。
        :type categories: str
        :param exclude_statuses: **参数解释：** 排除状态列表，逗号分隔。
        :type exclude_statuses: str
        """
        
        

        self._active = None
        self._url = None
        self._app_auth_type = None
        self._app_ak = None
        self._app_sk = None
        self._categories = None
        self._exclude_statuses = None
        self.discriminator = None

        if active is not None:
            self.active = active
        if url is not None:
            self.url = url
        if app_auth_type is not None:
            self.app_auth_type = app_auth_type
        if app_ak is not None:
            self.app_ak = app_ak
        if app_sk is not None:
            self.app_sk = app_sk
        if categories is not None:
            self.categories = categories
        if exclude_statuses is not None:
            self.exclude_statuses = exclude_statuses

    @property
    def active(self):
        r"""Gets the active of this LinkSettingDto.

        **参数解释：** 是否开启集成Link服务 **取值范围：** true：开启集成Link服务，false：未开启集成Link服务。

        :return: The active of this LinkSettingDto.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        r"""Sets the active of this LinkSettingDto.

        **参数解释：** 是否开启集成Link服务 **取值范围：** true：开启集成Link服务，false：未开启集成Link服务。

        :param active: The active of this LinkSettingDto.
        :type active: bool
        """
        self._active = active

    @property
    def url(self):
        r"""Gets the url of this LinkSettingDto.

        **参数解释：** Link服务的对接地址。

        :return: The url of this LinkSettingDto.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this LinkSettingDto.

        **参数解释：** Link服务的对接地址。

        :param url: The url of this LinkSettingDto.
        :type url: str
        """
        self._url = url

    @property
    def app_auth_type(self):
        r"""Gets the app_auth_type of this LinkSettingDto.

        **参数解释：** Link服务的对接鉴权类型，ak_sk代表使用ak和sk来鉴权。

        :return: The app_auth_type of this LinkSettingDto.
        :rtype: str
        """
        return self._app_auth_type

    @app_auth_type.setter
    def app_auth_type(self, app_auth_type):
        r"""Sets the app_auth_type of this LinkSettingDto.

        **参数解释：** Link服务的对接鉴权类型，ak_sk代表使用ak和sk来鉴权。

        :param app_auth_type: The app_auth_type of this LinkSettingDto.
        :type app_auth_type: str
        """
        self._app_auth_type = app_auth_type

    @property
    def app_ak(self):
        r"""Gets the app_ak of this LinkSettingDto.

        **参数解释：** Link服务的对接鉴权ak。

        :return: The app_ak of this LinkSettingDto.
        :rtype: str
        """
        return self._app_ak

    @app_ak.setter
    def app_ak(self, app_ak):
        r"""Sets the app_ak of this LinkSettingDto.

        **参数解释：** Link服务的对接鉴权ak。

        :param app_ak: The app_ak of this LinkSettingDto.
        :type app_ak: str
        """
        self._app_ak = app_ak

    @property
    def app_sk(self):
        r"""Gets the app_sk of this LinkSettingDto.

        **参数解释：** Link服务的对接鉴权sk，作为返回值时若已配置则返回掩码，掩码格式为************。

        :return: The app_sk of this LinkSettingDto.
        :rtype: str
        """
        return self._app_sk

    @app_sk.setter
    def app_sk(self, app_sk):
        r"""Sets the app_sk of this LinkSettingDto.

        **参数解释：** Link服务的对接鉴权sk，作为返回值时若已配置则返回掩码，掩码格式为************。

        :param app_sk: The app_sk of this LinkSettingDto.
        :type app_sk: str
        """
        self._app_sk = app_sk

    @property
    def categories(self):
        r"""Gets the categories of this LinkSettingDto.

        **参数解释：** 可关联类型列表，逗号分隔。

        :return: The categories of this LinkSettingDto.
        :rtype: str
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        r"""Sets the categories of this LinkSettingDto.

        **参数解释：** 可关联类型列表，逗号分隔。

        :param categories: The categories of this LinkSettingDto.
        :type categories: str
        """
        self._categories = categories

    @property
    def exclude_statuses(self):
        r"""Gets the exclude_statuses of this LinkSettingDto.

        **参数解释：** 排除状态列表，逗号分隔。

        :return: The exclude_statuses of this LinkSettingDto.
        :rtype: str
        """
        return self._exclude_statuses

    @exclude_statuses.setter
    def exclude_statuses(self, exclude_statuses):
        r"""Sets the exclude_statuses of this LinkSettingDto.

        **参数解释：** 排除状态列表，逗号分隔。

        :param exclude_statuses: The exclude_statuses of this LinkSettingDto.
        :type exclude_statuses: str
        """
        self._exclude_statuses = exclude_statuses

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LinkSettingDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
