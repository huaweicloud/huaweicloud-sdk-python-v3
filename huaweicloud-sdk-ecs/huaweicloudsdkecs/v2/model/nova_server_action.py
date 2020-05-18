# coding: utf-8

import pprint
import re

import six


class NovaServerAction(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'action': 'str',
        'instance_uuid': 'str',
        'message': 'str',
        'project_id': 'str',
        'request_id': 'str',
        'updated_at': 'str',
        'start_time': 'str',
        'user_id': 'str'
    }

    attribute_map = {
        'action': 'action',
        'instance_uuid': 'instance_uuid',
        'message': 'message',
        'project_id': 'project_id',
        'request_id': 'request_id',
        'updated_at': 'updated_at',
        'start_time': 'start_time',
        'user_id': 'user_id'
    }

    def __init__(self, action=None, instance_uuid=None, message=None, project_id=None, request_id=None, updated_at=None, start_time=None, user_id=None):  # noqa: E501
        """NovaServerAction - a model defined in huaweicloud sdk"""

        self._action = None
        self._instance_uuid = None
        self._message = None
        self._project_id = None
        self._request_id = None
        self._updated_at = None
        self._start_time = None
        self._user_id = None
        self.discriminator = None

        self.action = action
        self.instance_uuid = instance_uuid
        self.message = message
        self.project_id = project_id
        self.request_id = request_id
        self.updated_at = updated_at
        self.start_time = start_time
        self.user_id = user_id

    @property
    def action(self):
        """Gets the action of this NovaServerAction.

        行为动作  取值范围：  create , delete , evacuate , restore , stop , start , reboot , rebuild , revertResize , confirmResize , detach_volume , attach_volume , attach_interface , detach_interface , lock , unlock , resize , migrate , pause , unpause , suspend , resume , rescue , unrescue , changePassword , shelve ,unshelve , live-migration , live_migration_cancel , live_migration_force_complete , trigger_crash_dump, extend_volume

        :return: The action of this NovaServerAction.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this NovaServerAction.

        行为动作  取值范围：  create , delete , evacuate , restore , stop , start , reboot , rebuild , revertResize , confirmResize , detach_volume , attach_volume , attach_interface , detach_interface , lock , unlock , resize , migrate , pause , unpause , suspend , resume , rescue , unrescue , changePassword , shelve ,unshelve , live-migration , live_migration_cancel , live_migration_force_complete , trigger_crash_dump, extend_volume

        :param action: The action of this NovaServerAction.
        :type: str
        """
        self._action = action

    @property
    def instance_uuid(self):
        """Gets the instance_uuid of this NovaServerAction.

        弹性云服务器ID。

        :return: The instance_uuid of this NovaServerAction.
        :rtype: str
        """
        return self._instance_uuid

    @instance_uuid.setter
    def instance_uuid(self, instance_uuid):
        """Sets the instance_uuid of this NovaServerAction.

        弹性云服务器ID。

        :param instance_uuid: The instance_uuid of this NovaServerAction.
        :type: str
        """
        self._instance_uuid = instance_uuid

    @property
    def message(self):
        """Gets the message of this NovaServerAction.

        行为完成状态信息。

        :return: The message of this NovaServerAction.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this NovaServerAction.

        行为完成状态信息。

        :param message: The message of this NovaServerAction.
        :type: str
        """
        self._message = message

    @property
    def project_id(self):
        """Gets the project_id of this NovaServerAction.

        项目ID。

        :return: The project_id of this NovaServerAction.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this NovaServerAction.

        项目ID。

        :param project_id: The project_id of this NovaServerAction.
        :type: str
        """
        self._project_id = project_id

    @property
    def request_id(self):
        """Gets the request_id of this NovaServerAction.

        请求ID。

        :return: The request_id of this NovaServerAction.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this NovaServerAction.

        请求ID。

        :param request_id: The request_id of this NovaServerAction.
        :type: str
        """
        self._request_id = request_id

    @property
    def updated_at(self):
        """Gets the updated_at of this NovaServerAction.

        更新时间。

        :return: The updated_at of this NovaServerAction.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this NovaServerAction.

        更新时间。

        :param updated_at: The updated_at of this NovaServerAction.
        :type: str
        """
        self._updated_at = updated_at

    @property
    def start_time(self):
        """Gets the start_time of this NovaServerAction.

        行为开始时间。

        :return: The start_time of this NovaServerAction.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this NovaServerAction.

        行为开始时间。

        :param start_time: The start_time of this NovaServerAction.
        :type: str
        """
        self._start_time = start_time

    @property
    def user_id(self):
        """Gets the user_id of this NovaServerAction.

        用户ID。

        :return: The user_id of this NovaServerAction.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this NovaServerAction.

        用户ID。

        :param user_id: The user_id of this NovaServerAction.
        :type: str
        """
        self._user_id = user_id

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
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NovaServerAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
