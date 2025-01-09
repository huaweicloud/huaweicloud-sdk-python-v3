# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateScriptRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'script_id': 'str',
        'body': 'UpdateScriptReq'
    }

    attribute_map = {
        'script_id': 'script_id',
        'body': 'body'
    }

    def __init__(self, script_id=None, body=None):
        """UpdateScriptRequest

        The model defined in huaweicloud sdk

        :param script_id: 脚本ID。
        :type script_id: str
        :param body: Body of the UpdateScriptRequest
        :type body: :class:`huaweicloudsdkworkspace.v2.UpdateScriptReq`
        """
        
        

        self._script_id = None
        self._body = None
        self.discriminator = None

        self.script_id = script_id
        if body is not None:
            self.body = body

    @property
    def script_id(self):
        """Gets the script_id of this UpdateScriptRequest.

        脚本ID。

        :return: The script_id of this UpdateScriptRequest.
        :rtype: str
        """
        return self._script_id

    @script_id.setter
    def script_id(self, script_id):
        """Sets the script_id of this UpdateScriptRequest.

        脚本ID。

        :param script_id: The script_id of this UpdateScriptRequest.
        :type script_id: str
        """
        self._script_id = script_id

    @property
    def body(self):
        """Gets the body of this UpdateScriptRequest.

        :return: The body of this UpdateScriptRequest.
        :rtype: :class:`huaweicloudsdkworkspace.v2.UpdateScriptReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateScriptRequest.

        :param body: The body of this UpdateScriptRequest.
        :type body: :class:`huaweicloudsdkworkspace.v2.UpdateScriptReq`
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
        if not isinstance(other, UpdateScriptRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
