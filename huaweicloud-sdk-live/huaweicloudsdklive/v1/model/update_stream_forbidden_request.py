# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateStreamForbiddenRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'specify_project': 'str',
        'body': 'StreamForbiddenSetting'
    }

    attribute_map = {
        'specify_project': 'specify_project',
        'body': 'body'
    }

    def __init__(self, specify_project=None, body=None):
        """UpdateStreamForbiddenRequest

        The model defined in huaweicloud sdk

        :param specify_project: op账号需要携带的特定project_id，当使用op账号时该值为所操作租户的project_id
        :type specify_project: str
        :param body: Body of the UpdateStreamForbiddenRequest
        :type body: :class:`huaweicloudsdklive.v1.StreamForbiddenSetting`
        """
        
        

        self._specify_project = None
        self._body = None
        self.discriminator = None

        if specify_project is not None:
            self.specify_project = specify_project
        if body is not None:
            self.body = body

    @property
    def specify_project(self):
        """Gets the specify_project of this UpdateStreamForbiddenRequest.

        op账号需要携带的特定project_id，当使用op账号时该值为所操作租户的project_id

        :return: The specify_project of this UpdateStreamForbiddenRequest.
        :rtype: str
        """
        return self._specify_project

    @specify_project.setter
    def specify_project(self, specify_project):
        """Sets the specify_project of this UpdateStreamForbiddenRequest.

        op账号需要携带的特定project_id，当使用op账号时该值为所操作租户的project_id

        :param specify_project: The specify_project of this UpdateStreamForbiddenRequest.
        :type specify_project: str
        """
        self._specify_project = specify_project

    @property
    def body(self):
        """Gets the body of this UpdateStreamForbiddenRequest.


        :return: The body of this UpdateStreamForbiddenRequest.
        :rtype: :class:`huaweicloudsdklive.v1.StreamForbiddenSetting`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateStreamForbiddenRequest.


        :param body: The body of this UpdateStreamForbiddenRequest.
        :type body: :class:`huaweicloudsdklive.v1.StreamForbiddenSetting`
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
        if not isinstance(other, UpdateStreamForbiddenRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
