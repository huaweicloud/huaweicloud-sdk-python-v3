# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecuteExerciseRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('user_token')

    openapi_types = {
        'user_token': 'str',
        'exercise_id': 'str',
        'body': 'PackageExerciseJudgeRequestBody'
    }

    attribute_map = {
        'user_token': 'user-token',
        'exercise_id': 'exercise_id',
        'body': 'body'
    }

    def __init__(self, user_token=None, exercise_id=None, body=None):
        r"""ExecuteExerciseRequest

        The model defined in huaweicloud sdk

        :param user_token: 具体调用者的用户token
        :type user_token: str
        :param exercise_id: 需判题的习题id
        :type exercise_id: str
        :param body: Body of the ExecuteExerciseRequest
        :type body: :class:`huaweicloudsdkclassroom.v3.PackageExerciseJudgeRequestBody`
        """
        
        

        self._user_token = None
        self._exercise_id = None
        self._body = None
        self.discriminator = None

        if user_token is not None:
            self.user_token = user_token
        self.exercise_id = exercise_id
        if body is not None:
            self.body = body

    @property
    def user_token(self):
        r"""Gets the user_token of this ExecuteExerciseRequest.

        具体调用者的用户token

        :return: The user_token of this ExecuteExerciseRequest.
        :rtype: str
        """
        return self._user_token

    @user_token.setter
    def user_token(self, user_token):
        r"""Sets the user_token of this ExecuteExerciseRequest.

        具体调用者的用户token

        :param user_token: The user_token of this ExecuteExerciseRequest.
        :type user_token: str
        """
        self._user_token = user_token

    @property
    def exercise_id(self):
        r"""Gets the exercise_id of this ExecuteExerciseRequest.

        需判题的习题id

        :return: The exercise_id of this ExecuteExerciseRequest.
        :rtype: str
        """
        return self._exercise_id

    @exercise_id.setter
    def exercise_id(self, exercise_id):
        r"""Sets the exercise_id of this ExecuteExerciseRequest.

        需判题的习题id

        :param exercise_id: The exercise_id of this ExecuteExerciseRequest.
        :type exercise_id: str
        """
        self._exercise_id = exercise_id

    @property
    def body(self):
        r"""Gets the body of this ExecuteExerciseRequest.

        :return: The body of this ExecuteExerciseRequest.
        :rtype: :class:`huaweicloudsdkclassroom.v3.PackageExerciseJudgeRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ExecuteExerciseRequest.

        :param body: The body of this ExecuteExerciseRequest.
        :type body: :class:`huaweicloudsdkclassroom.v3.PackageExerciseJudgeRequestBody`
        """
        self._body = body

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
        if not isinstance(other, ExecuteExerciseRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
