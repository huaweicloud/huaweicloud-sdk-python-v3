# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExerciseCodeResource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'polymeric_resource_id': 'str',
        'content': 'str',
        'code_answer': 'str'
    }

    attribute_map = {
        'id': 'id',
        'polymeric_resource_id': 'polymeric_resource_id',
        'content': 'content',
        'code_answer': 'code_answer'
    }

    def __init__(self, id=None, polymeric_resource_id=None, content=None, code_answer=None):
        r"""ExerciseCodeResource

        The model defined in huaweicloud sdk

        :param id: 习题内容存储id
        :type id: str
        :param polymeric_resource_id: 资源聚合id
        :type polymeric_resource_id: str
        :param content: 习题内容
        :type content: str
        :param code_answer: 参考答案
        :type code_answer: str
        """
        
        

        self._id = None
        self._polymeric_resource_id = None
        self._content = None
        self._code_answer = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if polymeric_resource_id is not None:
            self.polymeric_resource_id = polymeric_resource_id
        if content is not None:
            self.content = content
        if code_answer is not None:
            self.code_answer = code_answer

    @property
    def id(self):
        r"""Gets the id of this ExerciseCodeResource.

        习题内容存储id

        :return: The id of this ExerciseCodeResource.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ExerciseCodeResource.

        习题内容存储id

        :param id: The id of this ExerciseCodeResource.
        :type id: str
        """
        self._id = id

    @property
    def polymeric_resource_id(self):
        r"""Gets the polymeric_resource_id of this ExerciseCodeResource.

        资源聚合id

        :return: The polymeric_resource_id of this ExerciseCodeResource.
        :rtype: str
        """
        return self._polymeric_resource_id

    @polymeric_resource_id.setter
    def polymeric_resource_id(self, polymeric_resource_id):
        r"""Sets the polymeric_resource_id of this ExerciseCodeResource.

        资源聚合id

        :param polymeric_resource_id: The polymeric_resource_id of this ExerciseCodeResource.
        :type polymeric_resource_id: str
        """
        self._polymeric_resource_id = polymeric_resource_id

    @property
    def content(self):
        r"""Gets the content of this ExerciseCodeResource.

        习题内容

        :return: The content of this ExerciseCodeResource.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this ExerciseCodeResource.

        习题内容

        :param content: The content of this ExerciseCodeResource.
        :type content: str
        """
        self._content = content

    @property
    def code_answer(self):
        r"""Gets the code_answer of this ExerciseCodeResource.

        参考答案

        :return: The code_answer of this ExerciseCodeResource.
        :rtype: str
        """
        return self._code_answer

    @code_answer.setter
    def code_answer(self, code_answer):
        r"""Sets the code_answer of this ExerciseCodeResource.

        参考答案

        :param code_answer: The code_answer of this ExerciseCodeResource.
        :type code_answer: str
        """
        self._code_answer = code_answer

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
        if not isinstance(other, ExerciseCodeResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
