# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSparkJobRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_id': 'str',
        'body': 'CreateSparkJobRequestBody'
    }

    attribute_map = {
        'user_id': 'USER-ID',
        'body': 'body'
    }

    def __init__(self, user_id=None, body=None):
        r"""CreateSparkJobRequest

        The model defined in huaweicloud sdk

        :param user_id: 参数解释:   用户ID 示例: 48cc2c48765f481480c7db940d6409d1 约束限制:  无 取值范围: 无 默认取值: 无
        :type user_id: str
        :param body: Body of the CreateSparkJobRequest
        :type body: :class:`huaweicloudsdkdli.v1.CreateSparkJobRequestBody`
        """
        
        

        self._user_id = None
        self._body = None
        self.discriminator = None

        if user_id is not None:
            self.user_id = user_id
        if body is not None:
            self.body = body

    @property
    def user_id(self):
        r"""Gets the user_id of this CreateSparkJobRequest.

        参数解释:   用户ID 示例: 48cc2c48765f481480c7db940d6409d1 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The user_id of this CreateSparkJobRequest.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this CreateSparkJobRequest.

        参数解释:   用户ID 示例: 48cc2c48765f481480c7db940d6409d1 约束限制:  无 取值范围: 无 默认取值: 无

        :param user_id: The user_id of this CreateSparkJobRequest.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def body(self):
        r"""Gets the body of this CreateSparkJobRequest.

        :return: The body of this CreateSparkJobRequest.
        :rtype: :class:`huaweicloudsdkdli.v1.CreateSparkJobRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CreateSparkJobRequest.

        :param body: The body of this CreateSparkJobRequest.
        :type body: :class:`huaweicloudsdkdli.v1.CreateSparkJobRequestBody`
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
        if not isinstance(other, CreateSparkJobRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
