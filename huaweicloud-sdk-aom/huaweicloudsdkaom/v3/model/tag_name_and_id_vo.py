# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TagNameAndIdVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tag_id': 'str',
        'tag_name': 'str'
    }

    attribute_map = {
        'tag_id': 'tag_id',
        'tag_name': 'tag_name'
    }

    def __init__(self, tag_id=None, tag_name=None):
        """TagNameAndIdVo

        The model defined in huaweicloud sdk

        :param tag_id: 标签Id
        :type tag_id: str
        :param tag_name: 标签名称
        :type tag_name: str
        """
        
        

        self._tag_id = None
        self._tag_name = None
        self.discriminator = None

        if tag_id is not None:
            self.tag_id = tag_id
        if tag_name is not None:
            self.tag_name = tag_name

    @property
    def tag_id(self):
        """Gets the tag_id of this TagNameAndIdVo.

        标签Id

        :return: The tag_id of this TagNameAndIdVo.
        :rtype: str
        """
        return self._tag_id

    @tag_id.setter
    def tag_id(self, tag_id):
        """Sets the tag_id of this TagNameAndIdVo.

        标签Id

        :param tag_id: The tag_id of this TagNameAndIdVo.
        :type tag_id: str
        """
        self._tag_id = tag_id

    @property
    def tag_name(self):
        """Gets the tag_name of this TagNameAndIdVo.

        标签名称

        :return: The tag_name of this TagNameAndIdVo.
        :rtype: str
        """
        return self._tag_name

    @tag_name.setter
    def tag_name(self, tag_name):
        """Sets the tag_name of this TagNameAndIdVo.

        标签名称

        :param tag_name: The tag_name of this TagNameAndIdVo.
        :type tag_name: str
        """
        self._tag_name = tag_name

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
        if not isinstance(other, TagNameAndIdVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
