# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Target:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'extension_info': 'list[Extension]',
        'target_id': 'str'
    }

    attribute_map = {
        'extension_info': 'extension_info',
        'target_id': 'target_id'
    }

    def __init__(self, extension_info=None, target_id=None):
        """Target

        The model defined in huaweicloud sdk

        :param extension_info: 批量处理对象基本信息
        :type extension_info: list[:class:`huaweicloudsdkief.v1.Extension`]
        :param target_id: 批量处理对象ID
        :type target_id: str
        """
        
        

        self._extension_info = None
        self._target_id = None
        self.discriminator = None

        if extension_info is not None:
            self.extension_info = extension_info
        self.target_id = target_id

    @property
    def extension_info(self):
        """Gets the extension_info of this Target.

        批量处理对象基本信息

        :return: The extension_info of this Target.
        :rtype: list[:class:`huaweicloudsdkief.v1.Extension`]
        """
        return self._extension_info

    @extension_info.setter
    def extension_info(self, extension_info):
        """Sets the extension_info of this Target.

        批量处理对象基本信息

        :param extension_info: The extension_info of this Target.
        :type extension_info: list[:class:`huaweicloudsdkief.v1.Extension`]
        """
        self._extension_info = extension_info

    @property
    def target_id(self):
        """Gets the target_id of this Target.

        批量处理对象ID

        :return: The target_id of this Target.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """Sets the target_id of this Target.

        批量处理对象ID

        :param target_id: The target_id of this Target.
        :type target_id: str
        """
        self._target_id = target_id

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
        if not isinstance(other, Target):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
