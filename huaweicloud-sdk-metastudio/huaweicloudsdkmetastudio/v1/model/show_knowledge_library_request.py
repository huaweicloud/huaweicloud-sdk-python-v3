# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowKnowledgeLibraryRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_app_user_id': 'str',
        'knowledge_library_id': 'str'
    }

    attribute_map = {
        'x_app_user_id': 'X-App-UserId',
        'knowledge_library_id': 'knowledge_library_id'
    }

    def __init__(self, x_app_user_id=None, knowledge_library_id=None):
        r"""ShowKnowledgeLibraryRequest

        The model defined in huaweicloud sdk

        :param x_app_user_id: 第三方用户ID。不允许输入中文。
        :type x_app_user_id: str
        :param knowledge_library_id: 知识库ID。
        :type knowledge_library_id: str
        """
        
        

        self._x_app_user_id = None
        self._knowledge_library_id = None
        self.discriminator = None

        if x_app_user_id is not None:
            self.x_app_user_id = x_app_user_id
        self.knowledge_library_id = knowledge_library_id

    @property
    def x_app_user_id(self):
        r"""Gets the x_app_user_id of this ShowKnowledgeLibraryRequest.

        第三方用户ID。不允许输入中文。

        :return: The x_app_user_id of this ShowKnowledgeLibraryRequest.
        :rtype: str
        """
        return self._x_app_user_id

    @x_app_user_id.setter
    def x_app_user_id(self, x_app_user_id):
        r"""Sets the x_app_user_id of this ShowKnowledgeLibraryRequest.

        第三方用户ID。不允许输入中文。

        :param x_app_user_id: The x_app_user_id of this ShowKnowledgeLibraryRequest.
        :type x_app_user_id: str
        """
        self._x_app_user_id = x_app_user_id

    @property
    def knowledge_library_id(self):
        r"""Gets the knowledge_library_id of this ShowKnowledgeLibraryRequest.

        知识库ID。

        :return: The knowledge_library_id of this ShowKnowledgeLibraryRequest.
        :rtype: str
        """
        return self._knowledge_library_id

    @knowledge_library_id.setter
    def knowledge_library_id(self, knowledge_library_id):
        r"""Sets the knowledge_library_id of this ShowKnowledgeLibraryRequest.

        知识库ID。

        :param knowledge_library_id: The knowledge_library_id of this ShowKnowledgeLibraryRequest.
        :type knowledge_library_id: str
        """
        self._knowledge_library_id = knowledge_library_id

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
        if not isinstance(other, ShowKnowledgeLibraryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
