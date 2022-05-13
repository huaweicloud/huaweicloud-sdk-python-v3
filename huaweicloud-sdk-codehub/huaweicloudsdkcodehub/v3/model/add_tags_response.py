# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddTagsResponse:

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
        'message': 'str',
        'commit': 'CommitRepoV2'
    }

    attribute_map = {
        'name': 'name',
        'message': 'message',
        'commit': 'commit'
    }

    def __init__(self, name=None, message=None, commit=None):
        """AddTagsResponse

        The model defined in huaweicloud sdk

        :param name: 标签名称
        :type name: str
        :param message: 备注
        :type message: str
        :param commit: 
        :type commit: :class:`huaweicloudsdkcodehub.v3.CommitRepoV2`
        """
        
        

        self._name = None
        self._message = None
        self._commit = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if message is not None:
            self.message = message
        if commit is not None:
            self.commit = commit

    @property
    def name(self):
        """Gets the name of this AddTagsResponse.

        标签名称

        :return: The name of this AddTagsResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AddTagsResponse.

        标签名称

        :param name: The name of this AddTagsResponse.
        :type name: str
        """
        self._name = name

    @property
    def message(self):
        """Gets the message of this AddTagsResponse.

        备注

        :return: The message of this AddTagsResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this AddTagsResponse.

        备注

        :param message: The message of this AddTagsResponse.
        :type message: str
        """
        self._message = message

    @property
    def commit(self):
        """Gets the commit of this AddTagsResponse.


        :return: The commit of this AddTagsResponse.
        :rtype: :class:`huaweicloudsdkcodehub.v3.CommitRepoV2`
        """
        return self._commit

    @commit.setter
    def commit(self, commit):
        """Sets the commit of this AddTagsResponse.


        :param commit: The commit of this AddTagsResponse.
        :type commit: :class:`huaweicloudsdkcodehub.v3.CommitRepoV2`
        """
        self._commit = commit

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
        if not isinstance(other, AddTagsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
