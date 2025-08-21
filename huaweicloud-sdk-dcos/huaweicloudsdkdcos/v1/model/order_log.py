# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OrderLog:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'stage': 'str',
        'handler': 'str',
        'time': 'str',
        'action': 'str',
        'description': 'str',
        'status': 'str',
        'attachments': 'list[UploadFileInfo]'
    }

    attribute_map = {
        'stage': 'stage',
        'handler': 'handler',
        'time': 'time',
        'action': 'action',
        'description': 'description',
        'status': 'status',
        'attachments': 'attachments'
    }

    def __init__(self, stage=None, handler=None, time=None, action=None, description=None, status=None, attachments=None):
        r"""OrderLog

        The model defined in huaweicloud sdk

        :param stage: 阶段
        :type stage: str
        :param handler: 处理人
        :type handler: str
        :param time: 处理时间
        :type time: str
        :param action: 处理动作
        :type action: str
        :param description: 处理说明
        :type description: str
        :param status: 状态
        :type status: str
        :param attachments: 附件
        :type attachments: list[:class:`huaweicloudsdkdcos.v1.UploadFileInfo`]
        """
        
        

        self._stage = None
        self._handler = None
        self._time = None
        self._action = None
        self._description = None
        self._status = None
        self._attachments = None
        self.discriminator = None

        if stage is not None:
            self.stage = stage
        if handler is not None:
            self.handler = handler
        if time is not None:
            self.time = time
        if action is not None:
            self.action = action
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if attachments is not None:
            self.attachments = attachments

    @property
    def stage(self):
        r"""Gets the stage of this OrderLog.

        阶段

        :return: The stage of this OrderLog.
        :rtype: str
        """
        return self._stage

    @stage.setter
    def stage(self, stage):
        r"""Sets the stage of this OrderLog.

        阶段

        :param stage: The stage of this OrderLog.
        :type stage: str
        """
        self._stage = stage

    @property
    def handler(self):
        r"""Gets the handler of this OrderLog.

        处理人

        :return: The handler of this OrderLog.
        :rtype: str
        """
        return self._handler

    @handler.setter
    def handler(self, handler):
        r"""Sets the handler of this OrderLog.

        处理人

        :param handler: The handler of this OrderLog.
        :type handler: str
        """
        self._handler = handler

    @property
    def time(self):
        r"""Gets the time of this OrderLog.

        处理时间

        :return: The time of this OrderLog.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this OrderLog.

        处理时间

        :param time: The time of this OrderLog.
        :type time: str
        """
        self._time = time

    @property
    def action(self):
        r"""Gets the action of this OrderLog.

        处理动作

        :return: The action of this OrderLog.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this OrderLog.

        处理动作

        :param action: The action of this OrderLog.
        :type action: str
        """
        self._action = action

    @property
    def description(self):
        r"""Gets the description of this OrderLog.

        处理说明

        :return: The description of this OrderLog.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this OrderLog.

        处理说明

        :param description: The description of this OrderLog.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        r"""Gets the status of this OrderLog.

        状态

        :return: The status of this OrderLog.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this OrderLog.

        状态

        :param status: The status of this OrderLog.
        :type status: str
        """
        self._status = status

    @property
    def attachments(self):
        r"""Gets the attachments of this OrderLog.

        附件

        :return: The attachments of this OrderLog.
        :rtype: list[:class:`huaweicloudsdkdcos.v1.UploadFileInfo`]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        r"""Sets the attachments of this OrderLog.

        附件

        :param attachments: The attachments of this OrderLog.
        :type attachments: list[:class:`huaweicloudsdkdcos.v1.UploadFileInfo`]
        """
        self._attachments = attachments

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
        if not isinstance(other, OrderLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
