# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceStatusStatistics:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'static_name': 'str',
        'running_num': 'int',
        'stop_num': 'int',
        'hibernate_num': 'int',
        'other_num': 'int',
        'attached_num': 'int',
        'unattached_num': 'int',
        'cannot_attach_num': 'int',
        'in_process_num': 'int',
        'in_use_num': 'int',
        'unregistered_num': 'int',
        'ready_num': 'int',
        'disconnected_num': 'int',
        'unknown_num': 'int'
    }

    attribute_map = {
        'static_name': 'static_name',
        'running_num': 'running_num',
        'stop_num': 'stop_num',
        'hibernate_num': 'hibernate_num',
        'other_num': 'other_num',
        'attached_num': 'attached_num',
        'unattached_num': 'unattached_num',
        'cannot_attach_num': 'cannot_attach_num',
        'in_process_num': 'in_process_num',
        'in_use_num': 'in_use_num',
        'unregistered_num': 'unregistered_num',
        'ready_num': 'ready_num',
        'disconnected_num': 'disconnected_num',
        'unknown_num': 'unknown_num'
    }

    def __init__(self, static_name=None, running_num=None, stop_num=None, hibernate_num=None, other_num=None, attached_num=None, unattached_num=None, cannot_attach_num=None, in_process_num=None, in_use_num=None, unregistered_num=None, ready_num=None, disconnected_num=None, unknown_num=None):
        r"""InstanceStatusStatistics

        The model defined in huaweicloud sdk

        :param static_name: 统计对象名称(虚拟机组名称、桌面组名称)。
        :type static_name: str
        :param running_num: 运行数目(运行中、启动中、故障迁移中、迁移中)。
        :type running_num: int
        :param stop_num: 关机数目(关机中、已关机)。
        :type stop_num: int
        :param hibernate_num: 休眠数目(休眠中、已休眠)。
        :type hibernate_num: int
        :param other_num: 其他(未知、删除失败、删除中)。
        :type other_num: int
        :param attached_num: 已分配数目。
        :type attached_num: int
        :param unattached_num: 未分配数目。
        :type unattached_num: int
        :param cannot_attach_num: 不可分配数目(分配失败、解分配失败、解分配成功)。
        :type cannot_attach_num: int
        :param in_process_num: 处理中(分配中、解分配中)。
        :type in_process_num: int
        :param in_use_num: 使用中数目。
        :type in_use_num: int
        :param unregistered_num: 未注册数目。
        :type unregistered_num: int
        :param ready_num: 空闲数目。
        :type ready_num: int
        :param disconnected_num: 断开连接数目。
        :type disconnected_num: int
        :param unknown_num: 未知数目。
        :type unknown_num: int
        """
        
        

        self._static_name = None
        self._running_num = None
        self._stop_num = None
        self._hibernate_num = None
        self._other_num = None
        self._attached_num = None
        self._unattached_num = None
        self._cannot_attach_num = None
        self._in_process_num = None
        self._in_use_num = None
        self._unregistered_num = None
        self._ready_num = None
        self._disconnected_num = None
        self._unknown_num = None
        self.discriminator = None

        if static_name is not None:
            self.static_name = static_name
        if running_num is not None:
            self.running_num = running_num
        if stop_num is not None:
            self.stop_num = stop_num
        if hibernate_num is not None:
            self.hibernate_num = hibernate_num
        if other_num is not None:
            self.other_num = other_num
        if attached_num is not None:
            self.attached_num = attached_num
        if unattached_num is not None:
            self.unattached_num = unattached_num
        if cannot_attach_num is not None:
            self.cannot_attach_num = cannot_attach_num
        if in_process_num is not None:
            self.in_process_num = in_process_num
        if in_use_num is not None:
            self.in_use_num = in_use_num
        if unregistered_num is not None:
            self.unregistered_num = unregistered_num
        if ready_num is not None:
            self.ready_num = ready_num
        if disconnected_num is not None:
            self.disconnected_num = disconnected_num
        if unknown_num is not None:
            self.unknown_num = unknown_num

    @property
    def static_name(self):
        r"""Gets the static_name of this InstanceStatusStatistics.

        统计对象名称(虚拟机组名称、桌面组名称)。

        :return: The static_name of this InstanceStatusStatistics.
        :rtype: str
        """
        return self._static_name

    @static_name.setter
    def static_name(self, static_name):
        r"""Sets the static_name of this InstanceStatusStatistics.

        统计对象名称(虚拟机组名称、桌面组名称)。

        :param static_name: The static_name of this InstanceStatusStatistics.
        :type static_name: str
        """
        self._static_name = static_name

    @property
    def running_num(self):
        r"""Gets the running_num of this InstanceStatusStatistics.

        运行数目(运行中、启动中、故障迁移中、迁移中)。

        :return: The running_num of this InstanceStatusStatistics.
        :rtype: int
        """
        return self._running_num

    @running_num.setter
    def running_num(self, running_num):
        r"""Sets the running_num of this InstanceStatusStatistics.

        运行数目(运行中、启动中、故障迁移中、迁移中)。

        :param running_num: The running_num of this InstanceStatusStatistics.
        :type running_num: int
        """
        self._running_num = running_num

    @property
    def stop_num(self):
        r"""Gets the stop_num of this InstanceStatusStatistics.

        关机数目(关机中、已关机)。

        :return: The stop_num of this InstanceStatusStatistics.
        :rtype: int
        """
        return self._stop_num

    @stop_num.setter
    def stop_num(self, stop_num):
        r"""Sets the stop_num of this InstanceStatusStatistics.

        关机数目(关机中、已关机)。

        :param stop_num: The stop_num of this InstanceStatusStatistics.
        :type stop_num: int
        """
        self._stop_num = stop_num

    @property
    def hibernate_num(self):
        r"""Gets the hibernate_num of this InstanceStatusStatistics.

        休眠数目(休眠中、已休眠)。

        :return: The hibernate_num of this InstanceStatusStatistics.
        :rtype: int
        """
        return self._hibernate_num

    @hibernate_num.setter
    def hibernate_num(self, hibernate_num):
        r"""Sets the hibernate_num of this InstanceStatusStatistics.

        休眠数目(休眠中、已休眠)。

        :param hibernate_num: The hibernate_num of this InstanceStatusStatistics.
        :type hibernate_num: int
        """
        self._hibernate_num = hibernate_num

    @property
    def other_num(self):
        r"""Gets the other_num of this InstanceStatusStatistics.

        其他(未知、删除失败、删除中)。

        :return: The other_num of this InstanceStatusStatistics.
        :rtype: int
        """
        return self._other_num

    @other_num.setter
    def other_num(self, other_num):
        r"""Sets the other_num of this InstanceStatusStatistics.

        其他(未知、删除失败、删除中)。

        :param other_num: The other_num of this InstanceStatusStatistics.
        :type other_num: int
        """
        self._other_num = other_num

    @property
    def attached_num(self):
        r"""Gets the attached_num of this InstanceStatusStatistics.

        已分配数目。

        :return: The attached_num of this InstanceStatusStatistics.
        :rtype: int
        """
        return self._attached_num

    @attached_num.setter
    def attached_num(self, attached_num):
        r"""Sets the attached_num of this InstanceStatusStatistics.

        已分配数目。

        :param attached_num: The attached_num of this InstanceStatusStatistics.
        :type attached_num: int
        """
        self._attached_num = attached_num

    @property
    def unattached_num(self):
        r"""Gets the unattached_num of this InstanceStatusStatistics.

        未分配数目。

        :return: The unattached_num of this InstanceStatusStatistics.
        :rtype: int
        """
        return self._unattached_num

    @unattached_num.setter
    def unattached_num(self, unattached_num):
        r"""Sets the unattached_num of this InstanceStatusStatistics.

        未分配数目。

        :param unattached_num: The unattached_num of this InstanceStatusStatistics.
        :type unattached_num: int
        """
        self._unattached_num = unattached_num

    @property
    def cannot_attach_num(self):
        r"""Gets the cannot_attach_num of this InstanceStatusStatistics.

        不可分配数目(分配失败、解分配失败、解分配成功)。

        :return: The cannot_attach_num of this InstanceStatusStatistics.
        :rtype: int
        """
        return self._cannot_attach_num

    @cannot_attach_num.setter
    def cannot_attach_num(self, cannot_attach_num):
        r"""Sets the cannot_attach_num of this InstanceStatusStatistics.

        不可分配数目(分配失败、解分配失败、解分配成功)。

        :param cannot_attach_num: The cannot_attach_num of this InstanceStatusStatistics.
        :type cannot_attach_num: int
        """
        self._cannot_attach_num = cannot_attach_num

    @property
    def in_process_num(self):
        r"""Gets the in_process_num of this InstanceStatusStatistics.

        处理中(分配中、解分配中)。

        :return: The in_process_num of this InstanceStatusStatistics.
        :rtype: int
        """
        return self._in_process_num

    @in_process_num.setter
    def in_process_num(self, in_process_num):
        r"""Sets the in_process_num of this InstanceStatusStatistics.

        处理中(分配中、解分配中)。

        :param in_process_num: The in_process_num of this InstanceStatusStatistics.
        :type in_process_num: int
        """
        self._in_process_num = in_process_num

    @property
    def in_use_num(self):
        r"""Gets the in_use_num of this InstanceStatusStatistics.

        使用中数目。

        :return: The in_use_num of this InstanceStatusStatistics.
        :rtype: int
        """
        return self._in_use_num

    @in_use_num.setter
    def in_use_num(self, in_use_num):
        r"""Sets the in_use_num of this InstanceStatusStatistics.

        使用中数目。

        :param in_use_num: The in_use_num of this InstanceStatusStatistics.
        :type in_use_num: int
        """
        self._in_use_num = in_use_num

    @property
    def unregistered_num(self):
        r"""Gets the unregistered_num of this InstanceStatusStatistics.

        未注册数目。

        :return: The unregistered_num of this InstanceStatusStatistics.
        :rtype: int
        """
        return self._unregistered_num

    @unregistered_num.setter
    def unregistered_num(self, unregistered_num):
        r"""Sets the unregistered_num of this InstanceStatusStatistics.

        未注册数目。

        :param unregistered_num: The unregistered_num of this InstanceStatusStatistics.
        :type unregistered_num: int
        """
        self._unregistered_num = unregistered_num

    @property
    def ready_num(self):
        r"""Gets the ready_num of this InstanceStatusStatistics.

        空闲数目。

        :return: The ready_num of this InstanceStatusStatistics.
        :rtype: int
        """
        return self._ready_num

    @ready_num.setter
    def ready_num(self, ready_num):
        r"""Sets the ready_num of this InstanceStatusStatistics.

        空闲数目。

        :param ready_num: The ready_num of this InstanceStatusStatistics.
        :type ready_num: int
        """
        self._ready_num = ready_num

    @property
    def disconnected_num(self):
        r"""Gets the disconnected_num of this InstanceStatusStatistics.

        断开连接数目。

        :return: The disconnected_num of this InstanceStatusStatistics.
        :rtype: int
        """
        return self._disconnected_num

    @disconnected_num.setter
    def disconnected_num(self, disconnected_num):
        r"""Sets the disconnected_num of this InstanceStatusStatistics.

        断开连接数目。

        :param disconnected_num: The disconnected_num of this InstanceStatusStatistics.
        :type disconnected_num: int
        """
        self._disconnected_num = disconnected_num

    @property
    def unknown_num(self):
        r"""Gets the unknown_num of this InstanceStatusStatistics.

        未知数目。

        :return: The unknown_num of this InstanceStatusStatistics.
        :rtype: int
        """
        return self._unknown_num

    @unknown_num.setter
    def unknown_num(self, unknown_num):
        r"""Sets the unknown_num of this InstanceStatusStatistics.

        未知数目。

        :param unknown_num: The unknown_num of this InstanceStatusStatistics.
        :type unknown_num: int
        """
        self._unknown_num = unknown_num

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
        if not isinstance(other, InstanceStatusStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
