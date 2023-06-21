# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVmsSendTasksResponseMode:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'aim_basic_send_tasks': 'list[VmsSendTask]',
        'page_info': 'Page'
    }

    attribute_map = {
        'aim_basic_send_tasks': 'aim_basic_send_tasks',
        'page_info': 'page_info'
    }

    def __init__(self, aim_basic_send_tasks=None, page_info=None):
        """ListVmsSendTasksResponseMode

        The model defined in huaweicloud sdk

        :param aim_basic_send_tasks: 智能信息基础版任务查询列表。
        :type aim_basic_send_tasks: list[:class:`huaweicloudsdkkoomessage.v1.VmsSendTask`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkkoomessage.v1.Page`
        """
        
        

        self._aim_basic_send_tasks = None
        self._page_info = None
        self.discriminator = None

        if aim_basic_send_tasks is not None:
            self.aim_basic_send_tasks = aim_basic_send_tasks
        if page_info is not None:
            self.page_info = page_info

    @property
    def aim_basic_send_tasks(self):
        """Gets the aim_basic_send_tasks of this ListVmsSendTasksResponseMode.

        智能信息基础版任务查询列表。

        :return: The aim_basic_send_tasks of this ListVmsSendTasksResponseMode.
        :rtype: list[:class:`huaweicloudsdkkoomessage.v1.VmsSendTask`]
        """
        return self._aim_basic_send_tasks

    @aim_basic_send_tasks.setter
    def aim_basic_send_tasks(self, aim_basic_send_tasks):
        """Sets the aim_basic_send_tasks of this ListVmsSendTasksResponseMode.

        智能信息基础版任务查询列表。

        :param aim_basic_send_tasks: The aim_basic_send_tasks of this ListVmsSendTasksResponseMode.
        :type aim_basic_send_tasks: list[:class:`huaweicloudsdkkoomessage.v1.VmsSendTask`]
        """
        self._aim_basic_send_tasks = aim_basic_send_tasks

    @property
    def page_info(self):
        """Gets the page_info of this ListVmsSendTasksResponseMode.

        :return: The page_info of this ListVmsSendTasksResponseMode.
        :rtype: :class:`huaweicloudsdkkoomessage.v1.Page`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListVmsSendTasksResponseMode.

        :param page_info: The page_info of this ListVmsSendTasksResponseMode.
        :type page_info: :class:`huaweicloudsdkkoomessage.v1.Page`
        """
        self._page_info = page_info

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
        if not isinstance(other, ListVmsSendTasksResponseMode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
