# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlertGroup:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ding_talk_hook_url': 'str',
        'group_name': 'str',
        'id': 'str',
        'we_chat_work_hook_url': 'str',
        'we_link_group_no': 'str'
    }

    attribute_map = {
        'ding_talk_hook_url': 'dingTalkHookUrl',
        'group_name': 'group_name',
        'id': 'id',
        'we_chat_work_hook_url': 'weChatWorkHookUrl',
        'we_link_group_no': 'weLinkGroupNo'
    }

    def __init__(self, ding_talk_hook_url=None, group_name=None, id=None, we_chat_work_hook_url=None, we_link_group_no=None):
        """AlertGroup

        The model defined in huaweicloud sdk

        :param ding_talk_hook_url: 
        :type ding_talk_hook_url: str
        :param group_name: 告警组名称
        :type group_name: str
        :param id: 告警组ID
        :type id: str
        :param we_chat_work_hook_url: 
        :type we_chat_work_hook_url: str
        :param we_link_group_no: 
        :type we_link_group_no: str
        """
        
        

        self._ding_talk_hook_url = None
        self._group_name = None
        self._id = None
        self._we_chat_work_hook_url = None
        self._we_link_group_no = None
        self.discriminator = None

        if ding_talk_hook_url is not None:
            self.ding_talk_hook_url = ding_talk_hook_url
        if group_name is not None:
            self.group_name = group_name
        if id is not None:
            self.id = id
        if we_chat_work_hook_url is not None:
            self.we_chat_work_hook_url = we_chat_work_hook_url
        if we_link_group_no is not None:
            self.we_link_group_no = we_link_group_no

    @property
    def ding_talk_hook_url(self):
        """Gets the ding_talk_hook_url of this AlertGroup.

        :return: The ding_talk_hook_url of this AlertGroup.
        :rtype: str
        """
        return self._ding_talk_hook_url

    @ding_talk_hook_url.setter
    def ding_talk_hook_url(self, ding_talk_hook_url):
        """Sets the ding_talk_hook_url of this AlertGroup.

        :param ding_talk_hook_url: The ding_talk_hook_url of this AlertGroup.
        :type ding_talk_hook_url: str
        """
        self._ding_talk_hook_url = ding_talk_hook_url

    @property
    def group_name(self):
        """Gets the group_name of this AlertGroup.

        告警组名称

        :return: The group_name of this AlertGroup.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this AlertGroup.

        告警组名称

        :param group_name: The group_name of this AlertGroup.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def id(self):
        """Gets the id of this AlertGroup.

        告警组ID

        :return: The id of this AlertGroup.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AlertGroup.

        告警组ID

        :param id: The id of this AlertGroup.
        :type id: str
        """
        self._id = id

    @property
    def we_chat_work_hook_url(self):
        """Gets the we_chat_work_hook_url of this AlertGroup.

        :return: The we_chat_work_hook_url of this AlertGroup.
        :rtype: str
        """
        return self._we_chat_work_hook_url

    @we_chat_work_hook_url.setter
    def we_chat_work_hook_url(self, we_chat_work_hook_url):
        """Sets the we_chat_work_hook_url of this AlertGroup.

        :param we_chat_work_hook_url: The we_chat_work_hook_url of this AlertGroup.
        :type we_chat_work_hook_url: str
        """
        self._we_chat_work_hook_url = we_chat_work_hook_url

    @property
    def we_link_group_no(self):
        """Gets the we_link_group_no of this AlertGroup.

        :return: The we_link_group_no of this AlertGroup.
        :rtype: str
        """
        return self._we_link_group_no

    @we_link_group_no.setter
    def we_link_group_no(self, we_link_group_no):
        """Sets the we_link_group_no of this AlertGroup.

        :param we_link_group_no: The we_link_group_no of this AlertGroup.
        :type we_link_group_no: str
        """
        self._we_link_group_no = we_link_group_no

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
        if not isinstance(other, AlertGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
