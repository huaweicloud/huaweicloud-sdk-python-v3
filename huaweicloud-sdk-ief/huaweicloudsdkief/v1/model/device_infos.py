# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeviceInfos:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'relation': 'str',
        'comment': 'str',
        'device_ids': 'list[str]'
    }

    attribute_map = {
        'relation': 'relation',
        'comment': 'comment',
        'device_ids': 'device_ids'
    }

    def __init__(self, relation=None, comment=None, device_ids=None):
        """DeviceInfos

        The model defined in huaweicloud sdk

        :param relation: 设备和节点关系的名称，只允许中文字符、英文字母、数字、下划线、中划线，最大长度64
        :type relation: str
        :param comment: 设备和节点关系的描述，最大长度64，不允许^ ~ # $ % &amp; * &lt; &gt; ( ) [ ] { } &#39; \&quot; \\
        :type comment: str
        :param device_ids: 设备ID列表
        :type device_ids: list[str]
        """
        
        

        self._relation = None
        self._comment = None
        self._device_ids = None
        self.discriminator = None

        self.relation = relation
        if comment is not None:
            self.comment = comment
        self.device_ids = device_ids

    @property
    def relation(self):
        """Gets the relation of this DeviceInfos.

        设备和节点关系的名称，只允许中文字符、英文字母、数字、下划线、中划线，最大长度64

        :return: The relation of this DeviceInfos.
        :rtype: str
        """
        return self._relation

    @relation.setter
    def relation(self, relation):
        """Sets the relation of this DeviceInfos.

        设备和节点关系的名称，只允许中文字符、英文字母、数字、下划线、中划线，最大长度64

        :param relation: The relation of this DeviceInfos.
        :type relation: str
        """
        self._relation = relation

    @property
    def comment(self):
        """Gets the comment of this DeviceInfos.

        设备和节点关系的描述，最大长度64，不允许^ ~ # $ % & * < > ( ) [ ] { } ' \" \\

        :return: The comment of this DeviceInfos.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this DeviceInfos.

        设备和节点关系的描述，最大长度64，不允许^ ~ # $ % & * < > ( ) [ ] { } ' \" \\

        :param comment: The comment of this DeviceInfos.
        :type comment: str
        """
        self._comment = comment

    @property
    def device_ids(self):
        """Gets the device_ids of this DeviceInfos.

        设备ID列表

        :return: The device_ids of this DeviceInfos.
        :rtype: list[str]
        """
        return self._device_ids

    @device_ids.setter
    def device_ids(self, device_ids):
        """Sets the device_ids of this DeviceInfos.

        设备ID列表

        :param device_ids: The device_ids of this DeviceInfos.
        :type device_ids: list[str]
        """
        self._device_ids = device_ids

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
        if not isinstance(other, DeviceInfos):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
