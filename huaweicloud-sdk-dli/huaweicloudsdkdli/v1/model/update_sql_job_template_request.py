# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSqlJobTemplateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sql_id': 'str',
        'body': 'UpdateSqlTemplatesRequestBody'
    }

    attribute_map = {
        'sql_id': 'sql_id',
        'body': 'body'
    }

    def __init__(self, sql_id=None, body=None):
        """UpdateSqlJobTemplateRequest

        The model defined in huaweicloud sdk

        :param sql_id: 
        :type sql_id: str
        :param body: Body of the UpdateSqlJobTemplateRequest
        :type body: :class:`huaweicloudsdkdli.v1.UpdateSqlTemplatesRequestBody`
        """
        
        

        self._sql_id = None
        self._body = None
        self.discriminator = None

        self.sql_id = sql_id
        if body is not None:
            self.body = body

    @property
    def sql_id(self):
        """Gets the sql_id of this UpdateSqlJobTemplateRequest.

        :return: The sql_id of this UpdateSqlJobTemplateRequest.
        :rtype: str
        """
        return self._sql_id

    @sql_id.setter
    def sql_id(self, sql_id):
        """Sets the sql_id of this UpdateSqlJobTemplateRequest.

        :param sql_id: The sql_id of this UpdateSqlJobTemplateRequest.
        :type sql_id: str
        """
        self._sql_id = sql_id

    @property
    def body(self):
        """Gets the body of this UpdateSqlJobTemplateRequest.

        :return: The body of this UpdateSqlJobTemplateRequest.
        :rtype: :class:`huaweicloudsdkdli.v1.UpdateSqlTemplatesRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateSqlJobTemplateRequest.

        :param body: The body of this UpdateSqlJobTemplateRequest.
        :type body: :class:`huaweicloudsdkdli.v1.UpdateSqlTemplatesRequestBody`
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
        if not isinstance(other, UpdateSqlJobTemplateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
