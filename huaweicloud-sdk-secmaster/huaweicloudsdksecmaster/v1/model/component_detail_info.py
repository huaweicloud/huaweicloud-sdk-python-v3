# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComponentDetailInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'component_id': 'str',
        'component_name': 'str',
        'create_time': 'int',
        'description': 'str',
        'history_version': 'str',
        'maintainer': 'str',
        'time_zone': 'str',
        'update_time': 'int',
        'upgrade': 'str',
        'upgrade_fail_message': 'str',
        'version': 'str'
    }

    attribute_map = {
        'component_id': 'component_id',
        'component_name': 'component_name',
        'create_time': 'create_time',
        'description': 'description',
        'history_version': 'history_version',
        'maintainer': 'maintainer',
        'time_zone': 'time_zone',
        'update_time': 'update_time',
        'upgrade': 'upgrade',
        'upgrade_fail_message': 'upgrade_fail_message',
        'version': 'version'
    }

    def __init__(self, component_id=None, component_name=None, create_time=None, description=None, history_version=None, maintainer=None, time_zone=None, update_time=None, upgrade=None, upgrade_fail_message=None, version=None):
        r"""ComponentDetailInfo

        The model defined in huaweicloud sdk

        :param component_id: 组件id.
        :type component_id: str
        :param component_name: 组件名称
        :type component_name: str
        :param create_time: 毫秒时间戳
        :type create_time: int
        :param description: 相关描述
        :type description: str
        :param history_version: 历史版本
        :type history_version: str
        :param maintainer: 保持
        :type maintainer: str
        :param time_zone: 时区
        :type time_zone: str
        :param update_time: 毫秒时间戳
        :type update_time: int
        :param upgrade: **参数解释**: 升级 - NEED_UPGRADE 需要升级 - UPGRADING 升级中 - SUCCESS_UPGRADE 升级成功 - FAIL_UPGRADE 升级失败  **约束限制** 不涉及 **取值范围**: - NEED_UPGRADE - UPGRADING - SUCCESS_UPGRADE - FAIL_UPGRADE  **默认值** 不涉及
        :type upgrade: str
        :param upgrade_fail_message: 更新失败的消息
        :type upgrade_fail_message: str
        :param version: 安全云脑版本
        :type version: str
        """
        
        

        self._component_id = None
        self._component_name = None
        self._create_time = None
        self._description = None
        self._history_version = None
        self._maintainer = None
        self._time_zone = None
        self._update_time = None
        self._upgrade = None
        self._upgrade_fail_message = None
        self._version = None
        self.discriminator = None

        if component_id is not None:
            self.component_id = component_id
        if component_name is not None:
            self.component_name = component_name
        if create_time is not None:
            self.create_time = create_time
        if description is not None:
            self.description = description
        if history_version is not None:
            self.history_version = history_version
        if maintainer is not None:
            self.maintainer = maintainer
        if time_zone is not None:
            self.time_zone = time_zone
        if update_time is not None:
            self.update_time = update_time
        if upgrade is not None:
            self.upgrade = upgrade
        if upgrade_fail_message is not None:
            self.upgrade_fail_message = upgrade_fail_message
        if version is not None:
            self.version = version

    @property
    def component_id(self):
        r"""Gets the component_id of this ComponentDetailInfo.

        组件id.

        :return: The component_id of this ComponentDetailInfo.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        r"""Sets the component_id of this ComponentDetailInfo.

        组件id.

        :param component_id: The component_id of this ComponentDetailInfo.
        :type component_id: str
        """
        self._component_id = component_id

    @property
    def component_name(self):
        r"""Gets the component_name of this ComponentDetailInfo.

        组件名称

        :return: The component_name of this ComponentDetailInfo.
        :rtype: str
        """
        return self._component_name

    @component_name.setter
    def component_name(self, component_name):
        r"""Sets the component_name of this ComponentDetailInfo.

        组件名称

        :param component_name: The component_name of this ComponentDetailInfo.
        :type component_name: str
        """
        self._component_name = component_name

    @property
    def create_time(self):
        r"""Gets the create_time of this ComponentDetailInfo.

        毫秒时间戳

        :return: The create_time of this ComponentDetailInfo.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ComponentDetailInfo.

        毫秒时间戳

        :param create_time: The create_time of this ComponentDetailInfo.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def description(self):
        r"""Gets the description of this ComponentDetailInfo.

        相关描述

        :return: The description of this ComponentDetailInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ComponentDetailInfo.

        相关描述

        :param description: The description of this ComponentDetailInfo.
        :type description: str
        """
        self._description = description

    @property
    def history_version(self):
        r"""Gets the history_version of this ComponentDetailInfo.

        历史版本

        :return: The history_version of this ComponentDetailInfo.
        :rtype: str
        """
        return self._history_version

    @history_version.setter
    def history_version(self, history_version):
        r"""Sets the history_version of this ComponentDetailInfo.

        历史版本

        :param history_version: The history_version of this ComponentDetailInfo.
        :type history_version: str
        """
        self._history_version = history_version

    @property
    def maintainer(self):
        r"""Gets the maintainer of this ComponentDetailInfo.

        保持

        :return: The maintainer of this ComponentDetailInfo.
        :rtype: str
        """
        return self._maintainer

    @maintainer.setter
    def maintainer(self, maintainer):
        r"""Sets the maintainer of this ComponentDetailInfo.

        保持

        :param maintainer: The maintainer of this ComponentDetailInfo.
        :type maintainer: str
        """
        self._maintainer = maintainer

    @property
    def time_zone(self):
        r"""Gets the time_zone of this ComponentDetailInfo.

        时区

        :return: The time_zone of this ComponentDetailInfo.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        r"""Sets the time_zone of this ComponentDetailInfo.

        时区

        :param time_zone: The time_zone of this ComponentDetailInfo.
        :type time_zone: str
        """
        self._time_zone = time_zone

    @property
    def update_time(self):
        r"""Gets the update_time of this ComponentDetailInfo.

        毫秒时间戳

        :return: The update_time of this ComponentDetailInfo.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ComponentDetailInfo.

        毫秒时间戳

        :param update_time: The update_time of this ComponentDetailInfo.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def upgrade(self):
        r"""Gets the upgrade of this ComponentDetailInfo.

        **参数解释**: 升级 - NEED_UPGRADE 需要升级 - UPGRADING 升级中 - SUCCESS_UPGRADE 升级成功 - FAIL_UPGRADE 升级失败  **约束限制** 不涉及 **取值范围**: - NEED_UPGRADE - UPGRADING - SUCCESS_UPGRADE - FAIL_UPGRADE  **默认值** 不涉及

        :return: The upgrade of this ComponentDetailInfo.
        :rtype: str
        """
        return self._upgrade

    @upgrade.setter
    def upgrade(self, upgrade):
        r"""Sets the upgrade of this ComponentDetailInfo.

        **参数解释**: 升级 - NEED_UPGRADE 需要升级 - UPGRADING 升级中 - SUCCESS_UPGRADE 升级成功 - FAIL_UPGRADE 升级失败  **约束限制** 不涉及 **取值范围**: - NEED_UPGRADE - UPGRADING - SUCCESS_UPGRADE - FAIL_UPGRADE  **默认值** 不涉及

        :param upgrade: The upgrade of this ComponentDetailInfo.
        :type upgrade: str
        """
        self._upgrade = upgrade

    @property
    def upgrade_fail_message(self):
        r"""Gets the upgrade_fail_message of this ComponentDetailInfo.

        更新失败的消息

        :return: The upgrade_fail_message of this ComponentDetailInfo.
        :rtype: str
        """
        return self._upgrade_fail_message

    @upgrade_fail_message.setter
    def upgrade_fail_message(self, upgrade_fail_message):
        r"""Sets the upgrade_fail_message of this ComponentDetailInfo.

        更新失败的消息

        :param upgrade_fail_message: The upgrade_fail_message of this ComponentDetailInfo.
        :type upgrade_fail_message: str
        """
        self._upgrade_fail_message = upgrade_fail_message

    @property
    def version(self):
        r"""Gets the version of this ComponentDetailInfo.

        安全云脑版本

        :return: The version of this ComponentDetailInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ComponentDetailInfo.

        安全云脑版本

        :param version: The version of this ComponentDetailInfo.
        :type version: str
        """
        self._version = version

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
        if not isinstance(other, ComponentDetailInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
