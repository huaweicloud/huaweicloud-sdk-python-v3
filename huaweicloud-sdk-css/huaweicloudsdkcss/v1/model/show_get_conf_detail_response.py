# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowGetConfDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'status': 'str',
        'conf_content': 'str',
        'setting': 'Setting',
        'update_at': 'str',
        'desc': 'str'
    }

    attribute_map = {
        'name': 'name',
        'status': 'status',
        'conf_content': 'confContent',
        'setting': 'setting',
        'update_at': 'updateAt',
        'desc': 'desc'
    }

    def __init__(self, name=None, status=None, conf_content=None, setting=None, update_at=None, desc=None):
        r"""ShowGetConfDetailResponse

        The model defined in huaweicloud sdk

        :param name: 配置文件名称。
        :type name: str
        :param status: 配置文件状态。
        :type status: str
        :param conf_content: 配置文件内容。
        :type conf_content: str
        :param setting: 
        :type setting: :class:`huaweicloudsdkcss.v1.Setting`
        :param update_at: 更新时间。
        :type update_at: str
        :param desc: **参数解释**： 配置文件描述。 **取值范围**： 长度不超过128个字符。
        :type desc: str
        """
        
        super().__init__()

        self._name = None
        self._status = None
        self._conf_content = None
        self._setting = None
        self._update_at = None
        self._desc = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if conf_content is not None:
            self.conf_content = conf_content
        if setting is not None:
            self.setting = setting
        if update_at is not None:
            self.update_at = update_at
        if desc is not None:
            self.desc = desc

    @property
    def name(self):
        r"""Gets the name of this ShowGetConfDetailResponse.

        配置文件名称。

        :return: The name of this ShowGetConfDetailResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowGetConfDetailResponse.

        配置文件名称。

        :param name: The name of this ShowGetConfDetailResponse.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this ShowGetConfDetailResponse.

        配置文件状态。

        :return: The status of this ShowGetConfDetailResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowGetConfDetailResponse.

        配置文件状态。

        :param status: The status of this ShowGetConfDetailResponse.
        :type status: str
        """
        self._status = status

    @property
    def conf_content(self):
        r"""Gets the conf_content of this ShowGetConfDetailResponse.

        配置文件内容。

        :return: The conf_content of this ShowGetConfDetailResponse.
        :rtype: str
        """
        return self._conf_content

    @conf_content.setter
    def conf_content(self, conf_content):
        r"""Sets the conf_content of this ShowGetConfDetailResponse.

        配置文件内容。

        :param conf_content: The conf_content of this ShowGetConfDetailResponse.
        :type conf_content: str
        """
        self._conf_content = conf_content

    @property
    def setting(self):
        r"""Gets the setting of this ShowGetConfDetailResponse.

        :return: The setting of this ShowGetConfDetailResponse.
        :rtype: :class:`huaweicloudsdkcss.v1.Setting`
        """
        return self._setting

    @setting.setter
    def setting(self, setting):
        r"""Sets the setting of this ShowGetConfDetailResponse.

        :param setting: The setting of this ShowGetConfDetailResponse.
        :type setting: :class:`huaweicloudsdkcss.v1.Setting`
        """
        self._setting = setting

    @property
    def update_at(self):
        r"""Gets the update_at of this ShowGetConfDetailResponse.

        更新时间。

        :return: The update_at of this ShowGetConfDetailResponse.
        :rtype: str
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        r"""Sets the update_at of this ShowGetConfDetailResponse.

        更新时间。

        :param update_at: The update_at of this ShowGetConfDetailResponse.
        :type update_at: str
        """
        self._update_at = update_at

    @property
    def desc(self):
        r"""Gets the desc of this ShowGetConfDetailResponse.

        **参数解释**： 配置文件描述。 **取值范围**： 长度不超过128个字符。

        :return: The desc of this ShowGetConfDetailResponse.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        r"""Sets the desc of this ShowGetConfDetailResponse.

        **参数解释**： 配置文件描述。 **取值范围**： 长度不超过128个字符。

        :param desc: The desc of this ShowGetConfDetailResponse.
        :type desc: str
        """
        self._desc = desc

    def to_dict(self):
        import warnings
        warnings.warn("ShowGetConfDetailResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowGetConfDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
