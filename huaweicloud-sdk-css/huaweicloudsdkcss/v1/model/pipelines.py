# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Pipelines:

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
        'keep_alive': 'bool',
        'events': 'str',
        'update_at': 'str'
    }

    attribute_map = {
        'name': 'name',
        'status': 'status',
        'keep_alive': 'keepAlive',
        'events': 'events',
        'update_at': 'updateAt'
    }

    def __init__(self, name=None, status=None, keep_alive=None, events=None, update_at=None):
        """Pipelines

        The model defined in huaweicloud sdk

        :param name: 配置文件名称。
        :type name: str
        :param status: pipeline状态。
        :type status: str
        :param keep_alive: 是否开启常驻。
        :type keep_alive: bool
        :param events: 事件只有在“工作中”状态才可以实时查看（需要手动刷新），“已停止”状态请到output端查看迁移数据量。
        :type events: str
        :param update_at: 更新时间。
        :type update_at: str
        """
        
        

        self._name = None
        self._status = None
        self._keep_alive = None
        self._events = None
        self._update_at = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if keep_alive is not None:
            self.keep_alive = keep_alive
        if events is not None:
            self.events = events
        if update_at is not None:
            self.update_at = update_at

    @property
    def name(self):
        """Gets the name of this Pipelines.

        配置文件名称。

        :return: The name of this Pipelines.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Pipelines.

        配置文件名称。

        :param name: The name of this Pipelines.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this Pipelines.

        pipeline状态。

        :return: The status of this Pipelines.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Pipelines.

        pipeline状态。

        :param status: The status of this Pipelines.
        :type status: str
        """
        self._status = status

    @property
    def keep_alive(self):
        """Gets the keep_alive of this Pipelines.

        是否开启常驻。

        :return: The keep_alive of this Pipelines.
        :rtype: bool
        """
        return self._keep_alive

    @keep_alive.setter
    def keep_alive(self, keep_alive):
        """Sets the keep_alive of this Pipelines.

        是否开启常驻。

        :param keep_alive: The keep_alive of this Pipelines.
        :type keep_alive: bool
        """
        self._keep_alive = keep_alive

    @property
    def events(self):
        """Gets the events of this Pipelines.

        事件只有在“工作中”状态才可以实时查看（需要手动刷新），“已停止”状态请到output端查看迁移数据量。

        :return: The events of this Pipelines.
        :rtype: str
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this Pipelines.

        事件只有在“工作中”状态才可以实时查看（需要手动刷新），“已停止”状态请到output端查看迁移数据量。

        :param events: The events of this Pipelines.
        :type events: str
        """
        self._events = events

    @property
    def update_at(self):
        """Gets the update_at of this Pipelines.

        更新时间。

        :return: The update_at of this Pipelines.
        :rtype: str
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        """Sets the update_at of this Pipelines.

        更新时间。

        :param update_at: The update_at of this Pipelines.
        :type update_at: str
        """
        self._update_at = update_at

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
        if not isinstance(other, Pipelines):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
