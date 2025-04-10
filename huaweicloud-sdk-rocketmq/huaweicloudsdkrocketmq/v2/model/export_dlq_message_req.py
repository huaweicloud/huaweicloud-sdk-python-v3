# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportDlqMessageReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'topic': 'str',
        'msg_id_list': 'list[str]',
        'uniq_key_list': 'list[str]'
    }

    attribute_map = {
        'topic': 'topic',
        'msg_id_list': 'msg_id_list',
        'uniq_key_list': 'uniq_key_list'
    }

    def __init__(self, topic=None, msg_id_list=None, uniq_key_list=None):
        r"""ExportDlqMessageReq

        The model defined in huaweicloud sdk

        :param topic: 主题名称。
        :type topic: str
        :param msg_id_list: 消息ID列表。
        :type msg_id_list: list[str]
        :param uniq_key_list: 唯一Key列表。
        :type uniq_key_list: list[str]
        """
        
        

        self._topic = None
        self._msg_id_list = None
        self._uniq_key_list = None
        self.discriminator = None

        if topic is not None:
            self.topic = topic
        if msg_id_list is not None:
            self.msg_id_list = msg_id_list
        if uniq_key_list is not None:
            self.uniq_key_list = uniq_key_list

    @property
    def topic(self):
        r"""Gets the topic of this ExportDlqMessageReq.

        主题名称。

        :return: The topic of this ExportDlqMessageReq.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        r"""Sets the topic of this ExportDlqMessageReq.

        主题名称。

        :param topic: The topic of this ExportDlqMessageReq.
        :type topic: str
        """
        self._topic = topic

    @property
    def msg_id_list(self):
        r"""Gets the msg_id_list of this ExportDlqMessageReq.

        消息ID列表。

        :return: The msg_id_list of this ExportDlqMessageReq.
        :rtype: list[str]
        """
        return self._msg_id_list

    @msg_id_list.setter
    def msg_id_list(self, msg_id_list):
        r"""Sets the msg_id_list of this ExportDlqMessageReq.

        消息ID列表。

        :param msg_id_list: The msg_id_list of this ExportDlqMessageReq.
        :type msg_id_list: list[str]
        """
        self._msg_id_list = msg_id_list

    @property
    def uniq_key_list(self):
        r"""Gets the uniq_key_list of this ExportDlqMessageReq.

        唯一Key列表。

        :return: The uniq_key_list of this ExportDlqMessageReq.
        :rtype: list[str]
        """
        return self._uniq_key_list

    @uniq_key_list.setter
    def uniq_key_list(self, uniq_key_list):
        r"""Sets the uniq_key_list of this ExportDlqMessageReq.

        唯一Key列表。

        :param uniq_key_list: The uniq_key_list of this ExportDlqMessageReq.
        :type uniq_key_list: list[str]
        """
        self._uniq_key_list = uniq_key_list

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
        if not isinstance(other, ExportDlqMessageReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
