# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Actions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'action_type': 'str',
        'conf_content': 'str',
        'status': 'str',
        'update_at': 'str',
        'error_msg': 'str',
        'message': 'str'
    }

    attribute_map = {
        'id': 'id',
        'action_type': 'actionType',
        'conf_content': 'confContent',
        'status': 'status',
        'update_at': 'updateAt',
        'error_msg': 'errorMsg',
        'message': 'message'
    }

    def __init__(self, id=None, action_type=None, conf_content=None, status=None, update_at=None, error_msg=None, message=None):
        """Actions

        The model defined in huaweicloud sdk

        :param id: 操作记录id。
        :type id: str
        :param action_type: 操作类型。
        :type action_type: str
        :param conf_content: 配置文件内容。
        :type conf_content: str
        :param status: 操作状态。
        :type status: str
        :param update_at: 更新时间，格式为ISO8601：CCYY-MM-DDThh:mm:ss。
        :type update_at: str
        :param error_msg: 错误信息。当操作状态为success时该字段为null。
        :type error_msg: str
        :param message: 内容。
        :type message: str
        """
        
        

        self._id = None
        self._action_type = None
        self._conf_content = None
        self._status = None
        self._update_at = None
        self._error_msg = None
        self._message = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if action_type is not None:
            self.action_type = action_type
        if conf_content is not None:
            self.conf_content = conf_content
        if status is not None:
            self.status = status
        if update_at is not None:
            self.update_at = update_at
        if error_msg is not None:
            self.error_msg = error_msg
        if message is not None:
            self.message = message

    @property
    def id(self):
        """Gets the id of this Actions.

        操作记录id。

        :return: The id of this Actions.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Actions.

        操作记录id。

        :param id: The id of this Actions.
        :type id: str
        """
        self._id = id

    @property
    def action_type(self):
        """Gets the action_type of this Actions.

        操作类型。

        :return: The action_type of this Actions.
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """Sets the action_type of this Actions.

        操作类型。

        :param action_type: The action_type of this Actions.
        :type action_type: str
        """
        self._action_type = action_type

    @property
    def conf_content(self):
        """Gets the conf_content of this Actions.

        配置文件内容。

        :return: The conf_content of this Actions.
        :rtype: str
        """
        return self._conf_content

    @conf_content.setter
    def conf_content(self, conf_content):
        """Sets the conf_content of this Actions.

        配置文件内容。

        :param conf_content: The conf_content of this Actions.
        :type conf_content: str
        """
        self._conf_content = conf_content

    @property
    def status(self):
        """Gets the status of this Actions.

        操作状态。

        :return: The status of this Actions.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Actions.

        操作状态。

        :param status: The status of this Actions.
        :type status: str
        """
        self._status = status

    @property
    def update_at(self):
        """Gets the update_at of this Actions.

        更新时间，格式为ISO8601：CCYY-MM-DDThh:mm:ss。

        :return: The update_at of this Actions.
        :rtype: str
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        """Sets the update_at of this Actions.

        更新时间，格式为ISO8601：CCYY-MM-DDThh:mm:ss。

        :param update_at: The update_at of this Actions.
        :type update_at: str
        """
        self._update_at = update_at

    @property
    def error_msg(self):
        """Gets the error_msg of this Actions.

        错误信息。当操作状态为success时该字段为null。

        :return: The error_msg of this Actions.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this Actions.

        错误信息。当操作状态为success时该字段为null。

        :param error_msg: The error_msg of this Actions.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def message(self):
        """Gets the message of this Actions.

        内容。

        :return: The message of this Actions.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Actions.

        内容。

        :param message: The message of this Actions.
        :type message: str
        """
        self._message = message

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
        if not isinstance(other, Actions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
