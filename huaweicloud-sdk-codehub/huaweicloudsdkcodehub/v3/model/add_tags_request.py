# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddTagsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tag_name': 'str',
        'ref': 'str',
        'message': 'str'
    }

    attribute_map = {
        'tag_name': 'tag_name',
        'ref': 'ref',
        'message': 'message'
    }

    def __init__(self, tag_name=None, ref=None, message=None):
        """AddTagsRequest

        The model defined in huaweicloud sdk

        :param tag_name: 标签名称
        :type tag_name: str
        :param ref: 分支名称
        :type ref: str
        :param message: 备注
        :type message: str
        """
        
        

        self._tag_name = None
        self._ref = None
        self._message = None
        self.discriminator = None

        self.tag_name = tag_name
        self.ref = ref
        if message is not None:
            self.message = message

    @property
    def tag_name(self):
        """Gets the tag_name of this AddTagsRequest.

        标签名称

        :return: The tag_name of this AddTagsRequest.
        :rtype: str
        """
        return self._tag_name

    @tag_name.setter
    def tag_name(self, tag_name):
        """Sets the tag_name of this AddTagsRequest.

        标签名称

        :param tag_name: The tag_name of this AddTagsRequest.
        :type tag_name: str
        """
        self._tag_name = tag_name

    @property
    def ref(self):
        """Gets the ref of this AddTagsRequest.

        分支名称

        :return: The ref of this AddTagsRequest.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """Sets the ref of this AddTagsRequest.

        分支名称

        :param ref: The ref of this AddTagsRequest.
        :type ref: str
        """
        self._ref = ref

    @property
    def message(self):
        """Gets the message of this AddTagsRequest.

        备注

        :return: The message of this AddTagsRequest.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this AddTagsRequest.

        备注

        :param message: The message of this AddTagsRequest.
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
        if not isinstance(other, AddTagsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
